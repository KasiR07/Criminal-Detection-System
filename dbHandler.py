
import mysql.connector

def getConnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="crimerecords"
    )

def insertData(data):
    pass

def retrieveData(name):
    pass
