# Discod Module
import discord
from discord.ext import commands

# Installed modules
import random
import textwrap
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw

# Class Fan
class Fan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Ball
    @commands.command(name = "Ball", aliases = ["ball"])
    async def command_ball(self, ctx, arg):
        message = ["Да", "Нет", "Возможно", "Точно нет!", "Точно да!"]
        s = random.choice(message)

        await ctx.send(
            embed=discord.Embed(
                description=f'**:crystal_ball: Знаки говорят:** {s}',
                color=0x00ffff))

    @command_ball.error
    async def ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                embed=discord.Embed(
                    description=f'Пожалуйста, укажите сообщение.', 
                    color=0x00ffff))

# Test IQ
    @commands.command(name = "IQ", aliases = ["iq"])
    async def command_iq(self, ctx):
        r = random.randint(0, 310) 
        await ctx.send(
            embed = discord.Embed(
                description=f"**{ctx.author.mention} Поздравляю, ваш IQ равен: {r}**",
                color=0x00ffff))

# Avatar user
    @commands.command(name = "Avatar", aliases = ["avatar"])
    async def command_avatar(self, ctx, member : discord.Member = None):
        user = ctx.message.author if (member == None) else member

        PNG = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        JPEG = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.jpeg?size=1024".format(user)

        embed = discord.Embed(
            title = "**Ну разве не милашка?**",
            description = f"**Скачать: [PNG]({PNG}) | [JPEG]({JPEG})**",
            color = 0x00ffff)

        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)       

# Frezko Inage
    @commands.command(name = "Frezko", aliases = ["frezko"])
    async def command_frezko(self, ctx, *, msg: str):

        base = Image.open("./sorce/Images/Fresko.jpg") 
        draw = ImageDraw.Draw(base)
        lines = textwrap.wrap(msg, width=25)

        fnt = ImageFont.truetype("./sorce/Fonts/Roboto-Regular.ttf", 30)

        image_width, image_height = (base.width - 250, base.height - 45)
        font_width, font_height = fnt.getsize(msg)
        text_y = (image_height - font_height * len(lines)) / 2
        
        for line in lines:
            font_width, font_height = fnt.getsize(line)
            text_x = (image_width - font_width) / 2

            draw.text((text_x, text_y), line, (0, 0, 0), fnt)
            text_y += font_height

        base.save('./sorce/Pillow/Frezko1.png')

        await ctx.send(file = discord.File(fp = './sorce/Pillow/Frezko1.png'))

def setup(bot):
    bot.add_cog(Fan(bot))