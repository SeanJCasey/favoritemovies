class Movie():
    """ A class to handle media of type movie. """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        # self.summary = summary # commented out b/c movie text is not used in fresh_tomatoes.py
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

