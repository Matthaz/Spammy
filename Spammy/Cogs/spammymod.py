from discord.ext import commands
import discord
import asyncio


class Mod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="|     Change nickname of someone. SpammyMod role required.")
    async def nick(self, ctx, user: discord.Member, *, name: str):
        requiredRole = False
        for role in ctx.message.author.roles:
            if role.name == "SpammyMod" or ctx.message.author.id == "137021464896471041":
                requiredRole = True
                break

        try:
            if requiredRole == True or ctx.message.author.id == "137021464896471041":
                await self.bot.change_nickname(member=user, nickname="{}".format(name))
            else:
                await self.bot.say("`This user has insufficient permissions. The role SpammyMod is required to use this command.`")
        except:
            await self.bot.say("```Could not complete this request; FORBIDDEN: Bot role rank too low. \nIf help is required, join: https://discord.gg/ysndeCU```")

    @commands.command(pass_context=True, brief="|     Delete messages from a channel. SpammyMod role required.")
    async def purge(self, ctx, number:int):
        requiredRole = False
        channel = ctx.message.channel
        for role in ctx.message.author.roles:
            if role.name == "SpammyMod" or ctx.message.author.id == "137021464896471041":
                requiredRole = True
                break

        try:
            if requiredRole == True or ctx.message.author.id == "137021464896471041":
                counter = await self.bot.purge_from(channel, limit=number+1)
                message = await self.bot.say("`{} messages deleted`".format(len(counter)))
                await asyncio.sleep(3)
                await self.bot.delete_message(message)
            else:
                await self.bot.say("`This user has insufficient permissions. The role SpammyMod is required to use this command.`")
        except:
            await self.bot.say("```Could not complete this request; FORBIDDEN: Missing manage messages permission. \nIf help is required, join: https://discord.gg/ysndeCU```")

    @commands.command(pass_context=True, brief="|     Kick someone from the server. Spammymod role required.")
    async def kick(self, ctx, member: discord.Member):
        requiredRole = False
        for role in ctx.message.author.roles:
            if role.name =="SpammyMod" or ctx.message.author.id == "137021464896471041":
                requiredRole = True
                break
        try:
            if requiredRole == True or ctx.message.author.id == "137021464896471041":
                await self.bot.kick(member)
                message = await self.bot.say("**{}** Has been kicked".format(member))
                await asyncio.sleep(3)
                await self.bot.delete_message(message)
            else:
                await self.bot.say("`This user has insufficient permissions. The role SpammyMod is required to use this command.`")
        except:
            await self.bot.say("```Could not complete this request; FORBIDDEN: Missing Kick Members permission. \nIf help is required, join: https://discord.gg/ysndeCU```")



def setup(bot):
    bot.add_cog(Mod(bot))
