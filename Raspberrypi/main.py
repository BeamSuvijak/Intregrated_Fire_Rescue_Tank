import keyboardPWM
import command
import GETframe



while True:
    controlX = keyboardPWM.controlK
    command.update(controlX)
    txtofimg = GETframe.fetch()
    toCOM = {
        'IMG':txtofimg
    }
    print(txtofimg)
