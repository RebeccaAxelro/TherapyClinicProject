#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')

cursor = cnx.cursor()


print('Content-type:text/html\r\n\r\n')                                           
print('<html>')
print('<body>')
print('<div>')
print(' <form action="insertNewClient.py">')
print('Name:<br>')
print('<input type="text" name="name" >')
print('<br>')
print('Address:<br>')
print('<input type="text" name="address" >')
print('<br>')
print('Email:<br>')
print('<input type="text" name="email" >')
print('<br>')
print('phoneNumber:<br>')
print('<input type="text" name="phoneNumber" >')
print('<br><br>')
print('<input type="submit" value="Submit">')
print('</form>') 
print('</div>')
print('</body>')
print('</html>')


