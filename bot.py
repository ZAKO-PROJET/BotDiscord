import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix="+")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="PROTECT"))
    print("")
    print("----------------")
    print("|  BOT START   |")
    print("----------------")

@bot.command()
async def commands(ctx):
    embedVar = discord.Embed(title="Commands disponible", description="Les commande des catégorie", color=255)
    embedVar.add_field(name="+lock", value="Vérouille le salon", inline=False)
    embedVar.add_field(name="+unlock", value="Dévérouille le salon", inline=False)
    embedVar.add_field(name="+clear", value="Suprime les message", inline=False)
    embedVar.add_field(name="+renew", value="Recrée le channel", inline=False)
    embedVar.add_field(name="+create", value="Crée un channel", inline=False)
    embedVar.add_field(name="+delete", value="Supprime le channel", inline=False)
    embedVar.add_field(name="+kick", value="Kick une personne", inline=False)
    embedVar.add_field(name="+ban", value="Ban une personne", inline=False)
    embedVar.add_field(name="+lookup", value="Avoir des infos sur une personne", inline=False)
    embedVar.add_field(name="+rename", value="Renomer une personne", inline=False)
    embedVar.add_field(name="+ping", value="Serre a savoir si le bot est on", inline=False)
    embedVar.add_field(name="OPTION SUPPLÉMENTAIRE", value="AUTO-SNIPE", inline=False)
    await ctx.send(embed=embedVar)

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ping(ctx):
    embedVar = discord.Embed(title="|---------------|\n| BOT START |\n|---------------|", color=255)
    await ctx.send(embed=embedVar)

#lock / unlock
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send("Les membre ne peuvent plus parler dans ce channel !")

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
    await ctx.send("Les membre peuvent maintenant parler dans ce channel !")

#clear
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def clear(ctx, amount=100):
    await ctx.send("Message suprimé !")
    await ctx.channel.purge(limit=amount)
        
#kick
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.guild.kick(member)
    await ctx.send(f'Le membre {member.mention} a été kick pour {reason} !')
    embed = discord.Embed(title="UNMUTE", description=f" UNMUTE {member.mention}",colour=discord.Colour.blue())
    await ctx.send(embed=embed)

#test---------------------------------------------------------------------------
@bot.command()
async def ticket(ctx):
    text= "Pour créer un ticket apuyer sur la réaction si dessous !"
    emoji = await ctx.send(text)
    await emoji.add_reaction('📩')

@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == "📩":
        guild = bot.get_guild(payload.guild_id)
        channel = await guild.create_text_channel('Tickets')
        await message.channel.set_permissions(ctx.guild.default_role,view_channel=False)

#ban
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#create / delete
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def create(ctx, channel_name):
    serv = ctx.guild
    await serv.create_text_channel(channel_name)
    await ctx.send("Channel créer !")

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def delete(ctx):
    channel = ctx.channel
    await channel.delete()

#renwe
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def renew(ctx):
    channel = ctx.channel
    await channel.delete()
    channell = channel.name
    serv = ctx.guild
    await serv.create_text_channel(channell)

#nick
@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def rename(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nom de {member.mention} changer !')

#auto-snipe
@bot.event
async def on_message_delete(message):
    embed = discord.Embed(title="AUTO-SNIPE", description=f"Auteur: {message.author.name}\n Message supprimé: {message.content}", color=255)
    await message.channel.send(embed=embed)

#lookup
@bot.command()
async def lookup(ctx, member: discord.Member):
    embed = discord.Embed(title="LOOKUP", description=f"{member.mention}\n Bot : {member.bot}\n Pseudo : {member}\n ID:{member.id}\n Date de création du compte : {member.created_at}\n Rejoin le : {member.joined_at}\n Role le plus haut : {member.top_role}\n",colour=discord.Colour.blue())
    await ctx.send(embed=embed)

bot.run("TOKEN here")
