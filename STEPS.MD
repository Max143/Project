
REST web-Servcice Project Build form the scracth
-----------------------------------------------------------------------

Programming Language Used : Python Programming
Framework :  Django Framework
REST  : Django OPEN REST FRAMEWORK
DATABASE : PostgreSQL
Application Hosting : HEROKU cloud platform
Database Hosting : Clever-Cloud paltform
------------------------------------------------------------------------

STEP : 1

 - Web Service has all the funcationlity of CRUD.

        - C : CREATE Resources  Using  POST Method
        - R : RETRIEVE Respources using API Uisng GET Method
        - U : UPDATE Resources Using PUT Mehtod
        - D : DELETE Resources Using DELETE Method
-------------------------------------------------------------------------

STEP : 2

 -Testing :


Tested On DB.sqlite3 database. Test successful.
---------------------------------------------------------------------------

STEP : 3

 - Database Engine Change to PostgreSQL :

 Used PostgreSQL. 
----------------------------------------------------------------------------

STEP : 4 

 - Django Application Hosted on HEROKU  as instructed in Problem Statement.


 Link : https://bank-dir.herokuapp.com/api/
------------------------------------------------------------------------------

STEP : 5

 - DATABASE (PostgreSQL) Hosted on Clever-Cloud Platform

 Instance of PostgreSQL Creted on Clever-Cloud Platform and 
-------------------------------------------------------------------------------

STEP :  6

 - DATABASE HOST and Engine Change to Clever-Cloud Platform


In settings.py file, Database engine change to connect the hosted heroku applicaton with the database on 
Clever-Cloud Platform

# Data using Postgresql hosted on Clever-cloud 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bcfdjybghqxj8izvykql',
            'USER': 'u80egqq3wxhcjatntshf',
            'PASSWORD': 'u80egqq3wxhcjatntshf',
            'HOST': 'bcfdjybghqxj8izvykql-postgresql.services.clever-cloud.com',
            'PORT': '5432',
        }
    }
    # Database using Postgresql hosted on Heroku for testing purpose 
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'Bank',
    #         'USER': 'postgres',
    #         'PASSWORD': 'silverstone143',
    #         'HOST': '127.0.0.1',
    #         'PORT': '5432',
    #     }
    # }

 -------------------------------------------------------------------------------

STEP 7 


- TESTED 


- Application can access postgresql database hosted on clever-cloud platform and 
  api given in calling problem statement is successfully retreving result similiar to given
  in problem statement.
-------------------------------------------------------------------------------------------
