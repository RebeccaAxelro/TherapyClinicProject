#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# connect to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# sql staments and execution
sql1 = 'select therapistID, name from therapist'
cursor.execute(sql1)
therapistIDName= cursor.fetchall()

# start html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# form: what to insert, select your id/name
print('<form action="tInsert2.py">')
print('<p>Please select what you want to insert:</p>')
print('<input type="radio" name="insert" value="specializes"> New specialization<br>')
print('<input type="radio" name="insert" value="disorder"> New disorder<br>')
print('<input type="radio" name="insert" value="treatment"> New Treatment<br>')
print('<select name="therapistIDName">')
for i in therapistIDName:
  print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
print ('</select>')
print('<input type="submit" value="Submit">')
print('</form>')

print('</div>')
print('</body>')
print('</html>')
