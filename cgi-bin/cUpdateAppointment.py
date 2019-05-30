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
appointmentID = form.getvalue('appointment').split(',')[0].strip() 
date = form.getvalue('date')
duration = form.getvalue('duration')

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# UPDATE appointment- not working(cant get to this py file yet)
query = 'UPDATE appointment SET date = %s, duration = %s WHERE appointmentID=%s'
value = (date, duration)
cursor.execute(query, value)
cnx.commit()

print('<p>IT WORKS</p>')        
print('</div>')
print('</body>')
print('</html>')


