# Results

Here are reported the results of the statistical analisys, which will be summarised in the slideshow (TODO)

All results where obtained from files in `src/stats`

Note: Remember to generate the graphs running:

```sh
just stats
```

## Resource availablility

It would be interesting to see how many resources of each type (base, rare and why not even money) is available through cards for every player per game per number of players in the game.

This was explored in `res_avail.py`

The following graphs summarise the results:

![resource analisys](./../src/stats/assets/res_avail/resource_analysis_comprehensive.png)
![resource trend](./../src/stats/assets/res_avail/resource_trend_analysis.png)

### Resource Availability Summary

3 players:

- Total Base Resources: 14
- Total Rare Resources: 6
- Base/Player: 4.67
- Rare/Player: 2.00
- Base:Rare Ratio: 2.33:1

4 players:

- Total Base Resources: 21
- Total Rare Resources: 6
- Base/Player: 5.25
- Rare/Player: 1.50
- Base:Rare Ratio: 3.50:1

5 players:

- Total Base Resources: 28
- Total Rare Resources: 9
- Base/Player: 5.60
- Rare/Player: 1.80
- Base:Rare Ratio: 3.11:1

6 players:

- Total Base Resources: 30
- Total Rare Resources: 12
- Base/Player: 5.00
- Rare/Player: 2.00
- Base:Rare Ratio: 2.50:1

7 players:

- Total Base Resources: 30
- Total Rare Resources: 12
- Base/Player: 4.29
- Rare/Player: 1.71
- Base:Rare Ratio: 2.50:1


This means that the avarage ratio of base resources to rare resources in a game is:

(2.33 + 3.50 + 3.11 + 2.50 + 2.50) / 5 = 13.94 / 5 = 2.79

This provides a proof to justify the Resource Point system discussed later.

## Resource balance

Are all resources equally available per game per number of players?

This was explored in `res_balance.py`

The results are summarized in the following graphs:

![resource balance](./../src/stats/assets/res_balance/comprehensive_resource_grouped.png)
![resource comparison](./../src/stats/assets/res_balance/resource_comparison.png)

### Resource Distribution Summary

3 players:
  Base Resources:
    WOOD: 4 (25.0%)
    ORE: 4 (25.0%)
    BRICK: 4 (25.0%)
    STONE: 4 (25.0%)
  Rare Resources:
    GLASS: 2 (33.3%)
    PAPYRUS: 2 (33.3%)
    TEXTILES: 2 (33.3%)
  Totals: Base=16, Rare=6
  Per Player: Base=5.33, Rare=2.00
  Base:Rare Ratio: 2.67:1

4 players:
  Base Resources:
    WOOD: 7 (29.2%)
    ORE: 7 (29.2%)
    BRICK: 5 (20.8%)
    STONE: 5 (20.8%)
  Rare Resources:
    GLASS: 2 (33.3%)
    PAPYRUS: 2 (33.3%)
    TEXTILES: 2 (33.3%)
  Totals: Base=24, Rare=6
  Per Player: Base=6.00, Rare=1.50
  Base:Rare Ratio: 4.00:1

5 players:
  Base Resources:
    WOOD: 8 (25.0%)
    ORE: 8 (25.0%)
    BRICK: 8 (25.0%)
    STONE: 8 (25.0%)
  Rare Resources:
    GLASS: 3 (33.3%)
    PAPYRUS: 3 (33.3%)
    TEXTILES: 3 (33.3%)
  Totals: Base=32, Rare=9
  Per Player: Base=6.40, Rare=1.80
  Base:Rare Ratio: 3.56:1

6 players:
  Base Resources:
    WOOD: 9 (25.0%)
    ORE: 9 (25.0%)
    BRICK: 9 (25.0%)
    STONE: 9 (25.0%)
  Rare Resources:
    GLASS: 4 (33.3%)
    PAPYRUS: 4 (33.3%)
    TEXTILES: 4 (33.3%)
  Totals: Base=36, Rare=12
  Per Player: Base=6.00, Rare=2.00
  Base:Rare Ratio: 3.00:1

7 players:
  Base Resources:
    WOOD: 9 (25.0%)
    ORE: 9 (25.0%)
    BRICK: 9 (25.0%)
    STONE: 9 (25.0%)
  Rare Resources:
    GLASS: 4 (33.3%)
    PAPYRUS: 4 (33.3%)
    TEXTILES: 4 (33.3%)
  Totals: Base=36, Rare=12
  Per Player: Base=5.14, Rare=1.71
  Base:Rare Ratio: 3.00:1

## Card type distribution

What is an avarage city card type distribution?

## Card cost

A good baseline start would be to find the avarage cost of a card per era per number of players

This would be interesting to know as in a given game knowing the avarage cost of a card would enable the player to evaluate if his city currently produces enough resources by itself, or through trading with neighbors, to build most of the era cards.

Since not all resources are equal, a 'resource point' (RP) system must be used to enable the comparison between different card costs.

A good RP system would be to assign:

- 1 RP per base resource needed
- 1 RP per money needed
- 3 RP per rare resource needed

The value ration between base resource and rare resource is justified by the avarage resource availability ratio between base and rare resource is 2.79, as proven in the [Resource availablility](#resource-availability) chapter.

The value given for money is totally instinctive. An evaluation could be made based on the money obtained through cards and wonders, but this is not enough for a true justification, as trade between neighboring cities is hard to take account for without actual game data.

This was explored in `card_cost.py`

![card cost](./../src/stats/assets/card_cost/comprehensive_cost_analysis.png)

### Card Cost Analysis Summary

3 players:

- Era 1 average cost: 0.71 RP
- Era 2 average cost: 2.48 RP
- Era 3 average cost: 6.50 RP
- Overall average cost: 3.47 RP
- Total cards: 68

4 players:

- Era 1 average cost: 0.71 RP
- Era 2 average cost: 2.38 RP
- Era 3 average cost: 6.25 RP
- Overall average cost: 3.28 RP
- Total cards: 86

5 players:

- Era 1 average cost: 0.71 RP
- Era 2 average cost: 2.33 RP
- Era 3 average cost: 5.95 RP
- Overall average cost: 3.07 RP
- Total cards: 109

6 players:

- Era 1 average cost: 0.64 RP
- Era 2 average cost: 2.36 RP
- Era 3 average cost: 6.02 RP
- Overall average cost: 3.05 RP
- Total cards: 128

7 players:

- Era 1 average cost: 0.65 RP
- Era 2 average cost: 2.39 RP
- Era 3 average cost: 6.08 RP
- Overall average cost: 3.06 RP
- Total cards: 148

### Era Averages (Across All Player Counts)

- Era 1: 0.69 RP
- Era 2: 2.39 RP
- Era 3: 6.16 RP
- Era 1 → Era 2: +247.2% increase
- Era 2 → Era 3: +158.0% increase

These results prove that the game is pretty well built as most value distributions have very low variance, too low to be accidental.
