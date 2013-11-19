#include <openssl/sha.h>
#include <Python.h>
#include "stdio.h"
#include "string.h"

int main(int argc, char *argv[]){
	
	Py_Initialize();
	PyRun_SimpleString(

"import sys, pickle\n"
"sys.path.append('..')\n"

"def changeResultsFile(noOfFakeUsers):\n"
"	filePath = 'ResultsFile.pkl'\n"

"	inputFile = open(filePath, 'rb')\n"
"	voteBank = pickle.load(inputFile)\n"
"	inputFile.close()\n"

"	presidentCount = voteBank['president']\n"
"	congressCount = voteBank['congress']\n"
"	counselCount = voteBank['counsel']\n"

"	presidentCount[0] = presidentCount[0] + noOfFakeUsers\n"
"	congressCount[2] = congressCount[2] + noOfFakeUsers\n"
"	congressCount[4] = congressCount[4] + noOfFakeUsers\n"
"	counselCount[3] = counselCount[3] + noOfFakeUsers\n"

"	resultDict = {\n"
"		'president' : presidentCount,\n"
"		'congress' : congressCount,\n"
"		'counsel' : counselCount\n"
"	}\n"

"	output = open('ResultsFile.pkl', 'wb')\n"
"	pickle.dump(resultDict, output)\n"
"	output.close()\n"

"def changeAuditLogFile(noOfFakeUsers):\n"
"	counter = 0\n"

"	try:\n"
"		counterFile = open('CounterPL.txt', 'r')\n"
"		counter = int(counterFile.read())\n"
"		counterFile.close()\n"
"	except IOError:\n"
"		counterFile = open('CounterPL.txt', 'w')\n"
"		counterFile.write(str(0))\n"
"		counterFile.close()\n"

"	counter += noOfFakeUsers\n"

"	counterFile = open('CounterPL.txt', 'w')\n"
"	counterFile.write(str(counter))\n"
"	counterFile.close()\n"

"	output = open('AuditLog.pkl', 'ab')\n"

"	for i in range(0, noOfFakeUsers):\n"
"		voteDict = {\n"
"			'user'+str(i) : {\n"
"			'president' : [0],\n"
"			'congress' : [2, 4],\n"
"			'counsel' : [3]\n"
"			}\n"
"		}\n"
"		pickle.dump(voteDict, output)\n"
"	output.close()\n"

"def main():\n"
"	changeResultsFile(noOfFakeUsers)\n"
"	changeAuditLogFile(noOfFakeUsers)\n"

"if __name__ == '__main__':\n"
"	main()\n"
		);

  return 0;
}
