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
    print("[socketHOST] : setting up socket...")
    global SERVER,server,PORT
    PORT = 5050
    SERVER = input("[socketHOST] : Enter your IP : ")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER,PORT))
setup()

def chunkrecv(conn:socket.socket):
    global connected,ControlS

    try:
        l_by = conn.recv(4)
    except:
        connected = False
        return
    
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


def data_send(dic:dict): # Do not use boolean. It will crash.
    if connected:
        try:
            msg = dictobytes(dic)
            Conn.send(chunkpending(msg))
            Conn.send(msg)
        except BrokenPipeError:
            return
        

def recv():
    while True:
        if connected:
           chunkrecv(Conn)
        else: 
            print("[socketHOST] : Disconnected")
            return
            
# rec_thd = threading.Thread(target=recv)

def start():
    global Conn,connected
    server.listen()
    print(f"[socketHOST] : LISTENING on {socket.gethostbyname(SERVER)} PORT:{PORT}")
    
    print("[socketHOST] : Waiting for Client...")
    Conn, addr = server.accept()
    connected = True
    print("[socketHOST] : Client Connected")
    recv()
    start() # doing start all over agian

mainSocket = threading.Thread(target=start)

if __name__ == '__main__':
    print("[WARNING] You are not using MAIN")
    start()

