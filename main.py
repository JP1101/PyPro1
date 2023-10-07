import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion como {bot.user}')

@bot.command()
async def add(ctx, number1:float, number2:float):
    await ctx.send(number1 + number2)

@bot.command()
async def subtract(ctx, number1:float, number2:float):
    await ctx.send(number1 - number2)

@bot.command()
async def multiply(ctx, number1:float, number2:float):
    await ctx.send(number1 * number2)

@bot.command()
async def split(ctx, number1: float, number2: float):
    await ctx.send(number1 / number2)


equationslist = {
    "$add ",
    "$subtract ",
    "$multiply ",
    "$split "
}
@bot.command()
async def equations(ctx):
    await ctx.send(f"These are the equations that you can do with this bot {equationslist} ")

bot.run("Token")
