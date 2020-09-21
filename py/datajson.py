import mysql.connector
import json
import collections
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2508",
    database = "employees"
)
mydbcur = mydb.cursor()

mydbcur.execute("SELECT emp_no, birth_date, first_name, last_name, gender, hire_date")

row_list = []
for row in mydbcur.fetchall():
    data = collections.OrderedDict()
    data['emp_no']=row[0]
    data['birth_date']=row[1]
    data['first_name']=row[2]
    data['last_name']=row[3]
    data['gender']=row[4]
    data['hire_date']=row[5]
    row_list.append(data)
js = json.dumps(row_list)
fil = 'employ.json'
f = open(fil, 'w')
print(js, file=f)
