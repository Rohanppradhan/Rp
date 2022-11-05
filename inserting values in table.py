import mysql.connector

#connection.object
mydb =mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="Pradhan@12",
                                  database="STUDENT1")
mycursor=mydb.cursor()

"""name=input("Enter the name:")
salary=int(input("Enter the salary:"))
emp_id=input("Enter the emp_id:")
Address=input("Enter the adderss:")"""

#Inserting values into tables

s="INSERT INTO emp(name,salary,emp_id,Address) VALUES  (%s,%s,%s,%s)"
b1=("rohan",309,"rohan123","Cuttack")
mycursor.execute(s,b1)
mydb.commit()




