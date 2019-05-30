#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# connect to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# sql queries
sql1 = 'select therapistID, name from therapist'
cursor.execute(sql1)
therapistIDName= cursor.fetchall()

#start html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# form: which get do you want to do
print('<form action="tGet2.py">')
print('<p>Please select what you want to get:</p>')
print('<input type="radio" name="get" value="myInfo"> Get my information<br>')
print('<input type="radio" name="get" value="appointment"> Get my appoinments<br>')
print('<input type="radio" name="get" value="clientInfo"> Get my clients information<br>')
print('<input type="radio" name="get" value="disorder"> Get disorders<br>')
print('<input type="radio" name="get" value="treatment"> Get Treatments<br>')
print('<select name="therapistIDName">')
for i in therapistIDName:
  print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
print ('</select>')
print('<input type="submit" value="Submit">')
print('</form>')

print('</div>')
print('</body>')
print('</html>')
