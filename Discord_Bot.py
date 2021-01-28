import discord  
import os

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return  
    if message.content.startswith("hi"):
        await message.channel.send("Hello")
    
    if message.author.id == 446675888927408139:
       await message.reply("Hagu")
    
    if message.content.startswith("Wait"):
        await message.channel.send("Hello, What's up. Die")
    
    if message.content.startswith("Hi"):
        await message.channel.send("Wh")
    
    if message.content.startswith("h"):
        await message.channel.send("Hello, What's up. Die")
    
    if message.content.startswith("hi"):
        await message.channel.send("Hello, What's up. Die")


client.run("ODAyOTI1ODExODQxNDk5MTQ2.YA2U7w.EMKG4cW1VE91UuH5tXPg9ts30jY")

















