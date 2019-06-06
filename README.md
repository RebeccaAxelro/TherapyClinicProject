# TherapyClinicProject

Introduction: I built a web application with a MySQL database backend with HTML, CSS and Python. I built a therapy clinic with various entities and relationships.

ER Diagram: https://docs.google.com/document/d/1TR6Gui6ln7qAEFgcX39bbOp1EskyT8EmjlKTlBWbcDI/edit?usp=sharing

To run: http://ada.sterncs.net/~raxelrod/therapyclinic.html (Run on ada, server that we used in this course)

Frontend done in HTML and CSS: 
  Homepages: therapyclinic.html homepage.css
  Userpage: client.html therapist.html userpage.css
  
Within cgi-bin:
 - Have different python files embedded with html 
 - Does CRUD based on the differnt types of scenerios, based on which action and values are submitted.
 
 - Scenerios:
 1: Therapist
  a. GET tGet.py tGet2.py
    1. Appointments
    2. Therapist's information
    3. Client's information tGetClient.py
    4. Disorders
    5. Treatments
  b. CREATE tInsert.py tInsert2.py
    1. Specialization tInsertSpecialization.py
    2. Disorder tInsertDisorder.py
    3. Treatment tInsertTreatment.py
 2: Client
  a. GET cGet.py cGet2.py
    1. Appointments
    2. Client's information
    3. Therapist's information cGetTherapist.py
    3. Client's information
    4. Disorders
    5. Treatments
  b. CREATE cInsert.py cInsert2.py
    1. Diagnosis cInsertDiagnosis.py
    2. Appointment cInsertAppointment.py
  c. UPDATE cUpdate.py cUpdate2.py
    1. Client's information cUpdateInfo.py
    2. Appointment cUpdateAppointment.py
 3: CREATE new client newClient.py insertNewClient.py
 4: CREATE new therapist newTherapist.py insertNewTherapist.py
