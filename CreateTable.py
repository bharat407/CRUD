import pymysql as sql
try:
 #db=sql.connect(host="localhost",port=3306,user="root",passwd="123",db=input("Enter your database "))
 db = sql.connect(host=input("Enter your Host name:--  "), port=int(input("Enter your port no:-- ")),user=input("Enter your user name:--  "), passwd=input("Enter your passwd:--  "),db=input("Enter your database:-- "))
 cmd=db.cursor()
 #"create table Menu (Productid varchar(40) primary key,Productname varchar(50),Price int)"
 q=input("Enter a table which u want create:-- ")
 cmd.execute(q)
 if (q):
  ch = input("Are U Sure[yes/no]")
  if (ch == "yes"):
   print("Table Created")
  elif (ch == "no"):
   print("Table  not Created")
 db.close()
except Exception as e:
 print(e)