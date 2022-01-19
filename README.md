## Nestcord

The best API wrapper for discord you will ever need.


## Bot Example
```py
import nestcord
import asyncio

client = nestcord.Client()

async def main():
    await client.send(
        926115595307614252,
        content"Hello!"
    )

asyncio.run(main())
```

More examples in there `examples` directory.

## Supports
- Timeouts
- Interactions
- Components
