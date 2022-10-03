#CRUD
import pymysql as sql
try:
 #db=sql.connect(host="localhost",port=3306,user="root",passwd="xxx",db="resturant")\
 db = sql.connect(host=input("Enter your Host name:--  "), port=int(input("Enter your port no:-- ")), user=input("Enter your user name:--  "), passwd=input("Enter your passwd:--  "),db=input("Enter your database:-- "))
 cmd=db.cursor()
 id=input("Enter Product  Id U Want to Delete:")
 q = "Select * from laptop where Productid='{0}'".format(id)
 cmd.execute(q)
 row=cmd.fetchone()
 if(row):
     print("Product  Id:", row[0])
     print("Product  Name:", row[1])
     print("Price:", row[2])
     print("OfferPrice:",row[3])
     print("4] Exit")
     ch =(input('''Are U Sure[yes/no]:'''))
     if(ch=="yes"):
         q="delete from laptop where Productid='{0}'".format(id)
         cmd.execute(q)
         db.commit()
         print("Record Deleted..")
 else:
    print("Record Not Found...")
 db.close()
except Exception as e:
  print(e)
