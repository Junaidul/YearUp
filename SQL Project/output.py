import mysql.connector

plug = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lionelmessi1!",
    db = "menagerie",
)

c = plug.cursor()
c.execute("SELECT name, birth, MONTH(birth) FROM pet;")
data = c.fetchall()
for x in data:
    print(x)
c.close()
plug.close()