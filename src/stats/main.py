from stats.card_cost import main as card_cost
from stats.res_avail import main as res_avail
from stats.res_balance import main as res_balance
from stats.card_balance import main as card_balance
from stats.tech_balance import main as tech_balance
from stats.card_value import main as card_value

def generate_graphs():
    res_avail()
    res_balance()
    card_balance()
    card_cost()
    tech_balance()

def print_values():
    card_value()

def main():
    generate_graphs()
    print_values()

if __name__ == "__main__":
    main()
