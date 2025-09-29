from engine.production import Production
from engine.science import Science
from engine.cost import Cost

class Card:
    def __init__(self, name: str, cost: Cost, require_icon: str | None):
        self.name = name
        self.cost = cost
        # Remember that east and west both have the string "Trading Post" in require_icon of concats
        self.require_icon = require_icon

class BasicMaterial(Card):
    def __init__(self, name: str, cost: Cost, require_icon: str | None, production: Production):
        super().__init__(name, cost, require_icon)
        self.production = production

class ManufacturedProduct(Card):
    def __init__(self, name: str, cost: Cost, require_icon: str | None, production: Production):
        super().__init__(name, cost, require_icon)
        self.production = production

class MilitaryBuilding(Card):
    def __init__(self, name: str, cost: Cost, require_icon: str | None, military_strenght: int):
        super().__init__(name, cost, require_icon)
        self.military_strenght = military_strenght
        
class CivilBuilding(Card):
    def __init__(self, name: str, cost: Cost, require_icon: str | None, victory_points: int):
        super().__init__(name, cost, require_icon)
        self.victory_points = victory_points

class ScientificBuilding(Card):
    def __init__(self, name: str, cost: Cost, require_icon: str | None, science: Science):
        super().__init__(name, cost, require_icon)
        self.science = science

class CommercialBuilding(Card):
    def __init__(self, name: str, cost: Cost, require_icon: str | None):
        super().__init__(name, cost, require_icon)

class Guild(Card):
    def __init__(self, name: str, cost: Cost, require_icon: str | None):
        super().__init__(name, cost, require_icon)
