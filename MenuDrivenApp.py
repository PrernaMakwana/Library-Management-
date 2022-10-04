import pymysql 
con =pymysql.connect (host='localhost',user='root',passwd='',database='library')

def addbook():
    bn = input("Enter Book Name: ")
    c= input ("Enter the Book Code: ")
    t= input ("Total Books : ")
    s= input ("Enter Subject : ")
    data = (bn,c,t,s)
    sql= 'insert into books values(%s,%s,%s,%s)'

    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("-------------------------------------------")
    print("Data successfully")
    main()

def issueb():
    n= input("Enter Name: ") 
    r = input("Enter Reg No: ")  
    co = input("Enter Book Code: ")
    d=  input("Enter Date: ")
    a= "insert into issue values(%s,%s,%s,%s)"
    data= (n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("--------------------------------------------")
    print("Book issued  : ",n)
    bookup(co,-1)

def submitb():
    n= input("Enter Name: ") 
    r = input("Enter Reg No: ")  
    co = input("Enter Book Code: ")
    d=  input("Enter Date: ")
    a= "insert into submit values (%s,%s,%s,%s)"
    data= (n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("--------------------------------------------")
    print("Books submitted from : ",n)
    bookup(co,1)

def bookup(co,u):
    a="select Total from books Where BCODE = %s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL = %s where BCODE = %s"
    d= (t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac=input("Enter Books Code: ")
    a= "delete from books where BCODE = %s" 
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()   

def dispbook():
    a= "select * from books"
    c= con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name :",i[0])
        print("Book code :",i[1])    
        print("Total :",i[2])
        print("Subject :",i[3])
        print("------------------------------------------------------------------")
    main()

def main():
    print(''' 
                                                LIBRARY MANAGEMENT  
    1. ADD BOOKS
    2. ISSUE BOOK
    3. SUBMIT BOOK
    4. DELETE BOOK
    5. DISPLAY BOOKS
    ''')    
    
    choice=input("Enter Task No: ")
    print("-----------------------------------------------------------------------------------------------------------")
    if(choice=='1'):
        addbook()
    if(choice=='2'):
        issueb()
    if(choice=='3'):
        submitb() 
    if(choice=='4'):
        dbook()
    if(choice=='5'):
        dispbook()               
def pswd():
    ps=input("Enter the Password: ")
    if ps =='lib143':
        main()
    else:
        print("wrong Password ")
        pswd()        
pswd()        
       