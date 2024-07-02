import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# load .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

# define intents
intents = discord.Intents.default()
intents.message_content = True

# create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# event listener for when the bot goes online
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# test command: respond to hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hi!')

# run bot
bot.run(TOKEN)