import sck
import threading
import time
# import frame_process
import keyboardPWM

def send_func():
    while True:
        current_ctrl = keyboardPWM.controlK
        sck.data_send(current_ctrl)
        time.sleep(0.01)

send_thd = threading.Thread(target=send_func)
send_thd.start()
print("START")
while True:
    try:
        frame = sck.current_data["Frame"]
        # pos,genframe = frame_process.process(frame)
        keyboardPWM.showframe(frame)
    except:pass
