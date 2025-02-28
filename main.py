import sqlite3 as sql
#import makeDatabase

db = sql.connect("pokemon.db")
c = db.cursor()


# c.execute("UPDATE Pokemon SET hp = hp + 100 WHERE type1 ='Water'")
# db.commit()

# c.execute("DELETE FROM Pokemon WHERE type1 = 'Water'")

# c.execute("SELECT * FROM Pokemon WHERE type1 = 'Water'  ORDER BY hp DESC LIMIT 10    ")
# results = c.fetchall()


print("Welcome to Pokemon (text only version)")
print("You must capture the entirety of the population!")
id = int(input("Which Pokemon ID do you want?"))

#execute an SQL query to find the pokemon matching that ID
#print the name on the screen

c.execute("SELECT name FROM Pokemon WHERE ID = ?", (id,))

results = c.fetchall()
print(results[0][0])

catch = input("Would you like to catch this?")
if catch.lower().startswith("y"):
   # add this pokemon ID to the player table
   c.execute("INSERT INTO Player VALUES (?)", (id,))
   db.commit()

print("You now have...")
# print out all the IDs in the player's collection 
c.execute("SELECT Pokemon.name FROM Pokemon, Player WHERE Player.ID = Pokemon.ID")
results = c.fetchall()
for line in results:
   print("   " + str(line[0]))

deleted = input("Name a pokemon to remove: ")

# write a query to remove this pokemon from the player's collection
# if it is there
c.execute("DELETE FROM Player WHERE Player.ID IN (SELECT ID from Pokemon WHERE name = ?)", (deleted,))
db.commit()

print("You now have...")

# print out all the IDs in the player's collection 
c.execute("SELECT Pokemon.name FROM Pokemon, Player WHERE Player.ID = Pokemon.ID")
results = c.fetchall()
for line in results:
   print("   " + str(line[0]))