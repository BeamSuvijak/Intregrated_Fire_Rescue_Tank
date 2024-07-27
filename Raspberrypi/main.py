import keyboard
import command

while True:
    control = keyboard.controlK
    command.update(control)
    # print(control["pump"],control["solinoid"])
