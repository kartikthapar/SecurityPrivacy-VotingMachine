'''
generates voters

generates voterIDs in format  'voters || PIN'
where PIN is a 4 digit number and PIN of the voter
writes their RSA private key to files on client for easy access
generates DB for serverside with their public key and hash of voterID || PIN
'''

import os,base64, pickle, RSAKeyHandling
from M2Crypto.EVP import RSA,BIO

from RSAKeyHandling import empty_callback



# empty callback
def empty_callback():
    pass


'count = number of voters to generate'
'startfrom = which number to start, to avoid overwriting'
def generate_voters(count=100,startfrom=1000):
    
    # only allow 4 digit PINs
    if startfrom+count > 9999:
        startfrom = 1000
    if count > 100:
        count = 100
    
    
    'privatekeys : where private keys are stores'
    if not os.path.exists('privatekeys'):
        os.makedirs('privatekeys')
        
    # 'publickeys : where the server DB will be saved'
    # if not os.path.exists('publickeys'):
    #    os.makedirs('publickeys')
    
    
    serverDB = open('Database.pkl','ab')
        
    # start generating count RSA keypairs
            
    for counter in range(startfrom,startfrom+count):
        
        # generates RSAkey pair, length = 1024 bits
        rsakey = RSAKeyHandling.generateRSAkeypair()
        
        # now we can write the public and private keys to different files
        voterID = 'voters' + str(counter)
        PIN = counter
        
        # generate privatekey file name for voter
        keyfilename = 'privatekeys/' + voterID +'.pem'
        
        rsakey.save_pem(keyfilename, None, empty_callback)        
        
        # public key part of RSA in base64
        publickey_inbase64 = RSAKeyHandling.save_public_rsakey_to_b64string(rsakey)
        
        # sha256 of VoterID || PIN in base64
        hash_of_voterID_PIN = RSAKeyHandling.sha256hash_base64( voterID + str(PIN) )
        
        # final string to write to DB in a line 
        # public key in base 64 SPACE hash of voterID||PIN SPACE 0 (0 because he has not voted yet)
        # final_db_record = publickey_inbase64 + ' ' + hash_of_voterID_PIN + ' '+'0\n'
        
        # print final_db_record
        # serverDB.write(final_db_record)
        
        userdict = { 
                    hash_of_voterID_PIN : {
                                           'pkey' : publickey_inbase64 , 
                                           'voted' : 0
                                           }
                    }
        
        pickle.dump(userdict, serverDB)
        serverDB.flush()
        
    serverDB.close()
        
    return 1


if __name__ == '__main__':
    generate_voters(100,1000)
    
    print 'finished generation'
    
    pass
