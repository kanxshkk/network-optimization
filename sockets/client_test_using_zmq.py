import zmq
import time

def send_large_data_zmq():
    host = 'tcp://localhost:5555'  # The address of the ZeroMQ server
    large_data = "A" * 100000000  # Create 10MB of data (10,000,000 bytes)

    # Create a ZeroMQ context and REQ socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ is used for request-response communication
    socket.connect(host)

    try:
        start_time = time.time()  # Start timing the data transfer
        print(f"Sending {len(large_data)} bytes of data...")

        # Send the large data as a message (as bytes)
        socket.send(large_data.encode())  # Use encode() to convert to bytes

        # Receive the server's acknowledgment (response)
        response = socket.recv()  # Use recv() to receive raw binary data
        print(f"Received response: {response.decode()}")  # Assuming the server sends a string back

        end_time = time.time()  # End timing the data transfer
        print(f"Data transfer completed in {end_time - start_time} seconds")

    finally:
        socket.close()
        context.term()

if __name__ == "__main__":
    send_large_data_zmq()
