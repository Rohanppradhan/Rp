import mysql.connector

mydb= mysql.connector.connect(host="localhost",user="root",password="Pradhan@12")
if mydb:
 print("Connection created successfully")
else:
    print("Connection failed")
