import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

# Check current buffer sizes
send_buffer_size = socket.getsockopt(zmq.SNDHWM)
recv_buffer_size = socket.getsockopt(zmq.RCVHWM)

print(f"Send buffer size (SNDHWM): {send_buffer_size} bytes")
print(f"Receive buffer size (RCVHWM): {recv_buffer_size} bytes")
