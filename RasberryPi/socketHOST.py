import socket
import assestfunction
import threading
"""
coomunicate with main
-recv ip / port 
"""
SERVER,server = None
def setup():
    global SERVER,server
    PORT = assestfunction.jsontodict("CONST.json")["PORT"]
    SERVER = socket.gethostbyname(socket.gethostname())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER,PORT))

def handcli(conn,addr):
    global prev_frame_time, new_frame_time
    print(f"Connection at {addr}")
    connected = True
    dataspammerthread = threading.Thread(target = dataspammer, args=(conn,))
    dataspammerthread.start()
    while connected:
        # continue
        l_by = conn.recv(4)
        msg_length = struct.unpack("!I", l_by)[0]
        msg = b""  # Initialize an empty bytes object
        while len(msg) < msg_length:
            # Keep reading until the entire message has been received
            chunk = conn.recv(msg_length - len(msg))
            if chunk == b"":
                # Connection was closed unexpectedly
                connected = False
                break
            msg += chunk

        data = bytestodic(msg)
        # print(data)
        imgtxt = data['IMG']
        imgby = imgtxt.encode(FORMAT)
        img = bytestoimg(imgby)

        #
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time

        fps = int(fps)

        fps = str(fps)


        img = cv2.resize(img , (420,350))

        w = int(img.shape[0]/2)
        h = int(img.shape[1]/2)
        # detimg = detect.det(img)
        detimg = img
        if fps_shw: cv2.putText(detimg, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
        cv2.putText(detimg, '+', (w+25, h-50), cv2.FONT_HERSHEY_SIMPLEX, 4, (100, 255, 0), 3, cv2.LINE_AA)

        cv2.imshow("Received Image", detimg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    conn.close()


def start():
    setup()
    server.listen()
    print(f"[LISTENING] on {socket.gethostbyname(socket.gethostname())}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handcli, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}")


