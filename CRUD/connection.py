import mysql.connector

#connect to mysql-server with mysql-connector (using xampp)
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

#if succesfully connected
if db.is_connected():
  print("Connected With Database")
