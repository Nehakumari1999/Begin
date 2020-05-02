import tkinter as tk
from tkinter import*


def ext():
            exit()

def newin():
            newscreen=tk.Tk()
            newscreen.geometry("350x500")
            newscreen.config(bg='gray')
            label=tk.Label(newscreen,bg='gray',text="WELCOME TO OUR COCHING",font=('monotype corsiva',15, 'bold'))
            label.place(x=50,y=100)
            label5=tk.Label(newscreen,bg='gray',text="Create Password:")
            label6=tk.Label(newscreen,bg='gray',text="Confirm Password:")
            label5.place(x=30,y=200)
            label6.place(x=30,y=250)
            entry5=tk.Entry(newscreen,bd=1,show="*")
            entry6=tk.Entry(newscreen,bd=1,show="*")
            entry5.place(x=140,y=200)
            entry6.place(x=140,y=250)
            newbtn=tk.Button(newscreen,text=" Set password ",background="Black",foreground="white",width=18,height=1)
            newbtn.place(x=30,y=350)
            lbtn=tk.Button(newscreen,text="Goto Login",background="Black",foreground="white",width=10,height=1,command=logwin)         
            lbtn.place(x=200,y=350)
            newscreen.mainloop()




def logwin():
            logScreen=tk.Tk()
            logScreen.geometry("350x500")
            logScreen.config(bg='gray')
            label_1=tk.Label(logScreen,bg='gray',text="LOGIN IF YOU ARE REGISTERED",font=('monotype corsiva',15, 'bold'))
            label_1.place(x=30,y=100)
            label5_2=tk.Label(logScreen,bg='gray',text="Name:")
            label6_3=tk.Label(logScreen,bg='gray',text="Password:")
            label5_2.place(x=30,y=200)
            label6_3.place(x=30,y=250)
            entry5_0=tk.Entry(logScreen,bd=1)
            entry6_1=tk.Entry(logScreen,bd=1,show="*")
            entry5_0.place(x=140,y=200)
            entry6_1.place(x=140,y=250)
            lbtn_0=tk.Button(logScreen,text="Login",background="Black",foreground="white",width=5,height=1)         
            lbtn_0.place(x=150,y=300)
                                    
            logScreen.mainloop()


