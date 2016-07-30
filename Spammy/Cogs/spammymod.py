from discord.ext import commands
import discord


class Mod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="|   Chance nickname of someone. SpammyMod role required")
    async def nick(self, ctx, user: discord.Member, *, name: str):
        requiredRole = False
        for role in ctx.message.author.roles:
            if role.name == "SpammyMod":
                requiredRole = True

        if requiredRole == True:
            await self.bot.change_nickname(member=user, nickname="{}".format(name))
        else:
            await self.bot.say("`This user has insufficient permissions. The role SpammyMod is required to use this command.`")



def setup(bot):
    bot.add_cog(Mod(bot))
