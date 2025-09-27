import matplotlib.pyplot as plt
import numpy as np
from load.cards import load_all_cards
from engine.game_resource import Resource
from engine.card import BasicMaterial, ManufacturedProduct

def collect_resource_data():
    """Collect resource distribution data for all player counts"""
    player_counts = list(range(3, 8))
    
    # Define resources
    base_resources = {
        Resource.WOOD: [],
        Resource.ORE: [],
        Resource.BRICK: [],
        Resource.STONE: []
    }
    
    rare_resources = {
        Resource.GLASS: [],
        Resource.PAPYRUS: [],
        Resource.TEXTILES: []
    }
    
    total_base_per_player = []
    total_rare_per_player = []
    base_composition = {resource: [] for resource in base_resources.keys()}
    rare_composition = {resource: [] for resource in rare_resources.keys()}
    
    for player_number in player_counts:
        cards = load_all_cards(player_number)
        base_res = {resource: 0 for resource in base_resources.keys()}
        rare_res = {resource: 0 for resource in rare_resources.keys()}
        
        for card in cards:
            if isinstance(card, BasicMaterial):
                for prod in card.production.product:
                    for res in prod:
                        if res in base_res:
                            base_res[res] += 1
            if isinstance(card, ManufacturedProduct):
                for prod in card.production.product:
                    for res in prod:
                        if res in rare_res:
                            rare_res[res] += 1
        
        # Store the data
        total_base = sum(base_res.values())
        total_rare = sum(rare_res.values())
        
        total_base_per_player.append(total_base / player_number)
        total_rare_per_player.append(total_rare / player_number)
        
        for resource in base_resources.keys():
            base_resources[resource].append(base_res[resource])
            # Calculate percentage composition
            if total_base > 0:
                base_composition[resource].append(base_res[resource] / total_base * 100)
            else:
                base_composition[resource].append(0)
        
        for resource in rare_resources.keys():
            rare_resources[resource].append(rare_res[resource])
            # Calculate percentage composition
            if total_rare > 0:
                rare_composition[resource].append(rare_res[resource] / total_rare * 100)
            else:
                rare_composition[resource].append(0)
    
    return {
        'player_counts': player_counts,
        'base_resources': base_resources,
        'rare_resources': rare_resources,
        'total_base_per_player': total_base_per_player,
        'total_rare_per_player': total_rare_per_player,
        'base_composition': base_composition,
        'rare_composition': rare_composition
    }

