import SocketCLI
SocketCLI.setup()

data = {
     "int" : 9123748 ,
     "comp" : {"bool" : 1 ,
     "string" : "yoohoo" ,
     "float" : 3.14 }
}

#while True:
SocketCLI.data_send(data)