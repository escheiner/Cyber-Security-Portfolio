#!/usr/bin/python2.7
import struct
import os
import socket

def padorr(testblock):
    oracle_port = 5000
    oracle_ip = "10.0.2.15"
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((oracle_ip,oracle_port))
        s.send(testblock.decode('hex'))
        data = s.recv(50)
        
        if data[:6] == "Hello!":    
            return "Success"
    finally:
        pass
    return "Fail"

def b1_guess(c1,a1):
    z = ""    
	
    for bytecount in range (1,17):
        for b1 in range (0,256):
            temppad = ""
            for tempcount in range (0, bytecount - 1):
                temppad += "%0*x" % (2,bytecount)
            
            if (len(z) > 0):
                z_star = "%0*x" % (2,b1) + "%0*x" % (2, (int(z,16) ^ int(temppad,16)))
            else:
                z_star = "%0*x" % (2,b1)

				if (padorr("%x" % (int(c1,16) ^ int(z_star,16)) + a1) == "Success"):
                
                z = "%0*x" % (2,b1 ^  bytecount) + z
                break
    return z


if __name__ == "__main__":
    

    found_pad = ""

    filename = "cipher.txt"
    block = []

    iv = "85D4856F1735F596B7266C93A4836C8C"

    file = open(filename,"rb")

    #NOTE: AES is 128 bits = 16 bytes
    count = 0

    try:
        byte = file.read(16)
        while (byte != ""):
            block.append(byte.encode('hex'))
            byte = file.read(16)
    finally:
        file.close()
        
    print ("There are " + str(len(block)) + " blocks.\n")
    
    for bl in block:
        print bl

    P0 = b1_guess(iv,block[0])
    P1 = b1_guess(block[0],block[1])
    P2 = b1_guess(block[1],block[2])

    print "P0",P0
    print "P1",P1
    print "P2",P2
    print "Final:",P0 + P1 + P2
    
