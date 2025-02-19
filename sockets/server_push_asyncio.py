import asyncio

async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f"New connection from {client_address}")

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            writer.write(data)  # Echo back the received data
            await writer.drain()  # Ensure the data is sent back
    except Exception as e:
        print(f"Error with {client_address}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Connection closed for {client_address}")

async def start_server():
    server = await asyncio.start_server(handle_client, 'localhost', 65432)
    print("Server is running on localhost:65432")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_server())
