

from tkinter import *
from PIL import ImageTk,Image
import pymysql
import mysql.connector
from tkinter import messagebox
# Add your own database name and password here to reflect in the code

con = pymysql.connect(host="bkyfpohtp5zs0hlporjm-mysql.services.clever-cloud.com",user="uj2vuvzzrsaiktia",password="Stxfp1PMvNNeOywW2pMW",database="bkyfpohtp5zs0hlporjm")
cur = con.cursor()

mydb = mysql.connector.connect(
    host="bkyfpohtp5zs0hlporjm-mysql.services.clever-cloud.com",
    user="uj2vuvzzrsaiktia",
    password="Stxfp1PMvNNeOywW2pMW",
    database="bkyfpohtp5zs0hlporjm")

def addbook():
    bookname = input("Enter book name: ")
    bookcode = input("Enter book code:")
    totalbooks = input("Total books:")
    subject = input("Enter subject:")
    data = (bookname,bookcode,totalbooks,subject)
    sql = "insert into books(bookname,bookcode,totalbooks,subject) values(%s,%s,%s,%s)"
    c = mydb.cursor()

    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")
    main()


def issueb():
    name = input("Enter name:")
    rno  = input("Enter rno:")
    code = input("Enter book code:")
    date = input("Enter date:")
    sql  = "insert into issue(name,regno,bcode,idate) values(%s,%s,%s,%s)"
    data =(name,rno,code,date)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book issued to :",name)
    main()
    bookup(code,-1)


def submitb():
    name = input("Enter name:")
    regno  = input("Enter rno:")
    code = input("Enter book code:")
    sdate = input("Enter date:")
    sql = "insert into submit(name,regno,bcode,sdate) values(%s,%s,%s,%s)"
    data = (name,regno,code,sdate)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book submitted from :",name)
    bookup(code,1)


def bookup(co,u):
    sql = "select TOTAL from books where BCODE = %s"
    data = (co,)
    c = mydb.cursor()
    c.execute(sql,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set TOTAL = %s where BCODE = %s"
    d = (t,co)
    c.execute(sql,d)
    mydb.commit()
    main()


def dbook():
    ac = input("Enter book code:")
    sql = "delete from books where BCODE = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    main()


def dispbook():
    sql = "select * from books"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name:",i[0])
        print("Book code:",i[1])
        print("Total:",i[2])
        print("................")
    main()


def main():
    print("""............LIBRARY MANAGEMENT.............
    1.Add book
    2.Issue book
    3.Submit book
    4.Delete book
    5.Display book
    """)
    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issueb()
    elif(choice == '3'):
        submitb()
    elif(choice == '4'):
        dbook()
    elif(choice == '5'):
        dispbook()
    else:
        print("wrong choice")
        main()


def password():
    import random
    ps = random.randint(000000,100000)

    user = input("Enter Username: ")
    print("Your password is:",ps)

    verify = input("Enter password:")

    if verify == str(ps):
        main()
    else:
        verify != str(ps)
        print("wrong password")
        password()

password()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("C:/Users/prave/Downloads/library-management-project-python/lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addbook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=dbook)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=dispbook)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueb)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = submitb)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
