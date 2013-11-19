#!/usr/bin/env python

import sys
from Tkinter import *
import tkMessageBox, tkFont
from tkFileDialog import askopenfilename
import Auditor


#==============================================================
# define global variables

# define window parameters
WINDOW_WIDTH_MAIN = 400
WINDOW_HEIGHT_MAIN = 175

auditLogFile = None
resultFile = None

#==============================================================


#==============================================================
# define server GUI

class AuditDaemon(Tk):
    
    def createWidgets(self):
        
        # get fonts
        headingFont = tkFont.Font(family = "Myriad Pro",size = 28)
        fileFont = tkFont.Font(family = "Myriad Pro",size = 14)
        
        # create heading
        self.noteLabel = Label(self, 
                                text = "Auditor",
                                font = headingFont)
        
        x = (WINDOW_WIDTH_MAIN - self.noteLabel.winfo_reqwidth())/2
        self.noteLabel.place(x = (WINDOW_WIDTH_MAIN - self.noteLabel.winfo_reqwidth())/2, y = 10)
        
        _padding_bw = 10 # padding in between button and label
        
        # RESULT FILE--------------------------------------------------------------------------------------------
        # create a StringVar() variable to control text for ResultFile's label
        fileLabelVar = StringVar()
        
        # set text to initial value
        fileLabelVar.set("Click button to select file")
        
        # create ResultFile button
        self.resultFileButton = Button(self, text = "Result Log File", width = 12, 
                                    command = lambda i=fileLabelVar: self.getResultFile(i))
                                    
        # create ResultFile label
        self.resultFileLabel = Label(self, textvariable = fileLabelVar, font = fileFont)
        
        # place resultfile button and label
        _len_line = self.resultFileButton.winfo_reqwidth() + _padding_bw + self.resultFileLabel.winfo_reqwidth()
        xButton = (WINDOW_WIDTH_MAIN - _len_line)/2
        self.resultFileButton.place(x = xButton, y = 63)
        self.resultFileLabel.place(x = xButton + self.resultFileButton.winfo_reqwidth() + _padding_bw, y = 65)
        
        
        # AuditLogFile---------------------------------------------------------------------------------------------------
        # create a StringVar() variable to control text for AuditLogFile's label
        auditLabelVar = StringVar()
        
        # set text to initial value
        auditLabelVar.set("Click button to select file")
        
        # create AuditLogFile button
        self.auditFileButton = Button(self, text = "Audit Log File", width = 12,
                                            command = lambda i=auditLabelVar: self.getAuditLogFile(i))
                                            
        # create AuditLogFile label
        self.auditFileLabel = Label(self, textvariable = auditLabelVar, font = fileFont)
        
        # place AuditLogFile button and label
        _len_line = self.auditFileButton.winfo_reqwidth() + _padding_bw + self.auditFileLabel.winfo_reqwidth()        
        xButton = (WINDOW_WIDTH_MAIN - _len_line)/2
        self.auditFileButton.place(x = xButton, y = 93)
        self.auditFileLabel.place(x = xButton + self.resultFileButton.winfo_reqwidth() + _padding_bw, y = 95)
        
        #create button to go next
        self.startButton = Button(self, text = "Start Audit", width = 9, command = self.startAudit)
        self.startButton.place(x = WINDOW_WIDTH_MAIN/2 - self.startButton.winfo_reqwidth()/2, y = WINDOW_HEIGHT_MAIN - 40)
        


    def getResultFile(self, var):
        """
        Usage: self.getResultFile(StringVar() type variable)
        Description: get the path of the result file
        """
        
        global resultFile
        
        # get resultFile from file dialog window.
        # change textvariable accordingly
        # file type must be of type --- pickle database
        resultFile = askopenfilename(initialdir = './', filetypes=(("Pickle database", "*.pkl"),))
        if resultFile != "":
            var.set("Result File Selected")
        else:
            var.set("Click button to select file")


        
    def getAuditLogFile(self, var):
        """
        Usage: self.getAuditLogFile(StringVar() type variable)
        Description: get the path of the audit log file
        """

        global auditLogFile

        # get auditLogFile from file dialog window.
        # change textvariable accordingly
        # file type must be of type --- pickle database
        auditLogFile = askopenfilename(initialdir = './', filetypes=(("Pickle database", "*.pkl"),))
        if auditLogFile != "":
            var.set("Audit Log File Selected")
        else:
            var.set("Click button to select file")



    def startAudit(self):
        """
        Usage: self.startAudit()
        Description: Compare results from both audit log file and the result file
        """
        
        # check if both are valid files
        # if not, return from this function
        # comment out for debugging
        global auditLogFile, resultFile
        
        if auditLogFile == "" or auditLogFile == None or resultFile == "" or resultFile == None:
            tkMessageBox.showwarning(title = "Select Log Files",
                                    message = "Select both log files to audit.")
            return
        
        # if no audit log file is set, set them to default databases
        # used for debugging purposes.
        # usually the above check commented
        if auditLogFile == None:
            auditLogFile = 'AuditLog.pkl'
        if resultFile == None:
            resultFile = 'ResultFile.pkl'
        
        auditorObj = Auditor.Auditor()

        # parse result and log files
        auditCount = auditorObj.parseAuditLogFile(auditLogFile)
        resultCount = auditorObj.parseResultsFile(resultFile)
        
        # process audit
        success = auditorObj.startAudit(auditCount, resultCount)
        
        # display the result
        self.displayResult(success)        


    def displayResult(self, success):
        """
        Usage: self.displayResult(0) or self.displayResult(1)
        Description: Shows an error dialogue box if the audit log file and the result file values do not match.
                     Shows a success dialogue box if the audit log file and the result file values match.
        """
        
        if not success:
            tkMessageBox.showerror(title = "Election Failure",
                                message = "The votes from the audit log file and the result file don't match.")
        else:
            tkMessageBox.showinfo(title = "Election Success",
                                message = "The votes from the audit log file and the result file match.")
        sys.exit()
    
        
    def __init__(self, master=None):
        Tk.__init__(self)
        self.createWidgets()

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


def main():
    server = AuditDaemon()
    centerWindow(server, WINDOW_WIDTH_MAIN, WINDOW_HEIGHT_MAIN)
    server.mainloop()

if __name__ == "__main__":
    main()
    
    
    