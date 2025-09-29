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
