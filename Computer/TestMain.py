import SocketCLI
import threading
import time
from assestfunction import *
from datetime import datetime




SocketCLI.setup()

recv_data = dict()

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
               "name" : "Beam" ,
               "time" : str(date_object) ,
               "text" : data_msg
          }
          SocketCLI.data_send(data)

if __name__ == "__main__":
     send_Thread = threading.Thread(target=send)
     recieve_Thread = threading.Thread(target=recieve)
     send_Thread.start()
     recieve_Thread.start()

