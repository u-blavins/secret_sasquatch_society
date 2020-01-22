import pyodbc
from sqlalchemy import create_engine
import urllib

server = 'secretsasquatchsociety.database.windows.net'
database = 'sasquatch'
username = 'Sasquatch'
password = 'Whadyatalkinabeet1'
driver = '{ODBC Driver 17 for SQL Server}'


cnxn = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
params = urllib.quote_plus(cnxn)
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str, echo=True)

print('connection is ok')
print(engine_azure.table_names())