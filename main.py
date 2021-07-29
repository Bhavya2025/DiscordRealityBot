#Import Discord Package in terminal py -3 -m pip install -U discord.py
import discord
from discord.ext import commands
from keep_alive import keep_alive
#Client (bot)
client = commands.Bot(command_prefix = 'r ')

fileBulb = discord.File("bulb.gif" )
fileWG = discord.File("WG.gif")
fileRock = discord.File("rock.gif" )
fileOca = discord.File("ocacity.gif")
fileBday = discord.File("PremBirthday.mp4")

@client.event
async def on_ready():
    global general_channel
    general_channel = client.get_channel(865595211371511818)
    await general_channel.send("bot started :)",delete_after = 5)

@client.command()
async def bday(ctx):
  await ctx.channel.send(file = fileBday)
  await ctx.channel.send(f"{ctx.author.mention} wishes you happy birthday ") 
   

@client.command()
async def dance(ctx,member: discord.Member = None):
    if member is None:
     member = ctx.author

    if(member.id == 707273608455651349): #BulbCheck
        await  ctx.channel.send(file=fileBulb)
   
    if(member.id == 749881509502255126):  #Rock_EhCheck
        await ctx.channel.send(file=fileRock)
    
    if(member.id == 685425922748448820):  #OcacityCheck
        await  ctx.channel.send(file=fileOca)
    
    if(member.id == 765411940561321995): #WG check
        await  ctx.channel.send(file=fileWG)

@client.command()
async def dm(ctx,member:discord.Member):
  await ctx.send("what do you want to say")
  def check(m):
    return m.author.id == ctx.author.id
  message = await client.wait_for("message",check=check)

  await ctx .send(f"sent message to {member}",)

  await member.send(f"{ctx.author.mention} Has a message for you:\n {message.content}")
@client.command()
@commands.has_role("[OWNERs]")

async def clear(ctx,amout=5):
    if(amout > 100):
        await ctx.send("Max msgs deleting limit exceded",delete_after = 3)
        return
    else:
        await ctx.channel.purge(limit = amout) 
        await ctx.send(f'{amout} messages Cleared by {ctx.author.mention}',delete_after = 4)
    
   
    
keep_alive()
client.run("ODY3NjM5MjY2MzMzODE4OTAx.YPkCCQ.XS68UzPtS7karc8ncsLNyTD-Hxk")