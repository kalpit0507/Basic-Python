#WAP to connect Python to SQL
import mysql.connector as sqlObj
mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
if mycon.is_connected():
    print("Successful")
else:
    print("Sorry!!! Connectivity not done")
cursor=mycon.cursor()
cursor.execute("SHOW TABLES")
t=tuple(cursor)
print(t)
mycon.close()
