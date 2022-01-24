import asyncio
from datetime import datetime

from discord.ext import commands


class AsyncTimer:
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    def cancel(self):
        self._task.cancel()


class Timer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.start_time = None

    async def calculate_time(self):
        """Calculate time elapsed in minutes.

        :return: integer of elapsed minutes
        """
        elapsed_seconds = (datetime.now() - self.start_time).total_seconds()
        elapsed_minutes = elapsed_seconds // 60
        elapsed_seconds %= 60
        return elapsed_minutes, elapsed_seconds

    @commands.group(invoke_without_command=True, aliases=['t'])
    async def timer(self, ctx):

        if self.start_time is None:
            usr_msg = f"Timer is currently not started!"
        else:
            minutes, seconds = await self.calculate_time()
            usr_msg = f"Timer has been running for {minutes} minutes and {seconds:.1f} seconds!"

        await ctx.send(usr_msg)

    @timer.command()
    async def end(self, ctx):

        self.start_time = datetime.now()
        minutes, seconds = self.calculate_time()
        await ctx.send(f"Ended timer at {minutes} minutes and {seconds:.1f} seconds!")
        self.start_time = None

    @timer.command()
    async def start(self, ctx):
        self.start_time = datetime.now()
        await ctx.send(f"Started time at {self.start_time}")


def setup(bot):
    bot.add_cog(Timer(bot))
