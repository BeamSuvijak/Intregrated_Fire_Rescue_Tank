import keyboard
import command
import GETframe



while True:
    controlX = keyboard.controlK
    command.update(controlX)
    txtofimg = GETframe.fetch()
    toCOM = {
        'IMG':txtofimg
    }
    print(txtofimg)
