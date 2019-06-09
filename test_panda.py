from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
from lib.data_filter import DataFilter
import os



test_json_path = os.getcwd() + '/data/song_data/'
file_finder = FileFinder(test_json_path, '*.json')
data_loader = DataLoader(file_finder.return_file_names())
panda_json = data_loader.create_json_from_files()
print(panda_json.artist_id)
data_filter = DataFilter(panda_json)

print(data_filter.return_dicts_of_data())
