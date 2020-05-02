from tkinter import *
import sqlite3


def rootSec():
            win2 = Tk()
            win2.geometry('800x600')
            win2.config(bg='Gray')
            win2.title("Registration Form")
            #label0 = Label(win2, bg='Gray',text="Student dataabase",width=20,font=("bold", 20))
            #label0.place(x=90,y=53)
            #self.Button(win2, text='Student dataabase',width=20,bg='brown',fg='white',command=info).place(x=5,y=380)
            conn = sqlite3.connect('Form.db')
            cursor=conn.cursor()
                        
            label_11 = Label(win2,bg='Gray',text="FullName",width=20,font=("bold", 10))
            label_11.grid(row=0, column=0)


            label_22 = Label(win2,bg='Gray', text="Email",width=20,font=("bold", 10))
            label_22.grid(row=0, column=1)

            label_33 = Label(win2,bg='Gray', text="Gender",width=20,font=("bold", 10))
            label_33.grid(row=0, column=2)


            label_44 = Label(win2,bg='Gray', text="country",width=20,font=("bold", 10))
            label_44.grid(row=0, column=3)


            label_5= Label(win2,bg='Gray', text="Class",width=20,font=("bold", 10))
            label_5.grid(row=0, column=4)
            
            cursor.execute('SELECT * FROM Student')
            data= cursor.fetchall()
            for index, dat in enumerate(data):
                        Label(win2,bg='Gray',  text=dat[0]).grid(row=index+1, column=0)
                        Label(win2,bg='Gray',  text=dat[1]).grid(row=index+1, column=1)
                        Label(win2,bg='Gray',  text=dat[2]).grid(row=index+1, column=2)
                        Label(win2,bg='Gray',  text=dat[3]).grid(row=index+1, column=3)
                        Label(win2,bg='Gray',  text=dat[4]).grid(row=index+1, column=4)

                      
            
            win2.mainloop
                        
                        
                        

            
                        

