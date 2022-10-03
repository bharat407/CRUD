import pymysql as sql
try:
 db=sql.connect(host="localhost",port=3306,user="root",passwd="xxx",db="appel")
 #db = sql.connect(host=input("Enter your Host name:--  "), port=int(input("Enter your port no:-- ")),user=input("Enter your user name:--  "), passwd=input("Enter your passwd:--  "),db=input("Enter your database:-- "))
 cmd=db.cursor()
 pat=input("Enter Pattern:")
 #input("Search by name-- ")
 q="Select * from Products where Productname like '%{0}%'".format(pat)
 cmd.execute(q)
 rows=cmd.fetchall()
 if(len(rows)>0):
     print(rows)
 else:
    print("Record Not Found...")
 db.close()
except Exception as e:
  print(e)
