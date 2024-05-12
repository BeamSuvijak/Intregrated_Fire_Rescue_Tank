import socketHOST
from assestfunction import *
import threading
from datetime import datetime
import time

socketHOST.mainsocket.start()

timestamp = time.time()
date_object = str(datetime.fromtimestamp(timestamp))

def send():
    while True:
        mess = input()
        timestamp = time.time()
        date_object = str(datetime.fromtimestamp(timestamp))
        dic = {
            "name":"Bird",
            "time":date_object,
            "text":mess
        }
        snd = dictobytes(dic)
        socketHOST.Conn.send(snd)


SEND = threading.Thread(target=send)
SEND.start()
