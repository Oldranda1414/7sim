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

This means that the avarage ratio of base resources to rare resources in a game is:

(2.33 + 3.50 + 3.11 + 2.50 + 2.50) / 5 = 13.94 / 5 = 2.79

This provides a proof to justify the Resource Point system discussed later.

## Resource balance

Are all resources equally available per game per number of players?

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

