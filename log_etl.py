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

	timestamp_unpacked_dataset = map(
		unpack_timestamp, timestamp_data_set.itertuples(name=None, index=False)
	)

	songplay_dataset = data_filter.return_unique_dataframe_subset(
		['ts', 'firstName', 'lastName', 'level', 'song', 'artist', 'artist', 'sessionId']
	)
		
	ancillary_artist_insert = 'insert into d_artist (artist_name) values (%s) on conflict (artist_name) do nothing'

	ancillary_song_insert = 'insert into d_song (song_name, artist_id) values (%s, (select artist_id from d_artist where artist_name=%s)) on conflict (song_name, artist_id) do nothing'

	user_query = 'insert into d_app_user (first_name, last_name, gender, level) values (%s, %s, %s, %s) on conflict (first_name, last_name) do nothing'

	timestamp_query = 'insert into d_timestamp (year, month, day, hour, minute, second, weekday, timestamp, user_id) values (%s, %s, %s, %s, %s, %s, %s, %s, (select user_id from d_app_user where first_name = %s and last_name = %s))'

	songplay_query = 'insert into f_songplay (start_time,user_id, level,song_id,artist_id,session_id) values (%s, (select user_id from d_app_user where first_name = %s and last_name = %s), %s, (select song_id from d_song where song_name = %s and artist_id = (select artist_id from d_artist where artist_name = %s)),(select artist_id from d_artist where artist_name= %s),%s)'

	database_wrapper = DatabaseWrapper()
	database_wrapper.execute_batch_query(user_query, list(users.itertuples(index=False, name=None)))
	database_wrapper.execute_batch_query(ancillary_artist_insert, list(log_artist_set.itertuples(index=False, name=None)))
	database_wrapper.execute_batch_query(ancillary_song_insert, list(log_song_set.itertuples(index=False, name=None)))
	database_wrapper.execute_batch_query(timestamp_query, list(timestamp_unpacked_dataset))
	database_wrapper.execute_batch_query(songplay_query, list(songplay_dataset.itertuples(index=False, name=None)))

def unpack_timestamp(row):
	new_row = list(datetime.fromtimestamp(int(row[0] // 1000)).timetuple()[0: 7])
	new_row[-1] = new_row[-1] > 5
	new_row.extend(row)
	return tuple(new_row)
