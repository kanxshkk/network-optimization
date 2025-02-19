import socket
import time

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)  # Set buffer to 1KB

# Bind the socket to the address and port
server_address = ('localhost', 65432)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is up and running. Waiting for a connection...")

# Accept a connection
connection, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

try:
    # Introduce artificial delay to simulate slow processing
    print("Delaying processing to simulate a backlog... (5 seconds delay)")
    time.sleep(5)  # 5-second delay before processing data

    # Receive data (buffered in chunks)
    data = connection.recv(1024)
    print(f"Received message fragment: {data[:50].decode('utf-8')}...")

    # Log before sending the response
    print("Echoing the message back to the client...")

    # Delay before sending the response
    time.sleep(5)
    connection.sendall(data)

    print("Message sent back to the client.")
finally:
    # Close the connection
    connection.close()
    print("Connection closed.")
