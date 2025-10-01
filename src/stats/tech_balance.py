from engine.card import ScientificBuilding
from engine.science import Science
from load.cards import load_all_cards

def main():
    techs: list[dict[Science, int]] = []
    for player_number in range(3,8):
        player_tech: dict[Science, int] = {
                Science.WRITING: 0,
                Science.ENGINEERING: 0,
                Science.MATHEMATICS: 0
            }
        tech_cards = [card for card in load_all_cards(player_number) if isinstance(card, ScientificBuilding)]
        for card in tech_cards:
            player_tech[card.science] += 1

        techs.append(player_tech)
    
    for player_tech in techs:
        for tech, number in player_tech.items():
            print(f"{tech}, {number}")
