import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola! soy un bot {bot.user}!')

@bot.command()
async def check(ctx):
    nombre = "viuda negra"
    lugar = "campos de cultivo"
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await ctx.send(file_name)
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
            await ctx.send(f"esta araña llamada {nombre} se encuentra en {lugar}")
    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("TOKEN")
