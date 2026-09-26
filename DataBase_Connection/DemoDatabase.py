import sqlite3
from sqlite3 import Error

def get_connection(d_path):
    print('inside connection')
    try :
        conn = sqlite3.connect(d_path)
        print('Connected !!')
        return  conn
    except Error as e :
        print(e)
        return None
#
# def execute_query(conn,query):
#     try:
#         cursor = conn.cursor()
#         cursor.execute(query)
#         conn.commit()
#         print('Query executed !!')
#     except Error as e :
#         print(e)
#         return None

def execute_select_query(conn,query):
    try :
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print('Query executed !!')
        return result
    except Error as e :
        print(e)
        return None

path = "C:\\Users\\PGCP-AI.STUDENTSDC\\Desktop\\DataBase\\users.sqlite3"
conn = get_connection(path)

create_table = """CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT);"""

execute_query(conn, create_table)

# add_users = """
# INSERT INTO
#   users (name, age, gender, nationality)
# VALUES
#   ('James', 25, 'male', 'USA'),
#   ('Leila', 32, 'female', 'France'),
#   ('Brigitte', 35, 'female', 'England'),
#   ('Mike', 40, 'male', 'Denmark'),
#   ('Elizabeth', 21, 'female', 'Canada');
# """
#
# execute_query(conn, add_users)

fetch_users = """SELECT * from users;"""

results = execute_select_query(conn, fetch_users)
for result in results:
    print(result)

update_user = """
UPDATE users SET age = 22 WHERE name = 'Mike'
"""
execute_query(conn, update_user)

fetch_users = """SELECT * from users;"""

results = execute_select_query(conn, fetch_users)
for result in results:
    print(result)

delete_user = """
DELETE from users WHERE id = 5"""

execute_query(conn, delete_user)

select_females = """SELECT name, age, nationality
FROM users WHERE gender = 'female'"""

females = execute_select_query(conn, select_females)
for female in females:
    print(female)