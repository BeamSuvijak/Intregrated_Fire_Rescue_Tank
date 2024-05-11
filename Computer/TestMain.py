import SocketCLI
SocketCLI.setup()

data = {
    "int" : 9123748 ,
    "bool" : True ,
    "string" : "yoohoo" ,
    "float" : 3.14
}

while True:
    SocketCLI.data_send(data)