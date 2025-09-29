import os
import matplotlib.pyplot as plt
import numpy as np
from load.cards import load_all_cards
from engine.card_type import Type, card_type as get_card_type  # renamed to avoid shadowing

def collect_card_type_data():
    """Collect card type distribution data for all player counts"""
    player_counts = list(range(3, 8))  # [3,4,5,6,7]

    # Initialize storage for counts per type per player count
    card_types = {
        Type.RAW_MATERIAL: [],
        Type.MANUFACTURED_GOOD: [],
        Type.CIVIC_STRUCTURE: [],
        Type.COMMERCIAL_STRUCTURE: [],
        Type.MILITARY_STRUCTURE: [],
        Type.SCIENTIFIC_STRUCTURE: [],
        Type.GUILD: []
    }

    total_cards_per_player = []
    type_composition = {t: [] for t in card_types.keys()}

    for player_number in player_counts:
        cards = load_all_cards(player_number)
        count = {t: 0 for t in card_types.keys()}

        for card in cards:
            c_type = get_card_type(card)
            if c_type in count:
                count[c_type] += 1

        # Add guild cards (number of players + 2)
        guild_count = player_number + 2
        count[Type.GUILD] += guild_count

        # Total cards includes guilds
        total_cards = len(cards) + guild_count

        # Cards per player (on average) for this player count
        total_cards_per_player.append(total_cards / player_number if player_number > 0 else 0.0)

        for t in card_types.keys():
            card_types[t].append(count[t])
            if total_cards > 0:
                type_composition[t].append(count[t] / total_cards * 100.0)
            else:
                type_composition[t].append(0.0)

    return {
        'player_counts': player_counts,
        'card_types': card_types,
        'total_cards_per_player': total_cards_per_player,
        'type_composition': type_composition
    }

def _center_offsets(num_bars, width):
    """Return offsets for grouped bars to be centered at x indices."""
    center = (num_bars - 1) / 2.0
    return [width * (i - center) for i in range(num_bars)]

default_map = {
    Type.RAW_MATERIAL: '#8B4513',         # Brown
    Type.MANUFACTURED_GOOD: '#808080',    # Grey
    Type.CIVIC_STRUCTURE: '#1E90FF',      # Blue
    Type.COMMERCIAL_STRUCTURE: '#FFD700', # Yellow
    Type.MILITARY_STRUCTURE: '#DC143C',   # Red
    Type.SCIENTIFIC_STRUCTURE: '#32CD32', # Green
    Type.GUILD: '#800080' # Purple
}
cmap = plt.get_cmap('tab10')

def get_color(card_type, i=0):
    """Return color for a card type, fallback to colormap if not in default_map."""
    return default_map.get(card_type, cmap(i % 10))

def get_colors(types):
    """Return colors for a sequence of card types."""
    return [get_color(t, i) for i, t in enumerate(types)]

