import pymysql.cursors

import csv
import sys

maxint = (sys.maxsize)
decrement = True

while decrement:

    decrement = False

    try:
        csv.field_size_limit(maxint)
    except OverflowError:
        maxint = int(maxint/10)
        decrement = True


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


#CREATE DATABASE
try:
    with connection.cursor() as cursor:
        # Create a new record

        sql = """CREATE TABLE films 
                (id int NOT NULL KEY AUTO_INCREMENT,
                adult VARCHAR(500), 
                genres VARCHAR(500), 
                title VARCHAR(500), 
                vote_avg DOUBLE(5,0), 
                popularity DOUBLE(5,0), 
                production_co VARCHAR(500), 
                production_stu VARCHAR(500), 
                language VARCHAR(500), 
                release_date DATE, 
                runtime INT, 
                revenue INT, 
                budget int)"""

        cursor.execute(sql)
        connection.commit()
except:
    # connection is not autocommit by default. So you must commit to save
    # your changes.

    print('Table Exists')


with open('films2.csv',errors = 'ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    with connection.cursor() as cursor:
        # Create a new record




        for row in csv_reader:
            # print(row)
            sql = """insert into films (adult,  budget, popularity, release_date, revenue, runtime, title, vote_avg) 
                values ("{}", "{}","{}", "{}","{}", "{}","{}","{}")""".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6], row[7])
            cursor.execute(sql)
            # print('got here')
            # print(cursor.fetchall())
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            # connection.commit()
            # if line_count == 0:
            #     print(f'Column names are {", ".join(row)}')
            #     line_count += 1
            # else:
            #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            #     line_count += 1
        

#     # print(f'Processed {line_count} lines.')








# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)


# # CREATE DATABASE
# try:
#     with connection.cursor() as cursor:
#         # Create a new record

#         sql = """CREATE TABLE films 
#                 (id int NOT NULL KEY AUTO_INCREMENT,
#                 adult VARCHAR(100), 
#                 genres VARCHAR(100), 
#                 title VARCHAR(100), 
#                 vote_avg DOUBLE(5,0), 
#                 popularity DOUBLE(5,0), 
#                 production_co VARCHAR(100), 
#                 production_stu VARCHAR(100), 
#                 language VARCHAR(100), 
#                 release_date DATE, 
#                 runtime INT, 
#                 revenue INT, 
#                 budget int)"""

#         cursor.execute(sql)
#         connection.commit()
# except:
    # connection is not autocommit by default. So you must commit to save
    # your changes.

#     print('Table Exists')



#CREATE DATABASE
# try:
#     with connection.cursor() as cursor:
#         # Create a new record

        # sql = """CREATE TABLE users 
        #         (id int NOT NULL KEY AUTO_INCREMENT,
        #         email VARCHAR(20), 
        #         username VARCHAR(20))"""

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

# with connection.cursor() as cursor:
#     # Read a single record
#     sql = '''SELECT username FROM users WHERE username="{}"'''.format('ola')
#     cursor.execute(sql)
#     result = cursor.fetchmany(2)
#     print(result)
# connection.close()