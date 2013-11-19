#!/usr/bin/env python

import sys
sys.path.append('..')
import Auditor, Server

# =========================================
# Test's Auditor functionality

def main():
    
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
    
    # write content to audit log file
    serverObj = Server.Server()
    serverObj.addToAuditLogFile(voteDict[0])
    serverObj.addToAuditLogFile(voteDict[1])
    serverObj.addToAuditLogFile(voteDict[2])
    
    # parse audit log file
    auditorObj = Auditor.Auditor()
    auditCount = auditorObj.parseAuditLogFile(None) # no file name given: used for test
    
    for i in range(0, len(auditCount)):
        print auditCount[i]
    
    
if __name__ == "__main__":
    main()