import socketHOST

socketHOST.mainsocket.start()

while True:
    data = socketHOST.Control
    if(data): print(data)
