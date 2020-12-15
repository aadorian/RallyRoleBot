import json
import sys
import traceback

import discord
from discord.ext import commands, tasks
from discord.utils import get

import data
import rally_api
import validation
import errors

from cogs import update_cog

from constants import *
from utils import pretty_print


class PurchaseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_after_invoke(self, ctx):
        await pretty_print(
            ctx, "Command completed successfully!", title="Success", color=SUCCESS_COLOR
        )

    @errors.standard_error_handler
    async def cog_command_error(self, ctx, error):
        # All other Errors not returned come here. And we can just print the default TraceBack.
        print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )

    @commands.command(
        name="purchase",
        help="Display purchase message",
    )
    async def purchase_message(self, ctx):
        coin = data.get_default_coin(ctx.guild.id) or ""
        default = f"You can purchase by using a Credit/Debit card or a number of different Crypto Currencies! Buying earns rewards, supports the community, and you can even get vip Status! (hint: there's a secret VIP room for those who hold X # of ;) https://www.rally.io/creator/{coin}"
        message = data.get_purchase_message(ctx.guild.id) or default
        await ctx.send(message)

    @commands.command(
        name="set_purchase_message",
        help=" <message> Message displayed when user types the purchase command",
    )
    @validation.owner_or_permissions(administrator=True)
    async def set_purchase_message(self, ctx, message):
        data.add_purchase_message(ctx.guild.id, message)

    @commands.command(
        name="set_donating_message",
        help=" <message> Message displayed when user types the donate command",
    )
    @validation.owner_or_permissions(administrator=True)
    async def set_donate_message(self, ctx, message):
        data.add_donate_message(ctx.guild.id, message)

    @commands.command(
        name="donate",
        help="Display donate message",
    )
    async def donate_message(self, ctx):
        coin = data.get_default_coin(ctx.guild.id) or ""
        default = f"You can donate by going to https://www.rally.io/creator/{coin}. Your donation helps grow and support the community and creator - Plus there are 10  tiers of Donation badges to earn to show of your support! https://www.rally.io/creator/{coin}"
        message = data.get_purchase_message(ctx.guild.id) or default
        await ctx.send(message)

    @commands.command(
        name="balance",
        help="Display registered user's coin balance",
    )
    async def balance(self, ctx):
        rally_id = data.get_rally_id(ctx.message.author.id)
        if rally_id:
            balances = rally_api.get_balances(rally_id)
            await ctx.send(balances)
        else:
            await ctx.send(
                f"{ctx.message.author.mention} hasn't verified yet. Type help in DM."
            )
