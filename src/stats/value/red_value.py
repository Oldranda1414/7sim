from engine.card import MilitaryBuilding
from load.cards import load_cards
from stats.util import get_rp
from stats.value.util import conditioned_print, conditioned_println

def print_and_get_value(quiet: bool = False) -> dict[str, float]:
    player_averages = calculate_player_averages()
    era_averages: list[float] = []
    for i in range(len(player_averages[0])):
        military_sum = 0.0
        for eras in player_averages:
            military_sum += eras[i]
        era_averages.append(military_sum/5)

    conditioned_print(quiet, f"    Military Points per era per player")
    for index, era_average in enumerate(player_averages):
        conditioned_print(quiet, f"        For {index + 3} players")
        for index, value in enumerate(era_average):
            conditioned_print(quiet, f"            For {index} era: {value}")
    conditioned_println(quiet)

    conditioned_print(quiet, f"    Average Military Points per era per player")
    for index, era in enumerate(era_averages):
        conditioned_print(quiet, f"        For {index + 1} era: {round(era)} (from: {era})")
    conditioned_println(quiet)

    military_cards_values: list[dict[str, float]] = []
    military_VP: tuple[int, int, int] = (2,6,10)
    for era in range(3):
        military_cards_values.append({})
        for card in [card for card in load_cards(7, era + 1) if isinstance(card, MilitaryBuilding)]:
            # Sanity check print
            # conditioned_print(quiet, card.name)
            # conditioned_print(quiet, f"({military_VP[era]}/({era_averages[era]} + 1)) * {card.military_strenght} / {get_rp(card.cost)}")
            military_cards_values[era][card.name] =  (military_VP[era]/(era_averages[era] + 1)) * card.military_strenght / get_rp(card.cost)

    red_card_value: dict[str, float] = {}
    for era, era_values in enumerate(military_cards_values):
        conditioned_print(quiet, f"    For {era + 1} era:")
        for name, card_value in era_values.items():
            red_card_value[name] = card_value
            conditioned_print(quiet, f"        {name}: {card_value}")
    return red_card_value

def calculate_player_averages() -> list[list[float]]:
    player_averages: list[list[float]] = []
    for player_number in range(3,8):
        era_averages: list[float] = []
        for era in range(1,4):
            cards = [card for card in load_cards(player_number, era) if isinstance(card, MilitaryBuilding)]
            average = sum_military_power(cards) / player_number
            era_averages.append(average)
        player_averages.append(era_averages)
    return player_averages

def sum_military_power(cards: list[MilitaryBuilding]) -> int:
    result = 0
    for card in cards:
        result += card.military_strenght
    return result
