import discord 
from discord import Embed
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()
mudae = "React with any emoji to claim!"

def message_contains(message, text):
    return text in message.content or any(embed_contains(embed, text) for embed in message.embeds)

def embed_contains(embed, text):
    return (text in embed.description
         )
class data:
    def __init__(self,content,timeS,author):
      self.content = content
      self.timeStamp = timeS
      self.author = author
    def __repr__(self):
      return f'content: {self.content} time: {self.timeStamp} author: {self.author}'
@client.event
async def on_ready():
  print("Welcome, {0.user}".format(client))  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.author.bot and len(message.embeds) != 0:
    if(embed_contains(message.embeds[0],mudae)):
      await message.add_reaction("\N{GRINNING FACE}")
    
keep_alive()
client.run(os.getenv('TOKEN'))

