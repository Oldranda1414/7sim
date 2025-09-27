import matplotlib.pyplot as plt
import numpy as np
from load.cards import load_cards
from engine.card import Cost
from engine.game_resource import resource_type, ResourceType

def _get_rp(cost: Cost) -> int:
    total = cost.money
    for resource in cost.resources:
        if resource_type(resource) == ResourceType.BASE:
            total += 1
        elif resource_type(resource) == ResourceType.RARE:
            total += 3
    return total

def collect_cost_data():
    """Collect cost data for all player counts and eras"""
    player_counts = list(range(3, 8))
    eras = [1, 2, 3]
    
    # Data structures
    era_data = {era: [] for era in eras}
    overall_avg_data = []
    total_cards_per_player = []
    
    for player_number in player_counts:
        era_costs = {1: 0, 2: 0, 3: 0}
        era_card_counts = {1: 0, 2: 0, 3: 0}
        total_cost_all_eras = 0
        total_cards_all_eras = 0
        
        for era in eras:
            cards = load_cards(player_number, era)
            total_cost = 0
            for card in cards:
                cost_value = _get_rp(card.cost)
                total_cost += cost_value
                total_cost_all_eras += cost_value
                era_costs[era] += cost_value
                era_card_counts[era] += 1
                total_cards_all_eras += 1
            
            # Calculate average for this era
            if era_card_counts[era] > 0:
                era_avg = era_costs[era] / era_card_counts[era]
                era_data[era].append(era_avg)
            else:
                era_data[era].append(0)
        
        # Calculate overall average for this player count
        if total_cards_all_eras > 0:
            overall_avg = total_cost_all_eras / total_cards_all_eras
            overall_avg_data.append(overall_avg)
            total_cards_per_player.append(total_cards_all_eras)
        else:
            overall_avg_data.append(0)
            total_cards_per_player.append(0)
    
    return {
        'player_counts': player_counts,
        'eras': eras,
        'era_data': era_data,
        'overall_avg_data': overall_avg_data,
        'total_cards_per_player': total_cards_per_player
    }

