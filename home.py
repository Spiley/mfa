from tkinter import *
from subprocess import call
import time
from tkinter import messagebox

start = time.time()

while(time.time()-start>10):
    messagebox.showinfo(title='Ongeldig', message="Code niet meer geldig. Log opnieuw in.")
    print('iets')


tkWindow = Tk()  
tkWindow.geometry('925x500+300+200')  
tkWindow.title('Inloggen')
tkWindow.configure(bg="#fff")
tkWindow.resizable(False,False)

global email
global passw
email = StringVar()
passw = StringVar()

img = PhotoImage(file='home.png')
Label(tkWindow,image=img,bg='white').place(x=50,y=50)

img2 = PhotoImage(file='mark.png')
#resize img2
img2 = img2.subsample(5,5)
Label(tkWindow,image=img2,bg='white').place(x=70,y=70)

frame=Frame(tkWindow,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text= 'Welkom', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)

Label(frame,text= 'Deze sessie duurt 30 min',fg='#57a1f8', bg='white').place(x=100,y=50)
def stop():
    tkWindow.destroy()
    call(["python", "login.py"])

Button(tkWindow,width=39, pady=7, text="Uitloggen", bg='#57a1f8', fg='white',border=0,command=stop).place(x=67,y=360)  




tkWindow.mainloop()




