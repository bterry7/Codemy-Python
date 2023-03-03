import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

from tkinter import * # tkinter is isntalled with Python

def hello():
    hello_label = Label(root,text="Hello "+myTextBox.get())
    hello_label.pack()


root = Tk() # create window
root.title('Test')
root.geometry("400x600") # window size (pixels?)

# Create Label
myLabel = Label(root,text="Enter your first name:")
myLabel.pack() # put on screen

myTextBox = Entry(root,width=30)
myTextBox.pack()

myButton = Button(root,text="Submit",command=hello)
myButton.pack()

root.mainloop() # execute