from tkinter import *
def printName():
    print("Hello Udhay")


root = Tk()
theLabel = Label(root,text="Hello")
button1  = Button(root,text="Enter")
button1.bind("<Button-1>",printName())

button1.pack(side=LEFT)
theLabel.pack()
root.mainloop()