#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()                   
nameid = form.getvalue('clientIDName')
clientID = nameid.split(',')[0].strip()
name = nameid.split(',')[1].strip()

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# get therapist information
query = 'select * from client  where clientID = %s'
value = (clientID,)
cursor.execute(query, value)
clientInfo = cursor.fetchall()
# NOT WORKING
for row in clientInfo:
    print('<p>clientID: ' + str(row[0])+ '<br>')
    print('Cleint Name: ' + row[1] + '<br>')
    print('Address: ' + row[2] + '<br>')
    print('Email: ' + row[3] + '<br>')
    print('Phone Number: ' + row[4] + '</p>')

print('</div>')
print('</body>')
print('</html>')


