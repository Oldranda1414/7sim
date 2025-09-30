from engine.card import CommercialBuilding
from engine.card_type import Type
from engine.gain import Coin, Condition
from stats.util import get_rp

def get_value(card: CommercialBuilding):
    if get_rp(card.cost) == 0:
        return _calculate_victory_points(card) + 1
    return _calculate_victory_points(card) / get_rp(card.cost)

average_cards = {
        Type.RAW_MATERIAL: 3.58,
        Type.MANUFACTURED_GOOD: 1.80,
        Type.MILITARY_STRUCTURE: 3.31,
        Type.SCIENTIFIC_STRUCTURE: 3.66,
        Type.CIVIC_STRUCTURE: 3.62,
        Type.COMMERCIAL_STRUCTURE: 3.53,
        Type.GUILD: 1.44
        }

def _calculate_victory_points(card: CommercialBuilding) -> float:
    if len(card.gains) == 0:
        raise ValueError("cannot calculate victory points of commercial card with no gain effect")
    count = 0
    for gain in card.gains:
        prize = gain.prize
        mult = gain.multiplier
        if mult:
            prize *= average_cards[mult.card_type]
            if mult.condition == Condition.NEIGHBOR:
                prize *= 2
        if isinstance(gain.prize, Coin):
            prize /= 3
        count += prize
    return count
