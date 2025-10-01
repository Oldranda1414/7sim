from engine.card_type import Type
from engine.gain import PrizeType, Condition
from engine.card import CommercialBuilding, Guild

average_cards = {
        Type.RAW_MATERIAL: 3.58,
        Type.MANUFACTURED_GOOD: 1.80,
        Type.MILITARY_STRUCTURE: 3.31,
        Type.SCIENTIFIC_STRUCTURE: 3.66,
        Type.CIVIC_STRUCTURE: 3.62,
        Type.COMMERCIAL_STRUCTURE: 3.53,
        Type.GUILD: 1.44
        }


def calculate_gain_VP(card: Guild | CommercialBuilding) -> float:
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
        if gain.prize_type == PrizeType.COIN:
            prize /= 3
        count += prize
    return count

def conditioned_print(quiet: bool, args):
    if not quiet:
        print(args)
def conditioned_println(quiet: bool):
    if not quiet:
        print("")
