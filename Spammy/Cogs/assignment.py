from discord.ext import commands
import aiohttp
import asyncio

class Assignment():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fetch_image(self, identifier):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://imgur.com/gallery/{}'.format(identifier)) as response:
                print(response.status)
                await self.bot.say(await response.text())


def setup(bot):
    bot.add_cog(Assignment(bot))