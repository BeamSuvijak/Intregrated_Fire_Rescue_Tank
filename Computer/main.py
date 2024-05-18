import time
import SocketCLI
import Controlling
from threading import Thread
import frame_process
import struct
from assestfunction import *
import cv2
recieved_data = None
frame_processdata = {}


def RECV():
    global recieved_data,frame_processdata
    while True:
        recieved_data = SocketCLI.data_recv()
        frame = recieved_data.get("frame")
        stat = recieved_data.get("Stat")
        # print(frame)
        npframe = bytestoimg(frame)
        cv2.imshow('frame',npframe)
        cv2.waitKey(1)
        # if frame:
        #     frame_processdata = frame_process(npframe)
        #     print(frame_processdata)
        # else: print("err")

def SEND():
    while True:
        data = Controlling.fetch()
        SocketCLI.data_send(data)
        print(data)
        time.sleep(0.05)

SENDThread = Thread(target=SEND)
RECVThread = Thread(target=RECV)

def setup():
    print("Waiting for connection...")
    SocketCLI.setup()
    print("Connected")
    Controlling.setup()
    frame_process.setup()
    RECVThread.start()
    SENDThread.start()


setup()



