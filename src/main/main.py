from loader import load_cards

def main():
    era = 1
    era2_path = "./assets/era2_cards.json"
    era3_path = "./assets/era3_cards.json"
    # era2_cards = load_cards(era2_path) 
    # era3_cards = load_cards(era3_path) 
    for i in range (3, 8):
        print(f"era 1 cards for {i} players count: {len(load_cards(era, i))}. should be {7*i}")
    # print(era2_cards[0])
    # print(era3_cards[-1])

if __name__ == "__main__":
    main()
