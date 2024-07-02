import discord
from discord.ext import commands
import aiohttp
import json

class Bored(commands.Cog):
    #initialise by getting api link from config
    def __init__(self, bot):
        self.bot = bot
        with open('data/config.json') as f:
            self.config = json.load(f)
        self.bored_api_url = self.config['bored_api_url']

    # helper function to get a random activity
    async def get_random_activity(self):
        url = f"{self.bored_api_url}/activity/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    return None

    # helper function to get a random activity by type
    async def get_activity_by_type(self, activity_type=None):
        url = f"{self.bored_api_url}/activity"
        params = {}
        if activity_type:
            params['type'] = activity_type

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    return None

    # command to get a random activity
    @commands.command(name='bored')
    async def bored(self, ctx):
        activity = await self.get_random_activity()
        if activity:
            await ctx.send(f"Here's something you can do: **{activity['activity']}**")
        else:
            await ctx.send("Couldn't fetch an activity. The API is probably down, try again later.")

    # command to get a random recreational activity
    @commands.command(name='bored_recreational')
    async def bored_recreational(self, ctx):
        activity = await self.get_activity_by_type('recreational')
        if activity:
            await ctx.send(f"Here's something recreational you can do: **{activity['activity']}**")
        else:
            await ctx.send("Couldn't fetch a recreational activity. The API is probably down, try again later.")

    # command to get a random social activity
    @commands.command(name='bored_social')
    async def bored_social(self, ctx):
        activity = await self.get_activity_by_type('social')
        if activity:
            await ctx.send(f"Here's something social you can do: **{activity['activity']}**")
        else:
            await ctx.send("Couldn't fetch a social activity. The API is probably down, try again later.")

    # command to get a random recreational or social activity, can be specified by person
    @commands.command(name='imbored')
    async def imbored(self, ctx, participants: int):
        if participants < 1:
            await ctx.send("Please provide a valid number of participants.")
            return

        activity = await self.get_activity_by_type(participants=participants)
        if activity:
            await ctx.send(f"Here's something you can do with {participants} {'person' if participants == 1 else 'people'}: **{activity['activity']}**")
        else:
            await ctx.send("Couldn't fetch an activity. The API is probably down, try again later.")

async def setup(bot):
    await bot.add_cog(Bored(bot))



