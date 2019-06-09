import pandas as pd
from pandas.io.json import json_normalize
import json
from collections import defaultdict
pd.set_option('display.max_columns', 30)

class DataLoader:

	def __init__(self, matched_files):
		self.matched_files = matched_files

	def create_json_from_files(self):

		json_array = []
		value_dict = defaultdict(list)

		for f in self.matched_files:
			json_array.extend(fetch_json_data(f))

		for json in json_array:
			for key in json:
				value_dict[key].append(json[key])

		panda = pd.DataFrame.from_records(json_array)
		return panda



def fetch_json_data(filename):
		json_array = []
		with open(filename, 'r') as f:
			json_data = json.load(f)
			json_array.append(json_data)

		return json_array
	

