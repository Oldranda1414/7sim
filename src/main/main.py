from loader import load_cards

def main():
    era = 2
    for i in range (3, 8):
        print(f"era 1 cards for {i} players count: {len(load_cards(era, i))}. should be {7*i}")

if __name__ == "__main__":
    main()
