# Results

Here are reported the results of the statistical analisys, which will be summarised in the slideshow (TODO)

All results where obtained from files in `src/stats`

## Resource availablility

It would be interesting to see how many resources of each type (base, rare and why not even money) is available through cards for every player per game per number of players in the game.

This was explored in `res_avail.py`

## Card cost

A good baseline start would be to find the avarage cost of a card per era per number of players

This would be interesting to know as in a given game knowing the avarage cost of a card would enable the player to evaluate if his city currently produces enough resources by itself, or through trading with neighbors, to build most of the era cards.

Since not all resources are equal, a 'resource point' (RP) system must be used to enable the comparison between different card costs.

A good RP system, totally made up on the spot without much though, would be to assign:

- 1 RP per base resource needed
- 1 RP per money needed
- 3 RP per rare resource needed

TODO check if this is a sensible system with resource availablility stat results
