"""Shared constants: shell types, item names, limits."""

LIVE = "LIVE"      # red shell
BLANK = "BLANK"    # blue shell
SHELL_COLOR = {LIVE: "red", BLANK: "blue"}

MAX_SLOTS = 6                 # max items per side
ITEMS_FROM_STAGE = 1          # items appear only on stage 2 and 3
MAX_STAGE = 1
DEFAULT_LIVES = [3, 4, 6]     # stage 1 / 2 / 3

BEER = "Beer"
MAGNIFIER = "Magnifying glass"
CIGARETTES = "Cigarettes"
HANDSAW = "Handsaw"
HANDCUFFS = "Handcuffs"
PHONE = "Cheap phone"
PILLS = "Pills"
INVERTER = "Inverter"
ITEMS = [BEER, MAGNIFIER, CIGARETTES, HANDSAW, HANDCUFFS, PHONE, PILLS, INVERTER]
