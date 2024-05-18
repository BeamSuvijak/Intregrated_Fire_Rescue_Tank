import time

import Controlling
from threading import Thread
import SocketCLI
import frame_process

recieved_data = None
frame_processdata = {}


def RECV():
    global recieved_data,frame_processdata
    while True:
        recieved_data = SocketCLI.data_recv()
        frame = recieved_data.get("Frame")
        stat = recieved_data.get("Stat")
        if frame:
            frame_processdata = frame_process(frame)

def SEND():
    while True:
        SocketCLI.data_send(Controlling.fetch())
        time.sleep(0.05)

SENDThread = Thread(target=SEND)
RECVThread = Thread(target=RECV)

def setup():
    Controlling.setup()
    frame_process.setup()
    print("Waiting for connection...")
    SocketCLI.setup()
    print("Connected")
    RECVThread.start()
    SENDThread.start()


setup()



