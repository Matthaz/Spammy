from discord.ext import commands
from osuapi import OsuApi, AHConnector


with open("osukey.txt", "r") as f:
    var = f.read()


class Osu():
    def __init__(self, bot):
        self.bot = bot
        self.api = OsuApi(var.strip(), connector=AHConnector())

    @commands.command(brief="|  Posts osu profile and information")
    async def osu(self, name):
        profile = await self.api.get_user(username=name)
        await self.bot.say("```xl\n{}'s profile  \n-------------- \nRank: #{} (#{} {}) \nPP: {} | Level: {} \nTotal Score: {} \nAcc: {}``` \n<https://osu.ppy.sh/u/{}> \nhttps://a.ppy.sh/{}".format(name, profile[0].pp_rank, profile[0].pp_country_rank, profile[0].country, profile[0].pp_raw, profile[0].level, profile[0].total_score, profile[0].accuracy, profile[0].user_id, profile[0].user_id))


def setup(bot):
    bot.add_cog(Osu(bot))
