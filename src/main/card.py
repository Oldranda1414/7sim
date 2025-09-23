from card_type import Type
from game_resource import Resource
from effect import Effect
from icon import Icon

class Card:
    def __init__(self, name: str, card_type: Type, effect: Effect, cost: tuple[int, list[Resource]], give_icon: list[Icon], require_icon: Icon | None, era: int, player_number: int):
        if player_number < 3 or player_number > 7:
            raise ValueError("Player number requirement for cards must be in interval [3,7]")
        if era < 1 or era > 3:
            raise ValueError("card era must be in interval [1,3]")

        self.name = name
        self.type = card_type
        self.effect = effect
        self.cost = cost
        self.give_icon = give_icon
        self.require_icon = require_icon
        self.era = era
        self.player_number = player_number

    def __repr__(self):
        return f"<Card {self.name} (Era {self.era}, {self.type.value})>"
