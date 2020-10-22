import discord

import commands
import settings

client = discord.Client()
commands.set_client(client)


@client.event
async def on_ready():
    activity = discord.Activity(name='шоу "Измены"', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("""  _____     _               
 |  __ \   | |              
 | |__) |__| |_ _   _  __ _ 
 |  ___/ _ \ __| | | |/ _` |
 | |  |  __/ |_| |_| | (_| |
 |_|   \___|\__|\__, |\__,_|
                 __/ |      
                |___/        Bot started""")

@client.event
async def on_message(message):
    if message.author.bot == False:
        if message.content == "ping":
            await commands.ping(message)
        elif message.content.startswith("ban"):
            await commands.ban(message)
        elif message.content.startswith("to_console"):
            await commands.to_console(message)
        elif message.content.startswith("joke"):
            await commands.rand_joke(message)
client.run(settings.DISCORD_TOKEN, bot=settings.IS_BOT)
