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

from utils import pretty_print, send_to_dm
from constants import *


class RallyCommands(commands.Cog):
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

    @commands.command(name="set_rally_id", help="Set your rally id")
    @commands.dm_only()
    async def set_rally_id(self, ctx, rally_id):
        data.add_discord_rally_mapping(ctx.author.id, rally_id)


    @commands.command(name="unset_rally_id", help="Unset your rally id")
    @commands.dm_only()
    async def unset_rally_id(self, ctx, rally_id):
        data.remove_discord_rally_mapping(ctx.author.id, rally_id)

    @commands.command(
        name="admin_unset_rally_id",
        help=" <discord ID> <rally ID> Unset rally ID to discord ID mapping",
    )
    @validation.owner_or_permissions(administrator=True)
    async def admin_unset_rally_id(self, ctx, discord_id: discord.User, rally_id):
        data.remove_discord_rally_mapping(discord_id, rally_id)

  
