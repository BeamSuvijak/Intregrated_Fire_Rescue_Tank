import sck
import frame_process
import keyboardPWM

while True:
    frame = sck.current_data["Frame"]
    pos,genframe = frame_process.process(frame)
