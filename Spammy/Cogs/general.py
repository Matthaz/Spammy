from discord.ext import commands


class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="|   Posts the link to add this bot to your server")
    async def add(self):
        await self.bot.say(
            "Hi! Use this link to add me to your server: https://discordapp.com/oauth2/authorize?client_id=205988737690107904&scope=bot&permissions=8")

    @commands.command(pass_context=True, brief="|    Information on server hosting")
    async def hosting(self, ctx):
        await self.bot.say(
            "{}: Do you want to know how this bot is hosted or need a place to host your own? DigitalOcean is the place for you! Use this link for $10 starting credit: https://m.do.co/c/3fa7d1d8510a".format(ctx.message.author.mention))

def setup(bot):
    bot.add_cog(General(bot))
