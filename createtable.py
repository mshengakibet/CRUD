import sqlite3
conn=sqlite3.connect('company.db')
print("successfully opened database")

conn.execute("""CREATE TABLE Company2(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT  NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
TASK TEXT CHAIR(20))""")
print("successfuly created Company1 table")
conn.close()
