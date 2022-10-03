import pymysql as sql
try:
    db = sql.connect(host=input("Enter your Host name:--  "), port=int(input("Enter your port no:-- ")), user=input("Enter your user name:--  "), passwd=input("Enter your passwd:--  "))
    #(host="localhost", port=3306, user="root", passwd="xxx")
    cmd = db.cursor()
    q = input("Enter a database which u want create:-- ")
    cmd.execute(q)
    #print("Database Created")
    if (q):
        ch = input("Are U Sure[yes/no]")
        if (ch == "yes"):
            print("Database Created")
        elif (ch == "no"):
         print("Database not Created")
    db.close()
except Exception as e:
    print(e)
