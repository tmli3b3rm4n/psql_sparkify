from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
from lib.database_wrapper import DatabaseWrapper
from lib.query import query
from datetime import datetime
import os

def log_etl():

	log_json_path = os.getcwd() + '/data/log_data/'
	file_finder = FileFinder(log_json_path, '*.json')
	data_loader = DataLoader(file_finder.return_file_names())
	data_filter = DataFilter(data_loader.create_json_from_files())

	user_set = data_filter.return_unique_dataframe_subset(
		['firstName', 'lastName', 'gender', 'level'], 
		['firstName', 'lastName']
	)

	timestamp_data_set = data_filter.return_unique_dataframe_subset(
		['ts', 'firstName', 'lastName']
	)

	songplay_dataset = data_filter.return_unique_dataframe_subset(
		['ts', 'firstName', 'lastName', 'level', 'song', 'artist', 'artist', 'sessionId']
	)
	
	database_wrapper = DatabaseWrapper()

	database_wrapper.execute_batch_query(
		query['user_insert'], 
		list(user_set.itertuples(index=False, name=None))
	)
	
	database_wrapper.execute_batch_query(
		query['timestamp_insert'], 
		list(
			map(unpack_timestamp, timestamp_data_set.itertuples(name=None, index=False))
		)
	)
	
	database_wrapper.execute_batch_query(
		query['songplay_insert'], 
		list(songplay_dataset.itertuples(index=False, name=None))
	)

def unpack_timestamp(row):
	new_row = list(datetime.fromtimestamp(int(row[0] // 1000)).timetuple()[0: 7])
	new_row[-1] = new_row[-1] > 5
	new_row.extend(row)
	return tuple(new_row)
