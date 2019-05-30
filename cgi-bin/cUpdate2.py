#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# connect to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

#get values from form
form = cgi.FieldStorage()                 
update = form.getvalue('update') 
nameid = form.getvalue('clientIDName')
nameidsplit = nameid.split(',')
clientID = nameidsplit[0].strip()
name = nameidsplit[1].strip()

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
print('<div>')

# update your information
if update == 'information':
    print('<form action="cUpdateInfo.py">')
    print('Your ID: <input type="text" name="clientID" value="' + clientID + '" readonly><br>')
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

# update your appointment - not working
elif update == 'appointment':
    sql1 = 'select * from appointment where clientID = %s'
    value = (clientID,)
    cursor.execute(sql1)
    rows = cursor.fetchall()
    print('<form action="cUpdateAppointment.py">')
    print('Your ID: <input type="text" name="clientID" value="' + clientID + '" readonly><br>')
    print('<p>Please select your Appointment:</p>')
    print('<select name="appointment">')
    for i in rows:
        print('<option>' + str(i[0]) + ',' + str(i[4]) + ',' + i[5] + '</option>')
    print ('</select>')
    print('<input type="submit" value="Submit">')
    print('</form>')
    
print('</div>')
print('</body>')
print('</html>')


