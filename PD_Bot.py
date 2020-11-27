import requests
from PIL import Image
import discord
import random
from io import BytesIO
from discord.ext import commands

#Files Reading Io

f = open("dataBase\\rules.io","r")
rules = f.readlines()
f.close()

fLink = open("dataBase\\server.io","r")
server_link = fLink.readlines()
fLink.close()

with open("dataBase\\filterWord.io","r") as filterwr:
    filteredWords = filterwr.read().split('\n')
    filterwr.close()

warningWords = open("dataBase\\warningWord.io","r").read().split('\n')

greetingWords = ["Hey","Hello","Hi"]

#end File Reading

client = commands.Bot(command_prefix="<<")


pyCommand = ["It is in built python command it will print given argument to screen: ```Command : \n print('Hello world') \n Output : \n  Hello world ```"]

@client.event
async def on_ready():
    print("Bot is ready")

## Rules
@client.command()
async def rule(ctx,*,number=1):
    try:
        await ctx.send(rules[int(number)-1])
    except:
        await ctx.send("Program Dream have only 8 rules")

##clear message
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=1):
    try:
        await ctx.channel.purge(limit = amount)
    except:
        pass

##Invite Link
@client.command()
async def invite_link(ctx,*,number=1):
    try:
        await ctx.send(server_link[int(number)-1])
    except:
        await ctx.send("I have only 4 invite link of Program Dream")



##Random Image
@client.command()
async def randomImage(ctx):
    try:
        response = requests.get('https://source.unsplash.com/random')
        img = Image.open(BytesIO(response.content))
        img.save('dataBase\\Images\\random.jpg')
        await ctx.send(file = discord.File("dataBase\\Images\\random.jpg"))

    except:
        await ctx.send("Now, no random Image Present")


@client.command()
async def randomNumber(ctx,*,rang=99999):
    try:
        randomNumber = random.randint(0,rang)
        await ctx.send(f"""Your random number Is : {randomNumber}""")
    
    except:
        await ctx.send(f"""Your Command Is Wrong xD""")





#___________________________________Filtered Word_______________________________#
#_______________________________________________________________________________#


@client.event
async def on_message(msg):
    try:
        for word in filteredWords:
            if word in msg.content.lower():
                await msg.delete()
                id = msg.author.id
                await msg.channel.send(f""":five: No racism, xenophobia, homophobia, etc.""")
                await msg.channel.send(f"""<@{id}> {warningWords[random.randint(0,len(warningWords)-1)]}""")
    except:
        pass

    if (msg.content[0:5].lower().find("hello") != -1):
        await msg.channel.send(f"""<@{msg.author.id}>   Hi 💕💕""")
    
    if (msg.content[0:2].lower().find("hi") != -1):
        await msg.channel.send(f"""<@{msg.author.id}>   Hello ✨✨""")
    
    if (msg.content[0:3].find("hey") != -1):
        await msg.channel.send(f"""<@{msg.author.id}>   What's up Dude 🎃🎃""")
    
    if (msg.content[0:4].lower().find("ping") != -1):
        await msg.channel.send(f"""<@{msg.author.id}>   :regional_indicator_p: :o2: :regional_indicator_n: :regional_indicator_g:  ✨💕""")
    
    if (msg.content[0:4].lower().find("pong") != -1):
        await msg.channel.send(f"""<@{msg.author.id}>   :regional_indicator_p: :regional_indicator_i: :regional_indicator_n: :regional_indicator_g:   🎃💕""")
        
    if (msg.content[0:12].find("$sendMessage") != -1):
        try:
            for i in range(0,int(msg.content[13:14])):
                await msg.channel.send(f"""{msg.content[15:len(msg.content)]}""")
        except:
            await msg.channel.send(f"""{msg.content[15:len(msg.content)]}""")

    
    await client.process_commands(msg)




#___________________________________end filtered________________________________#
#_______________________________________________________________________________#







#___________________________________Welcome_____________________________________#
#_______________________________________________________________________________#

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general": # We check to make sure we are sending the message in the general channel
            await channel.send_message(f"""Welcome to the server {member.mention}""")
    
    await client.process_commands(member)


#___________________________________end Welcome_________________________________#
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


# @client.command()
# async def var(ctx,*,commandLine):
#     symbol = commandLine
#     symbolEqu = symbol.find("=")
#     varName = symbol[0:symbolEqu]
#     fileIo = open((varName+".txt"),"w")
#     fileIo.write(symbol[symbolEqu+1:len(symbol)])
#     fileIo.close()

# @client.command()
# async def echo(ctx,*,commandLine):
#     try:
#         fileIo = open((commandLine+".txt"),"r")
#         varValue = fileIo.read()
#         fileIo.close()

#         await ctx.send(varValue)
#     except:
#         await ctx.send(commandLine)


#__________________________________scripting___end______________________________#
#_______________________________________________________________________________#
















#_______________________________________________tic-tac-toe_game__________________________#
#_________________________________________________________________________________________#



#_______________________________________________tic-tac-toe_end___________________________#
#_________________________________________________________________________________________#



client.run("NzcyMDMxNTQ1NjE5NTEzMzQ0.X50waA.BfwUpx4nyuG3ePmYX248i3BZL5E")
