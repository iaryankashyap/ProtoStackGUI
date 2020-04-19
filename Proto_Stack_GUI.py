import tkinter as t
import random
import smtplib
from os import system
from time import sleep
Path="E:\\Projects\\CS\\Proto-stack\\Proto-Stack-GUI\\Database.txt"


def destruct_win():
    root.destroy()
    root4.destroy()
    root2.destroy()
    root7.destroy()



def otpsender(email):
    global x
    x=random.randint(4000,5000)
    content="Hello there,\nYour OTP is " + str(x) +"\n\nThank you for using ProtoStack."
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.ehlo()
    server.login("protostackportal@gmail.com","protostack123portal")
    server.sendmail("protostackportal@gmail.com",email,content)
    server.close()
    return x


def logport():
    global root7
    root7=t.Tk()
    root7.geometry("247x100")
    root7.title("WEB PORTAL")
    Lb1=t.Label(root7,text="Stack Implementation",font=("arial",16,"bold")).pack()
    lb=t.Label(root7,text="Please head towards the command line window",fg="grey",font=("calibri",8,)).pack()
    but=t.Button(root7,text="   OK   ",relief="groove",command=destruct_win).pack()
    
    root7.mainloop()

    print()
    print("Lets do some stack implementation.")
    print("Welcome..!!")
    inp=1
    c=0
    while c==0: 
        print("What you want to do?")
        print("[1]Enter a stack and perform actions")
        print("[2]Auto-generate a stack of your own size")
        p=int(input("Enter your choice:"))
        sleep(1)
        system('cls')
        if p==1:
            stack=eval(input("Enter your stack:"))
            c=1
        elif p==2:
            size=int(input("Enter the size of stack:"))
            stack=auto_stack(size)
            print("Stack Generated")
            display(stack)
            c=1
        else:
            print("Invalid input")
            continue
    while inp!=5:
        false_inp=input("Press Enter to continue...")
        sleep(1)
        system('cls')
        print("\n--------------------------")
        print("What you want to do??")
        print("\n[1]Insert an element on top")
        print("[2]Delete an element from top")
        print("[3]See the topmost item of your stack")
        print("[4]Display your stack")
        print("[5]Exit")
        print("--------------------------\n")
        inp=int(input("Enter your choice:"))
        print("\n--------------------------")
        sleep(2)
        system('cls')
        #conditions
        if inp==1:
            itm=int(input("Enter the item to be inserted:"))
            stack=insert_first_element(stack,itm)
            print("--------------------------\n")
        elif inp==2:
            if isempty(stack):
                print("Stack Underflow")
            else:
                stack=delete_first_element(stack)
            print("--------------------------\n")
        elif inp==3:
            if isempty(stack):
                print("stack is empty")
            else:
                print("Topmost Element:",stack[len(stack)-1])
        elif inp==4:
            if isempty(stack):
                print("stack is empty")
            else:
                display(stack)
        elif inp==5:
            continue
        else:
            print("invalid input")
    sleep(4)
    print("\n\nTHANK YOU FOR USING THIS PROGRAM..!!")
    i=input("Press Enter to Quit")

    

def isempty(Stack):
    '''Checks if a stack is empty or not'''
    if len(Stack)==0:
        return True
    else:
        return False



def delete_first_element(Stack):
    ''' Deletes the first element from the stack and returns a new stack'''
    g=Stack.pop()
    return Stack



def insert_first_element(Stack,element):
    '''Inserts an element at the first positon of the stack and returns a new stack'''
    Stack.append(element)
    return Stack



def auto_stack(size):
    '''Creates a random stack from the given size'''
    stack=[]
    for i in range(size):
        a=random.randint(0,9)
        stack.append(a)
    return stack



def display(Stack):
    '''Displays the stack vertically'''
    print()
    for i in range(len(Stack)-1,-1,-1):
        print(Stack[i])
    print()



def signup_submit():

    global otp
    global phone
    phone=phone_ent.get()
    email=email_ent.get()
    global root6
    if len(phone)!=10:
        phone_mismatch()
            
    else:
        root6=t.Tk()
        root6.geometry("300x300")
        root6.title("WEB PORTAL")
        Lb1=t.Label(root6,text="OTP Confirmation",font=("arial",16,"bold")).pack()
        Lb2=t.Label(root6,text="").pack()
        Lb3=t.Label(root6,text="An OTP has been sent to your email",font=("arial",9)).pack()
        x=otpsender(email)
        Lb3=t.Label(root6,text="Enter OTP:",font=("arial",9)).place(x=50,y=111)
        otp=t.Entry(root6,relief="groove",bd=4)
        otp.place(x=120,y=111)
    
        bt=t.Button(root6,text="Validate",relief="groove",command=otpcheck).place(x=155,y=140)
    
    
        root6.mainloop()
    


def otpcheck():
    global username
    username=username_ent.get()
    password=password_ent.get()
    
    otpc=otp.get()
    if str(x)==otpc:
        f=open(Path,"a")
        encryption=username+"#"+password+"#"+"."
        f.write(encryption)
        f.close()
        
        l=t.Label(root6,text="Registered Successfully",font=("arial",9)).place(x=100,y=260)
    else:
        l=t.Label(root6,text="OTP Registeration Failure",font=("arial",9)).place(x=100,y=260)




