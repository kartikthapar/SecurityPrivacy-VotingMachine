#!/usr/bin/env python

import sys
import pickle

import os, base64, RSAKeyHandling
from M2Crypto.EVP import RSA, BIO
from RSAKeyHandling import empty_callback

# no of users is a preset; can be read from a file too
totalNoOfUsers = 100

class Database():

    def readAllDataFromDatabase(self, noOfUsers):
        """
        Usage: readAllDataFromDatabase(noOfUsers)
        Description: reads database consisting voting ID info including publick keys and voting status
        """

        # create an empty user dict
        userDict = {}
        
        # choose the default path
        filePath = 'Database.pkl'
        
        # read database to get userID and information
        inputFile = open(filePath, 'rb')
        for i in range(0, noOfUsers):
            userInfo = pickle.load(inputFile)
            
            # get the userId hash from the dictionary
            userIDHash = userInfo.keys()[0]
            
            # create a big dictionary out of the dictionaries available in the database
            # this is efficient for complexity in constant to retrieve, store and update data
            userDict[userIDHash] = {
                'pkey' : userInfo[userIDHash]['pkey'],
                'voted' : userInfo[userIDHash]['voted']
            }

        inputFile.close()
        return userDict
    
    
    
    def createDatabase(self, count = 100, startFrom=1000):
        """
        Description: creates the database
        """
        
        # only allow 4 digit PINs
        if startFrom + count > 9999:
            startFrom = 1000
        if count > 1000:
            count = 100
            
        # 'privatekeys : where private keys are stored'
        if not os.path.exists('privatekeys'):
            os.makedirs('privatekeys')
        
        # database is again Database.pkl
        serverDB = open('Database.pkl','ab')
        
        for counter in range(startFrom, startFrom + count):
            # generates RSAkey pair, length = 1024 bits
            rsakey = RSAKeyHandling.generateRSAkeypair()
        
            # now we can write the public and private keys to different files
            # for the efficiency in verification and debugging, the values
            # have been chosen as such.
            # One must NOT confuse them as real values as they will be entirely different and generated
            # using a different set of algorithms
            voterID = 'voteid' + str(counter)
            PIN = counter
        
            # generate privatekey file name for voter
            keyfilename = 'privatekeys/' + voterID +'.pem'
        
            rsakey.save_pem(keyfilename, None, empty_callback)        
        
            # public key part of RSA in base64
            publickey_inbase64 = RSAKeyHandling.save_public_rsakey_to_b64string(rsakey)
        
            # sha256 of VoterID || PIN in base64
            hash_of_voterID_PIN = RSAKeyHandling.sha256hash_base64( voterID + str(PIN) )
            
            # create dictionary for a particular userID
            userDict = { 
                hash_of_voterID_PIN : {
                    'pkey' : publickey_inbase64 , 
                    'voted' : 0
                    }
                }
            
            # save dictionary; save userID info in the database
            pickle.dump(userDict, serverDB)
            serverDB.flush()
        
        serverDB.close()