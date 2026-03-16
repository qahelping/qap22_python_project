import sqlite3

DATABASE_URL = "sqlite:///memes.db"

conn = sqlite3.connect('memes.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memes (
id INTEGER PRIMARY KEY,
name TEXT UNIQUE NOT NULL
)
""")

conn.commit()

# cursor.execute("INSERT INTO memes (name) VALUES (?)", ("Токсис",))
# conn.commit()
#
# cursor.execute("SELECT * FROM memes")
# data = cursor.fetchall()
#
# for i in data:
#     id_mem, name = i
#     print(f"#{id_mem} - {name}")


cursor.execute("UPDATE memes SET name=? WHERE id=?", ("Кукареку", 2))
conn.commit()

cursor.execute("SELECT * FROM memes")
data = cursor.fetchall()

for i in data:
    id_mem, name = i
    print(f"#{id_mem} - {name}")

cursor.execute("DELETE FROM memes WHERE id=?", (8, ))
conn.commit()


cursor.execute("SELECT * FROM memes")
data = cursor.fetchall()

for i in data:
    id_mem, name = i
    print(f"#{id_mem} - {name}")


cursor.execute("DROP DATABASE memes.db;")

conn.close()
