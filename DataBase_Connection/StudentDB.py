import sqlite3
from sqlite3 import Error

def get_connection(path):
    try :
        connection = sqlite3.connect(path)
        print('Connected')
        return connection
    except Error as e:
        print(e)
        return None

def executeQuery(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print('Query executed !!')
    except Error as e:
        print(e)
        return None

def execute_select_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print('Query executed !!')
        return results
    except Error as e:
        print(e)
        return None

path = 'C:\\Users\\PGCP-AI.STUDENTSDC\\Desktop\\DataBase\\students.sqlite3'

db = get_connection(path)


# create_table = """CREATE TABLE IF NOT EXISTS students
# (Roll_NO INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   Marks INTEGER);"""
#
# executeQuery(db, create_table)

# add_student = """INSERT INTO students (name, age, gender, Marks) VALUES ('Priyanshu', 23, 'Male' ,90)"""
# executeQuery(db, add_student)

students = execute_select_query(db, 'SELECT * FROM students;')
for student in students:
    print(student)

# add_student = """INSERT INTO students (name, age, gender, Marks) VALUES
#     ('Viraj', 21, 'Male' ,95),
#     ('Pragati', 23, 'Female' ,70),
#     ('Satyam', 22, 'Male' ,80),
#     ('Kavya', 23, 'Female' ,75),
#     ('Disha', 21, 'Female' ,80);
#               """
# executeQuery(db, add_student)
