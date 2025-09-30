from engine.card import Guild
from stats.util import get_rp
from stats.value.util import calculate_gain_VP

def get_value(card: Guild):
    if get_rp(card.cost) == 0:
        return calculate_gain_VP(card) + 1
    return calculate_gain_VP(card) / get_rp(card.cost)

