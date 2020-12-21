from discord.ext import commands

from rally_api import valid_coin_symbol
from coingecko_api import valid_coin
import errors

class CommonCoin(commands.Converter):
    async def convert(self, ctx, argument):
        valid = valid_coin(argument)
        if not valid:
            raise errors.InvalidCoin("Invalid coin symbol")
        return argument

class CreatorCoin(commands.Converter):
    async def convert(self, ctx, argument):
        valid = valid_coin_symbol(argument)
        if not valid:
            raise errors.InvalidCoin("Invalid coin symbol")
        return argument