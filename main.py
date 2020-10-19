import discord

import commands
import settings

client = discord.Client()
@client.event
async def on_message(message):
    if message.author.bot == False:
        if message.content == "ping":
            await commands.ping(message)


client.run(settings.DISCORD_TOKEN, bot=settings.IS_BOT)
