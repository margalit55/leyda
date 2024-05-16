import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот я тебе помогу сортировкой мусора {bot.user}!')

@bot.command()
async def waste_sorting (ctx):
    await ctx.send('''желтый – пластик;
зеленый – несортированные коммунальные отходы;
оранжевый – опасные отходы;
синий – макулатура;
красный – стекло;
серый – электрооборудование, вышедшее из строя.
" * count_heh''')
    print(margo)
    
bot.run("")