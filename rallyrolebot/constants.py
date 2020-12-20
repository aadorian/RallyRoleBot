from discord import Color
# TODO: Place holder for now - can use __init__.py once dependencies such as 
# data.ROLE_MAPPINGS_TABLE and rally_api.BASE_URL have been removed

"""
 Constants useful for data module
"""
ROLE_MAPPINGS_TABLE = "mappings"
CHANNEL_MAPPINGS_TABLE = "channel_mappings"
RALLY_CONNECTIONS_TABLE = "rally_connections"

GUILD_ID_KEY = "guildId"
COIN_KIND_KEY = "coinKind"
REQUIRED_BALANCE_KEY = "requiredBalance"
ROLE_NAME_KEY = "roleName"
CHANNEL_NAME_KEY = "channel"
DISCORD_ID_KEY = "discordId"
RALLY_ID_KEY = "rallyId"

"""
 Constants useful for  rally_api module
"""

COIN_KIND_KEY = "coinKind"
COIN_BALANCE_KEY = "coinBalance"

BASE_URL = "https://api.rally.io/v1"
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"


"""
    Constants useful for update_cog module
"""
UPDATE_WAIT_TIME = 600

"""
    Miscellaneous constants
"""

ERROR_COLOR =  Color(0xFF0000)
SUCCESS_COLOR = Color(0x0000FF)
WARNING_COLOR = Color(0xFFFF00)
WHITE_COLOR = Color(0xFFFFFE)
INCREASE_DECREASE_GRADIENT_COLOR = [
    Color(0x9E1711), # Spartan Crimson
    Color(0xB12E21), # Chinese Brown
    Color(0xC34632), # International Orange
    Color(0xD65D42), # Medium Vermilion
    Color(0xE97452), # Burnt Sienna
    WHITE_COLOR,
    Color(0x95F985), # Light Green
    Color(0x4DED30), # Neon Green
    Color(0x26D701), # Harlequin Green
    Color(0x00C301), # Vivid Malachite
    Color(0x00AB08), # Islamic Green
]
