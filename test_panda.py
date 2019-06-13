from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
import os

test_json_path = os.getcwd() + '/data/song_data/'
file_finder = FileFinder(test_json_path, '*.json')
data_loader = DataLoader(file_finder.return_file_names())
panda_json = data_loader.create_json_from_files()

artists = panda_json.loc[:, 'artist_name']
print(artists)

