"""
shotgun.py - state of the shotgun ONLY. Python 3, standard library only.

Other files import it and read the state:

    from shotgun import shotgun, SHELL_LIVE, SHELL_BLANK

    shotgun.set_game_state(started=True, stage=1, current_side=0)
    if shotgun.can_make_new_load():
        info = shotgun.new_load()
    shotgun.current_shell        # 1 / 0 / None
    shotgun.shells_left          # int
    shotgun.load_order           # [1, 0, 0, 1 ...]  (copy)
    result = shotgun.shoot()     # takes the shell out
"""

import random

# ---------- shell values ----------
SHELL_LIVE = 1    # live  -> -1 health
SHELL_BLANK = 0   # blank -> no damage
# shell_skip is an action (eject shell without firing), see Shotgun.skip()

MAX_SHELLS = 8
MIN_SHELLS = 2
MAX_STAGE = 3


class Shotgun:
    def __init__(self):
        # ---- state coming from the game (set by game, read by shotgun) ----
        self.game_started = False
        self.stage = 0
        self.current_side = 0          # whose turn it is (number from game)

        # ---- state of the shotgun ----
        self._load = []                # load order: index 0 = 1st shell
        self.total_shells = 0          # amount of total shells in this load
        self.live_total = 0
        self.blank_total = 0
        self.items_per_side = 0        # number of items to give after new load

    # ================= read-only variables for other files =================
    @property
    def load_order(self):
        """Copy of the current load: [1st, 2nd, ... 8th]."""
        return list(self._load)

    @property
    def shells_left(self):
        return len(self._load)

    @property
    def live_left(self):
        return self._load.count(SHELL_LIVE)

    @property
    def blank_left(self):
        return self._load.count(SHELL_BLANK)

    @property
    def current_shell(self):
        """1st shell in the chamber (SHELL_LIVE / SHELL_BLANK) or None."""
        return self._load[0] if self._load else None

    @property
    def is_empty(self):
        return not self._load

    @property
    def damage(self):
        """Health lost if the current shell is fired."""
        return 1 if self.current_shell == SHELL_LIVE else 0

    # ================= game -> shotgun =================
    def set_game_state(self, started=None, stage=None, current_side=None):
        """Game calls this to give the shotgun its info."""
        if started is not None:
            self.game_started = bool(started)
        if stage is not None:
            self.stage = int(stage)
        if current_side is not None:
            self.current_side = current_side

    # ================= checks =================
    def check_game_start(self):
        return self.game_started

    def check_shells(self):
        """True when no shells are left (a new load is needed)."""
        return self.is_empty

    def check_stage(self):
        return 1 <= self.stage <= MAX_STAGE

    def can_make_new_load(self):
        """Everything yes -> new load is allowed."""
        return self.check_game_start() and self.check_shells() and self.check_stage()

    # ================= new load =================
    def amount_shotgun_maker(self):
        """Random amount of total shells (2..8)."""
        return random.randint(MIN_SHELLS, MAX_SHELLS)

    def new_load(self):
        """
        Make a new load if allowed. Returns a dict, or None if checks failed.
        The returned 'items' number is how many items the game should give.
        """
        if not self.can_make_new_load():
            return None

        self.total_shells = self.amount_shotgun_maker()
        # at least 1 live and 1 blank
        self.live_total = random.randint(1, self.total_shells - 1)
        self.blank_total = self.total_shells - self.live_total

        load = [SHELL_LIVE] * self.live_total + [SHELL_BLANK] * self.blank_total
        random.shuffle(load)
        self._load = load

        self.items_per_side = random.randint(1, 5)   # number of items to give

        return {
            "total": self.total_shells,
            "live": self.live_total,
            "blank": self.blank_total,
            "items": self.items_per_side,
        }

    # ================= actions =================
    def shoot(self):
        """Fire: takes the 1st shell out and returns it (None if empty)."""
        if self.is_empty:
            return None
        return self._load.pop(0)

    def skip(self):
        """shell_skip: eject the current shell without firing; returns it."""
        return self.shoot()

    def reset(self):
        self._load = []
        self.total_shells = self.live_total = self.blank_total = 0
        self.items_per_side = 0


# single shared instance - other files do: from shotgun import shotgun
shotgun = Shotgun()


if __name__ == "__main__":
    shotgun.set_game_state(started=True, stage=1, current_side=0)
    print("New load:", shotgun.new_load())
    print("Order:", shotgun.load_order)
    while not shotgun.is_empty:
        print("Current:", shotgun.current_shell, "| left:", shotgun.shells_left)
        shotgun.shoot()
    print("Empty -> can make new load:", shotgun.can_make_new_load())
