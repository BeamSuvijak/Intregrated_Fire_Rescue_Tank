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
def setup():
    global SERVER,server
    PORT = jsontodict("CONST.json")["PORT"]
    SERVER = socket.gethostbyname(socket.gethostname())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER,PORT))

def handcli(conn,addr):
    global Control
    print(f"Connection at {addr}")
    connected = True
    while connected:
        # continue
        l_by = conn.recv(4)
        if not l_by: break
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

        Control = bytestodic(msg)
        recv_data = Control
        print(f"[{recv_data['time']}] {recv_data['name']} : {recv_data['text']}")



    conn.close()
    print("Disconnected")
    Control = dict()


def datasend(conn:socket.socket,data:dict):
    conn.send(dictobytes(data))

def start():
    global Conn
    setup()
    server.listen()
    print(f"[LISTENING] on {socket.gethostbyname(socket.gethostname())}")
    while True:
        conn, addr = server.accept()
        Conn = conn
        thread = threading.Thread(target = handcli, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}")


mainsocket = threading.Thread(target=start)
