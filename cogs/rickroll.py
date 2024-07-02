import discord
from discord.ext import commands
import re

class Rickroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # regex pattern to find give up, giv up, giving up, etc
        pattern = re.compile(r'\bgiv(?:e|ing|in)? up\b', re.IGNORECASE)

        if pattern.search(message.content):
            await message.channel.send("Never gonna give you up, never gonna let you down, never gonna run around and desert you.")
        
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Rickroll(bot))
