import matplotlib.pyplot as plt
import numpy as np
from load.cards import load_all_cards
from engine.card import BasicMaterial, ManufacturedProduct

def collect_data():
    """Collect the data for all player counts"""
    player_counts = []
    base_res_per_player = []
    rare_res_per_player = []
    base_per_rare_ratios = []
    total_base_res = []
    total_rare_res = []
    
    for player_number in range(3, 8):
        cards = load_all_cards(player_number)
        base_res_avail = 0
        rare_res_avail = 0
        
        for card in cards:
            if isinstance(card, BasicMaterial):
                base_res_avail += len(card.production.product[0])
            if isinstance(card, ManufacturedProduct):
                rare_res_avail += len(card.production.product[0])
        
        player_counts.append(player_number)
        total_base_res.append(base_res_avail)
        total_rare_res.append(rare_res_avail)
        base_res_per_player.append(base_res_avail / player_number)
        rare_res_per_player.append(rare_res_avail / player_number)
        base_per_rare_ratios.append(base_res_avail / rare_res_avail)
    
    return {
        'player_counts': player_counts,
        'total_base_res': total_base_res,
        'total_rare_res': total_rare_res,
        'base_res_per_player': base_res_per_player,
        'rare_res_per_player': rare_res_per_player,
        'base_per_rare_ratios': base_per_rare_ratios
    }

def create_resource_analysis_plots(data):
    """Create comprehensive resource analysis plots"""
    
    player_counts = data['player_counts']
    
    # Create a figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Resource Availability Analysis by Player Count', fontsize=16, fontweight='bold')
    
    # Plot 1: Total resources available
    width = 0.35
    x = np.arange(len(player_counts))
    
    ax1.bar(x - width/2, data['total_base_res'], width, label='Base Resources', color='skyblue', alpha=0.8)
    ax1.bar(x + width/2, data['total_rare_res'], width, label='Rare Resources', color='lightcoral', alpha=0.8)
    ax1.set_xlabel('Number of Players')
    ax1.set_ylabel('Total Resources Available')
    ax1.set_title('Total Resources by Player Count')
    ax1.set_xticks(x)
    ax1.set_xticklabels(player_counts)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for i, v in enumerate(data['total_base_res']):
        ax1.text(i - width/2, v + max(data['total_base_res'])*0.01, f'{v}', ha='center', va='bottom', fontsize=9)
    for i, v in enumerate(data['total_rare_res']):
        ax1.text(i + width/2, v + max(data['total_rare_res'])*0.01, f'{v}', ha='center', va='bottom', fontsize=9)
    
    # Plot 2: Resources per player
    ax2.bar(x - width/2, data['base_res_per_player'], width, label='Base Resources/Player', color='dodgerblue', alpha=0.8)
    ax2.bar(x + width/2, data['rare_res_per_player'], width, label='Rare Resources/Player', color='indianred', alpha=0.8)
    ax2.set_xlabel('Number of Players')
    ax2.set_ylabel('Resources per Player')
    ax2.set_title('Average Resources per Player')
    ax2.set_xticks(x)
    ax2.set_xticklabels(player_counts)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Base to Rare resource ratio
    bars = ax3.bar(x, data['base_per_rare_ratios'], color='mediumseagreen', alpha=0.7)
    ax3.set_xlabel('Number of Players')
    ax3.set_ylabel('Ratio (Base:Rare)')
    ax3.set_title('Base to Rare Resource Ratio')
    ax3.set_xticks(x)
    ax3.set_xticklabels(player_counts)
    ax3.grid(True, alpha=0.3)
    
    # Add ratio values on bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.2f}:1', ha='center', va='bottom', fontweight='bold')
    
    # Plot 4: Stacked area chart showing resource distribution
    total_resources = [b + r for b, r in zip(data['total_base_res'], data['total_rare_res'])]
    base_percentage = [b/total*100 for b, total in zip(data['total_base_res'], total_resources)]
    rare_percentage = [r/total*100 for r, total in zip(data['total_rare_res'], total_resources)]
    
    ax4.stackplot(player_counts, [base_percentage, rare_percentage], 
                  labels=['Base Resources', 'Rare Resources'], 
                  colors=['skyblue', 'lightcoral'], alpha=0.8)
    ax4.set_xlabel('Number of Players')
    ax4.set_ylabel('Percentage of Total Resources (%)')
    ax4.set_title('Resource Distribution Percentage')
    ax4.legend(loc='upper left')
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim(0, 100)
    
    plt.tight_layout()
    return fig

def create_individual_trend_plots(data):
    """Create individual plots showing trends"""
    
    player_counts = data['player_counts']
    
    # Trend analysis plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot lines for different metrics
    line1, = ax.plot(player_counts, data['base_res_per_player'], 'o-', linewidth=2, 
                     markersize=8, label='Base Resources/Player', color='blue')
    line2, = ax.plot(player_counts, data['rare_res_per_player'], 's-', linewidth=2, 
                     markersize=8, label='Rare Resources/Player', color='red')
    
    # Create secondary y-axis for ratio
    line3, = ax.plot(player_counts, data['base_per_rare_ratios'], '^-', linewidth=2, 
                      markersize=8, label='Base:Rare Ratio', color='green')
    
    ax.set_xlabel('Number of Players')
    ax.set_ylabel('Resources per Player')
    ax.set_title('Resource Availability Trends by Player Count', fontsize=14, fontweight='bold')
    
    # Combine legends from both axes
    lines = [line1, line2, line3]
    labels = [line.get_label() for line in lines]
    ax.legend(lines, labels, loc='upper right')
    
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return fig

def main():
    # Collect data
    data = collect_data()
    
    # Create comprehensive analysis plot
    fig1 = create_resource_analysis_plots(data)
    
    # Create trend analysis plot
    fig2 = create_individual_trend_plots(data)
    
    # Display the plots
    # plt.show()
    
    # Save the plots
    save_dir = "src/stats/assets/res_avail/"
    fig1.savefig(save_dir + 'resource_analysis_comprehensive.png', dpi=300, bbox_inches='tight')
    fig2.savefig(save_dir + 'resource_trend_analysis.png', dpi=300, bbox_inches='tight')
    
    # Print summary statistics
    print("\n=== Resource Availability Summary ===")
    for i, players in enumerate(data['player_counts']):
        print(f"\n{players} players:")
        print(f"  Total Base Resources: {data['total_base_res'][i]}")
        print(f"  Total Rare Resources: {data['total_rare_res'][i]}")
        print(f"  Base/Player: {data['base_res_per_player'][i]:.2f}")
        print(f"  Rare/Player: {data['rare_res_per_player'][i]:.2f}")
        print(f"  Base:Rare Ratio: {data['base_per_rare_ratios'][i]:.2f}:1")

if __name__ == "__main__":
    main()
