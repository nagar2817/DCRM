import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ROHit@2817',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Nagar")

print("All done! , you can verify in mysql workdbench")