#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()                    
treatmentName = form.getvalue('treatmentName')


# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# Insert treatment                        
query = 'insert into treatment(treatmentName) values (%s)'
value = (treatmentName)
cursor.execute(query, value)
cnx.commit()


print('<p>IT WORKS</p>')        
print('</div>')
print('</body>')
print('</html>')


