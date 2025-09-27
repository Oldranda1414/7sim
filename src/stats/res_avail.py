from load.cards import load_all_cards
from engine.card import BasicMaterial, ManufacturedProduct

def main():
    for player_number in range(3,8):
        cards = load_all_cards(player_number)
        base_res_avail = 0
        rare_res_avail = 0
        for card in cards:
            if isinstance(card, BasicMaterial):
                base_res_avail += len(card.production.product[0])
            if isinstance(card, ManufacturedProduct):
                rare_res_avail += len(card.production.product[0])
        print_results(player_number, base_res_avail, rare_res_avail)

def print_results(player_number: int, base_res_availability: int, rare_res_availability: int):
    result = f"in a game with {player_number} players there are:\n {base_res_availability/player_number} base resources per player\n {rare_res_availability/player_number} rare resources per player\n {base_res_availability/rare_res_availability} base resource per rare resource available"
    print(result)
