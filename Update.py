import pymysql as sql
try:
 db = sql.connect(host=input("Enter your Host name:--  "), port=int(input("Enter your port no:-- ")), user=input("Enter your user name:--  "), passwd=input("Enter your passwd:--  "),db=input("Enter your database:-- "))
 #db=sql.connect(host="localhost",port=3306,user="root",passwd="xxx",db="resturant")
 cmd=db.cursor()
 id=input("Enter Product Id U Want to Update:")
 q="Select * from Products where Productid='{0}'".format(id)
 cmd.execute(q)
 row=cmd.fetchone()
 if(row):
     print("Product  Id:", row[0])
     print("Product  Name:", row[1])
     print("Price:", row[2])
     print("OfferPrice:",row[3])
     print("4] Exit")
     ch=int(input("Which Field U Want to Modify:"))
     if(ch==1):
         pn=input("Enter New Product  Name:")
         pat="Productname='{0}'".format(pn)
     elif(ch==2):
         pr=input("Enter New Price:")
         pat="Price={0}".format(pr)
     elif(ch==3):
         of=input("Enter OfferPrice:")
         pat="OfferPrice={0}".format(of)
     elif(ch==4):
        print("Exit")
     else:
        print("Wrong Option")
     if(ch>=1 and ch<=2):
         q="update Products set {0} where Productid='{1}'".format(pat,id)
         cmd.execute(q)
         db.commit()
         print("Record Updated..")
 else:
    print("Record Not Found...")
 db.close()
except Exception as e:
  print(e)
