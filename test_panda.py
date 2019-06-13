from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
import os
from sqlalchemy import create_engine

test_json_path = os.getcwd() + '/data/song_data/'
file_finder = FileFinder(test_json_path, '*.json')
data_loader = DataLoader(file_finder.return_file_names())
panda_json = data_loader.create_json_from_files()

artists = panda_json[['artist_name', 'artist_location', 'artist_longitude', 'artist_latitude']]
songs = panda_json[['title', 'year', 'duration', 'song_id']]
print(list(songs.itertuples(name=None)))

# try:
# 	engine = create_engine('postgresql://danielwork:Travel2015!@localhost:5432/sparkifydb')
# 	artists.to_sql('f_artist', if_exists='append', con=engine)
# except AttributeError as e:
# 	print('error inserting data into the db: ')
# 	print(e)
# 	exit(1)
