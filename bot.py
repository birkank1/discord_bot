import discord
from discord.ext import commands
import random

description = ()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)
#BOT ENTERED THE SERVER#
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
#GUIDE#
@bot.command()
async def guide(ctx):
    embed = discord.Embed(title="Komutlar", color=discord.Color.green())
    embed.add_field(name="clear", value="Belirtilen sayi kadar  mesaj siler", inline=False)
    embed.add_field(name="joined", value="Belirtilen kullanicinin ne zamandir sunucuda olduğunu gösterir", inline=False)
    embed.add_field(name="repeat", value="Belirtilen mesaji belirttiğiniz sayida tekrarlar", inline=False)
    await ctx.send(embed=embed)
    
#REPEAT SMTHNG#
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
#____ IS IN THE SERVER SINCE ____#
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
#SHOWING IMAGE ON COMMAND#
@bot.command()
async def smile (ctx):
    file_path = 'D:\\python pro derslerim\\discord_bot\\guldur.jpeg'
    file = discord.File(file_path, filename='guldur.jpeg')
    embed = discord.Embed(title="Its time to smile, show your teeths")
    embed.set_image(url='attachment://guldur.jpeg')
    await ctx.send(file=file, embed=embed)
#DELATING CERTAIN AMOUNT OF MESSAGES FROM A CHANNEL#
@bot.command(aliases=['clean'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, limit=None):
    if limit == "all":
        await ctx.channel.purge()
        embed = discord.Embed(title='All messages deleted from this chanell.', description=f'Thanks to {ctx.author} for opening us a bright future.')
    else:
        try:
            limit = int(limit)
            await ctx.channel.purge(limit=limit)
            embed = discord.Embed(title=f'{limit} massages delated from this chanell.', description=f'Thanks to {ctx.author} for opening space in chanell.')
        except ValueError:
            embed = discord.Embed(title='Error', description='Please enter a valid number or "all" .', color=discord.Color.red())
    await ctx.send(embed=embed)
    


bot.run('')
