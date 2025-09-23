from typing import Callable

from engine.player import Player
from engine.card import Card

class Strategy:
    def __init__(self, choose_next_card: Callable[[Player], Card]):
        self._choose_next_card = choose_next_card

    def choose_next_card(self, owner: Player) -> Card:
        return self._choose_next_card(owner)

