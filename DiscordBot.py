import discord
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(client.user.id)
    await client.change_presence(status=discord.Status.online, activity=discord.Game("이잉"))
    print("온라인")

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("확 씨 씨벌럼이 예찬이 엄마 처음보냐?")
    if message.content.startswith("노무현"):
        await message.channel.send("여긴응디시티")
    if message.content.startswith("응디시티 틀어줘"):
        await message.channel.send(";;p 응디시티")
        await message.channel.send(";;p 1")


client.run('Njc1NjU3OTI1Njc4ODU4Mjg3.Xj6VnA.ZmOmhHZbQh6vyf  cIwarEky-zQrw')
