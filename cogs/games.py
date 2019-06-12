import discord
from discord.ext import commands
import json
import aiohttp
from datetime import datetime

class Prices:
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Get Steam game price', pass_context=True)
    async def pricecheck(self, ctx):
        #strip start of the message
        game = ctx.message.content[12:]
        game_found = False
        steam_api = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(steam_api)
            response = await raw_response.text()
            response = json.loads(response)

        for i in response["applist"]["apps"]:
            if (i['name'] == game):
                game_found = True
                app = (i['appid'])
                session = aiohttp.ClientSession()
                price_response = await session.get(f"https://store.steampowered.com/api/appdetails/?appids={app}")
                priced = await price_response.json()
                await session.close()
                price = (priced[f"{app}"]["data"]["price_overview"].get('final_formatted'))
                msg = (f"{game} is currently {price}")
                image = (priced[f"{app}"]["data"].get('header_image'))
                discount = (priced[f"{app}"]["data"]["price_overview"].get('discount_price'))

                # embed code start
                embed = discord.Embed(description="Here is your result", color=3447003)
                embed.set_image(url=f"{image}")
                embed.add_field(name=f'Current {game} price', value=f'{price}', inline=False)
                if discount is int('0'):
                    pass
                else:
                    embed.add_field(name="Current Discount", value=f'{discount}% Off')
                embed.set_footer(text="Price current as of {}".format(datetime.now().strftime("%H:%M")))
                await ctx.channel.send(embed=embed)
        if not game_found:
            await ctx.channel.send(f"Could not find info on {game}")

def setup(client):
    client.add_cog(Prices(client))
