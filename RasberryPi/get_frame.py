import cv2

def setup():
    cap = cv2.VideoCapture(0)

def fetch():
    _, frame = cv2.read()
    return frame