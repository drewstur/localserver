import webbrowser

class Video():
	"""This class provides a way to store general video data"""

	def __init__(self, title, duration, storyline):
		self.title = title
		self.duration = duration 
		self.storyline = storyline

class Movie(Video):
	"""This class provides a way to store movie related information"""

	def __init__(self,  title, duration, storyline, poster_image, trailer_youtube):
		Video.__init__(self, title, duration, storyline)
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

class TvShow(Video):
	"""This class provides a way to store tv show related information"""

	def __init__(self,  title, duration, storyline, poster_image, trailer_youtube, episode, season):
		Video.__init__(self, title, duration, storyline)
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.tv_episode = episode
		self.tv_season = season

