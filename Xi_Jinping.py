import discord
from discord.ext import commands
import asyncio
import re

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

cagate = {}

conteggi_parole_canali = {}

try:
    with open('numcagate.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            user_id, count = line.strip().split(':')
            cagate[user_id] = int(count)
except FileNotFoundError:
    pass

@bot.command(name='depex', help="Depexa il coglione che lo merita.")
@commands.has_permissions(administrator=True) 
async def depex(ctx,member:discord.Member):    
    ruolo_id = 1215046884641738782
    ruolo = discord.utils.get(ctx.guild.roles, id=ruolo_id)
    if ctx.author.guild_permissions.administrator:
        await ctx.send(f"<@{member.id}> sta essendo depexato perchè ha la figa nel culo.")
        for role in member.roles:
            await member.remove_roles(role)
        await member.add_roles(ruolo)
        await ctx.send(f"<@{member.id}> ora è disabile.")
    else:
        await ctx.send("Dio negro non ho porcodio trovato il permesso ( diocane ).")

@bot.command(name='ping', help="Scrive Pong il coglione di Xi Jinping.")
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='negro', help="Ti insulta disabile.")
async def negro(ctx):
    await ctx.send('Frocio gay coglione 8========>')

@bot.command(name="bagno", help="Comando utile per Cristian che va in bagno ogni 60 secondi, questo comando tiene conto di ogni volta che sei andato in bagno.")
async def bagno(ctx):
    user_id = str(ctx.author.id)
    cagate[user_id] = cagate.get(user_id, 0) + 1

    with open("numcagate.txt", "w") as file:
        for user, count in cagate.items():
            file.write(f"{user}:{count}\n")

    await ctx.send(f"<@{user_id}> hai cagato {cagate[user_id]} volte")

@bot.command(name="gay", help="Insulta il coglione menzionato Dio Boia.")
async def gay(ctx, utente: discord.User):
        await ctx.send(f"Sei un coglione, {utente.mention}!")

@bot.command(name="contanegri", help="Conta quante volte una cazzo di parola e' stata scritta nel canale Dio Frocio.")
async def contanegri(ctx, parola: str = None):
    user_id = str(ctx.author.id)
    channel_id = str(ctx.channel.id)

    if channel_id not in conteggi_parole_canali:
        conteggi_parole_canali[channel_id] = {}

    if user_id not in conteggi_parole_canali[channel_id]:
        conteggi_parole_canali[channel_id][user_id] = {}

    if parola is None:
        await ctx.send(f"<@{user_id}>, disabile, inserisci la parola da cercare nel messaggio del comando. Coglione...")
        return

    conteggio_parola = conteggi_parole_canali[channel_id][user_id].get(parola, 0)

    await ctx.send(f"Il coglione ha scritto **'{parola}'** {conteggio_parola} volte, bravo disabile!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    user_id = str(message.author.id)
    channel_id = str(message.channel.id)

    if channel_id not in conteggi_parole_canali:
        conteggi_parole_canali[channel_id] = {}

    if user_id not in conteggi_parole_canali[channel_id]:
        conteggi_parole_canali[channel_id][user_id] = {}

    parole = re.findall(r'\b\w+\b', message.content.lower())

    for parola in parole:
        conteggi_parole_canali[channel_id][user_id][parola] = conteggi_parole_canali[channel_id][user_id].get(parola, 0) + 1

    await bot.process_commands(message)

@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(title="Comandi che puoi fare con il disa di Xi Jinping", description="Ecco i comandi coglione:")

    embed.add_field(name=".ping", value="Scrive Pong il coglione di Xi Jinping.", inline=False)
    embed.add_field(name=".negro", value="Ti insulta disabile.", inline=False)
    embed.add_field(name=".bagno", value="Comando utile per Cristian che va in bagno ogni 60 secondi, questo comando tiene conto di ogni volta che sei andato in bagno.", inline=False)
    embed.add_field(name=".gay", value="Insulta il coglione menzionato Dio Boia.", inline=False)
    embed.add_field(name=".contanegri", value="Conta quante volte una cazzo di parola e' stata scritta nel canale Dio Frocio.", inline=False)
    embed.add_field(name=".help", value="Ti mostra questa lista coglione.", inline=False)
    embed.add_field(name=".depex", value="Non funziona un cazzo, ma in teoria deve depexare i negri.", inline=False)
    embed.add_field(name=".clear", value="Cancella quanti porco dio di messaggi tu voglia perchè te sei un disabile pigro", inline=False)

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Non c'e' nessun comando con questo nome coglione, fai **.help** dato che non capisci un cazzo!")

@bot.command(name="clear", help="Cancella i messaggi nel canale.")
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
bot.run('yourtokenhere')