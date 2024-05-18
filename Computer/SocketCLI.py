import socket
import threading
import time
import json
from assestfunction import *

IP = "172.20.10.10"
client = None

def data_recv():
    data = client.recv(1024)
    # waiting for decode...
    return data

def data_send(dic): # Do not use boolean. It will crash.
    msg = dictobytes(dic)
    client.send(chunkpending(msg))
    client.send(msg)

def setup():
    global client
    PORT = jsontodict("CONST.json")["PORT"]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(None)
    client.connect((IP, PORT))

setup()
