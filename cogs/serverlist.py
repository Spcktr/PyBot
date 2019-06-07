import discord
from discord.ext import commands
import subprocess
import os


class Servers:
    def __init__(self, client):
        self.client = client

    @commands.command(brief="Get list of current ervers", pass_context=True)
    async def serverlist(self, ctx):
        """
        Will list out all the game servers currently running and thier status
        """
        await ctx.channel.send("Checking which servers are alive, one second please")
        embed = discord.Embed(
            description="Current Game Servers Online",
            color=3447003
        )
        embed.set_author(name='Server List')

        # Server listing
        gServer0 = os.system("ping -c 1 minecraft.example.com")
        if gServer0 == 0:
            server_response = ":large_blue_circle:"
        else:
            server_response = ":red_circle:"
        embed.add_field(name="Minecraft", value="**Pack:** Feed the Beast - Infinity Evolved \
                        \n **Server:** minecraft.example.com \n **Status** {0} "
                        .format(server_response), inline=False)

        embed.set_footer(
            text="Via .serverlist | If any problems or questions ask in relevant channel")
        await ctx.channel.send("Here are the current games and thier server status"
                               + ', ' + ctx.message.author.mention, embed=embed)

    @commands.command(brief='Ping an IP or website', pass_context=True)
    async def ping(self, ctx, arg1):
        """
        Check if a site or service is up. example .ping 8.8.8.8
        """
        r = os.system("ping -c 1 {0}".format(arg1))
        if r == 0:
            await ctx.channel.send("The service {0} is running".format(arg1))
        else:
            await ctx.channel.send("The service {0} doesn't seem to be working at the moment".format(arg1))


def setup(client):
    client.add_cog(Servers(client))
