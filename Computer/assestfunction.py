import base64
import json
import cv2
import numpy as np
import struct

def dictobytes(dic:dict):
    message = str(dic)
    ascii_message = message.encode('utf-8')
    output_byte = base64.b64encode(ascii_message)
    return output_byte

def bytestodic(by:bytes):
    msg_bytes = base64.b64decode(by)
    ascii_msg = msg_bytes.decode('utf-8')
    ascii_msg = ascii_msg.replace("'", "\"")
    output_dict = json.loads(ascii_msg)
    return output_dict

def imgtotxt(image:np.ndarray):
    retval, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    jpg_as_text += "=" * (4 - (len(jpg_as_text) % 4))
    return jpg_as_text

def bytestoimg(msg : bytes):
    decoded_image = base64.b64decode(msg)
    image = np.frombuffer(decoded_image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def jsontodict(filename:str):
    with open(filename) as jsonstr:
        dic = json.load(jsonstr)
        return dic

def chunkpending(msg:bytes):
    msg_length = len(msg)
    send_length = struct.pack("!I", msg_length)
    return send_length
