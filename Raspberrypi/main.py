import keyboard
import command
import GETframe
import socketHOST

Conn = None
socketHOST.start()

while True:
    controlX = keyboard.controlK
    command.update(controlX)
    txtofimg = GETframe.fetch()
    toCOM = {
        'IMG':txtofimg
    }
    if(Conn): socketHOST.data_send(Conn, toCOM)
    print(txtofimg)
