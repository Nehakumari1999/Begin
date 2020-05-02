from tkinter import *
import sqlite3
from RegistrationModule import* 


root = Tk()
root.geometry('800x600')
root.config(bg='Gray')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
Class=StringVar()
#var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   Classs=Class.get()
   conn = sqlite3.connect('Form.db')
   with conn:
               cursor=conn.cursor()
               cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Class TEXT)')
               cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Class) VALUES(?,?,?,?,?)',(name1,email,gender,country,Classs,))
               conn.commit()
               
   
             
label_0 = Label(root, bg='Gray',text="Registration form",width=20,font=('Lucida Calligraphy handwriting',18, 'bold'))
label_0.place(x=200,y=53)


label_1 = Label(root,bg='Gray',text="FullName",width=20,font=("bold", 10))
label_1.place(x=140,y=160)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=420,y=160)

label_2 = Label(root,bg='Gray', text="Email",width=20,font=("bold", 10))
label_2.place(x=128,y=210)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=420,y=210)

label_3 = Label(root,bg='Gray', text="Gender",width=20,font=("bold", 10))
label_3.place(x=130,y=260)

Radiobutton(root,bg='Gray', text="Male",padx = 5, variable=var, value=1).place(x=420,y=260)
Radiobutton(root, bg='Gray',text="Female",padx = 20, variable=var, value=2).place(x=475,y=260)

label_4 = Label(root,bg='Gray', text="country",width=20,font=("bold", 10))
label_4.place(x=130,y=310)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root, c, *list1)
droplist.config(bg='Gray')
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=420,y=310)

label_4 = Label(root,bg='Gray', text="Class",width=20,font=("bold", 10))
label_4.place(x=130,y=360)
entry_4 = Entry(root,textvar=Class)
entry_4.place(x=420,y=360)


                                                                                                                                                                              

Button(root, text='Student Details',width=13,bg='brown',fg='white',command=rootSec).place(x=700,y=2)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=280,y=410)

root.mainloop()

