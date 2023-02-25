import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

#SQLite Database comes with python, just have to import
import sqlite3

# Establish a connection
conn = sqlite3.connect('customer.db') #name of db to connect to. If it doesn't exist, Python creates it in same directory

c = conn.cursor() #cursor is how we do stuff with the db

# Create table

''' Do not need rerun creation (and probably others)
c.execute("""CREATE TABLE customer (
    first_name text,
    last_name text,
    emai text
    )""") 
conn.commit() # have to commit to perform changes
'''

# sqlite only has 5 data types, so simpler, but slightly restricted
#""" ....""" is a doc string, allowing for multiple line inputs


c.execute("INSERT INTO customer VALUES('Ben','Terry','test@fake.gmail.com')")
conn.commit


c.execute("SELECT * FROM customer") # does not do anythign by itself
items = c.fetchall()

for item in items:
    print(item[0])

conn.commit









# Close connection
conn.close()