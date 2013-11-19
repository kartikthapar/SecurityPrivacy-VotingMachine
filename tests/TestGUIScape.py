#!/usr/bin/env python

import sys, platform
from Tkinter import *
import tkFont

WINDOW_WIDTH_MS = 500
WINDOW_HEIGHT_MS = 100

class MainScreen(Tk):
    
    def createWidgets(self):
        # create heading

        headingFont = None
        if platform.system() == 'Darwin':
            headingFont = tkFont.Font(family="Myriad Pro",size=28)
        elif platform.system() == 'Windows':
            headingFont = tkFont.Font(family="Arial",size=24)
        elif platform.system() == 'Linux':
            headingFont = tkFont.Font(family="Arial",size=24)
            
        self.noteLabel = Label(self, 
                                text = "Press start to begin your voting session.",
                                font = headingFont)
        
        x = (WINDOW_WIDTH_MS - self.noteLabel.winfo_reqwidth())/2
        self.noteLabel.place(x = (WINDOW_WIDTH_MS - self.noteLabel.winfo_reqwidth())/2, y = 10)
        
        def startVoting():
            print "Authenticate --->"
            self.destroy()
        
        #create button to go next
        self.startButton = Button(self, text = "Start", command = startVoting)
        self.startButton.place(x = (WINDOW_WIDTH_MS - self.startButton.winfo_reqwidth())/2, y = 55)
        
    def __init__(self, master=None):
        Tk.__init__(self)
        self.createWidgets()

def centerWindow(window, _width, _height):
    # get screen attributes
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    
    #get coordinates
    x = screenWidth/2 - _width/2
    y = screenHeight/2 - _height/2
    window.geometry('%dx%d+%d+%d' % (_width, _height, x, y))
    window.resizable(0,0)


while 1:
    mainScreen = MainScreen()
    centerWindow(mainScreen, WINDOW_WIDTH_MS, WINDOW_HEIGHT_MS)
    mainScreen.mainloop()
    continue

    print "hello"