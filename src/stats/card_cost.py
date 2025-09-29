import matplotlib.pyplot as plt
import numpy as np
from load.cards import load_cards, load_guild_cards
from stats.util import get_rp

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
            if era == 3:
                cards += load_guild_cards()
            total_cost = 0
            for card in cards:
                cost_value = get_rp(card.cost)
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
    
    # Calculate era averages across all player counts
    era_averages = {}
    for era in eras:
        era_averages[era] = np.mean(era_data[era])
    
    return {
        'player_counts': player_counts,
        'eras': eras,
        'era_data': era_data,
        'overall_avg_data': overall_avg_data,
        'total_cards_per_player': total_cards_per_player,
        'era_averages': era_averages
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

def create_era_average_chart(data):
    """Create bar chart showing average cost per era (averaged across all player counts)"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    eras = data['eras']
    era_averages = data['era_averages']
    
    # Create bars
    colors = ['lightblue', 'lightcoral', 'lightgreen']
    bars = ax.bar(eras, [era_averages[era] for era in eras], color=colors, alpha=0.8, width=0.6)
    
    # Customize the chart
    ax.set_xlabel('Era', fontsize=12, fontweight='bold')
    ax.set_ylabel('Average Resource Points per Card', fontsize=12, fontweight='bold')
    ax.set_title('Average Card Cost by Era\n(Averaged Across All Player Counts)', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(eras)
    ax.set_xticklabels([f'Era {era}' for era in eras])
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar, era in zip(bars, eras):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
               f'{height:.2f} RP', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Add percentage increase annotations
    for i in range(1, len(eras)):
        prev_avg = era_averages[eras[i-1]]
        curr_avg = era_averages[eras[i]]
        increase_pct = ((curr_avg - prev_avg) / prev_avg) * 100
        ax.annotate(f'+{increase_pct:.1f}%', 
                   xy=(eras[i], curr_avg), 
                   xytext=(eras[i], curr_avg + 0.1),
                   ha='center', va='bottom', fontsize=10, fontweight='bold',
                   arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    
    plt.tight_layout()
    return fig

def create_combined_analysis_plot(data):
    """Create a comprehensive analysis plot with multiple subplots"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Comprehensive Card Cost Analysis', fontsize=16, fontweight='bold')
    
    # Flatten the axes array for easier indexing
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()
    
    player_counts = data['player_counts']
    eras = data['eras']
    era_data = data['era_data']
    overall_avg = data['overall_avg_data']
    era_averages = data['era_averages']
    
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
    ax2.plot(player_counts, p(player_counts), "r--", alpha=0.8, label='Trend')
    ax2.legend()
    
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
    
    # Subplot 5: Average cost per era (NEW - averaged across player counts)
    colors = ['lightblue', 'lightcoral', 'lightgreen']
    bars = ax5.bar(eras, [era_averages[era] for era in eras], color=colors, alpha=0.8)
    ax5.set_xlabel('Era')
    ax5.set_ylabel('Average Cost (RP)')
    ax5.set_title('Average Cost by Era\n(All Player Counts)')
    ax5.set_xticks(eras)
    ax5.set_xticklabels([f'Era {era}' for era in eras])
    ax5.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, era in zip(bars, eras):
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{height:.2f} RP', ha='center', va='bottom', fontweight='bold')
    
    # Subplot 6: Percentage increase between eras
    increases = []
    for i in range(1, len(eras)):
        prev_avg = era_averages[eras[i-1]]
        curr_avg = era_averages[eras[i]]
        increase_pct = ((curr_avg - prev_avg) / prev_avg) * 100
        increases.append(increase_pct)
    
    ax6.bar([1, 2], increases, color=['orange', 'purple'], alpha=0.7)
    ax6.set_xlabel('Era Transition')
    ax6.set_ylabel('Percentage Increase (%)')
    ax6.set_title('Cost Increase Percentage Between Eras')
    ax6.set_xticks([1, 2])
    ax6.set_xticklabels(['Era 1→2', 'Era 2→3'])
    ax6.grid(True, alpha=0.3)
    
    # Add value labels on percentage bars
    for i, increase in enumerate(increases):
        ax6.text(i+1, increase + 1, f'+{increase:.1f}%', 
                ha='center', va='bottom', fontweight='bold')
    
    # Hide the sixth subplot if we don't have data for it
    if len(increases) == 0:
        ax6.set_visible(False)
    
    plt.tight_layout()
    return fig

def main():
    # Collect data
    data = collect_cost_data()
    
    # Create individual charts
    fig1 = create_era_comparison_chart(data)
    fig2 = create_overall_average_chart(data)
    fig3 = create_era_average_chart(data)  # New chart
    fig4 = create_combined_analysis_plot(data)
    
    # Display the plots
    # plt.show()
    
    # Save the plots
    save_dir = "src/stats/assets/card_cost/"
    fig1.savefig(save_dir + 'era_cost_comparison.png', dpi=300, bbox_inches='tight')
    fig2.savefig(save_dir + 'overall_cost_average.png', dpi=300, bbox_inches='tight')
    fig3.savefig(save_dir + 'era_average_cost.png', dpi=300, bbox_inches='tight')
    fig4.savefig(save_dir + 'comprehensive_cost_analysis.png', dpi=300, bbox_inches='tight')
    
    # Print summary statistics
    print("\n=== Card Cost Analysis Summary ===")
    for i, players in enumerate(data['player_counts']):
        print(f"\n{players} players:")
        print(f"  Era 1 average cost: {data['era_data'][1][i]:.2f} RP")
        print(f"  Era 2 average cost: {data['era_data'][2][i]:.2f} RP")
        print(f"  Era 3 average cost: {data['era_data'][3][i]:.2f} RP")
        print(f"  Overall average cost: {data['overall_avg_data'][i]:.2f} RP")
        print(f"  Total cards: {data['total_cards_per_player'][i]}")
    
    print("\n=== Era Averages (Across All Player Counts) ===")
    for era in data['eras']:
        print(f"  Era {era}: {data['era_averages'][era]:.2f} RP")
    
    # Calculate percentage increases between eras
    for i in range(1, len(data['eras'])):
        prev_era = data['eras'][i-1]
        curr_era = data['eras'][i]
        increase = ((data['era_averages'][curr_era] - data['era_averages'][prev_era]) / data['era_averages'][prev_era]) * 100
        print(f"  Era {prev_era} → Era {curr_era}: +{increase:.1f}% increase")

if __name__ == "__main__":
    main()
