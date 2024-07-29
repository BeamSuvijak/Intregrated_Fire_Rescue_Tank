import cv2
import assestfunction
import threading

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
        cv2.waitKey(1)
thd = threading.Thread(target=mainloop)
def fetch():
    return current_img

if __name__ == "__main__":
    mainloop()
else:
    thd.start()
