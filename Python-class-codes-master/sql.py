import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
#CREATE DATABASE
# try:
#     with connection.cursor() as cursor:
#         # Create a new record

#         sql = """CREATE TABLE users 
#                 (id int NOT NULL KEY AUTO_INCREMENT,
#                 email VARCHAR(20), 
#                 username VARCHAR(20))"""

#         cursor.execute(sql)
#         connection.commit()
# except:
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.

#     print('Table Exists')



# with connection.cursor() as cursor:
#     # Create a new record
#     sql = """insert into users (username, email) 
#                 values ("{}", "{}")""".format('inyang@gmail.com','attah')
#     cursor.execute(sql)
#     print('got here')
#     # print(cursor.fetchall())
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
# connection.commit()

with connection.cursor() as cursor:
    # Read a single record
    sql = '''SELECT username FROM users WHERE username="{}"'''.format('ola')
    cursor.execute(sql)
    result = cursor.fetchmany(2)
    print(result)
connection.close()