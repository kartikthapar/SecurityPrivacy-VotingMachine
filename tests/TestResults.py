#!/usr/bin/env python

import sys
sys.path.append('..')
import Auditor, Server

# =========================================
# Checks the functionality of the file parser for the Results database.

def main():
    # using values from TestAuditor.py
    voteDict = [
        {"user1" : {
            "president" : [1],
            "congress" : [2, 3],
            "counsel" : [3]
        }},
        {"user2" : {
            "president" : [0],
            "congress" : [0, 3],
            "counsel" : [0]
        }},
        {"user3" : {
            "president" : [1],
            "congress" : [2, 4],
            "counsel" : [2]
        }}
    ]
    
    # write results to results file
    serverObj = Server.Server()
    serverObj.touchResultsFile()
    serverObj.addToResultsFile(voteDict[0]['user1'])
    serverObj.addToResultsFile(voteDict[1]['user2'])
    serverObj.addToResultsFile(voteDict[2]['user3'])
        
    # read the results file
    auditorObj = Auditor.Auditor()
    resultCount = auditorObj.parseResultsFile(None)
    
    for i in range(0, len(resultCount)):
        print resultCount[i]

if __name__ == "__main__":
    main()