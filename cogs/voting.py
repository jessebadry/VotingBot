import discord
from discord.ext import commands
from exceptions import error_handler


class VotePollSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        This event receives the the guild when the bot joins.
        """
        print(f'Joined {guild.name} with {guild.member_count} users!')

    @commands.command()
    @error_handler.handle_errors
    async def test(self, ctx):
        """
        A test command, Mainly used to show how commands and cogs should be laid out.
        """
        await ctx.send('Tested!')

    @commands.group(invoke_without_command=True)
    async def foo(self, ctx):
        """
        A sub command group, Showing how sub command groups can be made.
        """
        await ctx.send('try my subcommand')

    @foo.command(aliases=['an_alias'])
    @error_handler.handle_errors
    async def bar(self, ctx):
        """
        I have an alias!, I also belong to command 'foo'
        """
        raise NotImplementedError("brh")



def setup(bot):
    bot.add_cog(VotePollSystem(bot))