def create_base_resources_chart(data):
    """Create chart for base resources distribution with grouped bars"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Base Resources Distribution Analysis', fontsize=16, fontweight='bold')
    
    player_counts = data['player_counts']
    base_resources = data['base_resources']
    base_composition = data['base_composition']
    
    # Subplot 1: Absolute counts with grouped bars
    x = np.arange(len(player_counts))
    width = 0.15
    resources = list(base_resources.keys())
    colors = ['#8B4513', '#808080', '#CD7F32', '#B22222', '#A9A9A9']  # Brown, Gray, Bronze, Red, DarkGray
    
    for i, (resource, color) in enumerate(zip(resources, colors)):
        offset = width * (i - 2)  # Center the groups
        bars = ax1.bar(x + offset, base_resources[resource], width, 
                      label=resource.name, color=color, alpha=0.8)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{int(height)}', ha='center', va='bottom', fontsize=8)
    
    ax1.set_xlabel('Number of Players', fontweight='bold')
    ax1.set_ylabel('Total Resource Count', fontweight='bold')
    ax1.set_title('Absolute Base Resource Counts (Grouped Bars)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(player_counts)
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Subplot 2: Percentage composition with grouped bars
    for i, (resource, color) in enumerate(zip(resources, colors)):
        offset = width * (i - 2)
        bars = ax2.bar(x + offset, base_composition[resource], width,
                      label=resource.name, color=color, alpha=0.8)
        
        # Add percentage labels
        for bar, percentage in zip(bars, base_composition[resource]):
            if percentage > 3:  # Only label if significant percentage
                ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                        f'{percentage:.1f}%', ha='center', va='bottom', 
                        fontsize=8, fontweight='bold')
    
    ax2.set_xlabel('Number of Players', fontweight='bold')
    ax2.set_ylabel('Percentage Composition (%)', fontweight='bold')
    ax2.set_title('Base Resource Distribution (%) - Grouped Bars')
    ax2.set_xticks(x)
    ax2.set_xticklabels(player_counts)
    ax2.set_ylim(0, 100)
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig

def create_rare_resources_chart(data):
    """Create chart for rare resources distribution with grouped bars"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Rare Resources Distribution Analysis', fontsize=16, fontweight='bold')
    
    player_counts = data['player_counts']
    rare_resources = data['rare_resources']
    rare_composition = data['rare_composition']
    
    # Subplot 1: Absolute counts with grouped bars
    x = np.arange(len(player_counts))
    width = 0.25
    resources = list(rare_resources.keys())
    colors = ['#87CEEB', '#FFD700', '#FF69B4']  # SkyBlue, Gold, HotPink
    
    for i, (resource, color) in enumerate(zip(resources, colors)):
        offset = width * (i - 1)  # Center the groups
        bars = ax1.bar(x + offset, rare_resources[resource], width,
                      label=resource.name, color=color, alpha=0.8)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                        f'{int(height)}', ha='center', va='bottom', fontsize=9,
                        fontweight='bold')
    
    ax1.set_xlabel('Number of Players', fontweight='bold')
    ax1.set_ylabel('Total Resource Count', fontweight='bold')
    ax1.set_title('Absolute Rare Resource Counts (Grouped Bars)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(player_counts)
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Subplot 2: Percentage composition with grouped bars
    for i, (resource, color) in enumerate(zip(resources, colors)):
        offset = width * (i - 1)
        bars = ax2.bar(x + offset, rare_composition[resource], width,
                      label=resource.name, color=color, alpha=0.8)
        
        # Add percentage labels
        for bar, percentage in zip(bars, rare_composition[resource]):
            if percentage > 5:
                ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                        f'{percentage:.1f}%', ha='center', va='bottom', 
                        fontsize=9, fontweight='bold')
    
    ax2.set_xlabel('Number of Players', fontweight='bold')
    ax2.set_ylabel('Percentage Composition (%)', fontweight='bold')
    ax2.set_title('Rare Resource Distribution (%) - Grouped Bars')
    ax2.set_xticks(x)
    ax2.set_xticklabels(player_counts)
    ax2.set_ylim(0, 100)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig

