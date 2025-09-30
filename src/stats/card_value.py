from engine.card import CivilBuilding, CommercialBuilding, Guild
from load.cards import load_all_cards, load_guild_cards
from stats.util import get_rp
from stats.value.blue_value import get_value as get_civil_value
from stats.value.yellow_value import get_value as get_commercial_value
from stats.value.red_value import print_and_get_value as print_and_get_red_value
from stats.value.purple_value import get_value as get_purple_value


def average(values: list[float]):
    return sum(values)/len(values)

def main():
    base_cards = load_all_cards(7)
    guild_cards = load_guild_cards()

    arena_card = [card for card in base_cards if card.name == "Arena"][0]
    manual_yellow: dict[str, float] = {
            arena_card.name: 6 / get_rp(arena_card.cost)
        }

    decorators_card = [card for card in guild_cards if card.name == "Decorators Guild"][0]
    builders_card = [card for card in guild_cards if card.name == "Builders Guild"][0]
    manual_purple: dict[str, float] = {
            decorators_card.name: 7 / get_rp(decorators_card.cost),
            builders_card.name: 9 / get_rp(builders_card.cost)
        }

    blue_card_value: dict[str, float] = {}
    yellow_card_value: dict[str, float] = manual_yellow.copy()
    purple_card_value: dict[str, float] = manual_purple.copy()
    base_card_value: dict[str, float] = {**blue_card_value, **yellow_card_value, **purple_card_value}

    for card in base_cards:
        if isinstance(card, CivilBuilding):
            base_card_value[card.name] = get_civil_value(card)
            blue_card_value[card.name] = base_card_value[card.name]
        elif isinstance(card, CommercialBuilding):
            if len(card.gains) != 0:
                base_card_value[card.name] = get_commercial_value(card)
                yellow_card_value[card.name] = base_card_value[card.name]

    # calculated seperately
    red_card_value = print_and_get_red_value(quiet=True)
    # adding to final dict
    base_card_value = {**base_card_value, **red_card_value}

    for guild_card in guild_cards:
        if isinstance(guild_card, Guild):
            if len(guild_card.gains) != 0:
                base_card_value[guild_card.name] = get_purple_value(guild_card)
                purple_card_value[guild_card.name] = base_card_value[guild_card.name]

    all_values = [blue_card_value, yellow_card_value, red_card_value, purple_card_value]
    colors = ["Blue", "Yellow", "Red", "Purple"]
    for color, values in zip(colors, all_values):
        println()
        print(f"{color} card values:")
        for name, value in values.items():
            print(f"    {name}: {value}")
        println()
        print(f"    average card value: {average(list(values.values()))}")

def println():
    print("")

