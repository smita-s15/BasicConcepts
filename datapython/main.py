import sqlite3
print(sqlite3.version)


# Connect
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [("Bob", 30), ("Charlie", 22)])

conn.commit()

# Query
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Update
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
conn.commit()

# Delete
cursor.execute("DELETE FROM users WHERE name = ?", ("Charlie",))
conn.commit()

# Close
cursor.close()
conn.close()
