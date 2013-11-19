#!/usr/bin/env python

import sys, pickle
sys.path.append('..')
import Auditor

def changeResultsFile(noOfFakeUsers):    
    filePath = 'ResultsFile.pkl'
    inputFile = open(filePath, 'rb')
    voteBank = pickle.load(inputFile)
    inputFile.close()

    presidentCount = voteBank['president']
    congressCount = voteBank['congress']
    counselCount = voteBank['counsel']
    
    #I want to make president alpha win.
    presidentCount[0] = presidentCount[0] + noOfFakeUsers
    
    #I want epsilon to take charge.
    congressCount[2] = congressCount[2] + noOfFakeUsers
    congressCount[4] = congressCount[4] + noOfFakeUsers
    
    #I want counsel delta to lead
    counselCount[3] = counselCount[3] + noOfFakeUsers
    
    resultDict = {
        'president' : presidentCount,
        'congress' : congressCount,
        'counsel' : counselCount
    }
    
    output = open('ResultsFile.pkl', 'wb')
    pickle.dump(resultDict, output)
    output.close()

def changeAuditLogFile(noOfFakeUsers):
    
    counter = 0

    # read file
    try:
        counterFile = open("CounterPL.txt", 'r')
        counter = int(counterFile.read())
        counterFile.close()
    except IOError:
        counterFile = open("CounterPL.txt", 'w')
        counterFile.write(str(0))
        counterFile.close()

    # increment counter total-number-of-fake-user times
    counter += noOfFakeUsers

    # write counter back to the preference file
    counterFile = open("CounterPL.txt", 'w')
    counterFile.write(str(counter))
    counterFile.close()
        
    # need to write the exact same data to the audit file
    output = open('AuditLog.pkl', 'ab') # ap: append byte
    for i in range(0, noOfFakeUsers):
        voteDict = {
            "user"+str(i) : {
                "president" : [0],
                "congress" : [2, 4],
                "counsel" : [3]
            }
        }
        pickle.dump(voteDict, output)
    output.close()

    # parse audit log file
    auditorObj = Auditor.Auditor()
    auditCount = auditorObj.parseAuditLogFile(None) # no file name given: used for test

def main():
    noOfFakeUsers = 50000
    
    # change results file
    changeResultsFile(noOfFakeUsers)
    
    # change audit log
    changeAuditLogFile(noOfFakeUsers)
    
if __name__ == '__main__':
    main()
