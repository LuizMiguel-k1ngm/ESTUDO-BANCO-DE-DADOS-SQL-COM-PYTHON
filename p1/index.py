import sqlite3
banco = sqlite3.connect("primeiro.bamco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")

#cursor.execute("INSERT INTO pessoas VALUES('Aline', 22, 'aline_123@gmail.com')")


#banco.commit()

 cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) 