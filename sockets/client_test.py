import socket
import time

def send_large_data_raw_socket():
    host = 'localhost'
    port = 12345
    large_data = "A" * 1000000000  # Create 100MB of data (10,000,000 bytes)

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        start_time = time.time()  # Start timing the data transfer
        print(f"Sending {len(large_data)} bytes of data...")

        # Send the large data (no chunking)
        client_socket.sendall(large_data.encode())

        # Receive the echoed data (optional)
        response = client_socket.recv(1024)
        print(f"Received response: {response.decode()}")

        end_time = time.time()  # End timing the data transfer
        print(f"Data transfer completed in {end_time - start_time} seconds")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    send_large_data_raw_socket()
