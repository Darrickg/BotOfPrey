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

# load cogs
async def load_extensions():
    cogs = ['cogs.pokemon', 'cogs.bored']
    for cog in cogs:
        try:
            await bot.load_extension(cog)
        except Exception as e:
            print(f'failed to load cog {cog}: {e}')

# test command: respond to hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hi!')

# run bot
async def main():
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())