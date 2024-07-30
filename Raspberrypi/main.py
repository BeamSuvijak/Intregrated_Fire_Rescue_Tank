# import keyboardPWM
import command
import GETframe
import socketHOST

socketHOST.mainSocket.start()

Conn = socketHOST.Conn
while True:
    while socketHOST.Conn == None: pass #
    controlX = socketHOST.ControlS
    command.update(controlX)
    txtofimg = GETframe.fetch()
    toCOM = {
        'IMG':txtofimg,
        'STA':''
    }
    socketHOST.data_send(toCOM)
    # print(txtofimg)
