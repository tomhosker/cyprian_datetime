"""
This code defines some constants used across the project.
"""

# Local imports.
from pathlib import Path

# Paths.
DEFAULT_PATH_TO_CACHE_DB = str(Path.home()/".cyprian_datetime_cache.db")

# Calendar.
LAST_MONTH = 12
LEAP_MONTH = 13
CYPRIAN_GREGORIAN_YEAR_DIFF = 2013
YEAR_INITIAL = "T"

# Month names.
MONTH_NAMES_LATIN = (
    None,
    "Primilis",
    "Sectilis",
    "Tertilis",
    "Quartilis",
    "Quintilis",
    "Sextilis",
    "September",
    "October",
    "November",
    "December",
    "Unodecember",
    "Duodecember",
    "Intercalaris"
)
MONTH_NAMES = MONTH_NAMES_LATIN
