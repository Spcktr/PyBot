import discord
from discord.ext import commands
import random as r


class Puns(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Tells you a pun', pass_context=True)
    async def pun(self, ctx):

        puns = [
        'A backward poet writes inverse.',
        "A bicycle can't stand on its own because it is two tired.",
        'A boiled egg in the morning is hard to beat.',
        'A chicken crossing the road is poultry in motion.',
        'A dentist and a manicurist fought tooth and nail.',
        'A guy once bought compost. It was dirt cheap!',
        'A grenade thrown into a kitchen in France would result in Linoleum Blownapart.',
        'A hangover is the wrath of grapes.',
        'A lot of money is tainted - It taint yours and it taint mine.',
        'A man needs a mistress just to break the monogamy.',
        "A man's home is his castle, in a manor of speaking.",
        'A midget fortune-teller who escapes from prison is a small medium at large.',
        'A plateau is a high form of flattery.',
        'A singing fish went into a talent contest once. After the performance one of the judges said "I dont like the tuna your voice"',
        'Acupuncture is a jab well done.',
        'Bakers trade bread recipes on a knead to know basis.',
        'Condoms should be used on every conceivable occasion.',
        'Dancing cheek-to-cheek is really a form of floor play.',
        "Did you hear a guy's bar got flooded recently? Its no worries though, it didn't dampen his spirits",
        'Did you hear about the composer that killed a guy? They say the murder was orchestrated',
        "Did you hear about the guy whose whole left side was cut off? He's all right now.",
        "Did you hear they made a movie a few years ago about databases? It was so good they're making a SQL",
        'Dijon vu - the same mustard as before.',
        "Does the name Pavlov ring a bell?",
        "Every calendar's days are numbered.",
        "He had a photographic memory that was never developed.",
        "He often broke into song because he couldn't find the key.",
        "How do you get a dog to run faster? Whippet ",
        "I wondered why the baseball was getting bigger. Then it hit me.",
        "If you don't pay your exorcist, you get repossessed.",
        "In democracy it's your vote that counts; in feudalism it's your count that votes.",
        "Local Area Network in Australia: the LAN down under.",
        "Marathon runners with bad footwear suffer the agony of defeat.",
        "Once you've seen one shopping centre, you've seen a mall.",
        "Police were called to a day care where a three-year-old was resisting a rest.",
        "Practice safe eating - always use condiments.",
        "Reading while sunbathing makes you well red.",
        "She was engaged to a boyfriend with a wooden leg but broke it off.",
        "Shotgun wedding: A case of wife or death.",
        "Show me a piano falling down a mineshaft and I'll show you A-flat minor.",
        "The dead batteries were given out free of charge.",
        "The man who fell into an upholstery machine is fully recovered.",
        "The math professor went crazy with the blackboard. He did a number on it.",
        "The professor discovered that her theory of earthquakes was on shaky ground.",
        "The short fortune teller who escaped from prison was a small medium at large.",
        "Those who get too big for their britches will be exposed in the end.",
        "Those who jump off a Paris bridge are in Seine.",
        "Time flies like an arrow. Fruit flies like a banana.",
        "To write with a broken pencil is pointless.",
        "What do you call a bunch of overweight insects? Obees",
        "What do you call a ghost detective? An inspectre",
        "What do you call love in a field? A moor",
        "What do you get a lot of in troll blood? Hemogoblin",
        "What is hayfevers least favourite relative? Auntie Histamine",
        "What's the definition of a will? (It's a dead giveaway.)",
        "What is the worst part about getting something from a wig shop? The price you have toupee",
        "When a clock is hungry, it goes back four seconds.",
        "When an actress saw her first strands of gray hair she thought she'd dye.",
        "When the smog lifts in Los Angeles, U.C.L.A.",
        "When two egotists meet, it's an I for an I.",
        "With her marriage, she got a new name and a dress.",
        "Why did the nuclear plant worker go to the river? They wanted to go fission",
        "Why does the programmer have poor vision? They can't C#",
        "Why is heaven floaty? Because Helsinki",
        "Why were two molluscs fighting? They wanted to slug it out",
        "You feel stuck with your debt if you can't budge it.",
        "An alligator in a vest is an investigator.",
        "We can certainly taco 'bout it right here right now."
        ]

        pun = r.choice(puns)

        await ctx.channel.send(pun)

def setup(client):
    client.add_cog(Puns(client))
