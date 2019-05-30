#!/usr/bin/python3  

import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11',host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()                   
clientID=form.getvalue('clientID')
therapistIDName = form.getvalue('therapistIDName')
therapistID = therapistIDName.split(',')[0].strip()
treatmentIDName = form.getvalue('treatmentIDName')
treatmentID = treatmentIDName.split(',')[0].strip()
date = form.getvalue('date')
duration = form.getvalue('duration')


# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# Insert appointment
query = 'insert into appointment(clientID, therapistID, treatmentID, date, duration) values (%s, %s, %s, %s, %s)'
value = (clientID, therapistID, treatmentID, date, duration)
cursor.execute(query, value)
cnx.commit() 

print('<p>You inserted an appointment successfully!</p>')        
print('</div>')
print('</body>')
print('</html>')


