import sys
import json
import sqlite3

print("Python GitHub Integration Successful!")
print("Python version:", sys.version)

user = {
    "username": "Srinath165",
    "status": "success"
}

print(json.dumps(user, indent=4))

connection = sqlite3.connect(":memory:")
connection.execute(
    "CREATE TABLE test (id INTEGER, name TEXT)"
)
connection.execute(
    "INSERT INTO test VALUES (1, 'Srinath165')"
)

print("SQLite integration successful!")
connection.close()
