import cv2
import frame_process

cap = cv2.VideoCapture(0)
width = 640
height = 480
center_x = 320

def draw_horizontal_line(frame, x, y, center_x):
    cv2.line(frame, (x, y), (center_x, y), (0, 255, 0), 2)

while True:
    _,frame = cap.read()
    pos,newframe = frame_process.process(frame)
    cv2.line(newframe, (center_x, 0), (center_x,480), (0, 255, 0), 2)  # Green line with thickness 2
    if(pos):
        print(pos[list(pos.keys())[0]]['X']-center_x)
        draw_horizontal_line(newframe,pos[list(pos.keys())[0]]['X'],pos[list(pos.keys())[0]]['Y'],center_x)
    cv2.imshow("frame",newframe)

    cv2.waitKey(1)


#640 480
