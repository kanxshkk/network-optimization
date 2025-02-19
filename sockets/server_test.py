import socket

def start_raw_socket_server():
    host = 'localhost'
    port = 12345

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print(f"Server is running on {host}:{port}. Waiting for client connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")

        try:
            # Receive the full message (no chunking)
            full_data = client_socket.recv(1000000000)  # Max size based on data size (e.g., 1000MB)
            print(f"Received {len(full_data)} bytes of data.")

            # Optional: Send a response to the client
            client_socket.sendall(b"Data received")

        finally:
            # Clean up the connection
            client_socket.close()
            print(f"Connection from {client_address} closed.")

if __name__ == "__main__":
    start_raw_socket_server()
