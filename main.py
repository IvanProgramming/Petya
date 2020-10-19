import discord

import utils
import settings

client = discord.Client()
@client.event
async def on_message(message):
    if message.author.bot == True:
        if message.content == "ping":
            await utils.ping(message)


client.run(settings.DISCORD_TOKEN, bot=settings.IS_BOT)
