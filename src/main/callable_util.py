from typing import Callable

from game import Game
from player import Player

def chain(callables: list[Callable[[Game, Player], None]]) -> Callable[[Game, Player], None]:
    def chained(game: Game, owner: Player):
        for fn in callables:
            fn(game, owner)
    return chained
