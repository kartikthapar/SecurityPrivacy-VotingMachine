#!/usr/bin/env python

import sys
sys.path.append('..')
import Auditor, Server

# =========================================
# Checks the functionality of the check between the result's and auditlog's databases.

def main():
    serverObj = Server.Server()
    auditorObj = Auditor.Auditor()
    
    auditCount = auditorObj.parseAuditLogFile(None)
    resultCount = auditorObj.parseResultsFile(None)
    
    auditorObj.startAudit(auditCount, resultCount)
    
if __name__ == "__main__":
    main()