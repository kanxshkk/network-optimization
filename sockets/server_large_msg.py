import asyncio

# Function to handle incoming client connections
async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f"New connection from {client_address}")

    try:
        # Increase buffer size to handle larger data
        reader.set_read_buffer_size(10 * 1024 * 1024)  # 10MB buffer

        # Receive large data from the client
        data = await reader.read(10000000)  # Limit the data size to a large value
        print(f"Received message of size: {len(data)} bytes")

        # Echo back the received data
        writer.write(data)
        await writer.drain()  # Ensure the message is sent back

    except Exception as e:
        print(f"Error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Connection closed for {client_address}")


# Function to start the server
async def start_server():
    server = await asyncio.start_server(handle_client, 'localhost', 65432)
    print("Server is running on localhost:65432")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_server())
