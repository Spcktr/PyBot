import discord
from discord.ext import commands
import datetime as t
import time
import os


class WorldClock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Current world times', pass_context=True)
    async def clock(self,ctx):
        # country/time zones (in TZ format)
        # see: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        zones = [
            'GMT',
            'Australia/Sydney',
            'America/Los_Angeles',
            'America/New_York',
            'Asia/Dubai'
        ]
        # emoji flags, in order for each entry above
        flags = [
        ':flag_gb:',
        ':flag_au:',
        ':flag_us:',
        ':flag_us:',
        ':flag_ae:'
        ]
        embed = discord.Embed(
        description="Current time around the world",
            # change the embed colour here
            color=3447003
        )
        embed.set_author(name="Current Time")
        embed.set_footer(text="Via .clock | Server time: {0}".format(t.datetime.now().strftime("%H:%M")))

        #zip the two lists and show the times with flags
        for zone, flag in zip(zones, flags):
            os.environ['TZ'] = zone
            time.tzset()
            embed.add_field(name="Location: {0} {1}".format(flag, zone), \
                        value=time.ctime(), inline=False)
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(WorldClock(client))
