import mysql.connector

plug = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lionelmessi1!",
    db = "menagerie",
    allow_local_infile=True
)
c = plug.cursor()
data =  """LOAD DATA LOCAL INFILE 'pet.txt'
INTO TABLE pet
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
(name, owner, species, sex, birth, death);"""
c.execute(data)
plug.commit()

c.execute("SELECT * FROM pet;")
str = c.fetchall()
for x in str:
    print(x)
c.close()
plug.close()