def create_era_comparison_chart(data):
    """Create bar chart comparing costs across eras for each player count"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    player_counts = data['player_counts']
    eras = data['eras']
    era_data = data['era_data']
    
    # Set up bar positions
    x = np.arange(len(player_counts))
    width = 0.25
    
    # Create bars for each era
    bars1 = ax.bar(x - width, era_data[1], width, label='Era 1', color='lightblue', alpha=0.8)
    bars2 = ax.bar(x, era_data[2], width, label='Era 2', color='lightcoral', alpha=0.8)
    bars3 = ax.bar(x + width, era_data[3], width, label='Era 3', color='lightgreen', alpha=0.8)
    
    # Customize the chart
    ax.set_xlabel('Number of Players', fontsize=12, fontweight='bold')
    ax.set_ylabel('Average Resource Points per Card', fontsize=12, fontweight='bold')
    ax.set_title('Average Card Cost by Era and Player Count', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(player_counts)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    def add_value_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                   f'{height:.2f}', ha='center', va='bottom', fontsize=9)
    
    add_value_labels(bars1)
    add_value_labels(bars2)
    add_value_labels(bars3)
    
    # Add some analysis text
    max_cost = max(max(era_data[1]), max(era_data[2]), max(era_data[3]))
    ax.text(0.02, 0.98, f'Era Progression: Cost increases across eras',
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    return fig

def create_overall_average_chart(data):
    """Create bar chart for overall average cost per player count"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    player_counts = data['player_counts']
    overall_avg = data['overall_avg_data']
    total_cards = data['total_cards_per_player']
    
    # Create bars
    bars = ax.bar(player_counts, overall_avg, color='steelblue', alpha=0.7, width=0.6)
    
    # Customize the chart
    ax.set_xlabel('Number of Players', fontsize=12, fontweight='bold')
    ax.set_ylabel('Average Resource Points per Card', fontsize=12, fontweight='bold')
    ax.set_title('Overall Average Card Cost by Player Count\n(All Eras Combined)', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(player_counts)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, (bar, avg, count) in enumerate(zip(bars, overall_avg, total_cards)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
               f'{avg:.2f} RP', ha='center', va='bottom', fontweight='bold')
        # Add card count below
        ax.text(bar.get_x() + bar.get_width()/2., -0.1,
               f'{count} cards', ha='center', va='top', fontsize=9, color='gray')
    
    # Add trend line
    trend_x = np.array(player_counts)
    trend_y = np.array(overall_avg)
    z = np.polyfit(trend_x, trend_y, 1)
    p = np.poly1d(z)
    ax.plot(trend_x, p(trend_x), "r--", alpha=0.8, linewidth=2, label='Trend')
    
    ax.legend()
    
    plt.tight_layout()
    return fig

def create_combined_analysis_plot(data):
    """Create a comprehensive analysis plot with multiple subplots"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Comprehensive Card Cost Analysis', fontsize=16, fontweight='bold')
    
    player_counts = data['player_counts']
    eras = data['eras']
    era_data = data['era_data']
    overall_avg = data['overall_avg_data']
    
    # Subplot 1: Era comparison (similar to first chart)
    x = np.arange(len(player_counts))
    width = 0.25
    
    bars1 = ax1.bar(x - width, era_data[1], width, label='Era 1', color='lightblue')
    bars2 = ax1.bar(x, era_data[2], width, label='Era 2', color='lightcoral')
    bars3 = ax1.bar(x + width, era_data[3], width, label='Era 3', color='lightgreen')
    
    ax1.set_xlabel('Number of Players')
    ax1.set_ylabel('Average Cost (RP)')
    ax1.set_title('Cost by Era and Player Count')
    ax1.set_xticks(x)
    ax1.set_xticklabels(player_counts)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Overall average
    ax2.bar(player_counts, overall_avg, color='steelblue', alpha=0.7)
    ax2.set_xlabel('Number of Players')
    ax2.set_ylabel('Average Cost (RP)')
    ax2.set_title('Overall Average Cost')
    ax2.set_xticks(player_counts)
    ax2.grid(True, alpha=0.3)
    
    # Add trend line to overall average
    z = np.polyfit(player_counts, overall_avg, 1)
    p = np.poly1d(z)
    ax2.plot(player_counts, p(player_counts), "r--", alpha=0.8)
    
    # Subplot 3: Cost progression across eras (line chart)
    for era in eras:
        ax3.plot(player_counts, era_data[era], 'o-', linewidth=2, markersize=6, 
                label=f'Era {era}')
    ax3.set_xlabel('Number of Players')
    ax3.set_ylabel('Average Cost (RP)')
    ax3.set_title('Cost Progression Across Eras')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xticks(player_counts)
    
    # Subplot 4: Cost difference between eras
    era_diffs = []
    for i in range(len(player_counts)):
        diff_2_1 = era_data[2][i] - era_data[1][i]
        diff_3_2 = era_data[3][i] - era_data[2][i]
        era_diffs.append((diff_2_1, diff_3_2))
    
    diff_2_1 = [d[0] for d in era_diffs]
    diff_3_2 = [d[1] for d in era_diffs]
    
    ax4.bar(x - width/2, diff_2_1, width, label='Era 2 - Era 1', color='orange', alpha=0.7)
    ax4.bar(x + width/2, diff_3_2, width, label='Era 3 - Era 2', color='purple', alpha=0.7)
    ax4.set_xlabel('Number of Players')
    ax4.set_ylabel('Cost Increase (RP)')
    ax4.set_title('Cost Increase Between Consecutive Eras')
    ax4.set_xticks(x)
    ax4.set_xticklabels(player_counts)
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def main():
    # Collect data
    data = collect_cost_data()
    
    # Create individual charts
    fig1 = create_era_comparison_chart(data)
    fig2 = create_overall_average_chart(data)
    fig3 = create_combined_analysis_plot(data)
    
    # Display the plots
    # plt.show()
    
    # Save the plots
    save_dir = "src/stats/assets/card_cost/"
    fig1.savefig(save_dir + 'era_cost_comparison.png', dpi=300, bbox_inches='tight')
    fig2.savefig(save_dir + 'overall_cost_average.png', dpi=300, bbox_inches='tight')
    fig3.savefig(save_dir + 'comprehensive_cost_analysis.png', dpi=300, bbox_inches='tight')
    
    # Print summary statistics
    print("\n=== Card Cost Analysis Summary ===")
    for i, players in enumerate(data['player_counts']):
        print(f"\n{players} players:")
        print(f"  Era 1 average cost: {data['era_data'][1][i]:.2f} RP")
        print(f"  Era 2 average cost: {data['era_data'][2][i]:.2f} RP")
        print(f"  Era 3 average cost: {data['era_data'][3][i]:.2f} RP")
        print(f"  Overall average cost: {data['overall_avg_data'][i]:.2f} RP")
        print(f"  Total cards: {data['total_cards_per_player'][i]}")

if __name__ == "__main__":
    main()
