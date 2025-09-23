from enum import Enum

class Type(str, Enum):
    RAW_MATERIAL = "raw_material"
    MANUFACTURED_GOOD = "manufactured_good"
    CIVIC_STRUCTURE = "civic_structure"
    COMMERCIAL_STRUCTURE = "commercial_structure"
    MILITARY_STRUCTURE = "military_structure"
    SCIENTIFIC_STRUCTURE = "scientific_structure"
    GUILD = "guild"
