import discord
from discord.ext import commands
import aiohttp
import json

class Pokemon(commands.Cog):
    # initialise by getting api link from config
    def __init__(self, bot):
        self.bot = bot
        with open('data/config.json') as f:
            self.config = json.load(f)

    # !dex command
    @commands.command(name='dex')
    async def dex(self, ctx, *, name: str):
        # fetch info about pokemon by name
        url = f"{self.config['pokemon_api_url']}pokemon/{name.lower()}"

        # get data with link
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:

                # if succeed, process data
                if resp.status == 200:
                    data = await resp.json()
                    height = data['height'] / 10
                    weight = data['weight'] / 10
                    types = [t['type']['name'].title() for t in data['types']]
                    type_label = "Type" if len(types) == 1 else "Types"

                    # discord message layout
                    pokemon_info = (
                        f"**Name:** {data['name'].title()}\n"
                        f"**Dex Number:** {data['id']}\n"
                        f"**Height:** {height}m\n"
                        f"**Weight:** {weight}kg\n"
                        f"**{type_label}:** {', '.join(types)}"
                    )
                    
                    # send message
                    await ctx.send(pokemon_info)
                else:
                    await ctx.send("Pokemon not found!")

# wait for main to call
async def setup(bot):
    await bot.add_cog(Pokemon(bot))