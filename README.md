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
  - GET tGet.py tGet2.py
    - Appointments
    - Therapist's information
    - Client's information tGetClient.py
    - Disorders
    - Treatments
  - CREATE tInsert.py tInsert2.py
    - Specialization tInsertSpecialization.py
    - Disorder tInsertDisorder.py
    - Treatment tInsertTreatment.py
 2: Client
  - GET cGet.py cGet2.py
    - Appointments
    - Client's information
    - Therapist's information cGetTherapist.py
    - Client's information
    - Disorders
    - Treatments
  - CREATE cInsert.py cInsert2.py
    - Diagnosis cInsertDiagnosis.py
    - Appointment cInsertAppointment.py
  - UPDATE cUpdate.py cUpdate2.py
    - Client's information cUpdateInfo.py
    - Appointment cUpdateAppointment.py
 3: CREATE new client newClient.py insertNewClient.py
 4: CREATE new therapist newTherapist.py insertNewTherapist.py