def create_resource_comparison_chart(data):
    """Create chart comparing base vs rare resources"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Base vs Rare Resources Comparison', fontsize=16, fontweight='bold')
    
    player_counts = data['player_counts']
    total_base_per_player = data['total_base_per_player']
    total_rare_per_player = data['total_rare_per_player']
    
    # Subplot 1: Resources per player
    width = 0.35
    x = np.arange(len(player_counts))
    
    bars1 = ax1.bar(x - width/2, total_base_per_player, width,
                   label='Base Resources/Player', color='#2E8B57', alpha=0.8)  # SeaGreen
    bars2 = ax1.bar(x + width/2, total_rare_per_player, width,
                   label='Rare Resources/Player', color='#9370DB', alpha=0.8)  # MediumPurple
    
    ax1.set_xlabel('Number of Players', fontweight='bold')
    ax1.set_ylabel('Resources per Player', fontweight='bold')
    ax1.set_title('Average Resources Available per Player')
    ax1.set_xticks(x)
    ax1.set_xticklabels(player_counts)
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
    
    # Subplot 2: Base to Rare ratio
    base_rare_ratio = [base/rare if rare > 0 else 0 
                      for base, rare in zip(total_base_per_player, total_rare_per_player)]
    
    bars = ax2.bar(player_counts, base_rare_ratio, color='#FF8C00', alpha=0.7, width=0.6)
    ax2.set_xlabel('Number of Players', fontweight='bold')
    ax2.set_ylabel('Base : Rare Ratio', fontweight='bold')
    ax2.set_title('Base to Rare Resource Ratio per Player')
    ax2.set_xticks(player_counts)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Add ratio labels
    for bar, ratio in zip(bars, base_rare_ratio):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{ratio:.2f}:1', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    return fig

def create_comprehensive_analysis_plot(data):
    """Create comprehensive analysis plot with grouped bars instead of stacked"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Comprehensive Resource Distribution Analysis (Grouped Bars)', fontsize=18, fontweight='bold')
    
    ax1, ax2, ax3, ax4 = axes.flatten()
    
    player_counts = data['player_counts']
    base_resources = data['base_resources']
    rare_resources = data['rare_resources']
    base_composition = data['base_composition']
    rare_composition = data['rare_composition']
    
    # Subplot 1: Base resources - grouped bars for absolute counts
    x = np.arange(len(player_counts))
    width = 0.15
    resources = list(base_resources.keys())
    colors = ['#8B4513', '#808080', '#CD7F32', '#B22222', '#A9A9A9']
    
    for i, (resource, color) in enumerate(zip(resources, colors)):
        offset = width * (i - 2)  # Center the groups
        bars = ax1.bar(x + offset, base_resources[resource], width,
                      label=resource.name, color=color, alpha=0.8)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                        f'{int(height)}', ha='center', va='bottom', fontsize=8)
    
    ax1.set_xlabel('Number of Players')
    ax1.set_ylabel('Total Resource Count')
    ax1.set_title('Base Resources - Grouped Bars')
    ax1.set_xticks(x)
    ax1.set_xticklabels(player_counts)
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Subplot 2: Rare resources - grouped bars for absolute counts
    rare_colors = ['#87CEEB', '#FFD700', '#FF69B4']
    rare_res_list = list(rare_resources.keys())
    
    for i, (resource, color) in enumerate(zip(rare_res_list, rare_colors)):
        offset = width * (i - 1)  # Center the groups (fewer resources)
        bars = ax2.bar(x + offset, rare_resources[resource], width,
                      label=resource.name, color=color, alpha=0.8)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{int(height)}', ha='center', va='bottom', fontsize=9)
    
    ax2.set_xlabel('Number of Players')
    ax2.set_ylabel('Total Resource Count')
    ax2.set_title('Rare Resources - Grouped Bars')
    ax2.set_xticks(x)
    ax2.set_xticklabels(player_counts)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Subplot 3: Base resource composition with grouped bars
    for i, (resource, color) in enumerate(zip(resources, colors)):
        offset = width * (i - 2)
        bars = ax3.bar(x + offset, base_composition[resource], width,
                      label=resource.name, color=color, alpha=0.8)
        
        # Add percentage labels
        for bar, percentage in zip(bars, base_composition[resource]):
            if percentage > 3:
                ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                        f'{percentage:.1f}%', ha='center', va='bottom', 
                        fontsize=8, fontweight='bold')
    
    ax3.set_xlabel('Number of Players')
    ax3.set_ylabel('Percentage Composition (%)')
    ax3.set_title('Base Resource Distribution (%) - Grouped Bars')
    ax3.set_xticks(x)
    ax3.set_xticklabels(player_counts)
    ax3.set_ylim(0, 100)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Subplot 4: Rare resource composition with grouped bars
    for i, (resource, color) in enumerate(zip(rare_res_list, rare_colors)):
        offset = width * (i - 1)
        bars = ax4.bar(x + offset, rare_composition[resource], width,
                      label=resource.name, color=color, alpha=0.8)
        
        # Add percentage labels
        for bar, percentage in zip(bars, rare_composition[resource]):
            if percentage > 5:
                ax4.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                        f'{percentage:.1f}%', ha='center', va='bottom', 
                        fontsize=9, fontweight='bold')
    
    ax4.set_xlabel('Number of Players')
    ax4.set_ylabel('Percentage Composition (%)')
    ax4.set_title('Rare Resource Distribution (%) - Grouped Bars')
    ax4.set_xticks(x)
    ax4.set_xticklabels(player_counts)
    ax4.set_ylim(0, 100)
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig

