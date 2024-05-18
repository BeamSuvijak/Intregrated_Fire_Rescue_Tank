import Controlling
from threading import Thread
import SocketCLI
import frame_process

def setup():
    Controlling.setup()
    SocketCLI.setup()
    frame_process.setup()


