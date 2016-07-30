#!/usr/bin/env python


from discord.ext import commands
import discord


var = "Spammy.exe's Command List"
bot = commands.Bot(command_prefix='=', description=var, pm_help=True)

bot.load_extension("Cogs.myanimelist")
bot.load_extension("Cogs.memes")
bot.load_extension("Cogs.general")
bot.load_extension("Cogs.spammymod")
bot.load_extension("Cogs.osu")


@bot.event
async def on_ready():
    print("Ready to go!")
    print(bot.user.id)
    await bot.change_status(discord.Game(name="=help for more info"))


with open("login.txt", "r") as f:
    var = f.read()

print(var)

bot.run(var.strip())
