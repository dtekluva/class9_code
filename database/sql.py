import pymysql.cursors

#
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)




with connection.cursor() as cursor:
    # Create a new record
    sql = """SELECT * FROM films WHERE (name = 'ola' OR name = 'attah')"""

    cursor.execute(sql)
    print('got here')
    result = cursor.fetchall()
    print(result)
  




# with connection.cursor() as cursor:
#     # Create a new record
#     sql = """insert into people (name, age, email) 
#                 values ("{}", "{}", "{}")""".format('taofeek', 23, 'bisola@gmail.com')
#     cursor.execute(sql)
#     print('got here')
#     # print(cursor.fetchall())
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()










# def add(row):

#     # print(row)
#     sql = """insert into films (adult,  budget, popularity, release_date, revenue, runtime, title, vote_avg) 
#         values ("{}", "{}","{}", "{}","{}", "{}","{}","{}")""".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6], row[7])
#     cursor.execute(sql)

#     connection.commit()

# def select(value):

#     # print(row)
#     sql = '''SELECT title FROM films WHERE 
#                 title = "{}"'''.format(value)
#     cursor.execute(sql)
#     return (cursor.fetchall())
#     # connection.commit()









# file = open('films2.csv','r', errors = 'ignore')

# file_r = file.readline()
# i = 0
# with connection.cursor() as cursor:

#     for line in file:
#         # print('......',i)
#         # print('====',file.readline())
#         # print(len((file.readline()).split(',')))
#         if len((file.readline()).split(',')) == 8:
#             _list = file.readline().split(',')
#             # add(_list) #add from list

#             _filter = select(_list[6]) # SELECT BY TITLE
#             if len(_filter)<1:
#                 # print(_filter)
#                 print('---',_list[6])
#             # int(((file.readline()).split(','))[5])
#             # print(file.readline())
        
#     else:
#         i += 1
#         print(i)

#     print(i)