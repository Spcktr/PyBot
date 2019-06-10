import discord
from discord.ext import commands
import os
import aiohttp
import credentials

client = commands.Bot(command_prefix = ".")
a = discord.Game(name='.help for commands') # change online playing presence

intial_extensions = [
                    'cogs.crypto',
                    'cogs.weather',
                    'cogs.serverlist',
                    'cogs.search',
                    'cogs.worldclock',
                    'cogs.audio',
                    'cogs.puns',
                    'cogs.cheers'
                    ]

# bot is alive
@client.event
async def on_ready():
    print('|----------------------------------------------------|')
    print('|                                                    |')
    print('|                Logged in & ready                   |')
    print('|            I have logged in as {0.user}          |'.format(client))
    print('|                                                    |')
    print('|----------------------------------------------------|')



    await client.change_presence(status=discord.Status.online, activity=a)

# add cogs/exts
if __name__ == '__main__':
    for extension in intial_extensions:
        try:
             client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

client.run(credentials.TOKEN, bot=True, reconnect=True)
