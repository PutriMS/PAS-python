
from tkinter import *
from tkinter import messagebox
def login():
    username=entry1.get()
    password=entry2.get()

    if(username=="" and password==""):

        messagebox.showinfo("", "blank not allowed")
    elif(username=="sepri" and password=="12345"):

        messagebox.showinfo("", "login succed")
    else:
        messagebox.showinfo("","incorrect username/password")


root = Tk()
root.title("login")
root.geometry("400x300")

global entry1
global entry2

Label(root,text="LOGIN").place(x=170,y=10)
Label(root,text="username").place(x=20,y=40)
Label(root,text="password").place(x=20,y=100)
entry1 = Entry(root,bd=5)
entry1.place(x=140,y=40)
entry2 = Entry(root,bd=5)
entry2.place(x=140,y=100)

Button(root,text="Login",command= login,height=2,width=12,bd=6).place(x=100,y=180)
root.mainloop()