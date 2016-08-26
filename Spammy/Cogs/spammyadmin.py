from discord.ext import commands
import discord
import asyncio

class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="|     Ban a member from the server. SpammyAdmin role required.")
    async def ban(self, ctx, member: discord.Member):
        requiredRole = False
        for role in ctx.message.author.roles:
            if role.name == "SpammyAdmin" or ctx.message.author.id == "137021464896471041":
                requiredRole = True
                break

        try:
            if requiredRole == True or ctx.message.author.id == "137021464896471041":
                await self.bot.ban(member)
                message = await self.bot.say("**{}** Has been banned by {}".format(member, ctx.message.author))
                await asyncio.sleep(3)
                await self.bot.delete_message(message)
            else:
                await self.bot.say("`This user has insufficient permissions. The role SpammyAdmin is required to use this command.`")
        except:
            await self.bot.say("```Could not complete this request; FORBIDDEN: Missing Ban Members permission. \nIf help is required, join: https://discord.gg/ysndeCU```")


def setup(bot):
    bot.add_cog(Admin(bot))