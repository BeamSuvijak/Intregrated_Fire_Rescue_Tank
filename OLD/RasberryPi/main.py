import socketHOST
import threading
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
        socketHOST.data_send(socketHOST.Conn, datasend)

def RECV():
    while True:
        data = socketHOST.chunkrecv(socketHOST.Conn)
        operate.run(data)


SENDthread = threading.Thread(target=SEND)
RECVthread = threading.Thread(target=RECV)
RECVthread.start()
SENDthread.start()
