import asyncio

# Function to connect to the server and send/receive messages
async def connect_to_server(server_address, num_messages=10):
    try:
        # Establish the connection using asyncio
        reader, writer = await asyncio.open_connection(*server_address)

        for _ in range(num_messages):
            message = "Test Message".encode('utf-8')
            writer.write(message)
            await writer.drain()  # Ensure the message is sent
            response = await reader.read(1024)  # Read the response from the server
            print(f"Response from server: {response.decode()}")  # Print the response

        writer.close()  # Close the writer (connection)
        await writer.wait_closed()  # Wait until the connection is fully closed
    except Exception as e:
        print(f"Connection error: {e}")

# Function to start the stress test by connecting 10,000 clients
async def stress_test(server_address=('localhost', 65432), num_clients=10000):
    tasks = []
    
    # Create tasks for each client to connect to the server
    for _ in range(num_clients):
        task = asyncio.create_task(connect_to_server(server_address))
        tasks.append(task)

        # Introduce a small delay between client connections to reduce load on the system
        await asyncio.sleep(0.01)  # 10ms delay between connections (adjust as needed)

    # Wait for all tasks (clients) to complete
    await asyncio.gather(*tasks)

# Entry point to run the client code
if __name__ == "__main__":
    # Start the stress test with 10,000 clients
    asyncio.run(stress_test(num_clients=10000))
