import sqlite3

conn = sqlite3.connect('company.db')
print("connected")

conn.execute("insert into Company2(id,firstname,lastname,age,salary,task)\
              values(1,'japhet','Morty',23,37800.00,'manager')");
conn.execute("insert into Company2(id,firstname,lastname,age,salary,task)\
              values(2,'Alan','Dante',41,30580.00,'director')");
conn.execute("insert into Company2(id,firstname,lastname,age,salary,task)\
              values(3,'Alan','Dante',41,30580.00,'secretary')");
conn.execute("insert into Company2(id,firstname,lastname,age,salary,task)\
              values(4,'Anet','Kim',81,340500.00,'treasurer')");
conn.commit()

print("Successfully inserted values in Company1 tabel")
conn.close()
