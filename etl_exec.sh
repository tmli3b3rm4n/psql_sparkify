source venv_psql_sparkify/bin/activate
psql -U danielwork -d sparkifydb  -a -f sql/drop_table.sql 
psql -U danielwork -d sparkifydb  -a -f sql/create_table.sql
rm output.txt && python test_panda.py >> output.txt