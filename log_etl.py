from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
from lib.database_wrapper import DatabaseWrapper
import os

def log_etl():

	log_json_path = os.getcwd() + '/data/log_data/'
	file_finder = FileFinder(log_json_path, '*.json')
	data_loader = DataLoader(file_finder.return_file_names())
	log_dataframe = data_loader.create_json_from_files()
	data_filter = DataFilter(log_dataframe)

	users = data_filter.return_unique_dataframe_subset(
		['firstName', 'lastName', 'gender', 'level', ], ['firstName', 'lastName']
	)

	artists_from_log_db = data_filter.return_unique_dataframe_subset(
		['artist'], 'artist'
	)

	ancillary_artist_insert = 'insert into d_artist (artist_name) values (%s) ON CONFLICT (artist_name) DO NOTHING'
	print(artists_from_log_db.head(100))
	
	# user_query = 'insert into d_app_user (first_name, last_name, gender, level) values (%s, %s, %s, %s)'
	database_wrapper = DatabaseWrapper()
	# # database_wrapper.execute_batch_query(user_query, list(users.itertuples(index=False, name=None)))
	database_wrapper.execute_batch_query(ancillary_artist_insert, list(artists_from_log_db.itertuples(index=False, name=None)))


log_etl()
