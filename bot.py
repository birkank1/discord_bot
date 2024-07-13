import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)
#bot sunucuda#
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
#tekrarla#
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
#___ ne zamandır sunucuda#
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
#komutla resim gönderme#
@bot.command()
async def guldur(ctx):
    file_path = 'D:\\python pro derslerim\\discord_bot\\guldur.jpeg'
    file = discord.File(file_path, filename='guldur.jpeg')
    embed = discord.Embed(title="Gülme Zamanı!")
    embed.set_image(url='attachment://guldur.jpeg')
    await ctx.send(file=file, embed=embed)
    


bot.run('TOKEN GİRİLMELİ')
