#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# Connecting to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()                   
get = form.getvalue('get') 
nameid = form.getvalue('clientIDName')
clientID = str(nameid).split(',')[0].strip()
name = str(nameid).split(',')[1].strip()

# start of html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# get information
if get == 'myInfo':
    query = 'select clientID, name, address, phoneNumber, email, disorderName from client natural join diagnosed natural join disorder where clientID = %s'
    value = (clientID,)
    cursor.execute(query, value)
    clientInfo = cursor.fetchall()
    for row in clientInfo:
        print('<p>Your ID: ' + str(row[0]) + '<br>')
        print('Your Name: ' + row[1] + '<br>')
        print('Your Address: ' + row[2] + '<br>')
        print('Your Phone Number: ' + row[3] + '<br>')
        print('Your Email: ' + row[4] + '<br>')
        print('Your Diagnosis: ' + row[5] +'</p>' + '<br>')

# get appointment
elif get == 'appointment':
    query = 'select name, date, duration from appointment natural join therapist where clientID = %s'
    value = (clientID,)
    cursor.execute(query, value)
    clientAppInfo = cursor.fetchall()
    for row in clientAppInfo:
        print('<p> Therapist: ' + row[0] + '<br>')
        print('Date: ' + str(row[1]) + '<br>')
        print('Duration: ' + row[2] + '</p>')
 
# select your therapist
elif get == 'therapistInfo':
    query = 'select therapistID, name from therapist'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('<form action="cGetTherapist.py">')
    print('<p>Please select your therapists id/name:</p>')
    print('<select name="therapistIDName">')
    for i in rows:
        print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
    print ('</select>')
    print('<input type="submit" value="Submit">')
    print('</form>')

print('</div>')
print('</body>')
print('</html>')


