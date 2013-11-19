'''
Module to run server GUI and process concurrently
'''

# from CommandLineServer import *
from ServerGUI import *

def main():
    
    myGUI = ServerGUI()
    myGUI.run()
    

if __name__ == '__main__':
    main()
    
    
