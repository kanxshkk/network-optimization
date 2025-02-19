import asyncio
import time

async def handle_client(reader, writer):
    total_data_received = bytearray()
    print("Server is ready to receive data...")

    start_time = time.time()  # Start timing the data reception

    while True:
        data = await reader.read(1024)  # Read in chunks of 1024 bytes
        if not data:
            break  # No more data means the client has finished sending
        total_data_received.extend(data)

    end_time = time.time()  # End timing the data reception

    print(f"Received {len(total_data_received)} bytes of data.")
    print(f"Data reception completed in {end_time - start_time:.6f} seconds")

    writer.write(b"Data received successfully")
    await writer.drain()  # Ensure acknowledgment is sent
    writer.close()
    await writer.wait_closed()

async def start_server():
    server = await asyncio.start_server(handle_client, 'localhost', 5555)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_server())
