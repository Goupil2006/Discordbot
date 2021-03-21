import discord
import os
import wikipedia

client = discord.Client()
wikipedia.set_lang("en")

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(messege):
  if messege.author == client.user:
    return
  thepadge = wikipedia.random(pages=1)
  ausgabe =  wikipedia.page(thepadge).title + "\n" + wikipedia.page(thepadge).content + "\n" + wikipedia.page(thepadge).url
  while len(ausgabe) > 2000:
    thepadge = wikipedia.random(pages=1)
    ausgabe =  wikipedia.page(thepadge).title + "\n" + wikipedia.page(thepadge).content + "\n" + wikipedia.page(thepadge).url

  if messege.content.startswith('$wiki'):
    await messege.channel.send(ausgabe)

client.run(os.getenv('Token'))
