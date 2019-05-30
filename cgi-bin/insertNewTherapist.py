#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()                   
name = form.getvalue('name')
email = form.getvalue('email')
room_no = form.getvalue('room_no')

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# Insert therapist
query = 'insert into therapist(name, email, room_no) values (%s, %s, %s)'
value = (name, email, room_no)
cursor.execute(query, value)
cnx.commit()

print('<p>IT WORKS</p>')        
print('</div>')
print('</body>')
print('</html>')


