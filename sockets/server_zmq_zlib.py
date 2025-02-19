import zmq
import zlib

def start_zmq_server():
    host = 'tcp://localhost:5555'  # The address where the server will bind

    # Create a ZeroMQ context and REP socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # REP is used for reply after request
    socket.bind(host)

    print(f"Server is ready to receive messages at {host}...")

    while True:
        # Receive the compressed data
        compressed_data = socket.recv()  # Receive data as compressed bytes
        print(f"Received message of size: {len(compressed_data)} bytes")

        # Decompress the received data using zlib
        decompressed_data = zlib.decompress(compressed_data)  # Decompress the data
        print(f"Decompressed message size: {len(decompressed_data)} bytes")

        # Send acknowledgment (response) back to the client
        socket.send(b"Data received and decompressed successfully")

if __name__ == "__main__":
    start_zmq_server()
