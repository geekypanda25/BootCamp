import mysql.connector
from pandas import DataFrame
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import collections

avrosc = avro.schema.parse(open("employ.avsc", "rb").read())

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

writer = DataFileWriter(open("employees.avro", "wb"), DatumWriter(), avrosc )
for index,row in df.iterrows():
    data = collections.OrderDict()
    data['emp_no'] = row["emp_no"]
    data['birth_date'] = row["birth_date"]
    data['first_name'] = row["first_name"]
    data['last_name'] = row["last_name"]
    data['gender'] = row["gender"]
    data['hire_date'] = row["hire_date"]
    writer.append(data)
writer.close()