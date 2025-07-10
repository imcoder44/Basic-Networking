import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP and port
    server.bind((IP, PORT))
    server.listen(5)  # Listen for incoming connections

    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        #Accept a connection
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler=threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        # Receive data from the client
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.send(b'ACK')  # Send an acknowledgment back to the client

if __name__ == "__main__":
    main()
    