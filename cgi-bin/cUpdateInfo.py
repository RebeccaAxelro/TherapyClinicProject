#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()
clientID = form.getvalue('clientID')
address = form.getvalue('address') 
phoneNumber = form.getvalue('phoneNumber')
email = form.getvalue('email')

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# Update
query = 'UPDATE client SET address = %s, phoneNumber = %s, email = %s WHERE clientID=%s'
value = (address, phoneNumber, email, clientID)
cursor.execute(query, value)
cnx.commit()

print('<p>IT WORKS</p>')        
print('</div>')
print('</body>')
print('</html>')


