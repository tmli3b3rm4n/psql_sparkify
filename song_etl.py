from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
from lib.database_wrapper import DatabaseWrapper
from lib.query import query
import os

def song_etl():

	song_json_path = os.getcwd() + '/data/song_data/'
	file_finder = FileFinder(song_json_path, '*.json')
	data_loader = DataLoader(file_finder.return_file_names())
	song_dataframe = data_loader.create_json_from_files()
	data_filter = DataFilter(song_dataframe)

	artist_dataset = data_filter.return_unique_dataframe_subset(
	  ['artist_id', 'artist_name', 'artist_location', 'artist_longitude', 'artist_latitude'], 
		['artist_id', 'artist_name']
	)

	song_dataset = data_filter.return_unique_dataframe_subset(
		['song_id', 'title', 'year', 'duration', 'artist_name'], 
		['song_id', 'title']
	)

	database_wrapper = DatabaseWrapper()

	database_wrapper.execute_batch_query(
		query['artist_insert'], 
		list(artist_dataset.itertuples(index=False, name=None))
	)

	database_wrapper.execute_batch_query(
		query['song_insert'], 
		list(song_dataset.itertuples(index=False, name=None))
	)

song_etl()