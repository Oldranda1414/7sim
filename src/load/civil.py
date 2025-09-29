from engine.card import CivilBuilding
from load.generics import load_generics

def load_civil_building(card_data) -> CivilBuilding:
    name, cost, required_icon = load_generics(card_data)  
    victory_points = card_data["victory"]
    return CivilBuilding(name, cost, required_icon, victory_points)
