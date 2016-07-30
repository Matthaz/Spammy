from discord.ext import commands
import discord
from osuapi import OsuApi, AHConnector
import aiohttp
import asyncio


with open("osukey.txt", "r") as f:
    var = f.read()


class Osu():
    def __init__(self, bot):
        self.bot = bot
        self.osu = OsuApi(var.strip(), connector=AHConnector())

    @commands.command(brief="|  Posts osu profile and information")
    async def osuu(self, name):
        profile = await self.osu.get_user(username=name)
        await self.bot.say("```{}'s profile |  \n-------------- \nRank: #{} (#{} {}) \nTotal Score: {} \nAcc: {}``` \n<https://osu.ppy.sh/u/{}> \nhttps://a.ppy.sh/{}".format(name, profile[0].pp_rank, profile[0].pp_country_rank, profile[0].country, profile[0].total_score, profile[0].accuracy, profile[0].user_id, profile[0].user_id))


def setup(bot):
    bot.add_cog(Osu(bot))
