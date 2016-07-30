from discord.ext import commands
import discord
import urllib

class Memes():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="|    Tell yourself or your friends to kys :^)")
    async def kys(self, ctx, *, user: discord.Member = None):
        if user is None:
            await self.bot.upload('Pics.noose.jpg', content="{} Kill yourself faggot :^)".format(ctx.message.author.mention))
        else:
            await self.bot.upload('Pics.noose.jpg', content="{} Kill yourself faggot :^)".format(user.mention))

    @commands.command(pass_context=True, brief="|    Sends a nope gif")
    async def nope(self):
        await self.bot.upload('Pics.Nope_dog.gif')

    @commands.command(pass_context=True)
    async def lewd(self):
        urllib.urlretrieve("")


def setup(bot):
    bot.add_cog(Memes(bot))
