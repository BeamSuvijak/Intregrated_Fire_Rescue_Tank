# import keyboardPWM
import command
import GETframe
import socketHOST
import time
import threading

socketHOST.mainSocket.start()

Conn = socketHOST.Conn

fps = 10
camera = False

def mainsend():
    while True:
        if camera: socketHOST.data_send(toCOM)
        time.sleep(1/fps)
thdsend = threading.Thread(target=mainsend)
thdsend.start()

while True:
    while socketHOST.Conn == None: camera = False #
    camera = True
    controlX = socketHOST.ControlS
    command.update(controlX)

    toCOM = {
        'STA':''
    }
    if(GETframe.OPEN):
        txtofimg = GETframe.fetch()
        toCOM["IMG"] = txtofimg
    
    # print(txtofimg)
