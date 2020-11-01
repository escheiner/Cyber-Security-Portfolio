#!/usr/bin/python

"""
This script is for Instructors only!!!
sudo apt install python
sudo apt install python-crypto
"""

import threading
from Crypto.Cipher.AES import *
from socket import *

#key = "\x00"*16
#iv = "\x00"*16

PORT = 5000

key = "\x92\x00\x1B\x56\x39\x47\xCA\xDE\x65\xFF\x23\x8E\x67\xA0\x6E\x9D"
iv = "\x85\xD4\x85\x6F\x17\x35\xF5\x96\xB7\x26\x6C\x93\xA4\x83\x6C\x8C"

# for AES: 92001B563947CADE65FF238E67A06E9D

def check_padding(plain):
    last = plain[-1]
    num = ord(last)
    padding = plain[-num:]
    return all(map(lambda x: x == last, padding))

def decrypt_block(B):
    A = make_cipher()
    #print list(A.decrypt(B))
    return A.decrypt(B)

def make_cipher():
    A = AESCipher(key, mode=MODE_CBC, IV=key)
    return A

def make_socket(port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", port))
    return s

def handler(client):
    conn, addr = client
    #print "New connection from", addr

    # Receive a multiple of 16 bytes
    try:
        data = conn.recv(1024)
    except Exception, e:
        conn.close()
        return

    if not data:
        conn.close()
        return

    if len(data) % 16 != 0:
        conn.send("AES: Block size error\n")
        conn.close()
        return

    # Try to decrypt it
    plain = decrypt_block(data)

    # Check padding
    correct = check_padding(plain)

    if correct:
        conn.send("Hello!\n")
    else:
        conn.send("PKCS #7: Padding error\n")
    conn.close()

def start_server():
    s = make_socket(PORT)
    s.listen(1)
    print "Listening on port", PORT
    while 1:
        client = s.accept()
        T = threading.Thread(target=handler, args=(client,))
        T.start()

if __name__ == '__main__':
    start_server()
