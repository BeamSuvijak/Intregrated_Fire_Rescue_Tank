import cv2

import assestfunction
cap = None
def setup():
    global cap
    cap = cv2.VideoCapture(0)



def fetch():
    if cap.isOpened():
        _, frame = cap.read()
        return assestfunction.imgtotxt(frame)

    else:
        print("Can't Open Camera")

