import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="")

f = open("rules.io","r")
rules = f.readlines()
f.close()

fLink = open("server.io","r")
server_link = fLink.readlines()
fLink.close()

pyCommand = ["It is in built python command it will print given argument to screen: ```Command : \n print('Hello world') \n Output : \n  Hello world ```"]

@client.event
async def on_ready():
    print("Bot is ready")

## Rules
@client.command()
async def rule(ctx,*,number=1):
    await ctx.send(rules[int(number)-1])

##clear message
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit = amount)


##Invite Link
@client.command()
async def invite_link(ctx,*,number=1):
    await ctx.send(server_link[int(number)-1])


##Ping command
@client.command()
async def ping(ctx,*,member : discord.Member):
    await ctx.send(member)











#___________________________________Filtered Word_______________________________#
#_______________________________________________________________________________#

filteredWords = ["fuck","f u c k","f*uck","gay","stfu","puta","f*ck", "putain", "pussy", "kill yourself", "suicide you", "porn", "p*rn", "sex", "xxx", "i'm hot", "im hot", "im naked", "i'm naked", "xnxx", "xvideos", "naughty america", "riley reid", "badass", "bastard", "bitch", "cock", "guarrasdel", "http://discord.gg", "http://discord.com/invite", "https://discord.com/invite", "iplogger.org", "dansmovies", "forhertube", "lesbian8", "hot female", "hot girls", "hot sister", "dick", "suck my", "cked so hard", "i wish you die", "please die", "your useless", "program dream suck", "pd suck", "programdream suck", "dreamprogram suck", "pdream suck", "programd suck", "anic17 suck", "tim suck", "nick_z suck", "nina suck", "timmy suck", "moderation bot suck", "moderator bot suck", "suck anic17", "uck tim", "uck nick_z", "uck nina", "uck timmy", "uck moderation bot", "uck moderator bot" "this server is trash", "this server is shit", "this server is pure trash", "this server is pure shit", "you have low iq", "wheres your dignity", "your iq is low", "is your iq 0", "i will hack the server", "ill hack the server", "i hack the server", "join the server", "join this server", "please join server", "boobs", "ptain"]



@client.event
async def on_message(msg):
    author = msg.author
    authorid = msg.author.id
    print ("@{} user sent a message. (id: {})".format(author, authorid))
    for word in filteredWords:
        if word in msg.content.lower():
            await msg.delete()
    await client.process_commands(msg)



#___________________________________end filtered________________________________#
#_______________________________________________________________________________#




#___________________________________hi-hello____________________________________#
#_______________________________________________________________________________#


@client.command()
async def Hi(ctx):
    await ctx.send("Hello 🔥")

@client.command()
async def hi(ctx):
    await ctx.send("Hello ❤️")

@client.command()
async def HI(ctx):
    await ctx.send("Hello ✨")

@client.command()
async def Hello(ctx):
    await ctx.send("Hi 😊")

@client.command()
async def HELLO(ctx):
    await ctx.send("Hi 🎃")

@client.command()
async def hello(ctx):
    await ctx.send("Hi 😇")


#___________________________________end hi-hello________________________________#
#_______________________________________________________________________________#












#__________________________________python_help__________________________________#
#_______________________________________________________________________________#

@client.command()
async def python(ctx,*,commandLine):
    if commandLine == "print()":
        await ctx.send(pyCommand[0])

#__________________________________python_help_end______________________________#
#_______________________________________________________________________________#















#__________________________________scripting____________________________________#
#_______________________________________________________________________________#


@client.command()
async def var(ctx,*,commandLine):
    symbol = commandLine
    symbolEqu = symbol.find("=")
    varName = symbol[0:symbolEqu]
    fileIo = open((varName+".txt"),"w")
    fileIo.write(symbol[symbolEqu+1:len(symbol)])
    fileIo.close()

@client.command()
async def echo(ctx,*,commandLine):
    try:
        fileIo = open((commandLine+".txt"),"r")
        varValue = fileIo.read()
        fileIo.close()

        await ctx.send(varValue)
    except:
        await ctx.send(commandLine)


#__________________________________scripting___end______________________________#
#_______________________________________________________________________________#
















#_______________________________________________tic-tac-toe_game__________________________#
#_________________________________________________________________________________________#

@client.command()
async def tik(ctx):
    await ctx.send("tac 🍂")

@client.command()
async def Tik(ctx):
    await ctx.send("tac 🍂")

@client.command()
async def Tac(ctx):
    await ctx.send("toe 🍁")

@client.command()
async def tac(ctx):
    await ctx.send("toe 🍁")


@client.command()
async def toe(ctx):
    await ctx.send("tik 💕")


@client.command()
async def Toe(ctx):
    await ctx.send("tik 💕")

#_______________________________________________tic-tac-toe_end___________________________#
#_________________________________________________________________________________________#


#_________________________________Random__________________________________________________#
#_________________________________________________________________________________________#

@client.command()
async def randint(ctx,*,range=1):
    randIntt = random.randint(0,range)
    await ctx.send(randIntt)

#______________________________end-random________________________________________________#
#________________________________________________________________________________________#

# Replace TOKEN by your Discord bot token
client.run("TOKEN")
