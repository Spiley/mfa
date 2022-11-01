from subprocess import call
from tkinter import *
from tkinter import messagebox
from functools import partial
from email.message import EmailMessage
import ssl #for security
import smtplib
import random
import string
import time
#import os

#start timer
global start
start = time.time()

def validateLogin(verify):
    verify = verify.get()
    #get runtime variable
    runtime = time.time() - start
    if verify == code:
        if runtime > 300:
            messagebox.showinfo(title='Ongeldig', message="Code niet meer geldig. Log opnieuw in.")
        else:
            tkWindow.destroy()
            call(["python", "home.py"])
    else:
       messagebox.showinfo(title='Ongeldig', message="Onjuiste code!")
    return

code = ''.join(random.sample(string.ascii_letters + string.digits, 8))
file = open("login.txt","r")
file_text = file.read()
file.close
email_sender = 'prosechva@gmail.com'
email_password = 'strlevqfydnxjspl'
email_reciever = str(file_text)

subject = 'Uw Code'
body = "Beste Gebruiker, gebruik de volgende code om de verificatie te voltooien: " + code + ". Deze code is geldig voor 5 minuten"

em = EmailMessage()
em ['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

#window
tkWindow = Tk()  
tkWindow.geometry('925x500+300+200')  
tkWindow.title('Verificatie')
tkWindow.configure(bg="#fff")
tkWindow.resizable(False,False)

img = PhotoImage(file='verificatie.png')
Label(tkWindow,image=img,bg='white').place(x=110,y=90)

frame=Frame(tkWindow,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text= 'Verificatie', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)

otp = StringVar()

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'U heeft een code in uw email')
user = Entry(frame,width=25,border=0,bg="white", font=('Microsoft YaHei UI Light', 11),textvariable=otp )
user.place(x=30,y=80)
user.insert(0,'U heeft een code in uw email')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,bg='black').place(x=25,y=107)

validateLogin = partial(validateLogin, otp)

Button(tkWindow,width=39, pady=7, text="Inloggen", bg='#57a1f8', fg='white',border=0,command=validateLogin).place(x=510,y=300)  

#Label(tkWindow, text="Er is een email gestuurd met daarin uw code").grid(row=5, column=1)

#username label and text entry box
#otpLabel = Label(tkWindow, text="code").grid(row=0, column=0)

#otpEntry = Entry(tkWindow, textvariable=otp).grid(row=0, column=1)  




#login button
#loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  


tkWindow.mainloop()






