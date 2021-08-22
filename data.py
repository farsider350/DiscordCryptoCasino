import sqlite3
from config import DB_PATH

con = sqlite3.connect(DB_PATH, check_same_thread=True)

c = con.cursor()


# Uncomment below on first startup, recomment out on every startup after that.

# c.execute("""CREATE TABLE users(
#     userid text,
#     username text,
#     address text,
#     balance real
#     )""")

# c.execute("INSERT INTO users VALUES ('Test','Test', '0', '0')")

# c.execute("SELECT * FROM users")

# End uncomment section

def createWallet(raw, username, address, balance):
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
              (str(raw), str(username), str(address), str(balance)))
    con.commit()


c.execute("SELECT * FROM users")
print(c.fetchall())

con.commit()
# con.close()
