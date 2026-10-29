"""Settings data and the settings menu."""

from constants import DEFAULT_LIVES, ITEMS, MAX_SLOTS, MAX_STAGE
from ui import ask_int


def default_settings():
    return {
        "player_lives": DEFAULT_LIVES[:],
        "dealer_lives": DEFAULT_LIVES[:],
        "items": {name: True for name in ITEMS},
        "items_per_load": (1, 4),   # min, max items handed to each side per load
    }


def edit_lives(settings, key, label):
    for i in range(MAX_STAGE):
        current = settings[key][i]
        raw = input(f"{label} lives, stage {i + 1} (now {current}, 1-9, Enter = keep): ").strip()
        if raw == "":
            continue
        if raw.isdigit() and 1 <= int(raw) <= 9:
            settings[key][i] = int(raw)
        else:
            print("Ignored (must be 1-9).")


def edit_items(settings):
    while True:
        print("\nItems in game (stage 2 and 3):")
        for i, name in enumerate(ITEMS, 1):
            mark = "x" if settings["items"][name] else " "
            print(f"  {i} - [{mark}] {name}")
        print("  0 - back")
        choice = ask_int("Toggle item: ", 0, len(ITEMS))
        if choice == 0:
            return
        name = ITEMS[choice - 1]
        settings["items"][name] = not settings["items"][name]


def settings_menu(settings):
    while True:
        lo, hi = settings["items_per_load"]
        print("\n=== SETTINGS ===")
        print(f"1 - Player lives per stage: {settings['player_lives']}")
        print(f"2 - Dealer lives per stage: {settings['dealer_lives']}")
        print("3 - Enable / disable items")
        print(f"4 - Items handed out per load: {lo}-{hi}")
        print("5 - Reset to defaults")
        print("6 - Back")
        choice = ask_int("> ", 1, 6)
        if choice == 1:
            edit_lives(settings, "player_lives", "Player")
        elif choice == 2:
            edit_lives(settings, "dealer_lives", "Dealer")
        elif choice == 3:
            edit_items(settings)
        elif choice == 4:
            new_lo = ask_int("Minimum items per load (0-6): ", 0, MAX_SLOTS)
            new_hi = ask_int(f"Maximum items per load ({new_lo}-6): ", new_lo, MAX_SLOTS)
            settings["items_per_load"] = (new_lo, new_hi)
        elif choice == 5:
            settings.clear()
            settings.update(default_settings())
            print("Settings reset.")
        else:
            return
