import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2508",
    database = "employees"
)
mydbcur = mydb.cursor()

mydbcur.execute("SELECT emp_no, birth_date, first_name, last_name, gender, hire_date")


outf = open('employ.xml', 'w')
outf.write('<?xml version="1.0" ?>\n <employ>\n')
for row in mydbcur.fetchall():
    outf.write('<row>\n')
    outf.write('<emp_no>%s</emp_no>\n' % row[0])
    outf.write('<birth_date>%s</birth_date>\n' % row[1])
    outf.write('<first_name>%s</first_name>\n' % row[2])
    outf.write('<last_name>%s</last_name>\n' % row[3])
    outf.write('<gender>%s</gender>\n' % row[4])
    outf.write('<hire_date>%s</hire_date>\n' % row[5])
    outf.write('</row\n')
outf.write('</employ>\n')
outf.close()
