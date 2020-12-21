# Contributing to RallyRoleBot
🎉 Thanks for your contribution to this project! 🎉

The following is a set of guidelines for contributing to Atom and its packages, which are hosted by [Rally Creator Coin Tools](https://github.com/CreatorCoinTools) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

### Your First Code Contribution

Unsure where to begin contributing to RallyRoleBot? You can start by looking through the bounties on discord also available in the [issues](https://github.com/CreatorCoinTools/RallyRoleBot/issues) section of the GitHub.

**Be sure that you aren't attempting the same bounty or issue that another person has been assigned to!**

### Setup

Please see the [README](https://github.com/CreatorCoinTools/RallyRoleBot/blob/master/README.md) for deploying locally to your device!

### Pull Requests 
The process described here has several goals:

-   Maintain or Improve RallyRoleBot's quality
-   Fix problems that are important to users
-   Engage the community in working toward the best possible RallyRoleBot
-   Enable a sustainable system for maintainers to review contributions

#### Python Style Guide

Be sure to include PEP [multi-line docstring](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings) comments on every function in your pull request.

Be sure to use Python [black](https://pypi.org/project/black/) for all formatting. Do not execute `black *` but instead, do so on the files you commit.

##  Discord Library
RallyRoleBot is built on [Discord Python library](https://discordpy.readthedocs.io/) for developing bots. In keeping with that, there are a few guidelines.

-For every new set of functionality or commands, please create a [Cog](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html) that appropriately encompasses the commands. If the command is better integrated with an existing Cog, do so instead. All cogs can be found under `rallyrolebot/cogs/`
 
-All custom errors must be written and handled in `rallyrolebot/errors.py` 



-Oftentimes, there is a need to validate certain properties about the user issuing the command. Use discord [Checks](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#checks) when this is the case. Some examples can be found with the `owner_or_permissions` or `guild_only` checks.

-Additionally, you may need to validate certain properties about the arguments passed in. Use [Converters and Advanced Converters](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#converters) in that case. 

-Finally, be sure to use `utils.pretty_print` for outputs as it allows us to keep a consistent look and feel to the bot.

# Thanks! Happy Coding!
See more about how discord commands work [here](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html)
