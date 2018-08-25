import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')


@bot.event
async def on_ready():
    print("Ready when you are homie")
    print("I am running on " + (bot.user.name))
    print("With the ID: " + (bot.user.id))


@bot.command(pass_context=True)
async def info(ctx,user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))


@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Your test is too low, {}".format(user.name))
    await bot.kick(user)


bot.run("")
