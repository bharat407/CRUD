import pymysql as sql
try:
 db=sql.connect(host="localhost",port=3306,user="root",passwd="123",db="appel")
 #db = sql.connect(host=input("Enter your Host name:--  "), port=int(input("Enter your port no:-- ")),user=input("Enter your user name:--  "), passwd=input("Enter your passwd:--  "),db=input("Enter your database:-- "))
 cmd=db.cursor()
 min=input("Enter Min Price:")
 max=input("Enter Max Price:")
 #q=input('Search by price-- ')
 q="Select * from Products where Price between {0} and {1} ".format(min,max)
 cmd.execute(q)
 rows=cmd.fetchall()
 if(len(rows)>0):
     print(rows)
 else:
   print("Record Not Found....")
 db.close()
except Exception as e:
  print(e)