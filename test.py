import discord
from discord.ext import commands

TOKEN = 'MTExNTczNDc0NjM3NTQwOTcwNQ.GJE2mQ.SHbDW5lYA61V290k7wNYQ-D_kPvVijZS9qdEyE'  # токен Discord-бота
SAVE_DIRECTORY = 'C:/Users/ryanh/Desktop/Neuro-sama/test/promt.txt'  # директория сохранения сообщений
PREFIX = '/'

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

message_dict = {}  # словарь с сообщениями

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @bot.event
# async def on_message(message):
#     await bot.process_commands(message)
#     # Проверяем, что сообщение не от бота, чтобы избежать зацикливания
#     if message.author == bot.user:
#         return

#     # Проверяем, что сообщение не команда
#     if message.content.startswith(PREFIX):
#         return

#     if str(message.author) != "SeaVoice#8208":
#         return

@bot.event
async def on_message(message):
    # Проверяем, что сообщение не от бота, чтобы избежать зацикливания
    if message.author == bot.user:
        return

    # Проверяем, что сообщение не команда
    if message.content.startswith(PREFIX):
        return

    if str(message.author) != "SeaVoice#8208":
        return
    
    # Сохраняем сообщение в словаре
    message_dict[message.id] = {
        'author': str(message.author),
        'content': message.content,
        'timestamp': str(message.created_at)
    }

    print(f'Saved message from {message.author} with ID {message.id}')

    # Записываем словарь в файл
    save_to_file()

def save_to_file():
    with open(SAVE_DIRECTORY, 'w') as file:
        # for message_id, message_data in message_dict.items():
        #     file.write(f'Message ID: {message_id}\n')
        #     file.write(f'Author: {message_data["author"]}\n')
        #     file.write(f'Content: {message_data["content"]}\n')
        #     file.write(f'Timestamp: {message_data["timestamp"]}\n')
        #     file.write('\n')
        for message_id, message_data in message_dict.items():
            file.write(f'{message_data["content"]}\n')
            file.write('\n')


@bot.command(
    name="clear",
    description="You can type /clear <amount> in a text channel where the bot has permissions to delete messages. Replace <amount> with the desired number of messages to delete.",
)
async def clear(ctx, amount=5):
    """Clear a specified number of messages from the chat."""
    await ctx.channel.purge(limit=amount + 1)  # +1 чтобы удалить сообщение с командой
    await ctx.send(f"Cleared {amount} messages.")

bot.run(TOKEN)
 