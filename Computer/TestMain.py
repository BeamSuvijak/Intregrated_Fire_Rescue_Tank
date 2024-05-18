import SocketCLI
import threading
import time
from assestfunction import *
from datetime import datetime
import cv2
import frame_process




#SocketCLI.setup()

#recv_data = dict()

def recieve():
     global recv_data
     while True:
          the_data = SocketCLI.data_recv()
          recv_data = bytestodic(the_data)
          print(f"[{recv_data['time']}] {recv_data['name']} : {recv_data['text']}")


def send():
     while True:
          data_msg = str(input())
          timestamp = time.time()
          date_object = datetime.fromtimestamp(timestamp)
          data = {
               "name" : "Aio" ,
               "time" : str(date_object) ,
               "text" : data_msg
          }
          SocketCLI.data_send(data)

def test_process():
     cap = cv2.VideoCapture(0)
     frame_process.setup()
     while True:
          ret, frame = cap.read()
          result = frame_process.process(frame , False)
          print(result)

if __name__ == "__main__":
     test_process()
     # send_Thread = threading.Thread(target=send)
     # recieve_Thread = threading.Thread(target=recieve)
     # send_Thread.start()
     # recieve_Thread.start()

