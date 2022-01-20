# Discod Module
import discord
from discord.ext import commands
from discord.ext.commands import Cog, BucketType, cooldown

# Server Url
server = '[Серверу Теx. Поддержки](https://discord.gg/CWsuHRadJX)'

#Class Support
class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Message "Bot join gouild"
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            color = 0x00ffff,
            title = "BlueBerry - Information!",
            description = (
                f"Доброго времени суток! \n\n"
                f"Вы получили это сообщение т.к на ваш сервер **{guild.name}** был добавлен BlueBerry! \n"
                f"Это чисто информативное сообщение, сделанное для того, чтобы вы знали немного больше о том, чем пользуетесь:)"))
            
        embed.add_field(name = "Полезная информация:", value = (
            f"Создатель бота - <@478036348562046986> \n"
            f"Справка по командам - `>info` \n"
            f"Префикс - `>` \n"))

        embed.set_footer(
                text=f'{self.bot.user.name}#{self.bot.user.discriminator} | © 2021 Все права защищены!',
                icon_url=self.bot.user.avatar_url)

        await guild.owner.send(embed=embed)

        channel = self.bot.get_channel(800953526855532564)
        emb = discord.Embed(
            color = 0x00ffff,
            title = f"Бот присоединился к серверу: {guild.name}",
            description = (
                f"**Информация о сервере:** \n"
                f"**Сервер -** `{guild.name}`` \n"
                f"**ID сервера -** `{guild.id}` \n"
                f"**Владелец сервера -** `{guild.owner}`"))

        await channel.send(embed=emb)

# Bag Report
    @commands.command(name = "Report", aliases = ["report"])
    @cooldown(1, 3600, BucketType.user)
    async def command_report(self, ctx, *, msg: str):
        await ctx.send(embed = discord.Embed(
            title = "Баг репорт отправлен!",
            description = f"**Спасибо за вашу поддержку, мы в скорем времени рассмотрим вашу заявку\n Так же вы можете присоеденится к {server}**",
            color = 0x00ffff))
        
        channel = self.bot.get_channel(800953582216019989)
        msg.split(" ")
        emb = discord.Embed(
            description = (
                f"⏵ **Bag-Report от `{ctx.message.author.name}` \n\n"
                f"{msg}**"),
            color = 0x00ffff)
        await channel.send(embed=emb)

# FeedBack
    @commands.command(name = "FeedBack", aliases = ["Feedback", "feedback"])
    @cooldown(1, 3600, BucketType.user)
    async def command_feedback(self, ctx, *, msg: str):
        await ctx.send(embed = discord.Embed(
            title = "Спасибо за ваш отзыв!",
            description = f"**Спасибо за вашу поддержку!\n Так же вы можете присоеденится к {server}**",
            color = 0x00ffff))

        channel = self.bot.get_channel(800953366863806508)
        msg.split(" ")
        emb = discord.Embed(
            description = (
                f"⏵ **FeedBack от `{ctx.message.author.name}` \n\n"
                f"{msg}**"),
            color = 0x00ffff)
        await channel.send(embed=emb)

def setup(bot):
    bot.add_cog(Support(bot))