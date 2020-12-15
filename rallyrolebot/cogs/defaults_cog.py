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


class DefaultsCommands(commands.Cog):
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
        name="set_default_coin",
        help=" <coin name> Set a default coin to be used across the server",
    )
    @validation.owner_or_permissions(administrator=True)
    async def set_default_coin(self, ctx, coin_name):
        data.add_default_coin(ctx.guild.id, coin_name)

    @commands.command(
        name="change_prefix",
        help=" <prefix> Prefix for bot commands",
    )
    @validation.owner_or_permissions(administrator=True)
    async def set_prefix(self, ctx, prefix):
        data.add_prefix_mapping(ctx.guild.id, prefix)

    @commands.command(
        name="role_call",
        help=" <role> Display users who have access to a given role",
    )
    @validation.owner_or_permissions(administrator=True)
    async def role_call(self, ctx, role: discord.Role):
        for member in ctx.guild.members:
            if role in member.roles:
                await ctx.send(member)

    @commands.command(
        name="list_all_users",
        help="Display users who have been registered",
    )
    @validation.owner_or_permissions(administrator=True)
    async def list_all_users(self, ctx):
        await ctx.send(json.dumps([json.dumps(user) for user in data.get_all_users()]))
