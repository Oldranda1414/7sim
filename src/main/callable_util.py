from typing import Callable

from game import Game
from player import Player

def chain(callables: list[Callable[[Game, Player], None]]) -> Callable[[Game, Player], None] | None:
    if len(callables) == 0:
        return None
    def chained(game: Game, owner: Player):
        for fn in callables:
            fn(game, owner)
    return chained

def chain_points(callables: list[Callable[[Game, Player], int]]) -> Callable[[Game, Player], int] | None:
    if len(callables) == 0:
        return None
    def chained(game: Game, owner: Player):
        total = 0
        for fn in callables:
            total += fn(game, owner)
        return total
    return chained
