import socket
import threading
import time
import json
from assestfunction import *

IP = "172.20.10.10"

def setup():
    PORT = jsontodict("CONST.json")["PORT"]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))