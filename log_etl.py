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

	user_query = 'insert into f_app_user (first_name, last_name, gender, level) values (%s, %s, %s, %s)'

	database_wrapper = DatabaseWrapper()
	database_wrapper.execute_batch_query(user_query, list(users.itertuples(index=False, name=None)))

