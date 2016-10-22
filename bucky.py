from tkinter import *

#very basic window
#all the sliders and buttons are called widgets

#get a variable of any name
#below we are creating an object from a class
root = Tk() #this is a constructor
#from now on root is the name of the window

#call it whatever you want, where do you want it, what do you want in it
theLabel = Label(root,text="this is too easy")
theLabel.pack()#this will pack it in there
root.mainloop()