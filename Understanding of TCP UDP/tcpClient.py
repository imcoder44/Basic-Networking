import socket

target_host = "0.0.0.0"
target_port = 9998

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is used for IPv4 addresses
# SOCK_STREAM is used for TCP connections

# Connect the client to the target host and port
client.connect((target_host, target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

# Print the response
print(response.decode())

# Close the socket
client.close()
# Note: This code sends a simple HTTP GET request to Google and prints the response.
# Make sure to handle exceptions and errors in production code.