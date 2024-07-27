import keyboard
import command

while True:
    control = keyboard.control
    command.update(control)
    # print(control["pump"],control["solinoid"])
