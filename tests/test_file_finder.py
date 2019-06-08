import unittest
from lib.file_finder import FileFinder

class TestFileFinder(unittest.TestCase):

	def test_file_finder_finder(self):
		file_finder = FileFinder('foo_dir', '.txt')
		self.assertEqual(file_finder.start_directory, 'foo_dir')
		self.assertEqual(file_finder.file_type, '.txt')

