#!/usr/bin/env python

import sys, os
import pickle

class Server():
    
    def touchResultsFile(self, noOfTimes = None):
        """
        Description: create file; same as os.system('touch fileName')
        Usage: only used when the server starts; touchResultsFile()
        """
        
        # file name is precomputed but it can be chosen to anything; default is better
        fileName = 'ResultFile.pkl' 
        with file(fileName, 'a'): # 'with'
            os.utime(fileName, noOfTimes)
    

    def addToResultsFile(self, voteDict):
        """
        Usage: addToResultsFile(voteDict)
        Description: creates a combined dictionary Result and stores it into a pickle database
        """
        
        # create an empty resultDict dictionary to hold the entire result
        resultDict = {}
        
        # open the result file --- ResultFile.pkl
        # this will always be ok as the server runs touchResultFile() at the very starting
        results = open('ResultFile.pkl', 'rb')
        try:
            # for a newly created ResultFile, there will be no dictionaries
            # first addToResultsFile will fail with an EOFError
            # pickle.load(stream) to get the dictionary value
            resultDict = pickle.load(results)
        except EOFError:
            # if this is the first time, you are using addToResultsFile
            # use an empty dict for resultDict
            resultDict = {
                'president' : [0]*3,
                'congress' : [0]*5,
                'counsel' : [0]*4
            }
        results.close()
        
        # if length of the voteDict is greater than zero,
        # then increment the vote count for the particular president
        
        if len(voteDict['president']) > 0:
            value = voteDict['president'][0]
            resultDict['president'][value] += 1
        
        # as you can select more than 1 congress member, if the value of the list is greater than zero,
        # then for all the values inside the vote list for the particular singular vote, increment
        # results for congress members
        if len(voteDict['congress']) > 0:
            value = voteDict['congress']
            for val in value:
                resultDict['congress'][val] += 1
        
        # similar to the president scenario
        if len(voteDict['counsel']) > 0:
            value = voteDict['counsel'][0]
            resultDict['counsel'][value] += 1
        
        # resultDict = {
        #     'president' : [20, 40, 60],
        #     'congress' : [],
        #     'counsel' : []
        # }
        
        # not necessary, but still using the default database
        fileName = "ResultFile.pkl"

        # store result back into the pickle database it read from
        output = open(fileName, 'wb')
        pickle.dump(resultDict, output)
        output.close()
    
    
    def addToAuditLogFile(self, voteDict):
        """
        Usage: addToAuditLogFile(votedict)
               voteDict must be a single dictionary; for 1 Single voterID
        Description: adds vote to the vote bank located in AuditLog.pkl database
        """
        
        # initialize counter to zero [no of votes]
        counter = 0
        
        # reading the counterPL.txt file
        try:
            # if the file does not exist, will return in an IOError
            # read file and get the value of count
            counterFile = open("CounterPL.txt", 'r')
            counter = int(counterFile.read())
            counterFile.close()
        except IOError:
            # in case file not found and returned with an IOError,
            # create a file with counter value as 0
            counterFile = open("CounterPL.txt", 'w')
            counterFile.write(str(0))
            counterFile.close()

        # increment counter everytime you log to the audit log file; this is slow
        counter += 1
        
        # write counter back to the preference file
        counterFile = open("CounterPL.txt", 'w')
        counterFile.write(str(counter))
        counterFile.close()
        
        # the dictionary is the precomputed value and contains user-info (hashed) as well
        # need to write the exact same data to the audit file
        output = open('AuditLog.pkl', 'ab')
        pickle.dump(voteDict, output)
        output.close()
        
