from functools import partial
import tkinter as tk
from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox



def submit(n1, n2, n3, n4, n5):
    i = (n1.get())
    j = (n2.get())
    k = (n3.get())
    l = (n4.get())
    m = (n5.get())

    print(i)

    connection = MongoClient(
        "mongodb+srv://audumber:audumber@cluster0-bj3vd.mongodb.net/test?retryWrites=true&w=majority")

    database = connection['audu']
    collection = database['audu']

    mydoc = {"username": j, "password": k, "name": i, "email": l, "contact": m}

    collection.insert_one(mydoc)
    messagebox.showinfo("Title", "thankyou submited succesfuly")


top = tk.Tk()
top.geometry("500x350")
top.configure(bg="light sky blue")
# sbmitbtn2 = Button(top, text=" Submit", command=Submit(), bg="deep sky blue").place(x=140, y=300)

name = Label(top, text="Name", bg="light sky blue").place(x=50, y=50)
username = Label(top, text="UserName", bg="light sky blue", ).place(x=50, y=90)
passw = Label(top, text="Password", bg="light sky blue").place(x=50, y=130)
passw1 = Label(top, text="Re-Password", bg="light sky blue").place(x=50, y=170)
email = Label(top, text="Email", bg="light sky blue").place(x=50, y=220)
contact = Label(top, text="Contact", bg="light sky blue").place(x=50, y=260)

a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()
d = tk.StringVar()
e = tk.StringVar()
f = tk.StringVar()

e1 = tk.Entry(top, width=30, textvariable=a).place(x=140, y=50)
e2 = tk.Entry(top, width=30, bg="MediumPurple1", textvariable=b).place(x=140, y=90)
e3 = tk.Entry(top, width=30, bg="MediumPurple1", textvariable=c).place(x=140, y=130)
e4 = tk.Entry(top, width=30, textvariable=d).place(x=140, y=170)
e5 = tk.Entry(top, width=30, textvariable=e).place(x=140, y=220)
e6 = tk.Entry(top, width=30, textvariable=f).place(x=140, y=260)

submit = partial(submit, a, b, c, e, f)
sbmitbtn2 = tk.Button(top, text=" Submit", command=submit, bg="deep sky blue").place(x=140, y=300)

top.mainloop()