#!/usr/bin/env python

import sys
from Tkinter import *
import tkMessageBox, tkFont

import ElectionResults
import Server
from CommandLineServer import *

#==============================================================
# define global variables

# define window parameters
WINDOW_WIDTH_MAIN = 300
WINDOW_HEIGHT_MAIN = 100

presidentCount = [0]*3
congressCount = [0]*5
counselCount = [0]*4
#==============================================================


#==============================================================
# define server GUI

class ServerGUI(Tk):
    
    def createWidgets(self):
        # create font
        headingFont = tkFont.Font(family="Myriad Pro",size=28)
        
        # create heading
        self.noteLabel = Label(self, 
                                text = "Server",
                                font = headingFont)
        
        x = (WINDOW_WIDTH_MAIN - self.noteLabel.winfo_reqwidth())/2
        self.noteLabel.place(x = (WINDOW_WIDTH_MAIN - self.noteLabel.winfo_reqwidth())/2, y = 10)

        #create button to go next
        self.startButton = Button(self, text = "Start Server", width = 9, command = self.startServer)
        self.startButton.place(x = WINDOW_WIDTH_MAIN/2 - self.startButton.winfo_reqwidth(), y = WINDOW_HEIGHT_MAIN - 40)
        
        # create stop button for the server
        self.stopButton = Button(self, text = "Stop Server", width = 9, command = self.stopServer)
        self.stopButton.place(x = WINDOW_WIDTH_MAIN/2, y = WINDOW_HEIGHT_MAIN - 40)



    def startServer(self):
        
        # Algorithm startServer:
        # if checkServerStatus() == 1 or "RUNNING":
        #     print "[Note]: Server already running"
        #     return
        # else:
        #     start_server()
        #     print "[CONNECTION]: Server started."
        
        print "Server started"
        
        myserver = CommandLineServer()
        myserver.start()
    


    def stopServer(self):
        
        # Algorithm stopServer:
        # if checkServerStatus() == 0 or "STOPPED OR SLEEPING":
        #     print "[NOTE]: Server already in sleep/no=-run mode"
        # else:
        #     write_results_to_resultfile()
        #     stop_server()
        #     print "[CONNECTION]: Server stopped."

        print "Server Stopped"
        
        tkMessageBox.showinfo(title = "Server Message",
                            message = "Server has been shutdown. Voting is complete. Please don't mess up!")
        
	ElectionResults.showResults()
	# sys.exit()
        os._exit(1)
    
    
    def checkServerStatus(self):
        return 1 # for now
    
        
    def __init__(self):
        Tk.__init__(self)
        self.createWidgets()
        
    def run(self):
        centerWindow(self, WINDOW_WIDTH_MAIN, WINDOW_HEIGHT_MAIN)
        self.mainloop()
        

#==============================================================

def centerWindow(window, _width, _height):
    # get screen attributes
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    
    #get coordinates
    x = screenWidth/2 - _width/2
    y = screenHeight/2 - _height/2
    window.geometry('%dx%d+%d+%d' % (_width, _height, x, y))
    window.resizable(0,0)

'''
def main():
    server = ServerDaemon()
    centerWindow(server, WINDOW_WIDTH_MAIN, WINDOW_HEIGHT_MAIN)
    server.mainloop()

if __name__ == "__main__":
    main()
'''

# runs server GUI
'''
def runServerGUI():
   server = ServerDaemon()
   centerWindow(server, WINDOW_WIDTH_MAIN, WINDOW_HEIGHT_MAIN)
   server.mainloop()
'''

    
