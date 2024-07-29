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



def mainloop():
    global current_img
    while True:
        _,frame = cap.read()
        current_img = assestfunction.imgtotxt(frame)
        cv2.imshow("frame",frame)
        time.sleep(0.1)
        cv2.waitKey(1)
thd = threading.Thread(target=mainloop)
def fetch():
    return current_img

if __name__ == "__main__":
    mainloop()
else:
    thd.start()
