import discord

async def send_error_embed(channel, error_msg_text):
        """ This function can be used for send error message to selected channel """
        await channel.send(embed=discord.Embed(title="Ошибка",
                                                       description=error_msg_text,
                                                       color=discord.Color.red()))


def admin_permissions_required(send_error_message=False):
        """ This is decorator, used for admin only functions """
        def the_real_decorator(fn):
                async def check_admin_permissions(message):
                        if isinstance(message.author, discord.Member):
                                if message.author.guild_permissions.administrator:
                                        await fn(message)
                                else:
                                        if send_error_message:
                                                await send_error_embed(message.channel, "Недостаточно прав для исполнения команды")
                        else:
                                await send_error_embed(message.channel, "Данная команда не предназнченна для личных сообщений")
                return check_admin_permissions
        return the_real_decorator

