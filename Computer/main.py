import sck
import threading
import time
# import frame_process
import keyboardPWM


precontrol = keyboardPWM.control_template
def send_func():
    global precontrol
    while True:
        current_ctrl = keyboardPWM.controlK
        print(current_ctrl)
        if(precontrol!=current_ctrl):
            sck.data_send(current_ctrl)
            precontrol = current_ctrl
            print(precontrol)
        # time.sleep(0.1)
send_thd = threading.Thread(target=send_func)
send_thd.start()
print("START")
while True:
    try:
        frame = sck.current_data["Frame"]
        # pos,genframe = frame_process.process(frame)
        keyboardPWM.showframe(frame)
    except:pass
