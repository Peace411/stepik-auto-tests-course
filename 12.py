import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')
    print (str(int(15+15)))



root = Tk()

# This is the section of code which creates the main window
root.geometry('702x477')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates a button
Button(root, text='Button text!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=182, y=118)


root.mainloop()