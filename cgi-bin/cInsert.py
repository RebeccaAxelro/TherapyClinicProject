#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# sql statments and execution
sql1 = 'select clientID, name from client'
cursor.execute(sql1)
rows = cursor.fetchall()

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# form: what you want to get, select your id/name
print('<form action="cInsert2.py">')
print('<p>Please select what you want to insert:</p>')
print('<input type="radio" name="insert" value="appointment"> New appoinment<br>')
print('<input type="radio" name="insert" value="diagnosis"> New diagnosis<br>')
print('<p>Please select your id/name:</p>')
print('<select name="clientIDName">')
for i in rows:
  print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
print ('</select>')
print('<input type="submit" value="Submit">')
print('</form>')

print('</div>')
print('</body>')
print('</html>')
