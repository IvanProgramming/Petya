import time
import discord

async def ping(message):
        command_execution_start = time.time() 
        sended_message = await message.channel.send(embed=discord.Embed(title="Pong! ", color=discord.Color.red()))
        command_execution_end = time.time()
        command_execution_time = round(command_execution_end - command_execution_start, 2)
        edited_embed = sended_message.embeds[0]
        edited_embed.add_field(name="Время исполнения", value=f"{command_execution_time} сек")
        await sended_message.edit(embed=edited_embed)