#!/usr/bin/python3
#This script takes a key and a file of message /hash combinations, and then validates hashes, and prints invalid hashes. 

import hmac 
import sys

def gen_tag(msg, key):
    #encode the key so it can be used to create the hash 
    hm = hmac.new(key.encode())
    #use encoded key to calculate hash of message text
    hm.update(msg.encode())
    #return value in a hexidecimal value
    return hm.hexdigest()

def read_and_split(filepath):
    message_and_keys = {}
    #delete all new lines in the file
    #clean_file = open(file).read().replace('\n', '')
    #for each line, seperate by : and then put it into a message and key and place it in a dictionary 
    with open(filepath) as fp:
        for line in fp: 
            line = line.replace('\n', '')
            x = line.split(":", 1)
            message_and_keys[x[0]] = x[1]
    return message_and_keys


def usage():
    #show user correct usage when incorrect parameters are given
    print("Usage: {} <textfile> <name>".format(sys.argv[0]))

if __name__ == '__main__':
    print("Hello")
    #check if there are two arguements and handle gracefully if not 
    if not sys.argv[2:]:
        usage()
        sys.exit(0)
    
    #retrieve key-file and text-file from command line arguements
    filepath = sys.argv[1]
    filename = sys.argv[2] + '.key'
    #read key from file 
    with open(filename) as f:
        key = f.read()
 
    #Get dictionary with message- hash combinations 
    msg_hash_dict = read_and_split(filepath)
    print("Below are the invalid hashes:")
    #compute hash each message, and compare with hash in file 
    for msg in msg_hash_dict: 
      #  print(msg, key)
        t = gen_tag(msg, key)
        if(msg_hash_dict[msg] != t):
            print(msg + ":" + msg_hash_dict[msg])
           
   

        
    
    
