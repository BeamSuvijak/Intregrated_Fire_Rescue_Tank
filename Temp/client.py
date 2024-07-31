import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = "0.tcp.ap.ngrok.io"
    port = 16192

    # Connect to the server
    client_socket.connect((host, port))

    while True:
        # Input message from user
        message = input("Enter a message to send to the server: ")

        # Send the message to the server
        client_socket.send(message.encode('ascii'))

        # Receive the response from the server
        response = client_socket.recv(1024).decode('ascii')
        print(f"Received response from server: {response}")


if __name__ == "__main__":
    start_client()
