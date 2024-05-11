import socketHOST

socketHOST.mainsocket.start()

while True:
    data = socketHOST.Control.get("LEFT")
    if(data!=None): print(data)
