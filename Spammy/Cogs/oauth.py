from discord.ext import commands


class OAuth():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="|     Posts the link to add this bot to your server.")
    async def add(self):
        await self.bot.say(
            "Hi! Use this link to add me to your server: https://discordapp.com/oauth2/authorize?client_id=215020444355526656&scope=bot&permissions=402779143")


def setup(bot):
    bot.add_cog(OAuth(bot))
