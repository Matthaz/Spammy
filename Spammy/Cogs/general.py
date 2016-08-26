from discord.ext import commands
import aiohttp
import datetime


with open("weatherkey.txt", "r") as f:
    apiKey = f.read()


class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="|     Information on server hosting.")
    async def hosting(self, ctx):
        await self.bot.say("{}: Do you want to know how this bot is hosted or need a place to host your own? DigitalOcean is the place for you! Use this link for $10 starting credit: https://m.do.co/c/3fa7d1d8510a".format(ctx.message.author.mention))

    @commands.command(brief="|     Displays weather information for specified place.")
    async def weather(self, *,word="cityName, Country"):
        name = word.split(",")
        if len(name) == 1:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric".format(name[0].replace(" ", "_"), apiKey.strip())
        else:
            url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}&units=metric".format(name[0].replace(" ", "_"), name[1].replace(" ", "_"), apiKey.strip())

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
                                   .format(name[0].title(), data["sys"]["country"], data["coord"]["lat"],
                                           data["coord"]["lon"], data["weather"][0]["description"],
                                           data["main"]["humidity"], data["main"]["temp"],
                                           data["main"]["temp"]*1.8+32, data["clouds"]["all"],
                                           data["wind"]["speed"], sunrise, sunset))

    @commands.command(brief="|     Urban dictionary!")
    async def urban(self, *, word):
        try:
            var = word.replace(" ", "")
            url = "http://api.urbandictionary.com/v0/define?term={}".format(var)
            with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    data = await resp.json()
                    await self.bot.say(
                        "**{}** \n```{}\nExample:\n"
                        " {}```\nAuthor: **{}**  -  Rating: {} :thumbsup:/{} :thumbsdown: \nLink: <{}>".format(
                            word.title(), data["list"][0]["definition"], data["list"][0]["example"],
                            data["list"][0]["author"], data["list"][0]["thumbs_up"], data["list"][0]["thumbs_down"],
                            data["list"][0]["permalink"]))
        except:
            await self.bot.say("No definition for **{}** could be found, sorry.".format(word.title()))


    async def on_server_join(self, server):
        await self.bot.send_message(server,
                               content="```Hi! \nThanks for adding me to {}, I think i'm gonna like it here!"
                                       "\nIf you need any help with me, be sure to check out the #support channel in https://discord.gg/ysndeCU```".format(
                                   server))


def setup(bot):
    bot.add_cog(General(bot))
