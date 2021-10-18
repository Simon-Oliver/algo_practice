import sqlite3

con = sqlite3.connect("../chinook.db")
cur = con.cursor()

cur.execute('''
SELECT 
    EmployeeId, COUNT(ReportsTo)
FROM 
    employees
''')
result = cur.fetchall()
print(result)