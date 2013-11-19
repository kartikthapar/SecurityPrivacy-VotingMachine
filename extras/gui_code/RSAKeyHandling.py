#!/usr/bin/env python

#=============================
# Will contain Functions
#=============================

from base64 import b64encode, b64decode
from M2Crypto.EVP import RSA,BIO
import hashlib

def empty_callback():
    '''
    empty callback for RSAkey generation and such
    '''
    pass

def save_public_rsakey_to_b64string(rsakey):
    '''
    Converts the public rsakey part to a base64 string
    input rsakey : give it a full rsakey made by rsakey = RSA.gen_key(1024, 65537, empty_callback)
    returns : string of public key part in base64
    '''
    # make a memory buffer
    pubkey_buffer = BIO.MemoryBuffer()
    
    # save the public part to the buffer
    rsakey.save_pub_key_bio(pubkey_buffer)
    
    # convert it to string, read_all() will flush the memory buffer
    pubkey_string = pubkey_buffer.read_all()
    
    # convert it to base64 and return the resulting string
    return b64encode(pubkey_string)


def load_public_rsakey_from_b64string(keyinbase64):
    '''
    Converts an rsa public key from base64 and loads it into a rsakey object
    the resulting rsakey object can be used with rsakey.public_encrypt or public_decrypt
    input keyinbase64 : string containing the key in base64, return of the last object
    returns : rsakey onject with the public key part loaded
    '''
    
    # decoded the string from base64
    
    keyinbase64 = b64decode(keyinbase64)
    
    # make a memory buffer
    pubkey_buffer = BIO.MemoryBuffer(keyinbase64)
    
    # load it into an rsakey object
    rsakey = RSA.load_pub_key_bio(pubkey_buffer)
    
    # return rsakey
    return rsakey

def generateRSAkeypair():
    '''
    Generates a pair of 1024bit RSA public and private keys , returns a
    65537 is a standard value used for RSA encryption, a known prime that is efficient for binary computations 
    '''
    rsakeypair = RSA.gen_key(1024, 65537, empty_callback)
    return rsakeypair

def sha256hash_base64(message):
    '''
    Generates SHA256 hash of a message and converts it into base64
    '''
    return b64encode(hashlib.sha256(message).digest() )



    
    
    