"""Player input: asks what the human wants to do this action."""

from constants import MAX_SLOTS
from items import can_use
from ui import ask_int, render


def player_choice(game):
    """Return ("shoot_opp", None) | ("shoot_self", None) | ("item", item_name)."""
    p = game.player
    render(game)
    print(f"{p.name}, your move:")
    print("  1 - shoot Dealer")
    print("  2 - shoot yourself")
    print("  3 - use item")
    while True:
        choice = ask_int("> ", 1, 3)
        if choice == 1:
            return ("shoot_opp", None)
        if choice == 2:
            return ("shoot_self", None)
        if not any(p.items):
            print("You have no items.")
            continue
        slot = ask_int("Item slot (1-6, 0 = cancel): ", 0, MAX_SLOTS)
        if slot == 0:
            continue
        name = p.items[slot - 1]
        if name is None:
            print("That slot is empty.")
            continue
        ok, why = can_use(game, p, name)
        if not ok:
            print(why)
            continue
        return ("item", name)
