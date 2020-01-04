#dev-audumber chaudhari

from functools import partial
import tkinter as tk
import tryyy
from  tryyy import *
import pymongo
from pymongo import MongoClient
from tkinter import *


top = tk.Tk()
top.configure(bg="light sky blue")
top.geometry("500x350")

def log(e1,e2):
  idd=e1.get()
  pas=e2.get()
  connection = MongoClient(
    "mongodb+srv://audumber:audumber@cluster0-bj3vd.mongodb.net/test?retryWrites=true&w=majority")

  database = connection['audu']
  collection = database['audu']

  myquery = {"username": idd, "password": pas}

  mydoc = collection.find(myquery)
  k= "Great!! your logged In"
  for x in mydoc:
    top = Tk()
    frame = Frame(top)

    top.geometry("500x350")
    top.configure(bg="light sky blue")
    frame.pack()

    name = Label(top, text="Thank-You \n These was Demo login from Zsploit.co.in ",font=3, height=5, width = 35).place(x=70, y=50)



uname = Label(top, text="USERNAME").place(x=80, y=120)
password = Label(top, text="PASSWORD").place(x=80, y=170)
a = tk.StringVar()
b = tk.StringVar()
e1 = tk.Entry(top, width=30,textvariable=a).place(x=160, y=120)

e2 = tk.Entry(top, width=30,textvariable=b).place(x=160, y=170)

obj1=tryyy.au
log = partial(log,a,b)

sbmitbtn = Button(top, text=" LogIn ",command=log, bg="light blue", activebackground="deep sky blue").place(x=120, y=230)
sbmitbtn1 = Button(top, text=" SignUp ", bg="light blue", activebackground="deep sky blue").place(x=200, y=230)


top.mainloop()