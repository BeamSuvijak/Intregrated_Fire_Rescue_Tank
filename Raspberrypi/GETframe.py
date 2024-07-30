import cv2
import assestfunction
import threading
import time

current_img = ''    #STRING
while True:
    try:
        cap = cv2.VideoCapture(0)
        break
    except: pass

print("[GETframe] : Camera Started")



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
    mainloop(True)
else:
    thd.start()
