from discord.ext import commands
import aiohttp
import datetime


with open("weatherkey.txt", "r") as f:
    apiKey = f.read()


class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="|   Posts the link to add this bot to your server")
    async def add(self):
        await self.bot.say(
            "Hi! Use this link to add me to your server: https://discordapp.com/oauth2/authorize?client_id=205988737690107904&scope=bot&permissions=8")

    @commands.command(pass_context=True, brief="|    Information on server hosting")
    async def hosting(self, ctx):
        await self.bot.say("{}: Do you want to know how this bot is hosted or need a place to host your own? DigitalOcean is the place for you! Use this link for $10 starting credit: https://m.do.co/c/3fa7d1d8510a".format(ctx.message.author.mention))

    @commands.command(brief="|    Displays weather information for specified place")
    async def weather(self, *,word="cityName, Country"):
        name = word.split(",")
        if len(name) == 1:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric".format(name[0].replace(" ", "_"), apiKey)
        else:
            url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}&units=metric".format(name[0].replace(" ", "_"), name[1].replace(" ", "_"), apiKey)

        with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
                sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")
                await self.bot.say("**{}-{}** ({} {}) "
                                   "\n**Current Condition**: {} "
                                   "\n**Humidity**: {}%     **Temperature**: {}°C/{}°F "
                                   "\n**Clouds**: {}%     **Wind Speed**:{} m/s "
                                   "\n**Sunrise**: {} UTC/**Sunset**: {} UTC"
                                   .format(name[0], data["sys"]["country"], data["coord"]["lat"],
                                           data["coord"]["lon"], data["weather"][0]["description"],
                                           data["main"]["humidity"], data["main"]["temp"],
                                           data["main"]["temp"]*1.8+32, data["clouds"]["all"],
                                           data["wind"]["speed"], sunrise, sunset))



def setup(bot):
    bot.add_cog(General(bot))
