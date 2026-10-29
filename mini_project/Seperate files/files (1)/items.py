"""Item rules. Functions take the Game object as first argument."""

import random

from constants import (BEER, BLANK, CIGARETTES, HANDCUFFS, HANDSAW, INVERTER,
                       LIVE, MAGNIFIER, PHONE, PILLS)
from ui import pause, shell_text


def can_use(game, user, name):
    """Return (ok, reason). Checked before an item is consumed."""
    if name == HANDCUFFS and game.other(user).cuffed:
        return False, "Opponent is already handcuffed."
    if name == HANDSAW and game.saw:
        return False, "The barrel is already sawed off."
    return True, ""


def use_item(game, user, name):
    slot = user.items.index(name)
    user.items[slot] = None
    opp = game.other(user)
    is_player = user is game.player
    print(f"\n{user.name} uses {name}.")
    pause()

    if name == BEER:
        shell = game.pop_shell()
        print(f"The shotgun ejects a {shell_text(shell)} shell.")

    elif name == MAGNIFIER:
        current = game.shells[0]
        user.known[0] = current
        if is_player:
            print(f"You look into the chamber: {shell_text(current)}")
        else:
            print("Dealer peers into the chamber.")

    elif name == CIGARETTES:
        if user.hp < user.max_hp:
            user.hp += 1
            print(f"{user.name} heals 1 life.")
        else:
            print("Already at full health. No effect.")

    elif name == HANDSAW:
        game.saw = True
        print("Barrel sawed off. Next LIVE shell deals double damage.")

    elif name == HANDCUFFS:
        opp.cuffed = True
        print(f"{opp.name} is handcuffed and will skip the next turn.")

    elif name == PHONE:
        remaining = len(game.shells)
        if remaining < 2:
            print("Phone: ...nothing useful. Only one shell left.")
        else:
            idx = random.randint(1, remaining - 1)   # never the current shell
            user.known[idx] = game.shells[idx]
            if is_player:
                print(f"Phone: shell number {idx + 1} is {game.shells[idx]}.")
            else:
                print("Dealer listens to the phone.")

    elif name == PILLS:
        if random.random() < 0.5:
            before = user.hp
            user.hp = min(user.max_hp, user.hp + 2)
            print(f"Pills worked. {user.name} heals {user.hp - before} life.")
        else:
            user.hp -= 1
            print(f"Bad pills! {user.name} loses 1 life.")

    elif name == INVERTER:
        game.shells[0] = BLANK if game.shells[0] == LIVE else LIVE
        for side in (game.player, game.dealer):
            if 0 in side.known:
                side.known[0] = game.shells[0]
        print("The current shell has been inverted.")

    pause()
