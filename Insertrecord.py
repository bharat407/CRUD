import pymysql as sql
try:
    db = sql.connect(host=input("Enter your Host name:--  "), port=int(input("Enter your port no:-- ")), user=input("Enter your user name:--  "), passwd=input("Enter your passwd:--  "),db=input("Enter your database:-- "))
    #db = sql.connect(host="localhost", port=3306, user="root", passwd="xxx", db="resturant")
    cmd = db.cursor()
    T=int(input("Enter how many records u want insert:-- "))
    while(T):
     q=input("Enter data which u want:--\n command should be like \n {insert into table name values (enter your values using apostrophe''-- )\n")
     print(q)
     cmd.execute(q)
     db.commit()
     if (q):
        ch = input("Are U Sure[yes/no]")
        if (ch == "yes"):
            print("Record Submitted")
        elif (ch == "no"):
         print("Record not Submitted")
    db.close()
    T=T-1
except Exception as e:
    print(e)
