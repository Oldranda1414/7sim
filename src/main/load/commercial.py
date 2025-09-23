from card import CommercialBuilding
from load.generics import load_generics

def load_commercial_building(card_data) -> CommercialBuilding:
    name, cost, required_icon = load_generics(card_data)  
    return CommercialBuilding(name, cost, required_icon)
