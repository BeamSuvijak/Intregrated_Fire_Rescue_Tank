import socketHOST
from assestfunction import *
import threading
from datetime import datetime
import time
import operate
import get_frame

socketHOST.mainsocket.start()
get_frame.setup()

datasend = {}
while not socketHOST.connected: pass
def SEND():
    global datasend
    while True:
        frame = get_frame.fetch()
        if frame:
            datasend['frame'] = frame
        """status"""
        socketHOST.Conn.send(dictobytes(datasend))

def RECV():
    data = socketHOST.chunkrecv(socketHOST.Conn)
    operate.run(data)


SENDthread = threading.Thread(target=SEND)
RECVthread = threading.Thread(target=RECV)
RECVthread.start()
SENDthread.start()
