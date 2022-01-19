import nestcord
import asyncio

client = nestcord.Client()
button = nestcord.View(
    buttons = [
        nestcord.Component(
            label="Button",
            style=nestcord.Style.blurple
            )
        ]
)
async def main():
    await client.send(
        926115595307614252,
        content="Hello!"
        view=button,
    )

asyncio.run(main())