#!/usr/bin/env python

import sys
sys.path.append('..')
import Auditor, Server

# =========================================
# Checks the functionality of the check between the result's and auditlog's databases.

def main():
    # generate AuditLog
    
    serverObj = Server.Server()
    auditorObj = Auditor.Auditor()
    
    auditCount = auditorObj.parseAuditLogFile(None)
    resultCount = auditorObj.parseResultsFile(None)
    
    auditCheck(auditCount, resultCount)


def auditCheck(auditCount, resultCount):
    # if the lengths are not same --- WE ARE ...
    for i in range(0, len(auditCount)):
        if len(auditCount[i]) != len(resultCount[i]):
            print "ERROR - Votes are messed up"
            sys.exit()
        
    for i in range(0, len(auditCount)):
        for j in range(0, len(auditCount[i])):
            if auditCount[i][j] != resultCount[i][j]:
                print "Wrong voting"
                sys.exit()
            
    print "Voting is good."
    
    
if __name__ == "__main__":
    main()