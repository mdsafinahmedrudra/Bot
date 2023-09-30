import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.presences = True  # Enable presence intent
bot = commands.Bot(command_prefix='/', intents=intents)

# List of card image URLs
card_images = [
    "https://external-preview.redd.it/Jq4T6mnZU5_N3sYa4cxSdtoZlcOc57tE1xRYD4BCtWQ.jpg?auto=webp&s=1bd6e8986275a6f6f9feb1be8dde10c3f26ccd8b",
    "https://i.pinimg.com/736x/9e/9e/a4/9e9ea4b5246b3c97dede770892b47ac4.jpg",
    "https://i.redd.it/sgrcymz0ud0a1.png",
    "https://media.discordapp.net/attachments/1124371191768043590/1155776878360137758/29053950-5b7a-11ee-9e12-0b5864420975.webp?width=336&height=473",
    "https://media.discordapp.net/attachments/1135544849190367356/1155778367405162516/1695629300160.jpg?width=336&height=473",
    "https://media.discordapp.net/attachments/1135544849190367356/1155778401106399363/1695629207055.jpg?width=336&height=473"
]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    
    try:
        await bot.change_presence(activity=discord.Game(name='eFootball'))
        print('Bot status set.')
    except Exception as e:
        print(f'Error setting status: {e}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        if 'card' in message.content.lower():
            await send_random_card(message.channel)
        elif 'coinflip' in message.content.lower():
            await coinflip(message.channel)

        elif 'timeout' in message.content.lower():
            await message.channel.send('Shh kiddo!!')

        elif 'kill' in message.content.lower():
            await message.channel.send('Shh kiddo!!')

        elif 'siuu' in message.content.lower():
            await send_siuu_gif(message.channel)

        elif 'messi' in message.content.lower():
            await send_messi_gif(message.channel)

        elif 'vipul' in message.content.lower():
            await send_vipul_gif(message.channel)

    await bot.process_commands(message)

async def send_random_card(channel):
    random_card = random.choice(card_images)
    await channel.send(random_card)

async def coinflip(channel):
    result = random.choice(['Heads', 'Tails'])
    await channel.send(f'Coin flip: {result}')



@bot.command()
async def coinflip(ctx):
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(f'Coin flip: {result}')


# Function to send the "siuu" GIF
async def send_siuu_gif(channel):
    siuu_gif_url = 'https://media.giphy.com/media/xT1XGVp95GDPgFYmUE/giphy.gif'
    await channel.send(siuu_gif_url)


async def send_vipul_gif(channel):
    vipul_gif_url = 'https://i.ibb.co/WyNRFPS/65182e769de7a551068135.gif'
    await channel.send(vipul_gif_url)


async def send_messi_gif(channel):
    messi_gif_url = 'https://media.giphy.com/media/XcAskcEyoyld03drLt/giphy.gif'
    await channel.send(messi_gif_url)

@bot.command()
async def randommeme(ctx):
    # You can add code here to fetch a random meme from a source (API, website, etc.)
    await ctx.send("Here's a random meme!")
