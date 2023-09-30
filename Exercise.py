import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def createPassword(ctx, passwordCharacters = 8):
    await ctx.send("la contraseña generada es" + " " + gen_pass(passwordCharacters))

@bot.command()
async def list(ctx, wordtocopy):
    await ctx.send(wordtocopy)

bot.run("MTE1NjM4NTIwMTE3NDM2NDIwMQ.G8aqdg.oKL0uJoteWe7srZsgfkEzomhZYrrFfe7VLk63Y")
