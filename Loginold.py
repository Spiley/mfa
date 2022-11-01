from subprocess import call
from tkinter import *
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
        tkWindow.destroy()
        file = open("login.txt", "w")
        file.write(Usern)
        file.close()
        os.chdir("D:/Studie/resultaten/2022-2023/Project Security/IP1/Python")
        call(["python", "2step.py"])
        return True
    else:
        Label(tkWindow, text="incorrecte gegevens!").grid(row=5, column=1)  
        return False    

#window
tkWindow = Tk()  
tkWindow.geometry('400x200')  
tkWindow.title('Inloggen')
global email
global passw
email = StringVar()
passw = StringVar()


#username label and text entry box
Label(tkWindow, text="email").grid(row=0, column=0)
emailEntry = Entry(tkWindow, textvariable= email).grid(row=0, column=1)  

#password label and password entry box
Label(tkWindow,text="Password").grid(row=1, column=0)  
passwordEntry = Entry(tkWindow, textvariable= passw, show='*').grid(row=1, column=1)  

#login button
Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  


tkWindow.mainloop()

