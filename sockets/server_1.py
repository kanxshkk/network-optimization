import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 65432)  # You can use any valid port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is running and waiting for a connection...")

# Accept a client connection
connection, client_address = server_socket.accept()
print(f"Connected to client: {client_address}")

try:
    # Keep receiving data from the client
    while True:
        data = connection.recv(1024)
        if data:
            print(f"Received from client: {data.decode('utf-8')}")

            # Echo data back to the client
            response = f"Server received: {data.decode('utf-8')}"
            connection.sendall(response.encode('utf-8'))
            print("Sent response to client.")
        else:
            # No data indicates client has disconnected
            print("Client disconnected.")
            break

finally:
    connection.close()
    print("Connection closed.")
