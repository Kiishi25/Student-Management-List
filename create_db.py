import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd= 'O21H27BabaM!&',)

my_cursor = mydb.cursor()
#my_cursor.execute('CREATE DATABASE student_list')

my_cursor.execute('SHOW DATABASES')

for db in my_cursor:
    print(db)
