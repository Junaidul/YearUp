import mysql.connector

plug = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lionelmessi1!",
    db = "menagerie",
)

c = plug.cursor()
c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
data = c.fetchall()
for x in data:
    print(x)

c.close()
plug.close()