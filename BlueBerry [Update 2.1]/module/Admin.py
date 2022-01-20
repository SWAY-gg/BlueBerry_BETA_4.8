# Discod Module
import discord
from discord.ext import commands

# Installed modules
import asyncio
import traceback

# Class Admin
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Bot Activity Type
    @commands.Cog.listener()
    async def on_ready(self):
        while True: 
            guilds_count = len(self.bot.guilds)
            await self.bot.change_presence(status = discord.Status.idle, activity=discord.Game (name=f"BETA 4.8 | >help"))
            await asyncio.sleep(15)
            await self.bot.change_presence(status = discord.Status.idle, activity=discord.Game (name=f"Серверов: {guilds_count}"))
            await asyncio.sleep(15)

# Say
    @commands.command(name = "Say", aliases = ["say"])
    @commands.has_permissions(administrator = True)
    async def command_say(self, ctx, *, msg: str):
        await ctx.message.delete()
        values = msg.split(" ")

        table = {
            "aqua": 0x00ffff,
        }

        t = ""
        description = ""
        color = discord.Color.default()

        toggle = ""

        for i in values:
            if i == '/t':
                toggle = "T"
            elif i == '/d':
                toggle = "D"
            elif i == '/c':
                toggle = "C"
            else:
                if toggle == "T":
                    t += f"{i} "
                elif toggle == "C":
                    try:
                        lox: str = str(i).strip()
                        color = table[lox]
                    except:
                        color = 0
                else:
                    description += f"{i} "

        await ctx.send(embed=discord.Embed(title=t, description=description, color=color)) 

# Member banreom guild
    @commands.command(name = "Ban", aliases = ["ban"])
    @commands.has_permissions(ban_members=True)
    async def command_ban(self, ctx, user: discord.Member = None, *, reason="None"):
        if user == self.bot.user: return await ctx.send(
            embed = discord.Embed(
                title = ":x: Извините, Произола ошибка\n\n:o: Вы не можете этого сделать!\n✅ Решение: Используйте команду по назначению!",
                color = 0xff0000))

        if user == ctx.author: return await ctx.send(
            embed = discord.Embed(
                    title = ":x: Извините, Произола ошибка\n\n:o: Вы не можете забанить себя!\n✅ Решение: Используйте команду по назначению!",
                    color = 0xff0000))
        
        if user.top_role >= ctx.author.top_role:
            await ctx.send(
                embed = discord.Embed(
                        title = ":x: Извините, Произола ошибка!\n\n",
                        description = f":o: **У {user.mention} роль выше или равна вашей\n✅ Решение: Сообщите создатель/модератеру сервера об данной ситуации!**",
                        color = 0xff0000))
            return await user.send(
                embed=discord.Embed(
                    title = ":x: Пользователь пытался вас забанить",
                    description = (
                        f":o:** Пользователь {ctx.author.mention} пытался вас забанить с сервера ``{ctx.author.guild}``. \nID Пользователя: ``{ctx.author.id}`` \nПолное имя пользователя: ``{ctx.author.name}#{ctx.author.discriminator}``\n"
                        f"✅ Решение: Сообщите создатель/модератеру сервера об данной ситуации!**"),
                        color = 0x00ff00))
        if user:
            try:
                await user.ban(reason=f"{ctx.author}, reason: {reason}")   

                dis  = "Готово!"
                dis2 = f"**Пользователь: {user.mention} забанен!\nАдмин/Модератор: <@{ctx.author.id}>**"

                if reason != "None":
                    dis2 += f"Причина: ``{reason}``!**\n"
                
                await ctx.send(
                    embed = discord.Embed(
                        title = dis,
                        description = dis2,
                        color = 0x00ff00))

            except discord.Forbidden: return await ctx.send(
                embed = discord.Embed(
                    title= ":x: Извините, Произола ошибка",
                    description='**:o: **Не удалось забанить пользователя.\n\nОтсутстуют права: `Банить участников`**',
                    color = 0xff0000))

# Member ban on HackBan
    @commands.command(name = "HBan", aliases = ["HBAN"])
    @commands.has_permissions(administrator = True)
    async def command_hackban(self, ctx, user_id: int = None, *, reason="None"):
        if user_id == self.bot.user.id: return await ctx.send(
            embed = discord.Embed(
                title = ":x: Извините, Произола ошибка\n\n:o: Вы не можете этого сделать!\n✅ Решение: Используйте команду по назначению!",
                color = 0xff0000))

        if user_id == ctx.author.id: return await ctx.send(
            embed = discord.Embed(
                    title = ":x: Извините, Произола ошибка\n\n:o: Вы не можете забанить себя!\n✅ Решение: Используйте команду по назначению!",
                    color = 0xff0000))
        if user_id:
            try:
                user = await self.bot.fetch_user(user_id)
                await ctx.guild.ban(user, reason=f"{ctx.author}, reason: {reason}")

                dis  = "HackBan | Готово!"
                dis2 = f"**Пользователь: <@!{user.id}> забанен!\nАдмин/Модератор: <@{ctx.author.id}>**"

                if reason != "None":
                    dis2 += f"\n **Причина: ``{reason}``!**\n"
                
                await ctx.send(
                    embed = discord.Embed(
                        title = dis,
                        description = dis2,
                        color = 0x00ff00))

            except discord.Forbidden: return await ctx.send(
                embed = discord.Embed(
                    title= ":x: Извините, Произола ошибка",
                    description='**:o: **Не удалось забанить пользователя.\n\nОтсутстуют права: `Банить участников`**',
                    color = 0xff0000))

# Clear commad
    @commands.command(name = "Clear", aliases = ["clear"])
    @commands.has_permissions(manage_messages = True)
    async def command_clear(self, ctx, amount: int):

        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)
        await ctx.send(
            embed=discord.Embed(
                description=f'**✅ Удалено {amount} сообщений.**',
                color=0x00ffff),
                delete_after = 5)

    @command_clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                embed=discord.Embed(
                    description=f'**У вас нет прав для использования данной команды!**',
                    color=0xff0000))

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                description=f'**Обязательно укажите количевство сообщений!**',
                color=0xff0000))

# Commad error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if hasattr(ctx.command, 'on_error'):
            return
        
        error = getattr(exception, 'original', exception)

        embed = discord.Embed(
            title = "**:x: Извините, Произола ошибка\n\n:o: Команда не найдена!\n✅ Решение: Используйте Команду ``>help``**",
            color = 0xff0000)
            
        embed.description = f"**Ошибки:**```{error}```"
        embed.set_footer(
                text=f'{self.bot.user.name}#{self.bot.user.discriminator} | © 2021 Все права защищены!',
                icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_error(self, ctx, event, *args, **kwargs):
        embed = discord.Embed(
            title=f"**:x: Извините, Произола ошибка\n\n:o: У вас не достаточно прав!\n✅ Решение: Обратитесь к Администрации!**",
            color=0xff0000)

        embed.description = f"**Ошибки:**```{traceback.format_exc()}```"
        embed.set_footer(
                text=f'{self.bot.user.name}#{self.bot.user.discriminator} | © 2021 Все права защищены!',
                icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))