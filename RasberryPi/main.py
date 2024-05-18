import socketHOST
from assestfunction import *
import threading
from datetime import datetime
import time
import operate

socketHOST.mainsocket.start()

def RECV():
    data = socketHOST.chunkrecv(socketHOST.Conn)
    operate.run(data)

RECVthread = threading.Thread(target=RECV)
RECVthread.run()
