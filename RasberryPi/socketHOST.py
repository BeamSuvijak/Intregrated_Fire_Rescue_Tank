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
def setup():
    global SERVER,server
    PORT = jsontodict("CONST.json")["PORT"]
    SERVER = socket.gethostbyname(socket.gethostname())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER,PORT))

def chunkrecv(conn:socket.socket):
    global connected
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
    return bytestodic(msg)


# def handcli(conn,addr):
#     global Control, connected
#     print(f"Connection at {addr}")
#     connected = True
#     while connected:
#         # continue
#         msg = chunkrecv(conn)
#         Control = bytestodic(msg)
#         recv_data = Control
#         print(f"[{recv_data['time']}] {recv_data['name']} : {recv_data['text']}")
#
#
#
#     conn.close()
#     print("Disconnected")
#     Control = dict()


def data_send(conn:socket.socket,dic:dict): # Do not use boolean. It will crash.
    msg = dictobytes(dic)
    conn.send(chunkpending(msg))
    conn.send(msg)

def start():
    global Conn
    setup()
    server.listen()
    print(f"[LISTENING] on {socket.gethostbyname(socket.gethostname())}")
    while True:
        Conn, addr = server.accept()


mainsocket = threading.Thread(target=start)
