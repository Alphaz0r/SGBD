import os
from tkinter import *
from functools import partial
import database

def valider(username, password):
	ecole=database.Database(username.get(), password.get())

#window
tkWindow = Tk()  
tkWindow.geometry('250x100')  
tkWindow.title('Connexion')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

valider = partial(valider, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=valider).grid(row=4, column=0)  

tkWindow.mainloop()