--------------read me-------------------------

********************************************************************************************

SQLLITE3 DATABASE:

Make sure you should follow below commands to use mysql database in your django project

1. Django will take default database i.e. sqllite3

2. Check in settings.py file for reference at DATABASES (line number 78 to 83)


********************************************************************************************

Modules:

   I have used bellow modules in this project

  1. Django modules
  2. Serializers module
  3. rest_framework
  4. .serilizers

********************************************************************************************


EXPLANATION:

-> Created django project name (smsTask) and inside this created app name (eaf)

-> Implemented urls, views and models.

-> created superuser as admin, below are the credentials.
   Admin User name : admin
   password: 12345678
   * have given all permission that admin can delete, edit and add
 
-> used serilizers file for implement rest api


********************************************************************************************

POSTMAN Details:

task 1: Get all chemical elements
    API URL (http://127.0.0.1:8000/eaf/task-list/)
    Content-Type : application/json
    METHOD : GET
    JSON SAMPLE PAYLOAD:
       {
        "id": 2,
        "name": "B"
    	}


task 2:  Get a commodity by id
    API URL (http://127.0.0.1:8000/eaf/task-detailcomm/1/)
    Content-Type : application/json
    METHOD : PUT
    JSON SAMPLE PAYLOAD:
       {
          "id": 1,
          "name": "AA",
          "inventory": 203,
          "price": 181,
          "chemical_composition": 11
     }
	

task 3:  Update commodity by id
    API URL (http://127.0.0.1:8000/eaf/task-updatecomm/1/)
    Content-Type : application/json
    METHOD : PUT
    JSON SAMPLE PAYLOAD:
       {
          "id": 2,
          "name": "AAAAA",
          "inventory": 202,
          "price": 185,
          "chemical_composition": 17
     }


task 4:  Add and remove chemical concentration
    API URL (http://127.0.0.1:8000/eaf/task-deletecomm/1/)
    Content-Type : application/json
    METHOD : DELETE
    JSON SAMPLE PAYLOAD:
       {
          "id": 2,
          "name": "AAAAA",
          "inventory": 202,
          "price": 185,
          "chemical_composition": 17
     }

********************************************************************************************




