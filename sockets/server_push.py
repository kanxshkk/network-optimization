import socket
import threading

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(data)  # Echo back the received data
    except Exception as e:
        print(f"Error with {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Connection closed for {client_address}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(10000)  # Allow up to 10,000 connections
    print("Server is running on localhost:65432")

    while True:
        client_socket, client_address = server_socket.accept()
        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
