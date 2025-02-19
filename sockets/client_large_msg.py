import asyncio

# Function to connect to the server and send large data
async def connect_to_server(server_address, data_size):
    try:
        # Establish the connection using asyncio
        reader, writer = await asyncio.open_connection(*server_address)

        # Create a large message to send
        large_message = "A" * data_size  # Message of size 'data_size' characters
        print(f"Sending message of size: {data_size} bytes")

        # Send the large message
        writer.write(large_message.encode('utf-8'))
        await writer.drain()  # Ensure the message is sent
        response = await reader.read(1024)  # Read the response from the server
        print(f"Response from server: {response.decode()}")  # Print the response

        writer.close()  # Close the writer (connection)
        await writer.wait_closed()  # Wait until the connection is fully closed
    except Exception as e:
        print(f"Connection error: {e}")

# Function to start the stress test by sending large messages with different sizes
async def stress_test_with_data_size(server_address=('localhost', 65432), num_clients=1, max_data_size=1000000, step_size=100000):
    tasks = []
    
    # Loop to gradually increase the data size being sent
    for data_size in range(step_size, max_data_size + 1, step_size):
        print(f"Testing with data size: {data_size} bytes")
        
        # Create tasks for each client to send a large message
        for _ in range(num_clients):
            task = asyncio.create_task(connect_to_server(server_address, data_size))
            tasks.append(task)

        # Wait for all tasks (clients) to complete
        await asyncio.gather(*tasks)

# Entry point to run the client code
if __name__ == "__main__":
    # Start the test with clients sending increasing message sizes
    asyncio.run(stress_test_with_data_size(num_clients=1, max_data_size=1000000, step_size=100000))
