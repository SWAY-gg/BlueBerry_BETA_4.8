# Discod Module
import discord
from discord.ext import commands

# Installed modules
import nekos
import asyncio

# Class Nsfw
class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# On ready + check nsfw channel
    @commands.Cog.listener()
    async def on_ready(self):
        pass

    async def send(self, ctx, argument = None):
        if ctx.channel.is_nsfw():
            rnek = nekos.img(argument)
            emb = discord.Embed(color=0x00ffff)
            emb.set_image(url=rnek)

            await ctx.send(embed=emb)
        else:
            msg = await ctx.send(
                embed=discord.Embed(
                    description='**Не думаю, что это подходящий канал для такого контента...**', 
                    color=0x00ffff))
            await ctx.message.add_reaction('🔞')
            await asyncio.sleep(5)
            await msg.delete()

# Nsfw command 1
    @commands.command(name = "Pussy", aliases = ["pussy"])
    async def command_pussy(self, ctx):
        await self.send(ctx, 'pussy')

# Nsfw command 2
    @commands.command(name = "Hentai", aliases = ["hentai"])
    async def command_hentai(self, ctx):
        await self.send(ctx, 'hentai')

# Nsfw command 3
    @commands.command(name = "Kuni", aliases = ["kuni"])
    async def command_kuni(self, ctx):
        await self.send(ctx, 'kuni')

# Nsfw command 4
    @commands.command(name = "Anal", aliases = ["anal"])
    async def command_anal(self, ctx):
        await self.send(ctx, 'anal')

# Nsfw command 5
    @commands.command(name = "Tits", aliases = ["tits"])
    async def command_tits(self, ctx):
        await self.send(ctx, 'tits')

def setup(bot):
    bot.add_cog(Nsfw(bot))