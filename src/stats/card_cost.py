from load.cards import load_cards
from engine.card import Card, Cost
from engine.game_resource import resource_type, ResourceType

def main():
    for player_number in range(3,8):
        print(f"For {player_number} players:")
        for era in range(1,4):
            total_cost = 0
            cards = load_cards(player_number, era)
            for card in cards:
                total_cost += _get_rp(card.cost)
            print(f"    Avarage resource points per card for {era} era: {total_cost/len(cards)}")

def _get_rp(cost: Cost) -> int:
    total = cost.money
    for resource in cost.resources:
        if resource_type(resource) == ResourceType.BASE:
            total += 1
        elif resource_type(resource) == ResourceType.RARE:
            total += 3
    return total
