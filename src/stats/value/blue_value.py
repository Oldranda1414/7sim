from engine.card import CivilBuilding
from stats.util import get_rp

def get_value(card: CivilBuilding):
    if get_rp(card.cost) == 0:
        return card.victory_points + 1
    return card.victory_points / get_rp(card.cost)

