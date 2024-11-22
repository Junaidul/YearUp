import mysql.connector

plug = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lionelmessi1!"
)

c = plug.cursor()
c.execute("CREATE DATABASE menagerie")
c.execute("USE menagerie")
c.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);")
c.execute("DESCRIBE pet")
data = c.fetchall()
for x in data:
    print(x)

c.close()
plug.close()