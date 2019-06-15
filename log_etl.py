from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
from lib.database_wrapper import DatabaseWrapper
from datetime import datetime

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

	log_artist_set = data_filter.return_unique_dataframe_subset(
		['artist'], 'artist'
	)

	log_song_set = data_filter.return_unique_dataframe_subset(
		['song', 'artist'], ['song', 'artist']
	)

	timestamp_data_set = data_filter.return_unique_dataframe_subset(
		['ts', 'firstName', 'lastName']
	)

	timestamp_unpacked_dataset = list(timestamp_data_set.itertuples(name=None, index=False))
	sample_timestamp = timestamp_unpacked_dataset[0]
	print(sample_timestamp)
	sample = get_timetuple(sample_timestamp[0])
	sample[-1] = sample[-1] > 5
	sample.extend(sample_timestamp)
	print(sample)


	# ancillary_artist_insert = 'insert into d_artist (artist_name) values (%s) on conflict (artist_name) do nothing'
	# ancillary_song_insert = 'insert into d_song (song_name, artist_id) values (%s, (select artist_id from d_artist where artist_name=%s)) on conflict (song_name, artist_id) do nothing'
	# user_query = 'insert into d_app_user (first_name, last_name, gender, level) values (%s, %s, %s, %s)'
	# database_wrapper = DatabaseWrapper()

	# database_wrapper.execute_batch_query(user_query, list(users.itertuples(index=False, name=None)))
	# database_wrapper.execute_batch_query(ancillary_artist_insert, list(log_artist_set.itertuples(index=False, name=None)))
	# database_wrapper.execute_batch_query(ancillary_song_insert, list(log_song_set.itertuples(index=False, name=None)))


def get_timetuple(timestamp):
	return (list(datetime.fromtimestamp(int(timestamp // 1000)).timetuple()[0: 7]))
	


log_etl()


