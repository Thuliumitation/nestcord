import nestcord
import asyncio

client = nestcord.Client()

async def main():
    await client.send(
        926115595307614252,
        content="Hello!"
    )

asyncio.run(main())