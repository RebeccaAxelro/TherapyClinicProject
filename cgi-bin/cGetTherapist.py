#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()                   
nameid = form.getvalue('therapistIDName')
therapistID = nameid.split(',')[0].strip()
name = nameid.split(',')[1].strip()

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# get therapist information
query = 'select * from therapist where therapistID = %s'
value = (therapistID,)
cursor.execute(query, value)
therapistInfo = cursor.fetchall()
for row in therapistInfo:
    print('<p>Therapists ID:' + str(row[0]) + '<br>')
    print('Therapists Name: ' + row[1] + '<br>')
    print('Therapists Eamil: ' + row[2] + '<br>')
    print('Therapists Room Number: ' + row[3] + '</p>')

print('</div>')
print('</body>')
print('</html>')


