import discord  
client = discord.Client()


@client.event

async def on_ready():
    print("The bot is logged in as {0.user}".format(client))


 