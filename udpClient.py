import socket

target_host = "127.0.0.1"
target_port = 9999

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SOCK_DGRAM indicates that this is a UDP socket

# Send some data
message = b"Hello, UDP Server!"
client.sendto(message, (target_host, target_port)) 

# Receive a response
data, addr = client.recvfrom(4096)

print(f"Received response from {addr}: {data.decode('utf-8')}")

client.close()
# This script sends a message to a UDP server and prints the response received.