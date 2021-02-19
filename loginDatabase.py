import sqlite3

with sqlite3.connect("login.db") as db:
  cursor = db.cursor()

#cursor.execute(""" DROP TABLE USER""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS user (
  userID INTEGER PRIMARY KEY,
  username VARCHAR(20) NOT NULL,
  firstname VARCHAR(20) NOT NULL,
  surname VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL,
  position VARCHAR(20) NOT NULL,
  grade VARCHAR(20) NULL,
  plagarized VARCHAR(20) NOT NULL)
""")

cursor.execute("""INSERT INTO user (username, firstname, surname, password, position, grade, plagarized)
VALUES("test_user", "Sharujan", "Muthu", "test", "student",'' , 'False')
""")

db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())