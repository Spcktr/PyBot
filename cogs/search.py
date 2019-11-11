import discord
from discord.ext import commands
import aiohttp
import datetime
import ddg3


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    #duck duck go search
    @commands.command(brief='Web Search', pass_context=True)
    async def search(self, ctx, *args):
        """
        Search the web, uses DuckDuckGo for privacy
        """
        r = ddg3.query("'{0}'".format(args))
        result_type = ''
        result_type = r.type
        #answer results
        #answer_text = r.results[0].text
        #answer_url = r.results[0].url

        #disambiguation results
        result_text = r.related[0].text
        result_url = r.related[0].url

        embed = discord.Embed(
            description="Search results for {0}, {1}".format(args, ctx.message.author.mention),
            color=3447003,
            title='Here are your results',
        )
        embed.set_footer(text="Via .search @ {0} | Results via DuckDuckGo \
                            If any issues contact Waka#1920".format(datetime.datetime.now().strftime("%H:%M")))

        if result_type is 'answer':
            embed.add_field(name="__" + "Search Results" + "__", value="URL: {0} \n {1}" \
                            .format(r.results[0].url, r.results[0].text))
        else:
            embed.add_field(name="__" + "Search Results" + "__", value="URL: {0} \n {1}" \
                            .format(result_url, result_text))

        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Utilities(client))
