
class DataFilter:

	def __init__(self, json_data):
		self.json_data = json_data

	# def return_dicts_of_data(self):

	# 	filtered_data = {}
	# 	filtered_data['artist'] = []
	# 	filtered_data['song'] = []

class Artist:

	def __init__(self, name, location, latitude, longtitude):
		self.name = name
		self.location = location
		self.latitude = latitude
		self.longtitude = longtitude

class Song:
	
	def __init__(self, title, year, duration):
		self.title = title
		self.year = year
		self.duration = duration

