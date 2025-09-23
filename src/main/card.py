from card_type import Type
from game_resource import Resource
from effect import Effect
from icon import Icon

class Card:
    def __init__(self, name: str, card_type: Type, effect: Effect, cost: tuple[int, list[Resource]], give_icon: list[Icon], require_icon: Icon | None):
        self.name = name
        self.type = card_type
        self.effect = effect
        self.cost = cost
        self.give_icon = give_icon
        self.require_icon = require_icon
