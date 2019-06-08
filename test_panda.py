import pandas as pd
import psycopg2
import os
import glob
from lib.file_finder import FileFinder

test_json_path = os.getcwd() + '/data/song_data/'
print(test_json_path)
file_finder = FileFinder(test_json_path, '*.json')

print('\n'.join(file_finder.return_file_names()))
