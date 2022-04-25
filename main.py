import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import random
from keep_alive import keep_alive
from fifteen import FifteenAPI
from discord import FFmpegPCMAudio
import json
import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Exige400()",
  database="main"
)
cursor = db.cursor()
#^ basic imports for other features of discord.py and python ^
tts_api = FifteenAPI()
quotes = [
	"Very good! You are now in possession of the Aperture Science Handheld Portal Device.",
	"These intra dimensional gates have proven to be completely safe.",
	"Do not submerge The Device in liquid, even partially.",
	"Welcome to test chamber four.",
	"Good job! As part of a required test protocol, we will stop enhancing the truth in three... Two... One."
]
talkabout = [
    "What's the spiciest thing you've ever eaten?",
    "What's the best meal you've ever had?",
    "What's your favorite pickup line?",
    "What would you do with a million dollars?",
    "What's your dream job?",
    "What's your least favorite chore?",
    "If you could travel anywhere in the world, where would you go and why?",
    "What superpower would you want?",
    "If you won the lottery, what's the first thing you would buy?",
    "If you could only eat one meal for the rest of your life, what would it be?",
    "If you were trapped on an island and you could only bring three things with you, what would you take?",
    "What's your favorite movie ever?",
    "Who would play you in a movie about your life and what would the movie be called?",
    "If a genie offered you three wishes, what would you ask for?",
    "What's your favorite ice cream flavor?",
    "If you could have dinner with someone, living or dead, who would you invite and why?",
    "Who is your role model?",
    "What's your idea of a perfect day?"
]

bot = discord.Client()

bot = commands.Bot(command_prefix = 'gla ') #put your own prefix here

@bot.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@bot.command()
async def quote(ctx):
	randomquote = random.randint(0, 3)
	await ctx.send(quotes[randomquote])
	#why does this not like me anymore
@bot.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+ member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")
@bot.command()
async def ban(ctx, member : discord.Member, reason = None):
    try:
        await member.ban(reason)
        await ctx.send(member.mention + "Hit the ban hammer a bit hard") #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the ban members permission!")
@bot.command()
async def shop(ctx):
    try:
        sql = "SELECT * FROM items ORDER BY id"
        mycursor.execute(sql)
        items = mycursor.fetchall()
        embed = ctx.embed = discord.Embed(title="Shop", description="Welcome to the shop!", color=0x00ff00)
        for i in items:
            ctx.embed.add_field(name=itemname[i], value=f"{description[i]}\n {price[i]}", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Something went wrong")
@bot.command()
async def whattotalkabout(ctx):
    rand = random.randint(0, 17)
    await ctx.send(f"You could talk about {talkabout[rand]}")
    allowed_mentions = discord.AllowedMentions(everyone = True)
    await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions)
@bot.command()
async def fart(ctx):
    await ctx.send(file=discord.File(r"C:/Users/wrc02/Desktop/Coding/Glados/fart-with-reverb.mp3"))
@bot.command()
async def say(ctx, text):
    response = tts_api.save_to_file("GLaDOS", text)
    assert response["status"] == "OK"
    assert response["filename"] != None  # this is a generated filename of TTS file
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio(response["filename"])
    player = voice.play(source)
    time.sleep(5)
    await ctx.guild.voice_client.disconnect()
    time.sleep(5)
    os.remove(response["filename"])
keep_alive()
bot.run("OTU3MzI5MzI0OTkyNzU3ODcx.Yj9MaQ.ol9IDa4fD6kX3sSeLBGNHq-CTI0") #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value.