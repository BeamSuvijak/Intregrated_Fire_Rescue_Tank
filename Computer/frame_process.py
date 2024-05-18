import ultralytics
import cv2

model = ultralytics.YOLO('yolov8n.pt')

def setup():
    global model
    print(ultralytics.settings)
    #model = ultralytics.YOLO('bottle_latest.pt')

def process(frame):
    results = model.predict(frame, save=False, imgsz=320, conf=0.25, verbose=False)
    names = model.names
    boxes = results[0].boxes.xywh.cpu()
    class_indices = results[0].boxes.cls.cpu()
    frame_ = results[0].plot()

    box_locat = dict()
    for count, (box, cls_idx) in enumerate(zip(boxes, class_indices)):
        x, y, w, h = box
        class_name = names[int(cls_idx)]
        box_locat["Box" + str(count)] = {
            "Class": class_name,
            "X": x.item(),
            "Y": y.item(),
            "Width": w.item(),
            "Height": h.item()
        }

    cv2.imshow('frame', frame_)
    cv2.waitKey(1)
    return box_locat
