from engine.card import ScientificBuilding
from engine.science import Science
from load.cards import load_all_cards
from stats.util import get_rp
from stats.value.util import conditioned_print, conditioned_println

def print_and_get_value(quiet: bool = False) -> dict[str, float]:
    cards = set([card for card in load_all_cards(7) if isinstance(card, ScientificBuilding)])
    tech_cards: dict[Science, list[ScientificBuilding]] = {
            Science.WRITING: [],
            Science.ENGINEERING: [],
            Science.MATHEMATICS: []
        }
    for card in cards:
        tech_cards[card.science].append(card)
    average_cost: dict[Science, float]  = {
            Science.WRITING: 0.0,
            Science.ENGINEERING: 0.0,
            Science.MATHEMATICS: 0.0
        }
    conditioned_print(quiet, f"    Average cost per subject")
    for subject, subject_cards in tech_cards.items():
        for card in subject_cards:
            average_cost[subject] += get_rp(card.cost)
        average_cost[subject] /= len(subject_cards)
        conditioned_print(quiet, f"        {subject}: {average_cost[subject]}")
        conditioned_println(quiet)

    green_card_value: dict[str, float] = {str(science): (4 / cost) for science, cost in average_cost.items()}

    return green_card_value
