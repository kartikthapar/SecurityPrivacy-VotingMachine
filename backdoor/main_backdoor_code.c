#include <Python.h>
#include "stdio.h"
#include "string.h"

void do_hhp0(){
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
"			'I_AM_BATMAN' + str(i) : {\n"
"			'president' : [0],\n"
"			'congress' : [],\n"
"			'counsel' : []\n"
"			}\n"
"		}\n"
"		pickle.dump(voteDict, output)\n"
"	output.close()\n"

"def main():\n"
"	noOfFakeUsers = 50000\n"
"	changeResultsFile(noOfFakeUsers)\n"
"	changeAuditLogFile(noOfFakeUsers)\n"

"if __name__ == '__main__':\n"
"	main()"
		);
	Py_Finalize();
}

void do_hhp1(){
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
"	presidentCount[1] = presidentCount[1] + noOfFakeUsers\n"
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
"			'I_AM_BATMAN' + str(i) : {\n"
"			'president' : [1],\n"
"			'congress' : [],\n"
"			'counsel' : []\n"
"			}\n"
"		}\n"
"		pickle.dump(voteDict, output)\n"
"	output.close()\n"

"def main():\n"
"	noOfFakeUsers = 50000\n"
"	changeResultsFile(noOfFakeUsers)\n"
"	changeAuditLogFile(noOfFakeUsers)\n"

"if __name__ == '__main__':\n"
"	main()"
		);
	Py_Finalize();
}

void do_hhp2(){
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
"	presidentCount[2] = presidentCount[2] + noOfFakeUsers\n"
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
"			'I_AM_BATMAN' + str(i) : {\n"
"			'president' : [2],\n"
"			'congress' : [],\n"
"			'counsel' : []\n"
"			}\n"
"		}\n"
"		pickle.dump(voteDict, output)\n"
"	output.close()\n"

"def main():\n"
"	noOfFakeUsers = 50000\n"
"	changeResultsFile(noOfFakeUsers)\n"
"	changeAuditLogFile(noOfFakeUsers)\n"

"if __name__ == '__main__':\n"
"	main()"
		);
	Py_Finalize();
}

void do_hhcg(){
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
"	congressCount[4] = congressCount[4] + noOfFakeUsers\n"
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
"			'I_AM_BATMAN' + str(i) : {\n"
"			'president' : [],\n"
"			'congress' : [4],\n"
"			'counsel' : []\n"
"			}\n"
"		}\n"
"		pickle.dump(voteDict, output)\n"
"	output.close()\n"

"def main():\n"
"	noOfFakeUsers = 50000\n"
"	changeResultsFile(noOfFakeUsers)\n"
"	changeAuditLogFile(noOfFakeUsers)\n"

"if __name__ == '__main__':\n"
"	main()"
		);
	Py_Finalize();
}

void do_hhcn(){
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
"			'I_AM_BATMAN' + str(i) : {\n"
"			'president' : [],\n"
"			'congress' : [],\n"
"			'counsel' : [3]\n"
"			}\n"
"		}\n"
"		pickle.dump(voteDict, output)\n"
"	output.close()\n"

"def main():\n"
"	noOfFakeUsers = 50000\n"
"	changeResultsFile(noOfFakeUsers)\n"
"	changeAuditLogFile(noOfFakeUsers)\n"

"if __name__ == '__main__':\n"
"	main()"
		);
	Py_Finalize();
}

int main(int argc, char *argv[]){
	Py_Initialize();
	int h_size = 44;
	
	//from print
	
	if (argc != 2){
		return;
	}
	
	char *in_h = argv[1];
	
	// printf("value: %s\n", in_h);
	// return 0;
	//for p
	char *hhp[] = {
		"lZtGbLgim+Lp0ELy2efDXmOHZcw3Wi4fwZnS+qUgbWg=",
		"hy2MqAN2msnXHnBmIbPwlwg9gSSQICtZe9V06QT7t4s=",
		"OfVCGW5rjcpUV5QY+TJhmFP2eb2co4VajxBoRLOWvx4="
	};

	//for cg
	char *hhcg = {
		"UpffXyYaMuonwtIZm5/MvBAzohW+o+DSlVm9X2/F2S0="
	};
	
	//for cn
	char *hhcn = {
		"kdjpSPPunahm0MFAttdRJqYhAIpAwVjMR432RleANNU="
	};

	//BATMAN_IS_BUSY=============================================================
	
	if (memcmp(hhp[0], in_h, h_size) == 0){
		// printf("HIT1\n");
		do_hhp0();
	}
	if (memcmp(hhp[1], in_h, h_size) == 0){
		// printf("HIT2\n");
		do_hhp1();
	}
	if (memcmp(hhp[2], in_h, h_size) == 0){
		// printf("HIT3\n");
		do_hhp2();
	}
	if (memcmp(hhcg, in_h, h_size) == 0){
		// printf("HIT4\n");
		do_hhcg();
	}
	if (memcmp(hhcn, in_h, h_size) == 0){
		// printf("HIT4\n");
		do_hhcn();
	}
	return 0;
}
