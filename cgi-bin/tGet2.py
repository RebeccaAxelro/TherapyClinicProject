#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# connect to db
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get form values
form = cgi.FieldStorage()                        
get = form.getvalue('get') 
nameid = form.getvalue('therapistIDName')
therapistID = str(nameid).split(',')[0].strip()
name = str(nameid).split(',')[1].strip()

# html
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# get therapist's information
if get == 'myInfo':
    query = 'select therapistID, name, email, room_no, disorderName from therapist natural join specializes natural join disorder where therapistID = %s'
    value = (therapistID,)
    cursor.execute(query, value)
    therapistInfo = cursor.fetchall()
    for row in therapistInfo:
        print('<p>Your ID:' + str(row[0]) + '<br>')
        print('Your  Name: ' + row[1] + '<br>')
        print('Your Eamil: ' + row[2] + '<br>')
        print('Your Room Number: ' + row[3] + '<br>')
        print('Your Specialization: ' + row[4] + '</p>') 
# get appointment information
elif get == 'appointment':
    query = 'select name, date, duration from appointment natural join client where therapistID = %s'
    value = (therapistID,)
    cursor.execute(query, value)
    therapistAppInfo = cursor.fetchall()
    for row in therapistAppInfo:
        print('<p>Your clients name: ' + row[0] + '<br>')
        print('Date: ' + str(row[1]) + '<br>')
        print('Duration: ' + row[2] + '</p>')
        
# get client's  info    
elif get == 'clientInfo':
    query = 'select clientID, name from client'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('<form action="tGetClient.py">')
    print('<p>Please select your clients id/name:</p>')
    print('<select name="clientIDName">')
    for i in rows:
        print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
    print ('</select>')
    print('<input type="submit" value="Submit">')
    print('</form>')

# get disorder info
elif get == 'disorder':
    query = 'select * from disorder'
    cursor.execute(query)
    disorder = cursor.fetchall()
    for row in disorder:
       print('<p>Disorder Code: ' + row[0] + '<br>')
       print('Disorder Name: ' + row[1] + '</p>')

# get treatment info
elif get == 'treatment':
    query = 'select * from treatment'
    cursor.execute(query)
    treatment = cursor.fetchall()
    for row in treatment:
        print('<p>Treatment ID: ' + str(row[0]) + '<br>')
        print('Treatment Name: ' + row[1] + '</p>')

print('</div>')
print('</body>')
print('</html>')


