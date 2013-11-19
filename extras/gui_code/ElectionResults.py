#!/usr/bin/env python

import sys
import Auditor

def main():
    
    auditorObj = Auditor.Auditor()
    resultCount = auditorObj.parseResultsFile(None)

    nameList = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
    
    for i in range(0, 3):
        print "President %s scores: %d votes." % (nameList[i], resultCount[0][i])
    for i in range(0, 5):
        print "Congress member %s scores: %d votes." % (nameList[i], resultCount[1][i])
    for i in range(0, 4):
        print "Counsel member %s scores: %d votes." % (nameList[i], resultCount[2][i])
    
def getWinners(resultCount):
    presidentCount = resultCount[0]
    congressCount = resultCount[1]
    counselCount = resultCount[2]
    
    president = getMax(presidentCount, 1)
    congress = getMax(congressCount, 2)
    counsel = getMax(counselCount, 1)
    
    return president, congress, counsel
    
def getMax(count, total):
    if total == 1:
        max_index = max((v, i) for i, v in enumerate(count))[1]
        return max_index
    
    index = []
    if total == 2:
        max_index = max((v, i) for i, v in enumerate(count))[1]
        index.append(max_index)
        del count[max_index]
        max_index = max((v, i) for i, v in enumerate(count))[1]
        index.append(max_index)
        return sorted(index)
    
if __name__ == "__main__":
    main()