import sqlite3

con = sqlite3.connect("../chinook.db")
cur = con.cursor()

cur.execute(
    """
INSERT INTO employees(
   LastName,
   FirstName,
   Country
) VALUES(
    "Muster",
    "Max",
    "Australia"
    ) 
"""
)

cur.execute(
    """
SELECT 
    country, COUNT(Country)
FROM 
    employees
GROUP By country
"""
)

# cur.execute('''
# SELECT
#     *
# FROM
#     employees
# ''')

con.commit()

result = cur.fetchall()
print(result)
