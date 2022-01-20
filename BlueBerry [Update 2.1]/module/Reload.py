# Discod module
import discord
from discord.ext import commands

# Installed modules
import time
import asyncio
from colorama import Fore, Back, Style
from datetime import datetime, timedelta, timezone

# Color console
G  = Fore.CYAN  + "[" + Fore.GREEN + "+" + Fore.CYAN  + "]" + Fore.WHITE
B  = Fore.CYAN  + "[" + Fore.RED + "-" + Fore.CYAN  + "]" + Fore.WHITE
N  = Fore.CYAN  + "[" + Fore.CYAN + "○" + Fore.CYAN  + "]" + Fore.WHITE
A  = Fore.CYAN  + "[" + Fore.BLUE + "WARNING" + Fore.CYAN  + "]" + Fore.WHITE
T  = Fore.CYAN  + "[" + Fore.BLUE + "Time/Вермя" + Fore.CYAN  + "]" + Fore.WHITE
Y  = Fore.CYAN  + "[" + Fore.YELLOW + "OK" + Fore.CYAN  + "]" + Fore.WHITE

# Time
Time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

# Class Reload 
class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Reload extension
    @commands.is_owner()
    @commands.command(name = "Reload", aliases = ["reload"])
    async def command_reload(self, ctx, extension):
        try:
            self.bot.reload_extension(f"module.{extension}")
            print(f"{A} Modul {extension} start reload")
            await asyncio.sleep(0.1)
            print(f"{B} Modul {extension} has OFF")
            await asyncio.sleep(0.1)
            print(f"{G} Modul {extension} has ON")
            await asyncio.sleep(0.1)
            print(f"{Y} Modul {extension} has reload")
            print(f"{T} - {Time}")
            print("----------------------------- \n")

            await ctx.send(embed = discord.Embed(
                title = ":white_check_mark: Готово!",
                description = f"**<:module_reload:801016065000734740> Модуль [` {extension} `] перезагружен!**",
                color = 0x00ffff))

        except Exception as e:
            print(f"{A} Modul {extension} start reload")
            await asyncio.sleep(0.1)
            print(f"{B} Modul {extension} has not loaded")
            await asyncio.sleep(0.1)
            print(f"{B} Error: {e}")
            print(f"{T} - {Time}")
            print("----------------------------- \n")

            await ctx.send(embed = discord.Embed(
                title = ":x: Ошибка!",
                description =(
                    f"**<:module_extension:801016060349382687> Модуль [` {extension} `] не перезагружен!\n"
                    f"<:warning:797493218152677376> Причина: \n**"
                    f"```{e}``` \n"
                    ), color = 0x00ffff))

# Unload extension
    @commands.is_owner()
    @commands.command(name = "Unload", aliases = ["unload"])
    async def command_unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f"module.{extension}")
            print(f"{G} Modul {extension} has OFF")
            print(f"{T} - {Time}")
            print("----------------------------- \n")

            await ctx.send(embed = discord.Embed(
                title = "✅ Готово!",
                description = f"**<:module_unload:801016064380895232> Модуль [` {extension} `] выгружен!**",
                color = 0x00ffff))

        except Exception as e:
            print(f"{B} Modul {extension} has not unaded")
            await asyncio.sleep(0.1)
            print(f"{B} Error: {e}")
            print(f"{T} - {Time}")
            print("----------------------------- \n")

            await ctx.send(embed = discord.Embed(
                title = ":x: Ошибка!",
                description =(
                    f"**<:module_extension:801016060349382687> Модуль [` {extension} `] не выгружен!\n"
                    f"<:warning:797493218152677376> Причина: \n**"
                    f"```{e}``` \n"
                    ), color = 0x00ffff))

# Load extension
    @commands.is_owner()
    @commands.command(name = "Load", aliases = ["load"])
    async def command_load(self, ctx, extension):
        try:
            self.bot.load_extension(f"module.{extension}")
            print(f"{G} Modul {extension} has on")
            print(f"{T} - {Time}")
            print("----------------------------- \n")

            await ctx.send(embed = discord.Embed(
                title = "✅ Готово!",
                description = f"**<:module_load:801016063638765568> Модуль [` {extension} `] загружен!**",
                color = 0x00ffff))

        except Exception as e:
            print(f"{B} Modul {extension} has not loaded")
            await asyncio.sleep(0.1)
            print(f"{B} Error: {e}")
            print(f"{T} - {Time}")
            print("----------------------------- \n")

            await ctx.send(embed = discord.Embed(
                title = ":x: Ошибка!",
                description =(
                    f"**<:module_extension:801016060349382687> Модуль [` {extension} `] не загружен!\n"
                    f"<:warning:797493218152677376> Причина: \n**"
                    f"```{e}``` \n"
                    ), color = 0x00ffff))

def setup(bot):
    bot.add_cog(Reload(bot))