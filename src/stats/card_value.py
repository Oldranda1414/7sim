from engine.card import CivilBuilding, CommercialBuilding, Guild
from load.cards import load_all_cards, load_guild_cards, load_cards
from stats.util import get_rp
from stats.value.blue_value import get_value as get_blue_value
from stats.value.yellow_value import get_value as get_yellow_value
from stats.value.purple_value import get_value as get_purple_value
from stats.value.red_value import print_and_get_value as print_and_get_red_value
from stats.value.green_value import print_and_get_value as print_and_get_green_value


def average(values: list[float]):
    return sum(values)/len(values)

def main() -> None:
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
    all_card_value: dict[str, float] = {**blue_card_value, **yellow_card_value, **purple_card_value}

    for card in base_cards:
        if isinstance(card, CivilBuilding):
            all_card_value[card.name] = get_blue_value(card)
            blue_card_value[card.name] = all_card_value[card.name]
        elif isinstance(card, CommercialBuilding):
            if len(card.gains) != 0:
                all_card_value[card.name] = get_yellow_value(card)
                yellow_card_value[card.name] = all_card_value[card.name]

    # calculated seperately
    red_card_value = print_and_get_red_value(quiet=True)
    green_card_value = print_and_get_green_value(quiet=True)
    # adding to final dict
    all_card_value = {**all_card_value, **red_card_value, **green_card_value}

    for guild_card in guild_cards:
        if isinstance(guild_card, Guild):
            if len(guild_card.gains) != 0:
                all_card_value[guild_card.name] = get_purple_value(guild_card)
                purple_card_value[guild_card.name] = all_card_value[guild_card.name]

    all_values = [blue_card_value, yellow_card_value, red_card_value, purple_card_value, green_card_value]
    colors = ["Blue", "Yellow", "Red", "Purple", "Green"]
    average_card_values: dict[str, float] = {color: 0.0 for color in colors}
    for color, values in zip(colors, all_values):
        println()
        print(f"{color} card values:")
        for name, value in values.items():
            print(f"    {name}: {value}")
        println()
        average_card_values[color] = average(list(values.values()))
        print(f"    average card value: {average(list(values.values()))}")

    println()
    print(f"Final Averages:")
    for color, value in average_card_values.items():
        print(f"{color}: {value}")
    println()

    print("Best cards per era:")
    for era in range(1,4):
        print(f"    For {era} era")
        era_cards_names: set[str] = set([card.name for card in load_cards(7,era)])
        era_cards_values: dict[str, float] = {name: value for name, value in all_card_value.items() if name in era_cards_names}
        sorted_values = sorted(era_cards_values.items(), key=lambda x: x[1], reverse=True)
        for name, value in sorted_values:
            print(f"        {name}: {value}")

def println():
    print("")

