import webbrowser

class Video():
    """Stores universal information about different media"""
    def __init__(self, title, description, rating, duration, release, stars):
        self.title = title
        self.description = description
        self.rating = rating
        self.duration = duration
        self.release = release
        self.stars = stars

class Movie(Video):
    """Stores movie information for use in a website.
    """
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, title, description, rating, duration, release, stars, director, poster_image, trailer_youtube):
        Video.__init__(self, title, description, rating, duration, release, stars)
        self.director = director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    """Stores information about TV Shows
    """
