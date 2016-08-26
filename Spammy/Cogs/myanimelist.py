from discord.ext import commands


class Myanimelist():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="|     Links the specified user's MAL profile.")
    async def mal(self, user):
        await self.bot.say("http://myanimelist.net/profile/{}".format(user))

    @commands.command(brief="|     Links the specified user's MAL list.")
    async def mallist(self, user):
        await self.bot.say("http://myanimelist.net/animelist/{}".format(user))


def setup(bot):
    bot.add_cog(Myanimelist(bot))
