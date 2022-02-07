import discord
from discord.ext import commands
from func import game as g

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

lword = None

@client.event
async def on_ready():
    print("Ready!")
    game = discord.Game(name = "끝말잇기 준비중")
    await client.change_presence(activity = game)

@client.command(aliases=["초기화"])
async def startgame(ctx):
    g.reset_game()

@client.command(aliases=["단어"])
async def w(ctx, *, word):
    game = g.word_relay(word)

    res = game.choose_word()
    if res == None:
        await ctx.send("더이상 단어가 없어요..")
    else:
        lastword = res
        g.add_word(word)
        await ctx.send(lastword)

client.run("YOUR BOT TOKEN")