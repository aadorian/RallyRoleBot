import json
import sys
import traceback

import discord
from discord.ext import commands, tasks
from discord.utils import get

import data
import rally_api
import coingecko_api
import validation
import errors

from utils import pretty_print, send_to_dm
from constants import *

class RallyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_after_invoke(self, ctx):
        await pretty_print( ctx, "Command completed successfully!",  title= "Success", color=SUCCESS_COLOR)

    @errors.standard_error_handler
    async def cog_command_error(self, ctx, error):

        # All other Errors not returned come here. And we can just print the default TraceBack.
        print( "Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception( type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command(name="set_rally_id", help="Set your rally id")
    @commands.dm_only()
    async def set_rally_id(self, ctx, rally_id):
        data.add_discord_rally_mapping(ctx.author.id, rally_id)

    @commands.command(name="price", help="Get the price data of a coin")
    @validation.is_valid_coin()
    async def price(self, ctx, coin_symbol):
        price = coingecko_api.get_price_data(coin_symbol) or rally_api.get_price_data(coin_symbol)

        dataTitle = ""
        dataStr = ""

        if price is False:
            dataTitle = "Error"
            dataStr = "There was an error while fetching the coin data\nPlease try again"
        else:
            dataTitle = f"{coin_symbol.upper()} Price Data"
            dataStr = f"Current Price: {price['current_price']}\n\
                24H Price Change: {price['price_change_percentage_24h']}%\n\
                30D Price Change: {price['price_change_percentage_30d']}%"
        
        await pretty_print(ctx, dataStr, title=dataTitle, color=WARNING_COLOR)