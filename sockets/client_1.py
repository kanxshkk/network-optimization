import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 65432)
print("Connecting to the server...")
client_socket.connect(server_address)

try:
    # Send multiple messages to the server
    messages = ["Hello, Server!", "How are you?", "Goodbye!"]
    for msg in messages:
        print(f"Sending: {msg}")
        client_socket.sendall(msg.encode('utf-8'))

        # Wait for the server's response 
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

finally:
    client_socket.close()
    print("Connection closed.")
