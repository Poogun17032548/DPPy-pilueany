"""Data classes and exceptions used by the game."""

from constants import MAX_SLOTS


class DealerDead(Exception):
    pass


class PlayerDead(Exception):
    pass


class Side:
    """One participant: the player or the dealer."""

    def __init__(self, name):
        self.name = name
        self.hp = 0
        self.max_hp = 0
        self.items = [None] * MAX_SLOTS
        self.cuffed = False
        self.known = {}   # shell index (0 = current) -> LIVE / BLANK

    def reset_for_stage(self, max_hp):
        self.hp = self.max_hp = max_hp
        self.items = [None] * MAX_SLOTS
        self.cuffed = False
        self.known = {}

    def free_slots(self):
        return [i for i, item in enumerate(self.items) if item is None]

    def has(self, item):
        return item in self.items
