from engine.card import CivilBuilding, CommercialBuilding
from load.cards import load_all_cards, load_guild_cards
from stats.util import get_rp
from stats.value.blue_value import get_value as get_civil_value
from stats.value.yellow_value import get_value as get_commercial_value
from stats.value.red_value import print_and_get_value as print_and_get_red_values


def average(values: list[float]):
    return sum(values)/len(values)

def main():
    base_cards = load_all_cards(7)
    guild_cards = load_guild_cards()

    arena_card = [card for card in base_cards if card.name == "Arena"][0]
    manual_yellow: dict[str, float] = {
            arena_card.name: 6.0 / get_rp(arena_card.cost)
        }

    blue_card_value: dict[str, float] = {}
    yellow_card_value: dict[str, float] = manual_yellow.copy()
    base_card_value: dict[str, float] = {**blue_card_value, **yellow_card_value}

    for card in base_cards:
        if isinstance(card, CivilBuilding):
            base_card_value[card.name] = get_civil_value(card)
            blue_card_value[card.name] = base_card_value[card.name]
        elif isinstance(card, CommercialBuilding):
            if len(card.gains) != 0:
                base_card_value[card.name] = get_commercial_value(card)
                yellow_card_value[card.name] = base_card_value[card.name]

    print("Blue card values:")
    for name, value in blue_card_value.items():
        print(f"    {name}: {value}")
    println()
    print(f"    average card value: {average(list(blue_card_value.values()))}")
    for card_name in ["Altar", "Theater", "Well", "Baths"]:
        blue_card_value.pop(card_name)
    print(f"    average card value removing first era cards: {average(list(blue_card_value.values()))}")
    println()

    print("yellow card values:")
    for name, value in yellow_card_value.items():
        print(f"    {name}: {value}")
    print("")
    print(f"    average card value: {average(list(yellow_card_value.values()))}")
    println()

    print("red card values, it's complicated:")
    red_card_value = print_and_get_red_values()
    # adding to final dict
    base_card_value = {**base_card_value, **red_card_value}
    println()

def println():
    print("")

