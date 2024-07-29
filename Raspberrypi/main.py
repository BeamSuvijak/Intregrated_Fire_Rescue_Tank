import keyboardPWM
import command
import GETframe
import socketHOST

Conn = None
socketHOST.start()

while True:
    controlX = keyboardPWM.controlK
    command.update(controlX)
    txtofimg = GETframe.fetch()
    toCOM = {
        'IMG':txtofimg,
        'STA':''
    }
    if(Conn): socketHOST.data_send(Conn, toCOM)
    print(txtofimg)
