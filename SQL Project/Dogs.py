import mysql.connector

plug = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lionelmessi1!",
    db = "menagerie",
)

c = plug.cursor()
c.execute("SELECT owner FROM pet;")
data = c.fetchall()
print(data)
c.close()
plug.close()