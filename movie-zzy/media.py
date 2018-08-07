# -*- coding: utf-8 -*-

import webbrowser

'''
media: This module defined a class named Movie which used to store the information of my favorate movies.
'''

class Movie():
	def __init__(self,movie_title,movie_director,movie_role,movie_storyline,poster_image,trailer_youku,release_date):
		self.title = movie_title
		self.director = movie_director
		self.role = movie_role
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youku
		self.release_date = release_date

		"""
        Initialize the properties of Class Movie
        
        Args:
            movie_title: The title of favorite movie
            movie_director: The director of the movie
            movie_role: The main roles of the movie
            movie_stroyline: The main contents of the movie
            poster_image: The url of poster image of the movie
            trailer_youku: The url of the trailer of the movie in youku
            release_date: The release date of the movie
            
        return:
            None
        """

	def show_trailer(self):
		"""Open the trailer url of the movie by browser"""
		webbrowser.open(self.trailer_youtube_url)
