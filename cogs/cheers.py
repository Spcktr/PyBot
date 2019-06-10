import discord
from discord.ext import commands
import random as r
import re


class Cheers:
    def __init__(self, client):
        self.client = client

    client = commands.Bot(command_prefix="")

    @client.event
    async def on_message(self, message):
        if message.content.startswith(re.IGNORECASE('yay', 'YAY', 'yay!', 'YAY!')):

            cheers = [
            "HOORAH!",
            "HURRAY!",
            "OORAH!",
            "YAY!",
            "HOOHAH!",
            "HOOYAH!",
            'HUAH!',
            '♪ ┏(°.°)┛CHEERS!┗(°.°)┓ ♬'
            ]

            cheer = r.choice(cheers)
            await message.channel.send(cheer)

def setup(client):
    client.add_cog(Cheers(client))
