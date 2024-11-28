import asyncio
from nats.aio.client import Client as NATS

async def main():
    nats = NATS()
    
    await nats.connect("nats://public:thenewalbiondata@nats.albion-online-data.com:34222")
    print("Connected to NATS!")
    
    # Subscribe to a subject
    async def message_handler(msg):
        print(f"Received a message: {msg.data.decode()}")

    await nats.subscribe("market_updates", cb=message_handler)
    
    # Keep the connection alive
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
