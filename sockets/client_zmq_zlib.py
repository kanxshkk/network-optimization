import zmq
import zlib
import time

def send_large_data_zmq():
    host = 'tcp://localhost:5555'  # The address of the ZeroMQ server
    large_data = "A" * 1000000000  # Create 10MB of data (10,000,000 bytes)

    # Compress the data using zlib
    compressed_data = zlib.compress(large_data.encode())  # Compress to reduce data size

    # Create a ZeroMQ context and REQ socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ is used for request-response communication
    socket.connect(host)

    try:
        start_time = time.time()  # Start timing the data transfer
        print(f"Sending {len(compressed_data)} bytes of compressed data...")

        # Send the compressed data
        socket.send(compressed_data)

        # Receive the server's acknowledgment (response)
        response = socket.recv()  # Receive response from the server
        print(f"Received response: {response.decode()}")  # Assuming the server sends a string back

        end_time = time.time()  # End timing the data transfer
        print(f"Data transfer completed in {end_time - start_time} seconds")

    finally:
        socket.close()
        context.term()

if __name__ == "__main__":
    send_large_data_zmq()
