from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
from lib.database_wrapper import DatabaseWrapper
import os

def song_etl():

	song_json_path = os.getcwd() + '/data/song_data/'
	file_finder = FileFinder(song_json_path, '*.json')
	data_loader = DataLoader(file_finder.return_file_names())
	song_dataframe = data_loader.create_json_from_files()
	data_filter = DataFilter(song_dataframe)

	artists = data_filter.return_unique_dataframe_subset(
	    ['artist_name', 'artist_location', 'artist_longitude', 'artist_latitude'], 'artist_name')

	songs = data_filter.return_unique_dataframe_subset(
		['title', 'year', 'duration', 'artist_name'], 'title'
	)

	artist_query = 'insert into f_artist (artist_name, artist_location, artist_longitude, artist_latitude) values (%s, %s, %s, %s)'
	song_query = 'insert into f_song (song_name, year, length, artist_id) values (%s, %s, %s, (select artist_id from f_artist where artist_name=%s))'

	print(list(artists.itertuples()))

	database_wrapper = DatabaseWrapper()
	database_wrapper.execute_batch_query(artist_query, list(artists.itertuples(index=False, name=None)))
	database_wrapper.execute_batch_query(song_query, list(songs.itertuples(index=False, name=None)))

