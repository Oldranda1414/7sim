from load.cards import load_cards

def main():
    for era in range(1,4):
        for i in range (3, 8):
            if era == 3:
                print(f"era {era} cards for {i} players count: {len(load_cards(era, i)) + 2+i}. should be {7*i}")
            else:
                print(f"era {era} cards for {i} players count: {len(load_cards(era, i))}. should be {7*i}")

if __name__ == "__main__":
    main()