def submit():
    stock_username=entered_username.get()
    stock_password=entered_password.get()

    if passwordchecker(stock_username,stock_password):
        global root4
        root4=t.Tk()

        root4.geometry("300x300")
        root4.title("WEB PORTAL")
        Lb=t.Label(root4,text="Logged in Successfully",font=("arial",12,"bold")).pack()
        lb=t.Label(root4,text="Click To Continue").place(x=100,y=135)
        b=t.Button(root4,text="Continue",relief="groove",command=logport).place(x=120,y=165)
        
        root4.mainloop()
    else:
        root5=t.Tk()

        root5.geometry("300x300")
        root5.title("WEB PORTAL")
        Lb=t.Label(root5,text="Log in Failed",font=("arial",12,"bold")).pack()
        lb=t.Label(root5,text="Click To try again").place(x=97,y=135)
        b=t.Button(root5,text="Retry",relief="groove",command=login).place(x=125,y=165)
        
        root5.mainloop()




def login():
    
    
    global entered_username
    global entered_password 
    global root2
    entered_username=t.StringVar()
    entered_password=t.StringVar()
    
    root2=t.Tk()
    root2.geometry("300x300")
    root2.title("WEB PORTAL")
    Lb=t.Label(root2,text="Login Page",font=("arial",16,"bold")).pack()
    lb2=t.Label(root2,text="Enter Your Credentials",font=("arial",9))
    lb3=t.Label(root2,text="Username:").place(x=50,y=111)
    lb2.place(x=83,y=28)
    lb3=t.Label(root2,text="Password:").place(x=50,y=161)
    
    submit_page=t.Button(root2,text="Submit",relief="groove",command=submit).place(x=130,y=220)
    
    entered_username=t.Entry(root2,relief="groove",bd=4,)
    entered_username.place(x=110,y=110)
    entered_password=t.Entry(root2,relief="groove",bd=4)
    entered_password.place(x=110,y=160)
    
    
    
    
    root2.mainloop()
     
def phone_mismatch():
    root9=t.Tk()
    root9.geometry("247x100")
    root9.title("WEB PORTAL")
    Lb1=t.Label(root9,text="Stack Implementation",font=("arial",16,"bold")).pack()
    lb=t.Label(root9,text="Please enter a valid phone number",fg="grey",font=("calibri",8,)).pack()
    but=t.Button(root9,text="   OK   ",relief="groove",command=root9.destroy).pack()
    
    root9.mainloop()

def signup():
    
    
    global root3
    root3=t.Tk()
    root3.geometry("300x300")
    root3.title("WEB PORTAL")
    Lb=t.Label(root3,text="Sign Up Page",font=("arial",16,"bold")).pack()
    lb2=t.Label(root3,text="Enter Your Required Details",font=("arial",9))
    lb3=t.Label(root3,text="Username:").place(x=29,y=71)
    lb2.place(x=66,y=28)
    lb3=t.Label(root3,text="Phone:").place(x=40,y=100)
    lb4=t.Label(root3,text="E-mail:").place(x=40,y=131)
    lb5=t.Label(root3,text="Password:").place(x=29,y=161)
    lb6=t.Label(root3,text="Confirm:").place(x=35,y=191)
    


    global username_ent
    global phone_ent
    global email_ent
    global password_ent
    global cnf_ent


    username_ent=t.StringVar()
    phone_ent=t.StringVar()
    email_ent=t.StringVar()
    password_ent=t.StringVar()
    cnf_ent=t.StringVar()



    username_ent=t.Entry(root3,relief="groove",bd=4)
    username_ent.place(x=90,y=71)
    phone_ent=t.Entry(root3,relief="groove",bd=4)
    phone_ent.place(x=90,y=100)
    email_ent=t.Entry(root3,relief="groove",bd=4)
    email_ent.place(x=90,y=131)
    password_ent=t.Entry(root3,relief="groove",bd=4)
    password_ent.place(x=90,y=161)
    cnf_ent=t.Entry(root3,relief="groove",bd=4)
    cnf_ent.place(x=90,y=191)
    
    
    
    submit_page=t.Button(root3,text="Submit",relief="groove",command=signup_submit).place(x=130,y=230)
    
    root3.mainloop()    
    
    


def quitroot():
    root.quit()



def passwordchecker(username,password):
    c=""
    l=""
    o=""
    m=""
    users=[]
    data_list=[]
    f=open(Path,"r")
    r=f.read()
    for i in range(0,len(r)):
        if r[i]!=".":
            c=c+r[i]
        else:
            data_list=data_list+[c]
            c=""   
            continue    
    
    for i in range(0,len(data_list)):
        o=data_list[i]
        for j in range(0,len(o)):
            if o[j]!="#":
                m=m+o[j]
            else:
                users=users+[m]
                m=""
                
        o=""
    
    usernms=[]
    pswrds=[]
    for i in range(0,len(users),2):
        usernms=usernms+[users[i]]
    
    for i in range(1,len(users),2):
        pswrds=pswrds+[users[i]]
    
    f.close()
    
    for i in range(0,len(usernms)):
        if username==usernms[i]:
            if password==pswrds[i]:
                return True
            else:
                return False


#Main



global root
root=t.Tk()
root.geometry("300x300")

root.title("WEB PORTAL")
Lb=t.Label(root,text="Proto-Stack",fg="blue",font=("Agency FB",22,"bold")).pack()
Lb2=t.Label(root,text="This is a Client-Based Portal...",font=("arial",9)).pack()
Lb3=t.Label(root,text="Already Registered?",font=("arial",7)).place(x=100,y=90)
button1=t.Button(root,text="Login",relief="groove",command=login)
button1.place(x=125,y=110)
Lb4=t.Label(root,text="Don't have an account?",font=("arial",7)).place(x=94,y=149)
button2=t.Button(root,text="Sign Up",relief="groove",command=signup)
button2.place(x=120,y=170)
Lb5=t.Label(root,text="Click Here To Quit",fg="red",font=("arial",7,"underline")).place(x=104,y=240)
button3=t.Button(root,text="Quit",relief="groove",command=quitroot)
button3.place(x=130,y=260)
root.mainloop()

