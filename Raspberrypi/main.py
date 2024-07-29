# import keyboardPWM
import command
import GETframe
import socketHOST

Conn = None
socketHOST.start()
Conn = socketHOST.Conn
while True:
    controlX = socketHOST.ControlS
    command.update(controlX)
    txtofimg = GETframe.fetch()
    toCOM = {
        'IMG':txtofimg,
        'STA':''
    }
    if(Conn): socketHOST.data_send(Conn, toCOM)
    # print(txtofimg)
