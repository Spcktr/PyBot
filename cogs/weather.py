import discord
from discord.ext import commands
import json
import aiohttp
import datetime
import credentials


class Weather:
    def __init__(self, client):
        self.client = client

# rewrite
# check if arg is string or int
# use url that works with arg type
# print output based on the arg type used

    @commands.command(brief='Current weather', pass_context=True)
    async def weather(self, ctx, arg0, arg1=""):
        """
        Reports current weather. Example '.weather sydney' or '.weather sydney au' \
        If your location is two words, eg 'port maquarie' surround the location in quotes
        """
        if len(arg1) >= 1:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid={2}'.format(
                arg0, arg1, WEATHER)
        else:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(
                arg0, WEATHER)
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)

            #temp_celcius = response['main']['temp']-273.15
            await ctx.channel.send("Here is the forcast " + ctx.message.author.mention
                                   + "\nCurrent weather for {0}: \nIt is {1} \nCurrent temp: {2}°C \nHumidity: {3}%"
                                   .format(response['name'], response['weather'][0]['description'],
                                           round(response['main']['temp'] - 273.15), response['main']['humidity']))


def setup(client):
    client.add_cog(Weather(client))
