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
print(' <form action="insertNewTherapist.py">')
print('Name:<br>')
print('<input type="text" name="name" >')
print('<br>')
print('Email: first letter of your first name then last name @pathsahead.com<br>')
print('<input type="text" name="email" >')
print('<br>')
print('Room Number: 101-110 or 201-210<br>')
print('<input type="text" name="room_no" >')
print('<br><br>')
print('<input type="submit" value="Submit">')
print('</form>') 
print('</div>')
print('</body>')
print('</html>')


