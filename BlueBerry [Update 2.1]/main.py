# Discod Module
import discord
from discord.ext import commands

# Installed modules
import os
import time
import asyncio
from colorama import Fore, Back, Style
from datetime import datetime, timedelta, timezone

# Setting folder
import setting.config
from setting.config import bot

# Cliear console [Linux]
os.system("clear")

# Cosg list
cogs = [
    "Information",
    "Support",
    "Reload",
    "Admin",
    "Nsfw",
    "Fan"
]

# Color console
G  = Fore.CYAN  + "[" + Fore.GREEN + "+" + Fore.CYAN  + "]" + Fore.WHITE
B  = Fore.CYAN  + "[" + Fore.RED + "-" + Fore.CYAN  + "]" + Fore.WHITE
N  = Fore.CYAN  + "[" + Fore.CYAN + "+" + Fore.CYAN  + "]" + Fore.WHITE
A  = Fore.CYAN  + "[" + Fore.BLUE + "WARNING" + Fore.CYAN  + "]" + Fore.WHITE
T  = Fore.CYAN  + "[" + Fore.BLUE + "Time/Вермя" + Fore.CYAN  + "]" + Fore.WHITE
Y  = Fore.CYAN  + "[" + Fore.YELLOW + "OK" + Fore.CYAN  + "]" + Fore.WHITE

# Time
Time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

# Class Main 
class Main(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Client setting
client = Main(
    help_command = None,
    command_prefix = bot["PREFIX"],
    intents = discord.Intents.all())

# On ready event
@client.event	
async def on_ready():
	print(f"{N} Main file loaded\n")
	print(f"{G} {client.user.name} - Online")
	print(f"{G} discord.py - {discord.__version__}")
	print(f"{T} - {Time}")
	print("-----------------------------\n")

# Reload bot
@client.command()
@commands.is_owner()
async def restart(ctx, *, reconnect=True):
    await ctx.send(
        embed = discord.Embed(
            title = "Attention!",
            description = (f"**Bot {client.user.name} is Reload**"),
            color = 0x00ffff))
    try:
        await client.logout()

    except Exception as e:
        print(f"{e}")
        return

    finally:
        os.system("python3.8 main.py")

# Bot off
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(
        embed = discord.Embed(
            title = "Attention!",
            description = (f"**Bot {client.user.name} is Shutdown**"),
            color = 0x00ffff))
    try:
        await client.logout()

    except Exception as e:
        print(f"{e}")
        return

# Init main
if __name__ == "__main__":
    for extension in cogs:
        cog = f"module.{extension}"
        try:
            client.load_extension(cog)
        except Exception as e:
            print(e)

client.run(bot["TOKEN"])