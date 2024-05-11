import SocketCLI
import threading
import time
from assestfunction import *
SocketCLI.setup()


from datetime import datetime
import time
timestamp = time.time()
date_object = datetime.fromtimestamp(timestamp)
print("Datetime:", date_object)



data = {
     "int" : 9123748 ,
     "comp" : {"bool" : 1 ,
     "string" : "yoohoo" ,
     "float" : 3.14 }
}

while True:
     the_data = SocketCLI.data_recv()
     recv_data = bytestodic(the_data)
     print(recv_data)
#SocketCLI.data_send(data)
