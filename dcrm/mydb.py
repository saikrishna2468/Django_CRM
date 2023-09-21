
# install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector 

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='saikrishna2468',
)
cursorObject= database.cursor()

cursorObject.execute("CREATE DATABASE apt")

print('ALL DONE!')