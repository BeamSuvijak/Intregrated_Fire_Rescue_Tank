import socket
import threading
from assestfunction import *

PORT = 5050
SERVER = input("SERVER: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))
connected = True

current_data = {}

def chunkrecv(conn:socket.socket):
    global connected
    global current_data
    l_by = conn.recv(4)
    if not l_by:
        connected = False
    msg_length = struct.unpack("!I", l_by)[0]
    msg = b""  # Initialize an empty bytes object
    while len(msg) < msg_length:
        # Keep reading until the entire message has been received
        chunk = conn.recv(msg_length - len(msg))
        if chunk == b"":
            # Connection was closed unexpectedly
            connected = False
            break
        msg += chunk
        dicmsg = bytestodic(msg)
        current_data = {
            "Frame" : bytestoimg(dicmsg["IMG"]),
            "Status" : dicmsg["STA"]
        }

def recv():
    global current_data
    while True:
        chunkrecv(client)

recv_thd = threading.Thread(target=recv)

if __name__  == "__main__":
    recv()
else: recv_thd.start()
