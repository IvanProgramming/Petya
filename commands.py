import discord
import time

import utils

client_object = None
utils.client_object = client_object

def set_client(client):
    """ This method is used for setting client instance and trnsmitting them to all layers of bot logic"""
    client_object = client
    utils.client_object = client_object


async def ping(message):
    """ Simple Ping function with execution time benchmark """
    command_execution_start = time.time()
    await message.channel.trigger_typing()
    sended_message = await message.channel.send(embed=discord.Embed(title="Pong! ", color=discord.Color.red()))
    command_execution_end = time.time()
    command_execution_time = round(command_execution_end - command_execution_start, 2)
    edited_embed = sended_message.embeds[0]
    edited_embed.add_field(name="Время исполнения", value=f"{command_execution_time} сек")
    await sended_message.edit(embed=edited_embed)

@utils.sender_admin_permissions_required()
@utils.bot_ban_permissions_required()
@utils.bot_transmit_message_arguments
async def ban(message, user_id, reason="", *args):
    """ Ban function """
    user_id = utils.from_any2user_id(user_id)
    used_guild = message.guild
    guilty_member = await used_guild.fetch_member(user_id)
    await guilty_member.ban(reason=reason)
    await utils.send_ok_embed(message.channel, f"Пользователь {guilty_member.name}#{guilty_member.discriminator} успешно забанен")
