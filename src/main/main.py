from load.cards import load_cards
from card import BasicMaterial
from game_resource import Resource

def main():
    # testing around, derping stuff
    first_era_cards = load_cards(1,4)
    for card in first_era_cards:
        if isinstance(card, BasicMaterial):
            print(card.production.product)
    count_resource = sum(1 for card in first_era_cards if isinstance(card, BasicMaterial) and Resource.WOOD in card.production.product[0])
    print(f"{count_resource} resource cards in first era with 3 players")

if __name__ == "__main__":
    main()
