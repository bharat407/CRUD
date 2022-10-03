import pymysql as sql
try:
 db=sql.connect(host="localhost",port=3306,user="root",passwd="xxx",db="appel")
 cmd=db.cursor()
 bn=input("Enter Bill Number:")
 q="Select P.productid,P.productname,P.price,P.offer,S.qtysale,P.offer*S.qtysale as amount from products P,sale S where P.productid=S.productid and S.billno={0}".format(bn)
 cmd.execute(q)
 rows=cmd.fetchall()
 for row in rows:
     for col in row:
         print(col,end=",")
     print()
 db.close()
except Exception as e:
    print(e)
