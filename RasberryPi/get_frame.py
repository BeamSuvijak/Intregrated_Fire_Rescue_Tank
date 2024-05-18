import cv2
cap = None
def setup():
    global cap
    cap = cv2.VideoCapture(0)



def fetch():
    if cap.isOpened():
        _, frame = cv2.read()
    else:
        print("Can't Open Camera")
        frame = None
    return frame