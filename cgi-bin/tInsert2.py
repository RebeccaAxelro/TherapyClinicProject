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
nameid = form.getvalue('therapistIDName')
therapistID = nameid.split(',')[0].strip()
name = nameid.split(',')[1].strip()

# start html
print('Content-type:text/html\r\n\r\n')         
print('<html>')
print('<body>')
print('<div>')

# insert disorder
if insert == 'specializes':
    print('<form action="tInsertSpecialization.py">')
    print('Your ID: <input type="text" name="therapistID" value="' + therapistID + '" readonly><br>')
    print('<p>Select your specialization:</p>')
    query = 'select disorderCode, disorderName from disorder'
    cursor.execute(query)
    disorderCodeName= cursor.fetchall()
    print('<select name="disorderCodeName">')
    for i in disorderCodeName:
        print('<option>' + i[0] + ',' + i[1] + '</option>')
    print ('</select>')
    print('<br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>') 

# insert disorder 
elif insert == 'disorder':
    print('<form action="tInsertDisorder.py">')
    print('Disorder Code: Look at DSM-5 <br>')
    print('<input type="text" name="disorderCode" >')
    print('<br>')
    print('Disorder Name: Look at DSM-5<br>')
    print('<input type="text" name="disorderName" >')
    print('<br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>')

# insert treatment                                                              
elif insert == 'treatment':
    print('<form action="tInsertTreatment.py">')
    print('Treatment Name: <br>')
    print('<input type="text" name="treatmentName" >')
    print('<br>')
    print('<br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>')
    
print('</div>')
print('</body>')
print('</html>')


