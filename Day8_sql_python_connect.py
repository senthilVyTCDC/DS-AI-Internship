import mysql.connector

ps = input("Enter your Password: ")
# Step 1: connect to MySQL (initial connectection to create the database)
connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password=ps
)

cursor = connect.cursor()

# Step 2: Create a new database
cursor.execute("DROP DATABASE IF EXISTS datascience_projects")
cursor.execute("CREATE DATABASE datascience_projects")
print("Database created.")

# Step 3: Reconnect to the new database
connect.database = "datascience_projects"

# Step 4: Create the 'Projects' table
cursor.execute("""
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    domain VARCHAR(50),
    type VARCHAR(50),
    start_date DATE,
    end_date DATE,
    status VARCHAR(30)
)
""")
print("Table 'Projects' created.")

# Step 5: Insert sample data
insert_query = """
INSERT INTO Projects (project_id, project_name, domain, type, start_date, end_date, status)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

projects_data = [
    (101, 'Diabetic Retinopathy Detection', 'Healthcare', 'Computer Vision', '2025-07-15', '2025-08-15', 'In Progress'),
    (102, 'Iris Flower Classification', 'Botany', 'Classification', '2025-07-20', '2025-08-01', 'In Progress'),
    (103, 'Stock Price Forecasting', 'Finance', 'Time Series', '2025-07-10', '2025-08-10', 'Completed')
]

for project in projects_data:
    cursor.execute(insert_query, project)

connect.commit()
print("Sample data inserted.")

# Step 6: READ - Fetch all rows
print("\nAll Projects:")
cursor.execute("SELECT * FROM Projects")
for row in cursor.fetchall():
    print(row)

# Step 7: UPDATE - Update status of one project
cursor.execute("UPDATE Projects SET status = 'Completed' WHERE project_id = 102")
connect.commit()
print("\nUpdated status of project 102.")

# Step 8: READ again
print("\nProjects after update:")
cursor.execute("SELECT * FROM Projects")
for row in cursor.fetchall():
    print(row)

# Step 9: DELETE - Delete one project
cursor.execute("DELETE FROM Projects WHERE project_id = 103")
connect.commit()
print("\nDeleted project 103.")

# Step 10: Final READ
print("\nFinal list of projects:")
cursor.execute("SELECT * FROM Projects")
for row in cursor.fetchall():
    print(row)

# Step 11: Close connectection
cursor.close()
connect.close()
