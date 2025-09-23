from enum import Enum

class Resource(str, Enum):
    WOOD = "wood"
    ORE = "ore"
    CLAY = "clay"
    BRICK = "brick"
    STONE = "stone"
    GLASS = "glass"
    PAPYRUS = "papyrus"
    TEXTILES = "textiles"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)
