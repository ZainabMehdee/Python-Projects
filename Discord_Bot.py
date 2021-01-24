import discord  
import os

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is logged in as {0.user}".format(client))


@client.event
async def on_message(message_trigger):
    if message_trigger.author == client.user:
        return  
    if message_trigger.content.startswith("Hello", "hi" ).lower:
        await message_trigger.channel.send("What?")

client.run(os.getenv("TOKEN"))

















