import sqlite3

conn=sqlite3.connect('company.db')
print("successfully connected to the database")

conn.execute("UPDATE Company2 set SALARY=50000.00 where id=1 ")
conn.commit()


data=conn.execute("SELECT * FROM Company2")
for rows in data:
    print("id:",rows[0])
    print("firstname:",rows[1])
    print("lastname:",rows[2])
    print("age:",rows[3])
    print("salary:",rows[4])
    print("task:",rows[5])

conn.close()