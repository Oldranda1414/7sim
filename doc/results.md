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
- Base Resources:
  - WOOD: 4 (25.0%)
  - ORE: 4 (25.0%)
  - BRICK: 4 (25.0%)
  - STONE: 4 (25.0%)
- Rare Resources:
  - GLASS: 2 (33.3%)
  - PAPYRUS: 2 (33.3%)
  - TEXTILES: 2 (33.3%)
- Totals: Base=16, Rare=6
- Per Player: Base=5.33, Rare=2.00
- Base:Rare Ratio: 2.67:1

4 players:
- Base Resources:
  - WOOD: 7 (29.2%)
  - ORE: 7 (29.2%)
  - BRICK: 5 (20.8%)
  - STONE: 5 (20.8%)
- Rare Resources:
  - GLASS: 2 (33.3%)
  - PAPYRUS: 2 (33.3%)
  - TEXTILES: 2 (33.3%)
- Totals: Base=24, Rare=6
- Per Player: Base=6.00, Rare=1.50
- Base:Rare Ratio: 4.00:1

5 players:
- Base Resources:
  - WOOD: 8 (25.0%)
  - ORE: 8 (25.0%)
  - BRICK: 8 (25.0%)
  - STONE: 8 (25.0%)
- Rare Resources:
  - GLASS: 3 (33.3%)
  - PAPYRUS: 3 (33.3%)
  - TEXTILES: 3 (33.3%)
- Totals: Base=32, Rare=9
- Per Player: Base=6.40, Rare=1.80
- Base:Rare Ratio: 3.56:1

6 players:
- Base Resources:
  - WOOD: 9 (25.0%)
  - ORE: 9 (25.0%)
  - BRICK: 9 (25.0%)
  - STONE: 9 (25.0%)
- Rare Resources:
  - GLASS: 4 (33.3%)
  - PAPYRUS: 4 (33.3%)
  - TEXTILES: 4 (33.3%)
- Totals: Base=36, Rare=12
- Per Player: Base=6.00, Rare=2.00
- Base:Rare Ratio: 3.00:1

7 players:
- Base Resources:
  - WOOD: 9 (25.0%)
  - ORE: 9 (25.0%)
  - BRICK: 9 (25.0%)
  - STONE: 9 (25.0%)
- Rare Resources:
  - GLASS: 4 (33.3%)
  - PAPYRUS: 4 (33.3%)
  - TEXTILES: 4 (33.3%)
- Totals: Base=36, Rare=12
- Per Player: Base=5.14, Rare=1.71
- Base:Rare Ratio: 3.00:1

## Card type distribution

What is an average city card type distribution?

This was explored in `card_balance.py`

![card distribution](./../src/stats/assets/card_balance/card_availability.png)
![card distribution average](./../src/stats/assets/card_balance/average_card_distribution.png)

This shows that an average distribution across all games for every card type is for every city/player to have 3/4 of every card type, with the exception of manufactured goods and guild cards, which would be present 1/2 per city/player.

### Card Type Distribution Summary

3 players:
  Total cards: 63
  Cards per player: 21.00
  Card Type Breakdown:
    Raw Material: 10 (15.9%)
    Manufactured Good: 6 (9.5%)
    Civic Structure: 12 (19.0%)
    Commercial Structure: 9 (14.3%)
    Military Structure: 9 (14.3%)
    Scientific Structure: 12 (19.0%)
    Guild: 5 (7.9%)

4 players:
  Total cards: 82
  Cards per player: 20.50
  Card Type Breakdown:
    Raw Material: 15 (18.3%)
    Manufactured Good: 6 (7.3%)
    Civic Structure: 14 (17.1%)
    Commercial Structure: 13 (15.9%)
    Military Structure: 13 (15.9%)
    Scientific Structure: 15 (18.3%)
    Guild: 6 (7.3%)

5 players:
  Total cards: 106
  Cards per player: 21.20
  Card Type Breakdown:
    Raw Material: 20 (18.9%)
    Manufactured Good: 9 (8.5%)
    Civic Structure: 17 (16.0%)
    Commercial Structure: 17 (16.0%)
    Military Structure: 17 (16.0%)
    Scientific Structure: 19 (17.9%)
    Guild: 7 (6.6%)

6 players:
  Total cards: 126
  Cards per player: 21.00
  Card Type Breakdown:
    Raw Material: 22 (17.5%)
    Manufactured Good: 12 (9.5%)
    Civic Structure: 21 (16.7%)
    Commercial Structure: 23 (18.3%)
    Military Structure: 20 (15.9%)
    Scientific Structure: 20 (15.9%)
    Guild: 8 (6.3%)

7 players:
  Total cards: 147
  Cards per player: 21.00
  Card Type Breakdown:
    Raw Material: 22 (15.0%)
    Manufactured Good: 12 (8.2%)
    Civic Structure: 26 (17.7%)
    Commercial Structure: 29 (19.7%)
    Military Structure: 25 (17.0%)
    Scientific Structure: 24 (16.3%)
    Guild: 9 (6.1%)

#### Average Card Distribution per Player (Across All Player Counts)
  Scientific Structure: 3.66 cards per player
  Civic Structure: 3.62 cards per player
  Raw Material: 3.58 cards per player
  Commercial Structure: 3.53 cards per player
  Military Structure: 3.31 cards per player
  Manufactured Good: 1.80 cards per player
  Guild: 1.44 cards per player
  Total average cards per player (sum over types): 20.94

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

## Card Type Point Cost

All the statistics gathered till now will enable us to evaluate the Point production per Resource Point for every card type

This was explored in `card_value.py`

### Blue cards

- Altar: 4
- Theater: 4
- Well: 4
- Baths: 3.0
- Courthouse: 0.8
- Temple: 0.8
- Statue: 1.3333333333333333
- Acqueduct: 1.6666666666666667
- Gardens: 1.6666666666666667
- Senate: 1.5
- Town Hall: 1.0
- Pantheon: 0.5833333333333334
- Palace: 0.6153846153846154

average card value: 1.9204142011834322
average card value removing first era cards: 1.1072649572649573

The best cards:

- era 1:
    - Altar, Theater, Well
- era 2:
    - Acqueduct
- era 3:
    - Gardens, (Senate close second)
