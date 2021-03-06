import discord
from discord.ext import commands
import json
import aiohttp
import datetime


class Crypto(commands.Cog):
    def __init__(self, client):
        self.client = client


    # bitcoin command
    @commands.command(brief='Get Bitcoin prices', pass_context=True)
    async def btc(self, ctx): # change 'btc' to suit command style
        """
        Current Bitcoin price in USD and AUD
        """
        # USD price data source
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        # AUD price data source
        cs_url = 'https://www.coinspot.com.au/pubapi/latest'
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            price = round(response['bpi']['USD']['rate_float'], 2)
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(cs_url)
            au_response = await raw_response.text()
            au_response = json.loads(au_response)
        embed = discord.Embed(
            description="Here is the current price, {0}".format(ctx.message.author.mention),
            # change the color of the embed that is sent
            color=3447003,
            title="Current Bitcoin Price",
        )
        embed.set_footer(text="Via .bitcoin | Prices current @ {0} \
                        ".format(datetime.datetime.now().strftime("%H:%M")))
        embed.add_field(name='__' + 'Current Prices' + '__', value="${0} USD \n${1} AUD" \
                        .format(str(price), au_response['prices']['btc']['bid']))
        await ctx.channel.send(embed=embed)


    ############
    # This command now requires an API key from coinmarketcap
    ############

    # cryptocoin list
    @commands.command(Brief="List current coin prices", pass_context=True)
    async def coinlist(self, ctx): # change coinlist to suit command style
        """
        List of the top current cryptocoins
        """
        translate = 'AUD' #change currency here eg 'USD', 'GBP', 'EUR'
        limit = '10' # number of currencies to list
        url = 'https://api.coinmarketcap.com/v1/ticker/?convert={0}&limit={1}'.format(translate, limit)
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
        embed = discord.Embed(
            description="Top 10 Crypto Currencies & Price",
            # change the color of the embed that is sent
            color=3447003,
            title="Crypto Currency Exchange Rates",
        )
        # footer message
        embed.set_footer(text="Via .coinlist @ {0}| All prices in AUD.".format(datetime.datetime.now().strftime("%H:%M")))
        
        # cycle through the responses and list them in order
        for row in response:
            price = float(row['price_aud'])
            embed.add_field(name="__" + row['name'] + "__:", value="Current price " \
                            + "$**{0}**".format(round(price, 2)), inline=True)
        await ctx.channel.send("Here are the current prices of the top ten currencies" \
                                + ctx.message.author.mention, embed=embed)

def setup(client):
    client.add_cog(Crypto(client))
