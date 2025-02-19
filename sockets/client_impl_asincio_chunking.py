import asyncio
import time

async def send_large_data():
    large_data = "A" * 10_000_000  # Create 100MB of data
    reader, writer = await asyncio.open_connection('localhost', 5555)

    print(f"Sending {len(large_data)} bytes of data in chunks...")

    start_time = time.time()  # Start timing the data transmission

    # Send data in chunks of 1024 bytes
    chunk_size = 1024
    for i in range(0, len(large_data), chunk_size):
        chunk = large_data[i:i + chunk_size].encode()  # Convert to bytes
        writer.write(chunk)
        await writer.drain()  # Ensure each chunk is sent

    writer.close()
    await writer.wait_closed()

    end_time = time.time()  # End timing the data transmission

    print(f"Data sent successfully in {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    asyncio.run(send_large_data())
