    import discord
    from discord.ext import commands
    import random as r


    class Cheers:
        def __init__(self, client):
            self.client = client

        client = commands.Bot(command_prefix="")

        @client.event
        async def on_message(self, message):
            cheer_text = (
                'yay',
                'Yay',
                'YAY',
                'YAY!'
            )
            if message.content.startswith(cheer_text):

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
