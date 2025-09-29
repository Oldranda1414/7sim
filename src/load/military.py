from engine.card import MilitaryBuilding
from load.generics import load_generics

def load_military_building(card_data) -> MilitaryBuilding:
    name, cost, required_icon = load_generics(card_data)  
    military_strenght = card_data["military"]
    return MilitaryBuilding(name, cost, required_icon, military_strenght)
