import socket
import threading

def connect_to_server(server_address, num_messages=10):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        
        for _ in range(num_messages):
            message = "Test Message".encode('utf-8')
            client_socket.sendall(message)
            response = client_socket.recv(1024)
            print(f"Response from server: {response.decode()}")
        
        client_socket.close()
    except Exception as e:
        print(f"Connection error: {e}")

def stress_test(server_address=('localhost', 65432), num_clients=10000):
    threads = []
    for _ in range(num_clients):
        thread = threading.Thread(target=connect_to_server, args=(server_address,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    stress_test(num_clients=10000)  # Stress test with 10,000 clients
