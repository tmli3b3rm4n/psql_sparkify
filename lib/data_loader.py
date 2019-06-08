import pandas as pd

class DataLoader:

	def __init__(self, matched_files):
		self.matched_files = matched_files

	def create_json_from_files(self):
		return map(fetch_json_data, self.matched_files)


def fetch_json_data(data):
	return pd.read_json(data, lines=True)