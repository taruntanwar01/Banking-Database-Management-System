import mysql.connector 
from mysql.connector import Error

try:
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tarun9199',auth_plugin='mysql_native_password')
    print(mydb)

except Error as e:
    print('error is',e)