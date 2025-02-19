import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 65432)
client_socket.connect(server_address)

try:
    # Send a large message (10 million 'A's)
    large_message = "A" * 10000000  # 10 million characters
    print("Sending large message to the server...")
    for _ in range(100):  # Send 100 large messages
        client_socket.sendall(large_message.encode('utf-8'))

    print("Message sent successfully.")

    # Receive response
    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode('utf-8')}")
finally:
    # Close the connection
    client_socket.close()
    print("Connection closed.")
