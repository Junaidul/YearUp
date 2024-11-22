import mysql.connector

plug = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lionelmessi1!"
)

c = plug.cursor()
c.execute("DROP DATABASE IF EXISTS menagerie")
c.execute("SHOW DATABASES")
command = c.fetchall()
for x in command:
    print(x)


c.close()
plug.close()