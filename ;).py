import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('lol')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "哈囉" or message.content == "嗨":
        await message.channel.send('Hi')

    if message.content.startswith('!'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send(tmp[1])

client.run("MTA5ODg0OTU0MDc5MjEzNTY5MA.G1mnQ9.ykT7FA0GlX0gvfWSp5RHvOSRbgUu9N_yN5Asic")