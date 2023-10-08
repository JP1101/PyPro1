  import discord
from discord.ext import commands
import os, random, requests

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

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

meme_list = [    
    "mem1.jpg",
    "mem2.jpg",
    "mem3.jpg",
    "mem4.jpg",
    "mem5.jpg",
    "mem6.jpg",
    "mem7.jpg       "
]

img_name = random.choice(meme_list)

@bot.command()
async def meme(ctx):
    img_name = random.choice(meme_list)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)



def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def duck(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)





bot.run("🤐")