def create_trend_analysis_plot(data):
    """Create a plot showing trends for each resource type across player counts"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Resource Availability Trends by Player Count', fontsize=16, fontweight='bold')
    
    player_counts = data['player_counts']
    base_resources = data['base_resources']
    rare_resources = data['rare_resources']
    
    # Subplot 1: Base resource trends
    resources = list(base_resources.keys())
    colors = ['#8B4513', '#808080', '#CD7F32', '#B22222', '#A9A9A9']
    markers = ['o', 's', '^', 'D', 'v']
    
    for i, (resource, color, marker) in enumerate(zip(resources, colors, markers)):
        ax1.plot(player_counts, base_resources[resource], 
                marker=marker, linewidth=2, markersize=8,
                label=resource.name, color=color)
    
    ax1.set_xlabel('Number of Players', fontweight='bold')
    ax1.set_ylabel('Total Resource Count', fontweight='bold')
    ax1.set_title('Base Resource Trends')
    ax1.set_xticks(player_counts)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Rare resource trends
    rare_res_list = list(rare_resources.keys())
    rare_colors = ['#87CEEB', '#FFD700', '#FF69B4']
    rare_markers = ['o', 's', '^']
    
    for i, (resource, color, marker) in enumerate(zip(rare_res_list, rare_colors, rare_markers)):
        ax2.plot(player_counts, rare_resources[resource], 
                marker=marker, linewidth=2, markersize=8,
                label=resource.name, color=color)
    
    ax2.set_xlabel('Number of Players', fontweight='bold')
    ax2.set_ylabel('Total Resource Count', fontweight='bold')
    ax2.set_title('Rare Resource Trends')
    ax2.set_xticks(player_counts)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def main():
    # Collect data
    data = collect_resource_data()
    
    # Create individual charts with grouped bars
    fig1 = create_base_resources_chart(data)
    fig2 = create_rare_resources_chart(data)
    fig3 = create_resource_comparison_chart(data)
    fig4 = create_comprehensive_analysis_plot(data)
    fig5 = create_trend_analysis_plot(data)  # New trend analysis
    
    # Display the plots
    # plt.show()
    
    # Save the plots
    save_dir = "src/stats/assets/res_balance/"
    fig1.savefig(save_dir + 'base_resources_grouped.png', dpi=300, bbox_inches='tight')
    fig2.savefig(save_dir + 'rare_resources_grouped.png', dpi=300, bbox_inches='tight')
    fig3.savefig(save_dir + 'resource_comparison.png', dpi=300, bbox_inches='tight')
    fig4.savefig(save_dir + 'comprehensive_resource_grouped.png', dpi=300, bbox_inches='tight')
    fig5.savefig(save_dir + 'resource_trends.png', dpi=300, bbox_inches='tight')
    
    # Print summary statistics
    print("\n=== Resource Distribution Summary ===")
    for i, players in enumerate(data['player_counts']):
        print(f"\n{players} players:")
        
        print("  Base Resources:")
        total_base = 0
        for resource in data['base_resources'].keys():
            count = data['base_resources'][resource][i]
            percentage = data['base_composition'][resource][i]
            total_base += count
            print(f"    {resource.name}: {count} ({percentage:.1f}%)")
        
        print("  Rare Resources:")
        total_rare = 0
        for resource in data['rare_resources'].keys():
            count = data['rare_resources'][resource][i]
            percentage = data['rare_composition'][resource][i]
            total_rare += count
            print(f"    {resource.name}: {count} ({percentage:.1f}%)")
        
        print(f"  Totals: Base={total_base}, Rare={total_rare}")
        print(f"  Per Player: Base={data['total_base_per_player'][i]:.2f}, Rare={data['total_rare_per_player'][i]:.2f}")
        if total_rare > 0:
            ratio = total_base / total_rare
            print(f"  Base:Rare Ratio: {ratio:.2f}:1")

if __name__ == "__main__":
    main()
