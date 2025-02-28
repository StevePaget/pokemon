import sqlite3 as sql


db = sql.connect("pokemon.db")
c = db.cursor()

c.execute("DROP TABLE IF EXISTS Pokemon")
c.execute("CREATE TABLE Pokemon (ID INTEGER, name TEXT, type1 TEXT, type2 TEXT, hp INTEGER, attack INTEGER, defence INTEGER, speed INTEGER)")

f = open("pokemon.csv","r")
for line in f:
    bits = line.split(",")
    c.execute("INSERT INTO Pokemon VALUES (?,?,?,?,?,?,?,?)", bits)    
db.commit()

print("Made Database")

c.execute("DROP TABLE IF EXISTS Player")
c.execute("CREATE TABLE Player (ID INTEGER PRIMARY KEY )")

c.execute("INSERT INTO Player VALUES (23)")
c.execute("INSERT INTO Player VALUES (123)")
c.execute("INSERT INTO Player VALUES (87)")
db.commit()

