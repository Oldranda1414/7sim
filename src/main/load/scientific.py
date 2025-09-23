from card import ScientificBuilding
from load.generics import load_generics
from science import Science

def load_scientific_building(card_data) -> ScientificBuilding:
    name, cost, required_icon = load_generics(card_data)  
    science = Science[card_data["science"]]
    return ScientificBuilding(name, cost, required_icon, science)
