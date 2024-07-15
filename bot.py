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
    
#welcome message#
@bot.event
async def on_member_join(member):
    welcome_channel_id = ()  
    welcome_channel = bot.get_channel(welcome_channel_id)
    if welcome_channel:
        welcome_message = f"Hello {member.mention}, welcome to the server."
        await welcome_channel.send(welcome_message)
        
#GUIDE#
@bot.command()
async def guide(ctx):
    embed = discord.Embed(title="Komutlar", color=discord.Color.green())
    embed.add_field(name="clear", value="Deleates a certain amount of messages", inline=False)
    embed.add_field(name="joined", value="Shows a user is in this server since when", inline=False)
    embed.add_field(name="repeat", value="Repeats a message certain amount of times", inline=False)
    await ctx.send(embed=embed)
    
#REPEAT SMTHNG#
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    "Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
#____ IS IN THE SERVER SINCE ____#
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
#SHOWING IMAGE ON COMMAND#
@bot.command()
async def #something# (ctx):
    file_path = 'D:\'
    file = discord.File(file_path, filename=???.jpeg'')
    embed = discord.Embed(title="")
    embed.set_image(url='attachment://???.jpeg')
    await ctx.send(file=file, embed=embed)

#---------ADMIN COMMANDS-------------#    
#DELATING CERTAIN AMOUNT OF MESSAGES FROM A CHANNEL#
@bot.command(aliases=['clean'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, limit=None):  
    if not any(role.name in ["Admin" , "Ban Hammer"] for role in ctx.author.roles):
#If you want to choose only one role:  if "#any role you want#" not in [role.name for role in ctx.author.roles]:#
        await ctx.send("You should have  Admin or Ban Hammer role to use this command ")
        return
    if limit == "all": 
        await ctx.channel.purge()
        embed = discord.Embed(title='All massages cleared from chat.', description=f'Thanks to {ctx.author} for opening us a new future.')
    else:
        try:
            limit = int(limit)
            await ctx.channel.purge(limit=limit)
            embed = discord.Embed(title=f'{limit} massages.', description=f'Thanks to {ctx.author} to deleting messages.')
        except ValueError:
            embed = discord.Embed(title='Hata', description='Please chose a valid number or "all".', color=discord.Color.red())
    await ctx.send(embed=embed)

#BAN#
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if not any(role.name in ["Admin" , "Ban Hammer"] for role in ctx.author.roles):
#If you want to choose only one role:  if "any role you want" not in [role.name for role in ctx.author.roles]:#
        await ctx.send("You should have  Admin or Ban Hammer role to use this command.")
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member} banned. Reason: {reason}')

#UNBAN#
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member_name):
    if not any(role.name in ["Admin", "Ban Hammer"] for role in ctx.author.roles):
#If you want to choose only one role:  if "any role you want" not in [role.name for role in ctx.author.roles]:#
        await ctx.send("You should have  Admin or Ban Hammer role to use this command.")
        return
    async for ban_entry in ctx.guild.bans():
        user = ban_entry.user
        if user.name.lower() == member_name.lower():
            await ctx.guild.unban(user)
            await ctx.send(f'{user} unbanned.')
            return
    await ctx.send(f'{member_name} not found.')

#KICK#
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if not any(role.name in ["Admin", "Ban Hammer"] for role in ctx.author.roles):
#If you want to choose only one role:  if "any role you want" not in [role.name for role in ctx.author.roles]:#
        await ctx.send("You should have  Admin or Ban Hammer role to use this command.")
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member} kicked. Reason: {reason}')

bot.run('')
