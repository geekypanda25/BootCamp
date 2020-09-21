import mysql.connector
from pandas import DataFrame
import pyarrow as pya
import pyarrow.parquet as pyq
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2508",
    database = "employees"
)
mydbcur = mydb.cursor()

mydbcur.execute("SELECT emp_no, birth_date, first_name, last_name, gender, hire_date")

df = DataFrame(mydbcur.fetchall())
df.columns= mydbcur.column_names

table_pandas = pya.Table.from_pandas(df)
pyq.write_table(table_pandas, "employees_pq")

