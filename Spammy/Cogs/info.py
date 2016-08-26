from discord.ext import commands
import discord


class Info():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="|     Posts information on the server.")
    async def serverinfo(self, ctx):
        server = ctx.message.server
        await self.bot.say("Server info for **{}** \nServer Name: **{}**  -  Server Owner: **{}**  -  Member Count: **{}**"
                           "\nServer ID: **{}**  -  Region: **{}**  -  Created: **{}**"
                           "\nDefault Channel: **{}**  -  Icon: {}".format(server.name, server.name, server.owner,
                                                                           server.member_count, server.id, server.region,
                                                                           server.created_at,server.default_channel,
                                                                           server.icon_url))

    @commands.command(pass_context=True, brief="|     Information about the tagged user.")
    async def info(self, ctx, member: discord.Member = None):
        if member is None:
            person = ctx.message.author
            await self.bot.say("Name: **{}**  -  Unique Identifier: **{}**  -  ID: **{}**"
                               "\nDisplay Name: **{}**  -  Bot Account: **{}**  -  Mention String: **{}**"
                               "\nAccount Created: **{}**  -  Avatar: {}".format(person.name, person.discriminator,
                                                                                 person.id, person.display_name,
                                                                                 person.bot, person.mention,
                                                                                 person.created_at, person.avatar_url))
        else:
            person = member
            await self.bot.say("Name: **{}**  -  Unique Identifier: **{}**  -  ID: **{}**"
                               "\nDisplay Name: **{}**  -  Bot Account: **{}**  -  Mention String: **{}**"
                               "\nAccount Created: **{}**  -  Avatar: {}".format(person.name, person.discriminator,
                                                                                 person.id, person.display_name,
                                                                                 person.bot, person.mention,
                                                                                 person.created_at, person.avatar_url))

    @commands.command(pass_context=True, brief="|     Check a members permissions in a server.")
    async def perms(self, ctx, user: discord.User = None):
        if user is None:
            target = ctx.message.author
            var = target.permissions_in(channel=ctx.message.channel)
            perm = []
            for x in var:
                if x[1] is True:
                    perm.append(x[0])
            await self.bot.say("**{}'s** permissions are: ```xl\n{}\n```".format(ctx.message.author, "\n".join(perm)))
        else:
            target = user
            var = target.permissions_in(channel=ctx.message.channel)
            perm = []
            for x in var:
                if x[1] is True:
                    perm.append(x[0])
            await self.bot.say("**{}'s** permissions are: ```xl\n{}\n```".format(user, "\n".join(perm)))


    @commands.command(pass_context=True, hidden=True)
    async def listserver(self, ctx):
        if ctx.message.author.id == "137021464896471041":
            server = list(self.bot.servers)
            for x in server:
                print("Server: {}[{}]  -  Owner: {}  -  Member Count: {}".format(x.name, x.id, x.owner, x.member_count))

    async def on_server_join(self, server):
        server_role = server.roles
        role = []
        for x in server_role:
            role.append(x.name)
        await self.bot.send_message(destination=self.bot.get_channel("216358594466021377"),
                                    content=("I just joined a new server!"
                                             "\nServer Name: **{}**  -  Server Owner: **{}**  -  Member Count: **{}**"
                                             "\nServer ID: **{}**  -  Region: **{}**  -  Created: **{}**"
                                             "\nDefault Channel: **{}**  -  Icon: {}"
                                             "\nRoles: ```xl\n{}```"
                                             .format(server.name, server.owner, server.member_count,
                                                     server.id, server.region, server.created_at,
                                                     server.default_channel, server.icon_url, role[0])))

    @commands.command(pass_context=True, brief="|     Info about me!")
    async def about(self, ctx):
        server = self.bot.servers
        await self.bot.say("Hey! I'm **Spammy!** I'm a multi-function bot created by my owner, **Matt!** I was created"
                           " on the 22nd of July, 2016."
                           "\nI'm currently connected to **{} servers** and can see a total of **{} people**"
                           "\nIf you would like to know my commands, use `=help` for a list of all of them, and if you w"
                           "ould like any more help, join https://discord.gg/ysndeCU"
                           .format(len(server), len(set(self.bot.get_all_members()))))


def setup(bot):
    bot.add_cog(Info(bot))