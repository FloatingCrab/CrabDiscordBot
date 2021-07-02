# bot.py

import discord

with open("token") as token:
    TOKEN = token.read()

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# for crab gifs etc
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "banana crab":
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/626422692597202964/860522243036807218/crab_eating_Banana_video.gif")
    if message.content == "cherry crab":
        await message.channel.send("https://tenor.com/view/crab-eating-food-gif-9038987")
    if message.content == "pet the crab":
        await message.channel.send("https://tenor.com/view/crab-crab-petting-crabs-jacque-cousteau-cousteau-gif-3530356")

client.run(TOKEN)
