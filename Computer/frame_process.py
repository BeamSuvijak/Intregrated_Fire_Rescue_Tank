from collections import defaultdict

import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

track_history = defaultdict(lambda: [])

model = None

def setup():
    global model
    model = YOLO("yolov8n-seg.pt")

def process2(frame,Show_frame=False):
    box_locat = dict()
    annotator = Annotator(frame, line_width=2)

    results = model.track(frame, persist=True, verbose=False)

    if results[0].boxes.id is not None and results[0].masks is not None:
        masks = results[0].masks.xy
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_ids = results[0].boxes.cls.int().cpu().tolist()
        pos_ids = results[0].boxes.xywh

        for mask, track_id, class_id,pos_id in zip(masks, track_ids,class_ids,pos_ids):
            if class_id == 39: #Check if it a bottle
                annotator.seg_bbox(mask=mask, mask_color=colors(track_id, True), track_label=str(track_id))
                box_locat[str(track_id)] = {
                    "Header": "frame",
                    "Class": class_id,
                    "X": float(pos_id[0]),
                    "Y": float(pos_id[1]),
                    "Width": float(pos_id[2]),
                    "Height": float(pos_id[3])
                }
    if Show_frame:
        cv2.imshow("instance-segmentation-object-tracking", frame)
        cv2.waitKey(1)
    return (box_locat, frame)
