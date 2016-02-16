import webbrowser


class Movie():
    """
        Attributes:
        title (str): The title of the movie, in caps
        storyline (str): A synopsis of the movie's plot
        poster_image (str): URL for a portrait-oriented movie poster
                            image
        trailer_youtube (str): URL for the movie's trailer on YouTube
        movie_rating (str): A rating of the movie, in stars (using
                            asterisks). Maximum of 4

    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_rating = movie_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
