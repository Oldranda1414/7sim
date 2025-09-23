from card import Guild
from load.generics import load_generics

def load_guild(card_data) -> Guild:
    name, cost, required_icon = load_generics(card_data)  
    return Guild(name, cost, required_icon)
