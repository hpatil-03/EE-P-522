import socket

# Set up the socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Raspberry Pi's IP address and port
server_address = ('10.0.0.38', 1234)
sock.connect(server_address)
print('Connected to server address 10.0.0.38 and port 1234')

try:
    # Send a message to the server
    message = 'blink'
    sock.sendall(message.encode())
    print('Data sent = '+ message)
finally:
    # Clean up the connection
    sock.close()