def create_card_type_distribution_chart(data):
    """Create chart for card type distribution with grouped bars"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))
    fig.suptitle('Card Type Distribution Analysis', fontsize=16, fontweight='bold')

    player_counts = data['player_counts']
    card_types = data['card_types']
    type_composition = data['type_composition']

    # Subplot 1: Absolute counts with grouped bars
    x = np.arange(len(player_counts))
    width = 0.12
    types = list(card_types.keys())

    # Choose colors dynamically (one per type)
    types = list(card_types.keys())
    colors = get_colors(types)
    if len(types) > len(colors):
        # fallback to a colormap if more types exist
        colors = [cmap(i % 10) for i in range(len(types))]
    else:
        colors = colors[:len(types)]

    offsets = _center_offsets(len(types), width)

    for i, (card_type_key, color) in enumerate(zip(types, colors)):
        offset = offsets[i]
        bars = ax1.bar(x + offset, card_types[card_type_key], width,
                       label=card_type_key.name.replace('_', ' ').title(),
                       color=color, alpha=0.8)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax1.text(bar.get_x() + bar.get_width() / 2., height + 0.2,
                         f'{int(height)}', ha='center', va='bottom', fontsize=8)

    ax1.set_xlabel('Number of Players', fontweight='bold')
    ax1.set_ylabel('Total Card Count', fontweight='bold')
    ax1.set_title('Card Type Distribution - Absolute Counts\n(Grouped Bars)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(player_counts)
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3, axis='y')

    # Subplot 2: Percentage composition with grouped bars
    for i, (card_type_key, color) in enumerate(zip(types, colors)):
        offset = offsets[i]
        bars = ax2.bar(x + offset, type_composition[card_type_key], width,
                       label=card_type_key.name.replace('_', ' ').title(),
                       color=color, alpha=0.8)

        # Add percentage labels
        for bar, percentage in zip(bars, type_composition[card_type_key]):
            if percentage > 2:  # Only label if significant percentage
                ax2.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 1,
                         f'{percentage:.1f}%', ha='center', va='bottom',
                         fontsize=8, fontweight='bold')

    ax2.set_xlabel('Number of Players', fontweight='bold')
    ax2.set_ylabel('Percentage Composition (%)', fontweight='bold')
    ax2.set_title('Card Type Distribution - Percentage Composition\n(Grouped Bars)')
    ax2.set_xticks(x)
    ax2.set_xticklabels(player_counts)
    ax2.set_ylim(0, 100)
    ax2.grid(True, alpha=0.3, axis='y')

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # keep room for suptitle
    return fig

def create_card_type_trends_chart(data):
    """Create chart showing trends of card types across player counts"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Card Type Distribution Trends', fontsize=16, fontweight='bold')

    player_counts = data['player_counts']
    card_types = data['card_types']
    type_composition = data['type_composition']

    types = list(card_types.keys())

    # Colors/markers sized to types
    types = list(card_types.keys())
    colors = get_colors(types)
    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', 'X', '*'][:len(types)]

    for card_type_key, color, marker in zip(types, colors, markers):
        ax1.plot(player_counts, card_types[card_type_key],
                 marker=marker, linewidth=2, markersize=8,
                 label=card_type_key.name.replace('_', ' ').title(),
                 color=color)

    ax1.set_xlabel('Number of Players', fontweight='bold')
    ax1.set_ylabel('Total Card Count', fontweight='bold')
    ax1.set_title('Card Type Count Trends')
    ax1.set_xticks(player_counts)
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3)

    # Percentage trends
    for card_type_key, color, marker in zip(types, colors, markers):
        ax2.plot(player_counts, type_composition[card_type_key],
                 marker=marker, linewidth=2, markersize=8,
                 label=card_type_key.name.replace('_', ' ').title(),
                 color=color)

    ax2.set_xlabel('Number of Players', fontweight='bold')
    ax2.set_ylabel('Percentage Composition (%)', fontweight='bold')
    ax2.set_title('Card Type Percentage Trends')
    ax2.set_xticks(player_counts)
    ax2.set_ylim(0, 100)
    ax2.grid(True, alpha=0.3)
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig

def create_card_type_comparison_chart(data):
    """Create chart comparing card availability per player"""
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle('Cards per player by type', fontsize=16, fontweight='bold')

    player_counts = data['player_counts']
    card_types = data['card_types']

    # Cards per player by type (grouped bars)
    x = np.arange(len(player_counts))
    width = 0.12
    types = list(card_types.keys())
    colors = get_colors(types)
    offsets = _center_offsets(len(types), width)

    for i, (card_type_key, color) in enumerate(zip(types, colors)):
        offset = offsets[i]
        cards_per_player = [count / players if players > 0 else 0.0
                            for count, players in zip(card_types[card_type_key], player_counts)]
        bars = ax.bar(x + offset, cards_per_player, width,
                       label=card_type_key.name.replace('_', ' ').title(),
                       color=color, alpha=0.8)

        for bar, value in zip(bars, cards_per_player):
            if value > 0.1:  # Only label if significant
                ax.text(bar.get_x() + bar.get_width() / 2., value + 0.02,
                         f'{value:.2f}', ha='center', va='bottom', fontsize=7)

    ax.set_xlabel('Number of Players', fontweight='bold')
    ax.set_ylabel('Cards per Player', fontweight='bold')
    ax.set_title('Cards per Player by Type\n(Grouped Bars)')
    ax.set_xticks(x)
    ax.set_xticklabels(player_counts)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig

