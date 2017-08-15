import webbrowser

# This is our media.py file

# In order for us to create a web page we need to import webbrowser.


class movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
# A class is more like a storage place where we store all the information needed to run the code effectively. # noqa

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # We use (def) here to call on the __init__ method everytime the code is executed. # noqa
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# In the __init__ method, self refers to the newly created object; in other class methods, it refers to the instance whose method was called. (https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/) # noqa

    def show_trailer(self):
        # We also use the same system here to show us the trailer of the movies everytime I or someone else click on the poster of the movie. # noqa
        webbrowser.open(self.trailer_youtube_url)
# def is a keyword that we always use to define a method. We always used it when we are calling on a method (i.e. __init__, show_trailer...etc) to be executed on a continuous basis. # noqa
