from django.db import models
# import csv


class Branches(models.Model):
    
    ifsc       = models.CharField(max_length=1009)
    bank_id    = models.IntegerField()
    branch     = models.CharField(max_length=1009)
    address    = models.CharField(max_length=1500)
    city       = models.CharField(max_length=1999)
    district   = models.CharField(max_length=1999)
    state      = models.CharField(max_length=1000)
    bank_name  = models.CharField(max_length=1000)


    def __str__(self):
        return self.branch



class SDB:
    __db_conn = None   

    # Checking connection and creation one connection to db
    @staticmethod
    def getConnection():
        if SDB.__db_conn is None:
            pass
        return SDB.__db_conn

    # Closing connection
    @staticmethod
    def closeConnection():
        if SDB.__db_conn is not None:
            SDB.__db_conn.close()
            SDB.__db_conn = None

# import csv
# import psycopg2
# conn = psycopg2.connect("host=bx3yjvolaogctsuoox9n-postgresql.services.clever-cloud.com dbname=bx3yjvolaogctsuoox9n user=uqhxlypcswjebrbpkdxj password=6CFVpxBx6Qa5ftlExnx4")
# cur = conn.cursor()

# with open('C:/Users/Desktop/indian_banks/bank_branches.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader) # Skip the header row.
#     for row in reader:
        
#         conn.commit()
#         SDB.closeConnection()



# not required now

# import pyodbc
# # No. Longer Required. Used to upload csv content to postgres table via Django Model.
# data = csv.DictReader(open("C:/Users/Desktop/indian_banks/bank_branches.csv"))
# for row in data:
#     Branches.objects.create(ifsc=row['ifsc'], bank_id=row['bank_id'], branch=row['branch'], address=row['address'], city=row['city'], district=row['district'], state=row['state'], bank_name=row['bank_name'])
#     SDB.closeConnection()
# data.close()


