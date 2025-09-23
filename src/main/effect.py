from typing import Callable

from game import Game
from player import Player

class Effect:
    def __init__(self, on_play: Callable[[Game, Player], None], on_game_end: Callable[[Game, Player], None]):
        self._on_play = on_play
        self._on_game_end = on_game_end

    def on_play(self, game: Game, owner: Player):
        self._on_play(game, owner)

    def on_game_end(self, game: Game, owner: Player):
        self._on_game_end(game, owner)
