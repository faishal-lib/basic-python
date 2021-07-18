import mysql.connector

#connect to mysql-server with mysql-connector (using xampp)
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

#create new database
cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_super")

print("Berhasil membuat database")
