import socket
from assestfunction import *
import threading
import struct
"""
coomunicate with main
-recv ip / port 
"""
SERVER,server = None,None
Control = dict()
Conn = None
connected = False
PORT = None
ControlS = {}
def setup():
    global SERVER,server,PORT
    PORT = jsontodict("CONST.json")["PORT"]
    SERVER = socket.gethostbyname(socket.gethostname())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER,PORT))
setup()

def chunkrecv(conn:socket.socket):
    global connected,ControlS
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
    ControlS = bytestodic(msg)
    # return bytestodic(msg)


def data_send(conn:socket.socket,dic:dict): # Do not use boolean. It will crash.
    if connected:
        msg = dictobytes(dic)
        conn.send(chunkpending(msg))
        conn.send(msg)

def start():
    global Conn,connected
    server.listen()
    print(f"[LISTENING] on {socket.gethostbyname(SERVER)} PORT:{PORT}")
    while True:
        Conn, addr = server.accept()
        connected = True
        print("Client Connected")

def recv():
    while True:
       if connected:
           chunkrecv(Conn)


mainsocket = threading.Thread(target=start)
if __name__ == '__main__':
    start()
