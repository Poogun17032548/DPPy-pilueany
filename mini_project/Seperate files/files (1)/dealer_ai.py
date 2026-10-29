"""Dealer decision logic."""

import random

from constants import (BEER, BLANK, CIGARETTES, HANDCUFFS, HANDSAW, INVERTER,
                       LIVE, MAGNIFIER, PHONE, PILLS)
from items import can_use
from ui import pause


def dealer_choice(game):
    """Return ("shoot_opp", None) | ("shoot_self", None) | ("item", item_name)."""
    d = game.dealer
    pause(1.0)
    n = len(game.shells)
    live = game.shells.count(LIVE)       # remaining counts are public information
    current = d.known.get(0)

    def can(item):
        return d.has(item) and can_use(game, d, item)[0]

    # 1) utility items
    if current is None and can(MAGNIFIER):
        return ("item", MAGNIFIER)
    if d.hp < d.max_hp and can(CIGARETTES):
        return ("item", CIGARETTES)
    if can(PILLS) and 3 <= d.hp <= d.max_hp - 2:
        return ("item", PILLS)
    if can(HANDCUFFS) and n > 1:
        return ("item", HANDCUFFS)
    if can(PHONE) and n > 2 and not d.known:
        return ("item", PHONE)

    # 2) current shell is known
    if current == LIVE:
        if can(HANDSAW):
            return ("item", HANDSAW)
        return ("shoot_opp", None)
    if current == BLANK:
        if can(INVERTER) and random.random() < 0.5:
            return ("item", INVERTER)
        return ("shoot_self", None)

    # 3) unknown shell: play the odds
    if can(BEER) and n > 1 and random.random() < 0.5:
        return ("item", BEER)
    if live == n:
        return ("shoot_opp", None)
    if live == 0:
        return ("shoot_self", None)
    chance = live / n
    if chance > 0.5 or (chance == 0.5 and random.random() < 0.5):
        if can(HANDSAW) and random.random() < 0.6:
            return ("item", HANDSAW)
        return ("shoot_opp", None)
    return ("shoot_self", None)
