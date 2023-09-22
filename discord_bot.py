import discord
from discord.ext import commands

TOKEN = 'MTExNTczNDc0NjM3NTQwOTcwNQ.GJE2mQ.SHbDW5lYA61V290k7wNYQ-D_kPvVijZS9qdEyE'  # токен Discord-бота
SAVE_DIRECTORY = 'D:/Github/NeuroKEBAB/prompt.txt'  # директория сохранения сообщений
PREFIX = '/'

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

message_dict = {}  # словарь с сообщениями

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Проверяем, что сообщение не от бота, чтобы избежать зацикливания
    if message.author == bot.user:
        return

    # Проверяем, что сообщение не команда
    if message.content.startswith(PREFIX):
        return

    if str(message.author) != ".kikaa": #"SeaVoice#8208"
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
        for message_id, message_data in message_dict.items():
            file.write(f'{message_data["author"]}: {message_data["content"]}\n')
            file.write('\n')

bot.run(TOKEN)
 