from discord.ext import commands
import aiohttp
import asyncio

class Assignment():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def upimg2(self, ctx, url: str):
        with aiohttp.ClientSession() as session:  # Opens async HTTP session
            async with session.get(url) as response:  # Sends request, stores response.
                image = await response.content.read()  # Grabs image data from "stream"
                with open("unknown.jpg", 'wb') as dl_image:  # opens empty image send_file
                    dl_image.write(image)  # Writes image data into image file, then closes it
                await self.bot.send_file(ctx.message.channel, "unknown.jpg")  # uploads image


def setup(bot):
    bot.add_cog(Assignment(bot))