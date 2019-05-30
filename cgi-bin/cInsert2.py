#!/usr/bin/python3  
import mysql.connector
from mysql.connector import errorcode     
import cgi

# connect to DB
cnx = mysql.connector.connect(user='raxelro1', database='raxelro11', host='localhost', password='rikikiki98')
cursor = cnx.cursor()

# get values from form
form = cgi.FieldStorage()                   
insert = form.getvalue('insert') 
nameid = form.getvalue('clientIDName')
clientID = nameid.split(',')[0].strip()
name = nameid.split(',')[1].strip()

# start html
print('Content-type:text/html\r\n\r\n')         
print('<html>')
print('<body>')
print('<div>')

# insert appointment- select your therapist, treatment and insert date, duration
if insert == 'appointment':
    query = 'select therapistID, name from therapist'
    cursor.execute(query)
    therapistIDName= cursor.fetchall()
    print('<form action="cInsertAppointment.py">')
    print('Your ID: <input type="text" name="clientID" value="' + clientID + '" readonly><br>')
    print('<p>Select your therapist:</p>')
    print('<select name="therapistIDName">')
    for i in therapistIDName:
        print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
    print ('</select>')
    print('<br>')
    print('<p>Select your treatment:</p>')
    query = 'select treatmentID, treatmentName from treatment'
    cursor.execute(query)
    treatmentIDName= cursor.fetchall()
    print('<select name="treatmentIDName">')
    for i in treatmentIDName:
        print('<option>' + str(i[0]) + ',' + i[1] + '</option>')
    print ('</select>')
    print('<br><br>')
    print('Date: (format: yr-month-day hour:minute:seconds ex: 2019-06-02 13:00:00 <br>')
    print('<input type="text" name="date" >')
    print('<br>')
    print('Duration: <br>')
    print('<input type="text" name="duration" >')
    print('<br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>') 

# insert diagnosis    
elif insert == 'diagnosis':
    query = 'select disorderCode, disorderName from disorder'
    cursor.execute(query)
    disorderCodeName= cursor.fetchall()
    print('<form action="cInsertDiagnosis.py">')
    print('Your ID: <input type="text" name="clientID" value="' + clientID + '" readonly><br>')
    print('<select name="disorderCodeName">')
    for i in disorderCodeName:
        print('<option>' + i[0] + ',' + i[1] + '</option>')
    print ('</select>')
    print('<br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>')
    
print('</div>')
print('</body>')
print('</html>')
