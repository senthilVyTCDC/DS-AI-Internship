import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password='1817'
)

cursor = connect.cursor()
cursor.execute("DROP DATABASE IF EXISTS Employee")
cursor.execute("CREATE DATABASE Employee")
print("Database 'Employee' created.")
connect.database = "Employee"
cursor.execute("""
CREATE TABLE Emp (
    Emp_id INT PRIMARY KEY,
    Emp_name VARCHAR(100),
    salary INT,
    experience INT,
    joining DATE
)
""")
print("Table 'Emp' created.")
insert_query = """
INSERT INTO Emp (Emp_id, Emp_name, salary, experience, joining)
VALUES (%s, %s, %s, %s, %s)
"""
emp_data = [
    (100, 'kiran', 50000, 3, '2022-07-17')
]
for emp in emp_data:
    cursor.execute(insert_query, emp)
connect.commit()
print("Initial employee data inserted.")
print("\nAll Employees:")
cursor.execute("SELECT * FROM Emp")
for row in cursor.fetchall():
    print(row)
cursor.execute("UPDATE Emp SET salary = 60000 WHERE Emp_id = 100")
connect.commit()
print("\nUpdated salary of employee 100.")
print("\nEmployees after salary update:")
cursor.execute("SELECT * FROM Emp")
for row in cursor.fetchall():
    print(row)
cursor.execute(insert_query, (101, 'madesh', 5000, 1, '2024-07-17'))
connect.commit()
print("\nInserted employee 101.")
print("\nEmployees after inserting 101:")
cursor.execute("SELECT * FROM Emp")
for row in cursor.fetchall():
    print(row)
cursor.execute("DELETE FROM Emp WHERE Emp_id = 101")
connect.commit()
print("\nDeleted employee 101.")
print("\nFinal list of employees:")
cursor.execute("SELECT * FROM Emp")
for row in cursor.fetchall():
    print(row)
cursor.close()
connect.close()
