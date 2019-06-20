import psycopg2
from psycopg2.extras import execute_batch

class DatabaseWrapper:

	def __init__(self):

		try:
			self.conn = psycopg2.connect('dbname=sparkifydb user=danielwork')
			self.conn.autocommit=True
			self.cursor = self.conn.cursor()
		except:
			print('Unable to connect to the DB')
			exit(1)
		
	def execute_batch_query(self, query, dataset):

		try:
			execute_batch(self.cursor, query, dataset)
		except Exception as e:
			print('Unable to execute query')
			print(e)
			exit(1)

	def execute_single_query(self, query, data = None, action='read'):
		
		try:
			if action == 'read' and not data:
				return self.cur.execute(query)
			else:
				self.cur.execute(query, data)
		except Exception as e:
			print('Unable to execute query')
			print(e)
			exit(1)


