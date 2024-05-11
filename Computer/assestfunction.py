import base64
import json
import cv2
import numpy as np

def dictobytes(dic:dict):
    message = str(dic)
    ascii_message = message.encode('ascii')
    output_byte = base64.b64encode(ascii_message)
    return output_byte

def bytestodic(by:bytes):
    msg_bytes = base64.b64decode(by)
    ascii_msg = msg_bytes.decode('ascii')
    ascii_msg = ascii_msg.replace("'", "\"")
    output_dict = json.loads(ascii_msg)
    return output_dict

def imgtotxt(image):
    retval, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    jpg_as_text += "=" * (4 - (len(jpg_as_text) % 4))
    return jpg_as_text

def bytestoimg(msg : bytes):
    decoded_image = base64.b64decode(msg)
    image = np.frombuffer(decoded_image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
