import discord
import os
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(client.user.id)
    await client.change_presence(status=discord.Status.online, activity=discord.Game("예찬맘 1호 v0.1 || !도움말"))
    print("온라인")

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("확 씨 씨벌럼이 예찬이 엄마 처음보냐?")
    if message.content.startswith("노무현"):
        await message.channal.send(file=Discord.File("image.png"))
        await message.channel.send("여긴응디시티")
    if message.content.startswith("응디시티 틀어줘"):
        await message.channel.send(";;p 응디시티")
        await message.channel.send(";;p 1")
    if message.content.startswith("!도움말"):
        await message.channel.send("응디시티 틀어줘\n노무현\n!안녕")

token = os.environ["BOT_TOKEN"]
client.run(token)
