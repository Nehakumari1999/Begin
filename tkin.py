
from tkinter import*
from tkinModule import*



class student:
      def __init__(self,root):
            self.root=root
            
            self.root.geometry("350x500")
            self.root.config(bg='gray')
            self.root.title("Registration Form")
      #====================================AL VARIABLES======================================================================
            self.Name=StringVar()
            self.Course=StringVar()
            self.c=StringVar()
            self.Email=StringVar()
            self.var=IntVar()

      #======================================LABELS ND WIGETS=======================================================
                        
            label1=Label(self.root, bg='gray',text="Name:")
            label1.place(x=30,y=50)
            label2=Label(self.root,bg='gray',text="Course:")
            label2.place(x=30,y=100)
            #=====================OptionMenu===========
            c=StringVar()
            label_4 = Label(self.root,bg='Gray', text="country:",font=("bold", 10))
            label_4.place(x=30,y=150)
            list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
                        
            droplist=OptionMenu(root, c, *list1)
            #droplist.config(bg='Gray')
            droplist.config(width=15)
            c.set('select your country')        
            droplist.place(x=140,y=150)
            #=========================RadioButton===========
            var=IntVar()
            label47=Label(self.root,bg='gray',text="Gender:")
            label47.place(x=30,y=200)
            radbtn1=Radiobutton(self.root,bg='gray',text="M",variable=var,value=1)
            radbtn2=Radiobutton(self.root,bg='gray',text="F",variable=var,value=2)
            radbtn1.place(x=140,y=200)
            radbtn2.place(x=210,y=200)
                        
            label4=Label(self.root,bg='gray',text="Email:")
            label4.place(x=30,y=250)
            #=========================ENTRIES================
            Name=StringVar()
            Course=StringVar()
                       
            Email=StringVar()
                        
            entry1=Entry(self.root,textvar=Name)
            entry2=Entry(self.root,textvar=Course)
            entry4=Entry(self.root,textvar=Email)
            entry1.place(x=140,y=50)
            entry2.place(x=140,y=100)
            entry4.place(x=140,y=250)
            #======================set button for register===============

            exitbtn=Button(self.root,bg='Black',foreground="white",text="exit",command=ext)
            exitbtn.place(x=10,y=10)
            btn=Button(self.root,text="Registerd Now",background="Black",foreground="white",width=10,height=1)
            btn.place(x=110,y=330)
            nbtn=Button(self.root,text="Next",background="Black",foreground="white",width=5,height=1,command=newin)
            nbtn.place(x=210,y=330)
            
      
                        

                  
root=Tk()
ob=student(root)
ob1=student(root)
root.mainloop()
            
                   
