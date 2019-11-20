import pyodbc 
conn = pyodbc.connect(Driver='{SQL Server}',
                      Server='SQL-TEST\SQL-TEST',
                      Database='VBolsaTest74',
                      UID='consulta',
                      PWD='esmeralda130')

cursor = conn.cursor()
cursor.execute('SELECT * FROM db_name.Table')

for row in cursor:
    print(row)
