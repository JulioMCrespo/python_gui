#in this version we will learn how to organize the layout

from tkinter import *

root = Tk() #main window

#a frame is a basic rectangle with stuff in it
topFrame = Frame(root) #creates an invisible container in main root
#now place on window (place it anywhere)
topFrame.pack()
#frame also in the bottom
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

#lets put in some widget 
#button called on on topFrame that says Button 1 color red
button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text='Button 4', fg="purple")

#now we want to tell our program that we actually want to display widgets
#we want to pack them in
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
#the side=LEFT means pack it in the left frame and 
#place it as far left as possible
button4.pack(side=BOTTOM)


root.mainloop() #display on screen until we exit out