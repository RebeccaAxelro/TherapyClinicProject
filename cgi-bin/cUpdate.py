#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# connect to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# sql staments and execution
sql1 = 'select clientID, name from client'
cursor.execute(sql1)
clientIDName= cursor.fetchall()

# start html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# form: what to update, select your id/name
print('<form action="cUpdate2.py">')
print('<p>Please select what you want to update:</p>')
print('<input type="radio" name="update" value="information"> Update my information<br>')
print('<input type="radio" name="update" value="appointment"> Update my  appointments<br>')
print('<select name="clientIDName">')
for i in clientIDName:
  print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
print ('</select>')
print('<input type="submit" value="Submit">')
print('</form>')

print('</div>')
print('</body>')
print('</html>')
