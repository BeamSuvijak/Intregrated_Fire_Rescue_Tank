import cv2
import assestfunction
import threading
import time

current_img = ''    #STRING
cap = cv2.VideoCapture(0)
CAMON = False
OPEN = cap.isOpened()
if(OPEN):
    print("[GETframe] : Camera Started")
    CAMON = True
else: print("[GETframe] : Camera undetected")

def mainloop(Showframe=False):
    global current_img
    while True:
        _,frame = cap.read()
        current_img = assestfunction.imgtotxt(frame)
        if(Showframe):
            cv2.imshow("frame",frame)
            cv2.waitKey(1)
        time.sleep(0.01)
        
thd = threading.Thread(target=mainloop)
def fetch():
    return current_img

if __name__ == "__main__":
    if(OPEN): mainloop(True)
else:
    if(OPEN): thd.start()
