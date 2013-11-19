#!/usr/bin/env python

import sys
sys.path.append('..')
import pickle
import Database

totalNoOfUsers = 100

def readDataIntoList():
    """
    Description: reads database consisting voting ID info including publick keys and voting status
    """

    userDict = []
    filePath = 'Database.pkl'
        
    # read database to get userID and information
    inputFile = open(filePath, 'rb')
    for i in range(0, totalNoOfUsers):
        userInfo = pickle.load(inputFile)
        userIDHash = userInfo.keys()[0]
        value = {
            userIDHash : {
                'pkey' : userInfo[userIDHash]['pkey'],
                'voted' : userInfo[userIDHash]['voted']
                }
            }

        userDict.append(value)
                
    inputFile.close()
    testDatabase(userDict)
    # return userDict

    
def testDatabase(userDict):
    output = open('datacheck.pkl', 'ab')
    for i in range(0, len(userDict)):
        pickle.dump(userDict[i], output)
    output.close()


def main():
        databaseObj = Database.Database()
        databaseObj.createDatabase()
        readDataIntoList()
        sys.exit()


if __name__ == "__main__":
    main()

