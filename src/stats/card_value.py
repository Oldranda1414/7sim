from engine.card import CivilBuilding
from load.cards import load_all_cards, load_guild_cards
from stats.value.blue_value import get_value as get_civil_value

def average(values: list[float]):
    return sum(values)/len(values)

def main():
    base_cards = load_all_cards(7)
    guild_cards = load_guild_cards()

    base_card_value: dict[str, float] = {}
    blue_card_value: dict[str, float] = {}

    for card in base_cards:
        if isinstance(card, CivilBuilding):
            base_card_value[card.name] = get_civil_value(card)
            blue_card_value[card.name] = base_card_value[card.name]

    print("Blue card values:")
    for name, value in base_card_value.items():
        print(f"    {name}: {value}")
    print("")
    print(f"    average card value: {average(list(blue_card_value.values()))}")
    for card_name in ["Altar", "Theater", "Well", "Baths"]:
        blue_card_value.pop(card_name)
    print(f"    average card value removing first era cards: {average(list(blue_card_value.values()))}")


