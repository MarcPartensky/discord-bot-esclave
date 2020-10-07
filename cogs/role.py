from discord.ext import commands
from config.config import cluster, prefix
from functools import reduce

import discord

class Role(commands.Cog):
    """The goal of this cog is to sell roles or give bonuses when roles are given."""
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.group(name="rôle", aliases=['role'])
    async def role(self, ctx:commands.Context):
        """Groupe des commandes sur les rôles."""
        if not ctx.invoked_subcommand:
            await ctx.send(
                "> Cette commande est inexistante."
                "\n> Tapez `"
            )

    @role.command(aliases=['t'])
    async def top(self, ctx:commands.Context, member:discord.Member=None):
        """Affiche le rôle principal d'un joueur."""
        member = member or ctx.author
        if member == ctx.author:
            await ctx.send(f"Vous êtes {member.top_role}.")
        else:
            await ctx.send(f"{member.name} est {member.top_role}.")

    @role.command(name="liste", aliases=['list', 'l'])
    async def role_list(self, ctx:commands.Context):
        """Donne tous les rôles d'un membre."""
        #bad way to do it, too much processing
        member = member or ctx.author
        roles = list(reversed([f"*{r.name}*" for r in member.roles]))[:-1]
        string = f"{', '.join(roles[::-1])} et {roles[-1]}."
        if member == ctx.author:
            await ctx.send(f"> Vos rôles sont {string}.")
        else:
            await ctx.send(f"> Les rôles de **{member.name}** sont {string}.")

    @role.command(name="sauvegarder", aliases=['save', 's'])
    async def role_save(self, ctx:commands.Context, member:discord.Member=None):
        """Sauvegarde les rôles d'un membre."""
        member = member or ctx.author
        account = cluster.users.accounts[member.id]
        account.roles = [role.name for role in member.roles[1::]]
        if member==ctx.author:
            msg = "> Vos rôles sont sauvegardés."
        else:
            msg = f"> Les rôles de **{member.name}** sont sauvegardés."
        await ctx.send(msg)

    @role.command(name="sauvegardés", aliases=['saved', 'sd'])
    async def role_save(self, ctx:commands.Context, member:discord.Member=None):
        """Sauvegarde les rôles d'un membre."""
        member = member or ctx.author
        account = cluster.users.accounts[member.id]
        string
        if member==ctx.author:
            msg = "> Vos rôles sauvegardés sont {string_roles}."
        else:
            msg = f"> Les rôles de **{member.name}** sauvegardés sont {string_roles}."
        await ctx.send(msg)

    @role.command()
    @access.admin
    async def role_mach

    @commands.command()
    async def roles(self, ctx:commands.Context, member:discord.Member=None):
        """Liste tous les rôles du serveur."""
        roles = []
        roles.extend(map(lambda mb:mb.roles, ctx.guild.members))
        roles = reduce(lambda a,b:a+b, roles)
        roles = list(map(lambda role:role.name, set(roles)))
        msg = f"> La liste des rôles présents sur le serveur est: {roles}"
        await ctx.send(msg)

    # @role.command()
    # async def role_old(self, ctx:)



def setup(bot):
    bot.add_cog(Role(bot))
