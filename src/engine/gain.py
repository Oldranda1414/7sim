from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.card_type import Type

class Coin(int):
    pass
class VictoryPoint(int):
    pass

class Condition(Enum):
    OWN = "own"
    NEIGHBOR = "neighbor"

class Multiplier():
    def __init__(self, condition: Condition, card_type: "Type"):
        self.condition = condition
        self.card_type = card_type

class Gain():
    def __init__(self, prize: Coin | VictoryPoint, multiplier: Multiplier | None = None):
        self.prize = prize 
        self.multiplier = multiplier

