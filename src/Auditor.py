#!/usr/bin/env python

from __future__ import print_function
import sys, pickle

class Auditor():
    
    def parseAuditLogFile(self, filePath):
        """
        Usage: parseAuditLogFile(filePath)
               parseAuditLogFile(None)
        Description: To find the number of votes for respective categories in the election;
                     Only used in case of an Audit; i.e. after the election.
        """
        
        # voteDict format:
        # {hash(voterID + PIN), {president = [], counsel = [], congress = []}}
        # hash(voterID + PIN) is the key to voteDict
        
        # create an empty dict
        voteBank = {}
        totalNoOfPolls = 0 # set polls to zero
        
        # read file --- get value of total number of polls
        counterFile = open("CounterPL.txt", 'r')
        totalNoOfPolls = int(counterFile.read())
        counterFile.close()

        # set default counts for president, congress and counsel
        # these are separate lists
        presidentCount = [0]*3
        congressCount = [0]*5
        counselCount = [0]*4
        
        # create empty to store votes by multiple users
        presidentVote = []
        congressVote = []
        counselVote = []
        
        # if no file path is provided, use AuditLog.pkl
        # default database -- used for debugging
        if filePath == None:
            filePath = 'AuditLog.pkl'
        
        # read AuditLog file to parse vote data
        inputFile = open(filePath, 'rb')
        for i in range(0, totalNoOfPolls):
            
            # get votebank: a single vote: {user: {'president':[1], 'congress':[2, 3], 'counsel':[0]}}
            voteBank = pickle.load(inputFile)
            
            # get the user ID; only one key in the super voteBank dict
            userID = voteBank.keys()[0]
            
            # get respective votes; these are in tuples; append them to presidentVote
            presidentVote.append(voteBank[userID]['president'])
            congressVote.append(voteBank[userID]['congress'])
            counselVote.append(voteBank[userID]['counsel'])
            
        inputFile.close()
        
        # calculate votes
        for index in range(0, totalNoOfPolls):
            # president
            if len(presidentVote[index]) > 0:
                value = presidentVote[index][0] # president[index] -> list of votes by a single voterID, [0] => value
                presidentCount[value] += 1 # for a particular president-value, increment counter for that president
            
            # congress
            # congress has multiple votes; so we check for all the values and increment the votes for the same
            # congressVote[index] returns a list like [2, 4]; for each value in this list increment count
            if len(congressVote[index]) > 0:
                value = congressVote[index]
                for val in value:
                    congressCount[val] += 1
            
            # counsel
            if len(counselVote[index]) > 0:
                value = counselVote[index][0]
                counselCount[value] += 1
        
        # return a total count
        _voteCount = [presidentCount, congressCount, counselCount]
        return _voteCount
    
        
    def parseResultsFile(self, filePath):
        """
        Usage: parseResultsFile(filePath)
               parseResultsFile(None) #test
        Description: parses the Result file to obtain the vote information 
        """
        
        # format:
        # {president = [], congress = [], councel = []}
        # represents total count
        
        # create empty list to hold the result database
        voteBank = {}
        
        # default file incase no file specified
        # ResultFile.pkl used for debugging purposes
        if filePath == None:
            filePath = "ResultFile.pkl"
        
        # read the pickle database
        # get the result dictionary
        inputFile = open(filePath, 'rb')
        voteBank = pickle.load(inputFile)
        inputFile.close()
        
        # get president, congress, counsel counts and return them
        presidentCount = voteBank['president']
        congressCount = voteBank['congress']
        counselCount = voteBank['counsel']
        
        _voteCount = [presidentCount, congressCount, counselCount]
        return _voteCount


    def startAudit(self, auditCount, resultCount):
        """
        Description: Audits the votes and checks for any discrepancies in the votes in the result and the audit log files
        Usage: success = startAudit(count1, count2)
        """
        
        # if the lengths are not same, you must exit
        for i in range(0, len(auditCount)):
            if len(auditCount[i]) != len(resultCount[i]):
                print("ERROR - Votes are messed up")
                sys.exit()
        
        # check for vote number match
        # the two lists returned from the parsed file are simply the total counts for each files
        # check for list element by element and compare lists
        # if any element is different, return 0
        
        for i in range(0, len(auditCount)):
            for j in range(0, len(auditCount[i])):
                if auditCount[i][j] != resultCount[i][j]:
                    print ("Wrong voting")
                    return 0
            
        print ("Voting is good.")
        return 1