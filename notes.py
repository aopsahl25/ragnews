import sqlite3

#accessing databases (claremont.db and ragnews.db)
db = sqlite3.connect('ragnews.db')
#there is no standard file extension for sqlite; you can see: .db, .sql, .sqlite, .sqlite3

cursor = db.cursor()
#every time we create a databse we also create a cursor
sql = '''
SELECT count(*) FROM articles;
'''
#executing command
cursor.execute(sql)
row = cursor.fetchone()
print(f"row={row}")

cursor = db.cursor()
sql = '''
SELECT title FROM articles('trump harris debate)
'''
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(f"row={row}")
# make it ordered by how well the result matches the query
# take the top 10 of those