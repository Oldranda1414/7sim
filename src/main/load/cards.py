import json
import copy

from card import Card
from card_type import Type
from load.raw_material import load_raw_material
from load.manufactory import load_manufactory
from load.military import load_military_building
from load.civil import load_civil_building
from load.scientific import load_scientific_building
from load.commercial import load_commercial_building
from load.guild import load_guild

# card info taken from : https://7-wonders.fandom.com/wiki/List_of_Cards#Overview
CARD_REGISTRY_PATH = "./src/main/assets/cards.json"
ERA_REGISTRY_PATH = "./src/main/assets/era"

def load_cards(era: int, player_number: int) -> list[Card]:
    with open(CARD_REGISTRY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    card_registry: dict[str, Card] = {}
    for card in data["cards"]:
        card = _load_card(card)
        card_registry[card.name] = card

    with open(_get_era_resitry_path(era), "r", encoding="utf-8") as f:
        data = json.load(f)
    
    cards: list[Card] = []
    for card in data["era"]:
        name = card["name"]
        number = card["number"][player_number - 3]
        for _ in range(number):
            cards.append(copy.deepcopy(card_registry[name]))
    return cards

def _get_era_resitry_path(era_number: int) -> str:
    return f"{ERA_REGISTRY_PATH}/{era_number}.json"

def _load_card(card_data) -> Card:
    card_type=Type[card_data["type"]]
    if card_type == Type.RAW_MATERIAL:
        return load_raw_material(card_data)
    if card_type == Type.MANUFACTURED_GOOD:
        return load_manufactory(card_data)
    if card_type == Type.MILITARY_STRUCTURE:
        return load_military_building(card_data)
    if card_type == Type.CIVIC_STRUCTURE:
        return load_civil_building(card_data)
    if card_type == Type.SCIENTIFIC_STRUCTURE:
        return load_scientific_building(card_data)
    if card_type == Type.COMMERCIAL_STRUCTURE:
        return load_commercial_building(card_data)
    if card_type == Type.GUILD:
        return load_guild(card_data)
    raise ValueError("unrecognized card type")
