import discord
from discord.ext import commands
import aiohttp
import json
import io

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
                    
                    # get image for pokemon
                    sprite_url = data['sprites']['front_default']

                    # if exists, get from api
                    if sprite_url:
                        async with session.get(sprite_url) as sprite_resp:
                            if sprite_resp.status == 200:
                                sprite_data = await sprite_resp.read()

                                # define image file name
                                filename = f"{data['name'].title()}.png"

                                # add image to message
                                image = discord.File(io.BytesIO(sprite_data), filename=filename)

                                # make the message an embed
                                embed = discord.Embed(description=pokemon_info)
                                embed.set_image(url=f"attachment://{filename}")

                                # send
                                await ctx.send(file=image, embed=embed)
                            else:
                                # otherwise, just send the message
                                await ctx.send(pokemon_info)
                    else:
                        # otherwise, just send the message (part 2)
                        await ctx.send(pokemon_info)
                else:
                    # no pokemon found
                    await ctx.send("Pokémon not found!")

# wait for main to call
async def setup(bot):
    await bot.add_cog(Pokemon(bot))