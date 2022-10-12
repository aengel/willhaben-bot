import discord
import os


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'https://www.willhaben.at' in message.content:
        gearchannel = client.get_channel(1028398902610776184)
        await gearchannel.send(message.content)
        #await message.channel.send('ich will!')

client.run(my_secret)