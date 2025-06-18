import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""CREATE TABLE student(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    marks INTEGER,
    class VARCHAR(25),
    section VARCHAR(25)
)"""

# cursor.execute(table_info)

cursor.execute("INSERT INTO student(name,age,marks,class,section) VALUES('Rahul',15,85,'10th','A')")
cursor.execute("INSERT INTO student(name,age,marks,class,section) VALUES('Rohit',16,75,'10th','B')")
cursor.execute("INSERT INTO student(name,age,marks,class,section) VALUES('Raj',15,65,'10th','C')")  
cursor.execute("INSERT INTO student(name,age,marks,class,section) VALUES('Ravi',16,55,'10th','A')")
cursor.execute("INSERT INTO student(name,age,marks,class,section) VALUES('Raman',15,45,'10th','B')")
cursor.execute("INSERT INTO student(name,age,marks,class,section) VALUES('Rajesh',16,35,'10th','C')")
cursor.execute("INSERT INTO student(name,age,marks,class,section) VALUES('Rajiv',15,25,'10th','A')")
 
# cursor.execute("DELETE FROM table_name")
print("Table created successfully")

data=cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

connection.commit()
connection.close()

# import sqlite3

# connection = sqlite3.connect("student.db")
# cursor = connection.cursor()

# # Delete all rows from the student table
# cursor.execute("DELETE FROM student")

# # Commit changes and close connection
# connection.commit()
# connection.close()

# print("All entries deleted successfully.")
