import matplotlib.pyplot as plt
import numpy as np
from engine.card import ScientificBuilding
from engine.science import Science
from load.cards import load_all_cards

def collect_science_data():
    """Collect number of scientific buildings by science type for each player count"""
    player_counts = list(range(3, 8))
    techs: list[dict[Science, int]] = []

    for player_number in player_counts:
        player_tech: dict[Science, int] = {
            Science.WRITING: 0,
            Science.ENGINEERING: 0,
            Science.MATHEMATICS: 0
        }
        tech_cards = [
            card for card in load_all_cards(player_number) 
            if isinstance(card, ScientificBuilding)
        ]
        for card in tech_cards:
            player_tech[card.science] += 1

        techs.append(player_tech)
    
    return player_counts, techs

def create_science_chart(player_counts, techs):
    """Create grouped bar chart showing number of scientific buildings per science type"""
    fig, ax = plt.subplots(figsize=(12, 7))

    sciences = [Science.WRITING, Science.ENGINEERING, Science.MATHEMATICS]
    labels = [s.name.capitalize() for s in sciences]  # "Writing", "Engineering", "Mathematics"
    colors = ["skyblue", "lightcoral", "lightgreen"]

    x = np.arange(len(player_counts))  # positions for each player count
    width = 0.25

    # Draw one set of bars for each science type
    bars = []
    for i, science in enumerate(sciences):
        values = [player_tech[science] for player_tech in techs]
        bar = ax.bar(x + i*width - width, values, width, 
                     label=labels[i], color=colors[i], alpha=0.8)
        bars.append(bar)

    # Customize chart
    ax.set_xlabel("Number of Players", fontsize=12, fontweight="bold")
    ax.set_ylabel("Number of Science Buildings", fontsize=12, fontweight="bold")
    ax.set_title("Scientific Buildings by Type and Player Count", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(player_counts)
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")

    # Add value labels
    def add_value_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                   f"{height}", ha="center", va="bottom", fontsize=9)

    for barset in bars:
        add_value_labels(barset)

    plt.tight_layout()
    return fig

def main():
    player_counts, techs = collect_science_data()
    fig = create_science_chart(player_counts, techs)

    save_dir = "src/stats/assets/tech_balance/"
    fig.savefig(save_dir + "tech_balance.png", dpi=300, bbox_inches="tight")

    # Print summary
    print("\n=== Science Building Availability ===")
    for pc, player_tech in zip(player_counts, techs):
        print(f"\n{pc} players:")
        for tech, number in player_tech.items():
            print(f"  {tech.name.capitalize()}: {number}")

if __name__ == "__main__":
    main()