def create_comprehensive_card_analysis_plot(data):
    """Create comprehensive analysis plot with multiple subplots"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Comprehensive Card Type Distribution Analysis', fontsize=18, fontweight='bold')

    ax1, ax2, ax3, ax4 = axes.flatten()

    player_counts = data['player_counts']
    card_types = data['card_types']
    type_composition = data['type_composition']
    total_cards_per_player = data['total_cards_per_player']

    # Subplot 1: Absolute counts heatmap
    types_list = list(card_types.keys())
    type_names = [t.name.replace('_', ' ').title() for t in types_list]
    count_matrix = np.array([card_types[card_type] for card_type in types_list])

    im1 = ax1.imshow(count_matrix, cmap='Blues', aspect='auto')
    ax1.set_xlabel('Number of Players')
    ax1.set_ylabel('Card Types')
    ax1.set_title('Card Type Counts Heatmap')
    ax1.set_xticks(range(len(player_counts)))
    ax1.set_xticklabels(player_counts)
    ax1.set_yticks(range(len(types_list)))
    ax1.set_yticklabels(type_names)

    # Add count values to heatmap
    max_count = np.max(count_matrix) if count_matrix.size > 0 else 0
    for i in range(len(types_list)):
        for j in range(len(player_counts)):
            val = count_matrix[i, j]
            color = "white" if max_count > 0 and val > max_count / 2 else "black"
            ax1.text(j, i, f'{int(val)}', ha="center", va="center", color=color, fontweight='bold')

    # Subplot 2: Percentage composition heatmap
    comp_matrix = np.array([type_composition[card_type] for card_type in types_list])
    im2 = ax2.imshow(comp_matrix, cmap='RdPu', aspect='auto', vmin=0, vmax=100)
    ax2.set_xlabel('Number of Players')
    ax2.set_ylabel('Card Types')
    ax2.set_title('Card Type Composition Heatmap (%)')
    ax2.set_xticks(range(len(player_counts)))
    ax2.set_xticklabels(player_counts)
    ax2.set_yticks(range(len(types_list)))
    ax2.set_yticklabels(type_names)

    for i in range(len(types_list)):
        for j in range(len(player_counts)):
            val = comp_matrix[i, j]
            color = "white" if val > 50 else "black"
            ax2.text(j, i, f'{val:.1f}%', ha="center", va="center", color=color, fontweight='bold')

    # Subplot 3: Total cards per player trend
    ax3.plot(player_counts, total_cards_per_player, 'o-', linewidth=3, markersize=8, color='#4682B4')
    ax3.set_xlabel('Number of Players')
    ax3.set_ylabel('Cards per Player')
    ax3.set_title('Total Cards Available per Player')
    ax3.set_xticks(player_counts)
    ax3.grid(True, alpha=0.3)

    for i, value in enumerate(total_cards_per_player):
        ax3.annotate(f'{value:.2f}', (player_counts[i], value),
                     textcoords="offset points", xytext=(0, 10), ha='center', fontweight='bold')

    # Subplot 4: Dominant card types (top 3 for each player count)
    width = 0.25
    x = np.arange(len(player_counts))
    legend_labels = set()

    for i, player_count in enumerate(player_counts):
        # Get top 3 card types for this player count (by percentage)
        type_percentages = [(card_type, type_composition[card_type][i]) for card_type in types_list]
        type_percentages.sort(key=lambda x: x[1], reverse=True)
        top_3 = type_percentages[:3]

        for j, (card_type_key, percentage) in enumerate(top_3):
            offset = width * (j - 1)
            color = get_color(card_type_key, j)
            label = None
            if card_type_key not in legend_labels:
                label = card_type_key.name.replace('_', ' ').title()
                legend_labels.add(card_type_key)
            else:
                label = ""
            ax4.bar(i + offset, percentage, width,
                    color=color, alpha=0.8,
                    label=label)

    ax4.set_xlabel('Number of Players')
    ax4.set_ylabel('Percentage (%)')
    ax4.set_title('Top 3 Card Types by Player Count')
    ax4.set_xticks(range(len(player_counts)))
    ax4.set_xticklabels(player_counts)
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig

def create_average_card_distribution_chart(data):
    """Create bar chart showing average cards per player for each card type across all player counts"""
    player_counts = data['player_counts']
    card_types = data['card_types']

    # Calculate average (cards per player) for each card type across all player counts:
    # average_per_type = mean over player_counts of (count_for_that_player_count / players)
    average_per_type = {}
    for card_type in card_types.keys():
        per_player_values = [
            (count / players) if players > 0 else 0.0
            for count, players in zip(card_types[card_type], player_counts)
        ]
        average_per_type[card_type] = float(np.mean(per_player_values)) if per_player_values else 0.0

    # Sort by average value (descending)
    sorted_types = sorted(average_per_type.items(), key=lambda x: x[1], reverse=True)
    types_sorted = [item[0] for item in sorted_types]
    averages_sorted = [item[1] for item in sorted_types]

    fig, ax = plt.subplots(figsize=(12, 8))

    # Define color mapping based on card type (fallback to colormap if missing)
    colors = get_colors(types_sorted)

    bars = ax.bar(range(len(types_sorted)), averages_sorted, color=colors, alpha=0.8)

    type_names = [t.name.replace('_', ' ').title() for t in types_sorted]
    ax.set_xlabel('Card Type', fontweight='bold')
    ax.set_ylabel('Average Cards per Player', fontweight='bold')
    ax.set_title('Average Card Distribution per Player\n(Averaged Across All Player Counts)',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(types_sorted)))
    ax.set_xticklabels(type_names, rotation=45, ha='right')
    ax.grid(True, alpha=0.3, axis='y')

    for bar, value in zip(bars, averages_sorted):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height + 0.01,
                f'{value:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig

def main():
    # Collect data
    data = collect_card_type_data()

    # Create individual charts
    fig1 = create_card_type_distribution_chart(data)
    fig2 = create_card_type_trends_chart(data)
    fig3 = create_card_type_comparison_chart(data)
    fig4 = create_comprehensive_card_analysis_plot(data)
    fig5 = create_average_card_distribution_chart(data)  # New chart

    # Save the plots (ensure directory exists)
    save_dir = "src/stats/assets/card_balance/"
    os.makedirs(save_dir, exist_ok=True)
    fig1.savefig(os.path.join(save_dir, 'card_type_distribution.png'), dpi=300, bbox_inches='tight')
    fig2.savefig(os.path.join(save_dir, 'card_type_trends.png'), dpi=300, bbox_inches='tight')
    fig3.savefig(os.path.join(save_dir, 'card_availability.png'), dpi=300, bbox_inches='tight')
    fig4.savefig(os.path.join(save_dir, 'comprehensive_card_analysis.png'), dpi=300, bbox_inches='tight')
    fig5.savefig(os.path.join(save_dir, 'average_card_distribution.png'), dpi=300, bbox_inches='tight')

    # Print summary statistics
    print("\n=== Card Type Distribution Summary ===")
    for i, players in enumerate(data['player_counts']):
        total_cards = sum([data['card_types'][t][i] for t in data['card_types'].keys()])
        print(f"\n{players} players:")
        print(f"  Total cards: {total_cards}")
        print(f"  Cards per player: {data['total_cards_per_player'][i]:.2f}")

        print("  Card Type Breakdown:")
        for card_type in data['card_types'].keys():
            count = data['card_types'][card_type][i]
            percentage = data['type_composition'][card_type][i]
            if count > 0:
                print(f"    {card_type.name.replace('_', ' ').title()}: {count} ({percentage:.1f}%)")

    # Calculate and print averages (cards per player per type averaged across player counts)
    average_per_type = {}
    for card_type in data['card_types'].keys():
        per_player_values = [
            (count / players) if players > 0 else 0.0
            for count, players in zip(data['card_types'][card_type], data['player_counts'])
        ]
        average_per_type[card_type] = float(np.mean(per_player_values)) if per_player_values else 0.0

    print(f"\n=== Average Card Distribution per Player (Across All Player Counts) ===")
    sorted_averages = sorted(average_per_type.items(), key=lambda x: x[1], reverse=True)
    total_avg = sum(avg for _, avg in sorted_averages)
    for card_type, avg in sorted_averages:
        print(f"  {card_type.name.replace('_', ' ').title()}: {avg:.2f} cards per player")

    print(f"  Total average cards per player (sum over types): {total_avg:.2f}")

if __name__ == "__main__":
    main()
