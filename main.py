import discord
import os


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
my_secret = os.environ['TOKEN']
gearchannel_id = 1028398902610776184
matches = ["https://www.willhaben.at", "ebay.at", "ebay.de","ebay.com"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(x in message.content for x in matches):
        gearchannel = client.get_channel(gearchannel_id)
        await gearchannel.send(message.content)
        #await message.channel.send('ich will!')

client.run(my_secret)