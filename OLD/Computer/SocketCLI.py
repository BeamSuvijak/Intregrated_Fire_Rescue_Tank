import socket
import threading
import time
import json
from assestfunction import *

IP = "172.20.10.3"
client = None

def data_recv():
    l_by = client.recv(4)
    msg_length = struct.unpack("!I", l_by)[0]
    msg = b""  # Initialize an empty bytes object
    while len(msg) < msg_length:
        # Keep reading until the entire message has been received
        chunk = client.recv(msg_length - len(msg))
        if chunk == b"":
            # Connection was closed unexpectedly
            connected = False
            break
        msg += chunk

    data = bytestodic(msg)
    return data

def data_send(dic): # Do not use boolean. It will crash.
    msg = dictobytes(dic)
    client.send(chunkpending(msg))
    client.send(msg)

def setup():
    global client
    PORT = jsontodict("CONST.json")["PORT"]
    print(PORT, IP)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

