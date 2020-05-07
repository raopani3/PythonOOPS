import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="test123")
mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)
mycursor.execute("use sakila")
result = mycursor.execute("select * from actor")
for i in result:
    print(result)