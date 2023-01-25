#-----------------------------------------------------------------------------
# Name:        Angel Bot
# Purpose:     A discord bot that censors inappropriate and derogatory words when used in messages on any discord chat, the                bot itself has three different methods of censoring and can also be used to learn facts about cyber-                        bullying/mental health.
# Author:      Rahul Iyer, Abdullah Elganainy, Hasan Wehby
# Created:     20-February-2022
# Updated:     06-June-2022
#-----------------------------------------------------------------------------

import discord
from discord.ext import commands
from discord import *
import random
from list import blacklist

#identifying the prefix needed for the bot to be called
client = discord.Client(intents=discord.Intents.default())
#bot = commands.Bot(command_prefix='!')
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")

bot.remove_command('help')


#the bot connects to the main server to be online on all the servers it's in
@bot.event
async def on_connect():
    print("Bot Online")


phrase = ["I love you", "You are so nice", "You are amazing", "I like you"]
facts = [
    "In 2020, one in five amercians experienced mental health issues.",
    "One in six kids aged 5-17 years suffer from mental health issues each year.",
    "Suicide is the 2nd leading cause of death in the US among people between ages of 10-34.",
    "Depression is the leading cause of disabilty in the world",
    "The global economy loses about $1 Trillion USD every year due to decreased productivity caused by mental illness."
]


#the bot sends an embedded message after typing "!help", cont  aining all commands needed to use the bot
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="AngelBot",
        url="https://discord.com/",
        description="These are the commands to use the AngelBot",
        color=0xf0bd30)
    embed.add_field(name="!help", value="Help command", inline=False)
    embed.add_field(
        name="!positive",
        value=
        "Replaces all messages with blacklisted words with positive messages",
        inline=False)
    embed.add_field(name="!replace",
        value="Replaces all blacklisted words with '#'",
        inline=False)
    embed.add_field(name="!delete",
        value="Deletes all messages with blacklisted words",
        inline=False)
    embed.add_field(name="!fact", value="Sends a random fact", inline=False)
    embed.add_field(name="!off",
        value="Turns all of the censoring  off",
        inline=False)
    await ctx.send(embed=embed)


#the bot confirms the choice chosen
@bot.command()
async def positive(ctx):
    await ctx.send(
        "The bot now replaces all messages with blacklisted words with positive phrases"
    )


#the bot deletes the message sent by the person, containing a derogatory word, to be replaced with a positive phrase
@bot.event
async def on_message(message):
    for word in blacklist:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(
                str(random.choice(phrase)) + ' -' + message.author.mention)
    await bot.process_commands(message)


#the bot confirms the choice chosen
@bot.command()
async def replace(ctx):
    await ctx.send("The bot now replaces all blacklisted words with '####'")

    #the bot deletes the message sent by the person, containing a derogtory word, to send then the same message but replacing the word with "###"
    @bot.event
    async def on_message(message):
        for word in blacklist:
            if word in message.content.lower():
                await message.delete()
                msg = message.content.lower().replace(word, '####')
        await message.channel.send(msg + ' -' + message.author.mention)
        await bot.process_commands(message)


#the bot confirms the choice chosen
@bot.command()
async def delete(ctx):
    await ctx.send("The bot now deletes all messages with blacklisted words")

    #the bot deletes the message sent by the person containing a derogatory word, and then sends a warning on the channel along with mentioning (@) the person who sent the message
    @bot.event
    async def on_message(message):
        for word in blacklist:
            if word in message.content.lower():
                await message.delete()
                await message.channel.send(message.author.mention + ' You can not say that')
        await bot.process_commands(message)


#the bot sends a random fact about mental healt in the chat when called (!fact)
@bot.command()
async def fact(ctx):
    await ctx.send(str(random.choice(facts)))


#the bot becomes offline when "!off" is sent
@bot.command()
async def off(ctx):
    await ctx.send("The censoring is now off")

    @bot.event
    async def on_message(message):
        for word in blacklist:
            if word in message.content.lower():
                pass
        await bot.process_commands(message)


#token for the bot
token = ("TOKEN GOES HERE")
bot.run(token)
