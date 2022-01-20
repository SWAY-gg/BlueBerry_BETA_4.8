# Discod Module
import discord
from discord.ext import commands

# Installed modules
import psutil

# Bot invite Link url
invite_link = '[Add Bot](https://discord.com/oauth2/authorize?client_id=719739188131659878&scope=bot&permissions=8)'

# Class Information
class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

        self.process = psutil.Process()
        self.process.cpu_percent()
        self.startTime = 0

# Serverinfo
    @commands.command(name = "Serverinfo", aliases = ["serverinfo"])
    async def command_serverinfo(self, ctx):
        members = ctx.guild.members
        online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
        idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
        dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))

        offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))

        allonline = online + idle + dnd

        allchannels = len(ctx.guild.channels)
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)

        embed = discord.Embed(
            description =f"**Информация о сервере {ctx.guild.name}**",
            color = 0x00ffff)

        embed.add_field(name = "Основная информация:", value = (
            f"⏵ **Создатель сервера:** <@!{ctx.guild.owner.id}> \n"
            f"⏵ **Сервер создан:** `{ctx.guild.created_at.strftime('%d.%m.%Y')}` \n"
            f"⏵ **ID сервера:** `{ctx.guild.id}` \n"
            f"⏵ **Регион сервера:** `{ctx.guild.region}` \n"
            ), inline=False)

        embed.add_field(name = "Статистика по участникам:", value = (
            f"⏵ **Всего участников:** `{ctx.guild.member_count}` \n"
            f"⏵ **Онлайн:** `{allonline}`\n"
            f"⏵ **Оффлайн:** `{offline}`\n"
            ), inline=False)

        embed.add_field(name = "Статистика по каналам:", value = (
            f"⏵ **Всего каналов:** `{allchannels}` \n"
            f"⏵ **Текстовых каналов:** `{alltext}` \n"
            f"⏵ **Голосовых каналов:** `{allvoice}`\n"
            ), inline=False)

        embed.add_field(name = "Доп. Информация:", value = (
            f"⏵ **Уровень верефикации:** `{ctx.guild.verification_level}` \n"
            f"⏵ **Кол-во ролей:** `{allroles}` \n"
            # f"**Кол-во забаненых:** `{ctx.guild.ban}` \n"
            f"⏵ **Кол-во бустов:** `{ctx.guild.premium_subscription_count}` \n"   
            ), inline=False)

        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(
                text=f'{self.bot.user.name}#{self.bot.user.discriminator} | © 2021 Все права защищены!',
                icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

# USerinfo 
    @commands.command(name = "Userinfo", aliases = ["userinfo"])
    async def command_userinfo(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        l = []
        for i in user.roles:
            if i.name == '@everyone': pass
            else: l.append(i.mention)
            rols = ', '.join(l)

        if str(user.web_status) == 'online': online_stats = 'Онлайн (Веб)'
        elif str(user.web_status) == 'idle': online_stats = 'Отошел (Веб)'
        elif str(user.web_status) == 'dnd': online_stats = 'Не беспокоить (Веб)'

        elif str(user.mobile_status) == 'online': online_stats = 'Онлайн (Телефон)'
        elif str(user.mobile_status) == 'idle': online_stats = 'Отошел (Телефон)'
        elif str(user.mobile_status) == 'dnd': online_stats = 'Не беспокоить (Телефон)'

        elif str(user.status) == 'online': online_stats = 'Онлайн'
        elif str(user.status) == 'idle': online_stats = 'Отошел'
        elif str(user.status) == 'dnd': online_stats = 'Не беспокоить'
        elif str(user.status) == 'offline': online_stats = 'Оффлайн'

        if str(user.activity) != "ActivityType.custom":
            act = None
        else:
            act = user.activity
        
        if user in ctx.guild.premium_subscribers:
            premium = "Да"
        else:
            premium = "Нет"

        embed = discord.Embed(
            description = f"**Информация о {user.name}**",
            color = user.color)

        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name = "Основная информация:", value = (
            f"**⏵ Имя:** `{user}`\n"
            f"**⏵ Пинг:** {user.mention}\n"
            f"**⏵ ID Аккаунта:** `{user.id}`\n"), inline=False)

        embed.add_field(name = "Статистика:", value = (
            f"**⏵ Статус:** `{online_stats}`\n"
            f"**⏵ Буст сервера:** `{premium}`\n"
            f"**⏵ Кастомный cтатус:** `{act}`"), inline=False)

        embed.add_field(name = "Доп. Информация:", value = (
            f"**⏵ Зарегестрирован в Discord:** `{user.created_at.strftime('%d.%m.%Y')}`\n"
            f"**⏵ Присоеденился на сервер:** `{user.joined_at.strftime('%d.%m.%Y')}`\n\n"

            f"**⏵ Топ роль:** {user.top_role.mention}\n\n" 
            f"**⏵ Все роли:** {rols}\n"), inline=False)

        embed.set_footer(
                text=f'{self.bot.user.name}#{self.bot.user.discriminator} | © 2021 Все права защищены!',
                icon_url=self.bot.user.avatar_url)
        
        await ctx.send(embed = embed)

# Bot info
    @commands.command(name = "Botinfo", aliases = ["botinfo"])
    async def command_botinfo(self, ctx, *, member: discord.Member = None):
        embed = discord.Embed(
            title = "BlueBerry - Информация об Боте",
            description = (
                f"**Хотите добавить бота?\nнажмите сюда -> {invite_link}**"), 
            color = 0x00ffff)

        ping = self.bot.latency
        
        ping_emoji = "🟩🔳🔳🔳🔳"
        ping_list = [
            {"ping": 0.00000000000000000, "emoji": "🟩🔳🔳🔳🔳"},
            {"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
            {"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
            {"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
            {"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
            {"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
            {"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}
        ]
        for ping_one in ping_list:
            if ping <= ping_one["ping"]:
                ping_emoji = ping_one["emoji"]
                break

        memory_usage = self.process.memory_full_info().uss / 1024 ** 2
        cpu_usage = self.process.cpu_percent() / psutil.cpu_count()

        embed.add_field(name ='Нагрузка:', value = f"**Пинг:** `{ping * 1000:.0f} ms`\n{ping_emoji}\n", inline = True)
        embed.add_field(name = "Система:", value = "**CPU:** `{0:.2f} %`\n**ОЗУ:** `{1:.2f} МБ`".format(cpu_usage, memory_usage), inline = True)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        embed.set_footer(
                text = f'{self.bot.user.name}#{self.bot.user.discriminator} | © 2021 Все права защищены!',
                icon_url = self.bot.user.avatar_url)

        await ctx.send(embed=embed)       

# Help command
    @commands.command(name = "Help", aliases = ["help"])
    async def command_help(self, ctx):
        embed = discord.Embed(
            title = f"Список все команда {self.bot.user.name}",
            # description = f"**Для подробной информации: `>info-<Команда>`**",
            color = 0x00ffff)


        embed.add_field(name = "Развлечение:", value = ("**` Avatar, Ball, Iq, Frezko `**"), inline = False)
        embed.add_field(name = "Информация:", value = ("**` Serverinfo, Botinfo, Userinfo, `**"), inline = False)

        embed.add_field(name = "Администрация:", value = ("**` Ban, HBan, Say, Clear `**"), inline = False)
        embed.add_field(name = "NSFW:", value = ("**` Hentai, Kuni, Pussy, Tits, Anal `**"), inline = False)

        embed.add_field(name = "Welcome:", value = ("**` Set-welcome, Set-role, Check-welcome, Check-role `**"), inline = False)
        embed.add_field(name = "Support:", value = ("**` FeedBack, Report `**"), inline = False)

        embed.add_field(name = "OSU! Official:", value = ("**` Osu! `**"), inline = False)

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Information(bot))