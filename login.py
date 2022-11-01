from subprocess import call
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os 

def validateLogin():
    mydb = mysql.connector.connect( host="localhost", user="root", password="projectsec!", database="mysql")
    mycursor = mydb.cursor()
    Usern = email.get()
    psw = passw.get()

    sql = "select * from login where Usern = %s and psw = %s"
    mycursor.execute(sql, [(Usern), (psw)])
    result = mycursor.fetchall()
    if result:
        file = open("login.txt", "w")
        file.write(Usern)
        file.close()
        tkWindow.destroy()
        os.chdir("D:/Studie/resultaten/2022-2023/Project Security/IP1/Python")
        call(["python", "2step.py"])
        
        return True
    else:
        messagebox.showinfo(title='Ongeldig', message="Onjuiste email of wachtwoord") 
        return False    

#window
tkWindow = Tk()  
tkWindow.geometry('925x500+300+200')  
tkWindow.title('Inloggen')
tkWindow.configure(bg="#fff")
tkWindow.resizable(False,False)

global email
global passw
email = StringVar()
passw = StringVar()

img = PhotoImage(file='login.png')
Label(tkWindow,image=img,bg='white').place(x=50,y=50)

frame=Frame(tkWindow,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text= 'Inloggen', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)



def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,border=0,bg="white", font=('Microsoft YaHei UI Light', 11),textvariable= email )
user.place(x=30,y=80)
user.insert(0,'Email')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        code.insert(0,'Wachtwoord')

code = Entry(frame,width=25,fg='black',border=0,bg="white", font=('Microsoft YaHei UI Light', 11),textvariable= passw, show='*')
code.place(x=30,y=150)
code.insert(0,'Wachtwoord')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,bg='black').place(x=25,y=177)




#username label and text entry box
#Label(tkWindow,bg="white", text="Email").place(x=500,y=100)
#emailEntry = Entry(tkWindow, textvariable= email).grid(row=0, column=1)  

#password label and password entry box
#Label(tkWindow,text="Password").grid(row=1, column=0)  
#passwordEntry = Entry(tkWindow, textvariable= passw, show='*').grid(row=1, column=1)  

#login button
Button(tkWindow,width=39, pady=7, text="Inloggen", bg='#57a1f8', fg='white',border=0,command=validateLogin).place(x=510,y=300)  


tkWindow.mainloop()

