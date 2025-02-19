import zmq

def start_zmq_server():
    host = 'tcp://localhost:5555'  # The address where the server will bind

    # Create a ZeroMQ context and REP socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # REP is used for reply after request
    socket.bind(host)

    print(f"Server is ready to receive messages at {host}...")

    while True:
        # Receive a message (the large data) as bytes
        large_data = socket.recv()  # Use recv() to receive raw binary data
        print(f"Received message of size: {len(large_data)} bytes")

        # Send acknowledgment (response) back to the client
        socket.send(b"Data received successfully")

if __name__ == "__main__":
    start_zmq_server()
