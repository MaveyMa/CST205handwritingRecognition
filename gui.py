'''
NAME: Mavey Ma
LAST EDITED: March 30, 2016
DESCRIPTION: Graphical User Interface for iDigit with three buttons:
[DRAWPAD] - User draws number with mouse
[UPLOAD] - Browse and upload photo to analyze
[EXIT] - Closes window
'''
from Tkinter import *
import Tkinter as tk
import tkFont
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
#==========FUNCTION DEFINITIONS==========
#BUTTON DRAWPAD: ALLOWS USER TO OPEN DRAWPAD
def paint(event):
   black = "#000000"
   x1, y1 = (event.x - 5), (event.y - 5)
   x2, y2 = (event.x + 5), (event.y + 5)
   w.create_oval(x1, y1, x2, y2, fill=black)

def clear():
   w.delete("all")

def dibujar():
    canvas_width = 350
    canvas_height = 350
    #c = Tk()
    #INSTRUCTIONS IN UPPER RIGHT HAND CORNER
    message = Label(master, text = "Press & slowly drag the mouse to draw.",
                    font=courierText)
    message.place(x=0,y=25)
    #WHITE CANVAS
    d = Canvas(master, width=canvas_width, height=canvas_height)
    #d.place(x=175, y=100)
    d.bind("<B1-Motion>", paint)
    #CLEAR CANVAS
    clean = Button(master, text="CLEAR CANVAS", font=courierFont, 
                   fg="black", bg="white",
                   activeforeground="white", activebackground="black",
                   command=clear, width = 12)
    clean.place(x=460, y=0)

#BUTTON UPLOAD: ALLOWS USER TO SELECT A FILE TO UPLOAD
def browse():
    #Tk().withdraw() #this would prevent the root window from appearing
    filename = askopenfilename() #show an "Open" dialog box and return the path to the selected file
    im = Image.open(filename)
    tkimage = ImageTk.PhotoImage(im)
    tk.Label(master, image=tkimage).pack()
    return filename
#==========STYLE SET UP==========
#BOX
master = Tk()
#CREATE A CANVAS w SIZE 800x500
w = Canvas(master, width=600, height=500)
#CONTROL WHERE THINGS ARE LOCATED: EXPAND, FILL, SIDES
w.pack()
#SET FONT
courierFont = tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD)
courierText = tkFont.Font(family="Courier", size=15, weight=tkFont.BOLD)
#WINDOW TITLE
master.title("i d i g i t     [Number Identifier]")
#WELCOME TEXT
welcome = Label(master, text = "Welcome to iDigit.",
                    font=courierText)
welcome.place(x=0,y=0)
#NOTE: TOP FRAME IS DEFAULT
#BOTTOM LOCATION
bottomFrame = Frame(master)
bottomFrame.pack(side=BOTTOM)
#RIGHT LOCATION
rightFrame = Frame(master)
rightFrame.pack(side=RIGHT)
#LEFT LOCATION
leftFrame = Frame(master)
leftFrame.pack(side=LEFT)
#==========BUTTONS==========
""" TEMPLATE FOR BUTTON PARAMETERS
BUTTON(LOCATION, TEXT, FONT,
       FOREGROUND(COLOR OF TEXT), BACKGROUND,
       HOVERTEXT, HOVERGROUND)
"""
#BUTTON DRAWPAD: ALLOWS USER TO OPEN DRAWPAD
drawPadButton = Button(leftFrame, text="DRAWPAD", font=courierFont, 
                      fg="black", bg="LightBlue",
                      activeforeground="white", activebackground="#00BFFF",
                      command=dibujar, width = 12)
drawPadButton.pack(side=LEFT)

#BUTTON UPLOAD: ALLOWS USER TO SELECT A FILE TO UPLOAD
uploadButton = Button(leftFrame, text="UPLOAD", font=courierFont, 
                      fg="black", bg="LightGreen",
                      activeforeground="white", activebackground="#00BA37",
                      command=browse, width = 12)
uploadButton.pack(side=LEFT)

#BUTTON EXIT: CLOSES WINDOW
resetButton = Button(leftFrame, text="EXIT", font=courierFont,
                     fg="black", bg="pink",
                     activeforeground="white", activebackground="#FF0DF2",
                     command=quit, width = 12)
resetButton.pack(side=LEFT)
#==========PROCESS INPUT HERE==========

#END PROGRAM, RUN IT
mainloop()

"""
import Tkinter as tk

#Creates a window with a quit button that does so when clicked.
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()
"""
