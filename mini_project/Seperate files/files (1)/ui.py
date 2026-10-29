"""Input / output helpers: delays, number prompts, the game screen."""

import time

from constants import SHELL_COLOR

FAST = False  # set to True (e.g. in tests) to remove delays


def pause(seconds=0.8):
    if not FAST:
        time.sleep(seconds)


def ask_int(prompt, low, high):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and low <= int(raw) <= high:
            return int(raw)
        print(f"Enter a number from {low} to {high}.")


def shell_text(shell):
    return f"{SHELL_COLOR[shell].upper()} ({shell})"


def render(game):
    """Print the game screen. `game` is a game.Game instance."""
    p, d = game.player, game.dealer
    print("\n" + "=" * 44)
    print(f"Dealer {'i' * d.hp} | stage {game.stage} | {p.name} {'i' * p.hp}")
    print(f"Current load: {game.load_live} red, {game.load_blank} blue")
    print("Shells are loaded in random sequence")
    print("_" * 32)
    if game.holder == "table":
        where = "on table"
    else:
        where = f"in {game.holder.name}'s hands"
    print(f"Shotgun currently {where}")
    if game.saw:
        print("(barrel is sawed off: next LIVE shell deals double damage)")
    if p.cuffed:
        print(f"({p.name} is handcuffed)")
    if d.cuffed:
        print("(Dealer is handcuffed)")
    if p.known:
        parts = [f"shell {i + 1} = {shell_text(t)}" for i, t in sorted(p.known.items())]
        print("You know: " + ", ".join(parts))
    for side in (p, d):
        print(f"\nList of {side.name} items")
        for i, item in enumerate(side.items, 1):
            print(f"{i} {item if item else 'xxx'}")
    print("=" * 44)
