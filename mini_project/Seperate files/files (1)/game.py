"""Core game: stages, loading, shooting, turn order."""

import random

from constants import BLANK, ITEMS_FROM_STAGE, LIVE, MAX_STAGE
from dealer_ai import dealer_choice
from items import use_item
from models import DealerDead, PlayerDead, Side
from player import player_choice
from ui import pause, render, shell_text


class Game:
    def __init__(self, player_name, settings):
        self.settings = settings
        self.player = Side(player_name)
        self.dealer = Side("Dealer")
        self.stage = 1
        self.shells = []
        self.load_live = 0
        self.load_blank = 0
        self.saw = False        # handsaw active for the next shot
        self.holder = "table"   # "table" or a Side

    # ---------------- helpers ----------------
    def other(self, side):
        return self.dealer if side is self.player else self.player

    def check_deaths(self):
        if self.player.hp <= 0:
            raise PlayerDead()
        if self.dealer.hp <= 0:
            raise DealerDead()

    def pop_shell(self):
        shell = self.shells.pop(0)
        for side in (self.player, self.dealer):
            side.known = {i - 1: t for i, t in side.known.items() if i > 0}
        return shell

    # ---------------- stage / loading ----------------
    def start_stage(self):
        idx = self.stage - 1
        self.player.reset_for_stage(self.settings["player_lives"][idx])
        self.dealer.reset_for_stage(self.settings["dealer_lives"][idx])
        self.shells = []
        self.saw = False
        print(f"\n######## STAGE {self.stage} ########")
        print(f"Lives: {self.player.name} {self.player.max_hp}, Dealer {self.dealer.max_hp}")
        pause()

    def load_shotgun(self):
        total = random.randint(2, 8)
        live = random.randint(1, total - 1)
        blank = total - live
        self.shells = [LIVE] * live + [BLANK] * blank
        random.shuffle(self.shells)
        self.load_live, self.load_blank = live, blank
        self.saw = False
        self.holder = "table"
        for side in (self.player, self.dealer):
            side.known = {}
        print("\nD - Loading the shotgun...")
        pause()
        if self.stage >= ITEMS_FROM_STAGE:
            self.hand_out_items()
        render(self)
        pause()

    def hand_out_items(self):
        enabled = [name for name, on in self.settings["items"].items() if on]
        if not enabled:
            return
        lo, hi = self.settings["items_per_load"]
        amount = random.randint(lo, hi)
        for side in (self.player, self.dealer):
            got = []
            for _ in range(amount):
                free = side.free_slots()
                if not free:
                    break
                item = random.choice(enabled)
                side.items[free[0]] = item
                got.append(item)
            print(f"{side.name} receives: {', '.join(got) if got else 'nothing (no free slots)'}")
        pause()

    # ---------------- shooting ----------------
    def fire(self, shooter, target):
        shell = self.pop_shell()
        sawn = self.saw
        self.saw = False   # handsaw effect ends after ANY shot
        if shooter is target:
            print(f"\n{shooter.name} points the shotgun at themself...")
        else:
            print(f"\n{shooter.name} points the shotgun at {target.name}...")
        pause(1.2)
        if shell == LIVE:
            dmg = 2 if sawn else 1
            target.hp = max(0, target.hp - dmg)
            print(f"*BANG* - {shell_text(shell)}! {target.name} loses {dmg} life.")
        else:
            print(f"*click* - {shell_text(shell)}. Nothing happens.")
            if sawn:
                print("(the sawed-off effect is wasted)")
        pause()
        return shell

    # ---------------- turn / main loop ----------------
    def take_turn(self, actor):
        opp = self.other(actor)
        self.holder = actor
        while True:
            if actor is self.player:
                kind, arg = player_choice(self)
            else:
                kind, arg = dealer_choice(self)

            if kind == "item":                       # items never end the turn
                use_item(self, actor, arg)
                self.check_deaths()
                if not self.shells:                  # e.g. beer ejected the last shell
                    return
                continue

            target = opp if kind == "shoot_opp" else actor
            shell = self.fire(actor, target)
            self.check_deaths()
            if kind == "shoot_self" and shell == BLANK and self.shells:
                print(f"{actor.name} shot a blank at themself - the turn continues.")
                pause()
                continue
            return                                    # every other shot ends the turn

    def play(self):
        """Run the game. Returns True if the player won."""
        self.stage = 1
        self.start_stage()
        current = self.player
        while True:
            try:
                if not self.shells:                   # shotgun loads only when empty
                    self.load_shotgun()
                    current = self.player             # after a load the player starts
                if current.cuffed:
                    print(f"\n{current.name} is handcuffed and skips the turn. The cuffs break.")
                    current.cuffed = False
                    current = self.other(current)
                    pause()
                    continue
                self.take_turn(current)
                if self.shells:
                    current = self.other(current)
            except DealerDead:
                print("\nD - Dealer is down.")
                self.stage += 1
                if self.stage > MAX_STAGE:
                    print("\n*** You survived all stages. YOU WIN! ***")
                    return True
                print("Health is restored and the next stage begins.")
                pause()
                self.start_stage()
                current = self.player
            except PlayerDead:
                print(f"\n{self.player.name} is dead. GAME OVER.")
                return False
