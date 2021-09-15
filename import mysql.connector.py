import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping database MYDATABASE if already exists.
cursor.execute("DROP database IF EXISTS MyDatabase")

#Preparing query to create a database
sql = "CREATE database MYDATABASE";

#Creating a database
cursor.execute(sql)

#Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())