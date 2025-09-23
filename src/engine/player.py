from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.card import Card
    from engine.city import City
    from engine.strategy import Strategy


class Player:
    def __init__(self, strategy: "Strategy", city: "City"):
        self.strategy = strategy
        self.hand: list["Card"] = []
        self.city = city

    def execute_turn(self) -> list["Card"]:
        next_card = self.strategy.choose_next_card(self)
        self._play_card(next_card)
        self.hand.remove(next_card)
        return self.hand

    def draw_new_hand(self, new_hand: list["Card"]):
        self.hand = new_hand

    def _play_card(self, card: "Card"):
        pass
