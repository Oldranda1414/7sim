from loader import load_cards

def main():
    era1_path = "./src/main/assets/era1_cards.json"
    era2_path = "./assets/era2_cards.json"
    era3_path = "./assets/era3_cards.json"
    era1_cards = load_cards(era1_path) 
    # era2_cards = load_cards(era2_path) 
    # era3_cards = load_cards(era3_path) 
    print("era 1 cards total:",len(era1_cards), "should be 49")
    for i in range (3, 8):
        print(f"era 1 cards for {i} players count: {len([card for card in era1_cards if card.player_number <= i])}. should be {7*i}")
    # print(era2_cards[0])
    # print(era3_cards[-1])

if __name__ == "__main__":
    main()
