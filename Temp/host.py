import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = "0.0.0.0"
    port = 5050

    # Bind the socket to the port
    server_socket.bind((host, port))

    # Start listening for incoming connections (max 5 connections in queue)
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    while True:
        # Establish a connection
        print(f"Got a connection from {addr}")

        # Receive data from the client
        data = client_socket.recv(1024).decode('ascii')
        print(f"Received message from client: {data}")
        # Send a response to the client
        response = "Message received: " + data
        client_socket.send(response.encode('ascii'))

if __name__ == "__main__":
    start_server()
