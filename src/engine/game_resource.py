from enum import Enum

class Resource(str, Enum):
    WOOD = "wood"
    ORE = "ore"
    BRICK = "brick"
    STONE = "stone"
    GLASS = "glass"
    PAPYRUS = "papyrus"
    TEXTILES = "textiles"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

class ResourceType(str, Enum):
    BASE = "base"
    RARE = "rare"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

def resource_type(resource: Resource) -> ResourceType:
    rare_resources = [Resource.GLASS, Resource.PAPYRUS, Resource.TEXTILES]
    if resource in rare_resources:
        return ResourceType.RARE
    return ResourceType.BASE
