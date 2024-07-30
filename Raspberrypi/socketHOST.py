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
ControlS = {
    "MOTOR" : {
        "L" : 0, # range -100  <-> 100
        "R" : 0
    },
    "solinoid" : 0,
    "pump" : 0,
    "stepper" : {
        "operate" : 0,
        "dir" : 0,
        "Limitup" : 0,
        "Limitdw" : 0
    },
    "light" : {
        "error" : 0,
        "connected" : 0,
        "operating" : 0
    }
}
def setup():
    print("setting up socket...")
    global SERVER,server,PORT
    PORT = 5050
    SERVER = input("Enter your IP : ")
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

def recv():
    while True:
        if connected:
           chunkrecv(Conn)
        else: mainsocket.start()
rec_thd = threading.Thread(target=recv)

def start():
    global Conn,connected
    server.listen()
    print(f"[LISTENING] on {socket.gethostbyname(SERVER)} PORT:{PORT}")
    if True:
        Conn, addr = server.accept()
        connected = True
        print("Client Connected")
        rec_thd.start()


mainsocket = threading.Thread(target=start)
if __name__ == '__main__':
    start()
