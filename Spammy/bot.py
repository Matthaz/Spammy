#!/usr/bin/env python


from discord.ext import commands
import discord


var = "Spammy.exe's Command List"
bot = commands.Bot(command_prefix='=dev ', description=var, pm_help=True, help_attrs=dict(hidden=True))
cogs = ["Cogs.general", "Cogs.info", "Cogs.memes", "Cogs.myanimelist", "Cogs.oauth", "Cogs.osu", "Cogs.spammyadmin", "Cogs.spammymod"]


@bot.event
async def on_ready():
    print("Ready to go!")
    print(bot.user.id)
    await bot.change_status(discord.Game(name="I will rule the world!"))
    for x in cogs:
        bot.load_extension(x)


with open("login.txt", "r") as f:
    var = f.read()

print(var)

bot.run(var.strip())
