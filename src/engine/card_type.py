from enum import Enum

from engine.card import Card, BasicMaterial, CivilBuilding, CommercialBuilding, ManufacturedProduct, MilitaryBuilding, ScientificBuilding, Guild

class Type(str, Enum):
    RAW_MATERIAL = "raw_material"
    MANUFACTURED_GOOD = "manufactured_good"
    CIVIC_STRUCTURE = "civic_structure"
    COMMERCIAL_STRUCTURE = "commercial_structure"
    MILITARY_STRUCTURE = "military_structure"
    SCIENTIFIC_STRUCTURE = "scientific_structure"
    GUILD = "guild"

def card_type(card: Card) -> "Type":
    if isinstance(card, BasicMaterial):
        return Type.RAW_MATERIAL
    if isinstance(card, ManufacturedProduct):
        return Type.MANUFACTURED_GOOD
    if isinstance(card, MilitaryBuilding):
        return Type.MILITARY_STRUCTURE
    if isinstance(card, CivilBuilding):
        return Type.CIVIC_STRUCTURE
    if isinstance(card, ScientificBuilding):
        return Type.SCIENTIFIC_STRUCTURE
    if isinstance(card, CommercialBuilding):
        return Type.COMMERCIAL_STRUCTURE
    if isinstance(card, Guild):
        return Type.GUILD
    raise ValueError("unrecognized card type")

def from_color(color: str) -> Type:
    if color == "brown":
        return Type.RAW_MATERIAL
    elif color == "grey":
        return Type.MANUFACTURED_GOOD
    elif color == "red":
        return Type.MILITARY_STRUCTURE
    elif color == "blue":
        return Type.CIVIC_STRUCTURE
    elif color == "green":
        return Type.SCIENTIFIC_STRUCTURE
    elif color == "yellow":
        return Type.COMMERCIAL_STRUCTURE
    elif color == "purple":
        return Type.GUILD
    raise ValueError("invalid value for argument 'color'")

def card_colors() -> list[str]:
    return [
            "brown",
            "grey",
            "red",
            "blue",
            "green",
            "yellow",
            "purple"
            ]
