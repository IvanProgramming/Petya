import discord
import re
client_object = None


def parse_command(msg_text):
    """ Parsing command and split it to command, arguments """
    msg_text = re.sub("\\s{2,}", " ", msg_text)
    splitted_text = msg_text.split()
    return (splitted_text[0], splitted_text[1:])


async def send_ok_embed(channel, ok_msg_text, title="OK"):
    """ This functions sends ok messege """
    await channel.send(embed=discord.Embed(title=title,
                                           description=ok_msg_text,
                                           color=discord.Color.green()))


async def send_error_embed(channel, error_msg_text, title="Ошибка"):
    """ This function sends error message """
    await channel.send(embed=discord.Embed(title=title,
                                           description=error_msg_text,
                                           color=discord.Color.red()))


def sender_admin_permissions_required(send_error_message=False):
    """ This is decorator, used for admin only functions """
    def the_real_decorator(fn):
            async def check_user_admin_permissions(message, *args, **kwargs):
                if isinstance(message.author, discord.Member):
                    if message.author.guild_permissions.administrator:
                        await fn(message, *args, **kwargs)
                    else:
                        if send_error_message:
                            await send_error_embed(message.channel, "Недостаточно прав для исполнения команды")
                else:
                    await send_error_embed(message.channel, "Данная команда не предназнченна для личных сообщений")
            return check_user_admin_permissions
    return the_real_decorator


def bot_ban_permissions_required(send_error_message=True):
    """ Decorator, that checks is bot has a ban permissions """
    def the_real_decorator(fn):
        async def check_bot_permissions(message, *args, **kwargs):
            used_guild = message.guild
            bot_as_member = await used_guild.fetch_member(client_object.user.id)
            if bot_as_member.guild_permissions.ban_members or bot_as_member.guild_permissions.administrator:
                await fn(message, *args, **kwargs)
            else:
                await send_error_embed(message.channel, "У бота недостаточно прав для бана пользователей")
        return check_bot_permissions
    return the_real_decorator


def bot_transmit_message_arguments(fn):
    """ Decorator, that parses command and arguments and send them to function """
    async def transmit_args(message, *args, **kwargs):
        if message.content:
            await fn(message, *parse_command(message.content)[1], *args, **kwargs)
        else:
            await fn(message, *args, **kwargs)
    return transmit_args


def from_any2user_id(source):
    """ Converts mention or just id to user_id integer """
    if re.match("<@!\d{18}>", source):
        return source[3:-1]
    else:
        try:
            return int(source)
        except ValueError:
            return 0

def fetch_emojis(message_content):
    """ Function, that fetches all emojis into emoji project  """
    emojis = re.findall("<.:[a-zA-Z0-9_]{2,}:\d{18}>", message_content)
    emojis_objects = []
    for emoji in emojis:
        emoji_id = int(emoji[-19:-1])
        emojis_objects.append(client_object.get_emoji(emoji_id))
    return emojis_objects
