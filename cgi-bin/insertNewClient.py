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
address = form.getvalue('address')
email = form.getvalue('email')
phoneNumber = form.getvalue('phoneNumber')

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# Insert client
query = 'insert into client(name, address, email, phoneNumber) values (%s, %s, %s, %s)'
value = (name, address, email, phoneNumber)
cursor.execute(query, value)
cnx.commit() 

print('<p>IT WORKS</p>')        
print('</div>')
print('</body>')
print('</html>')


