import json
import copy
from typing import Callable

from card import Card
from card_type import Type
from game_resource import Resource
from effect import Effect
from icon import Icon
from game import Game
from player import Player
from callable_util import chain
from production import Production

# card info taken from : https://7-wonders.fandom.com/wiki/List_of_Cards#Overview
CARD_REGISTRY_PATH = "./src/main/assets/cards.json"
ERA_REGISTRY_PATH = "./src/main/assets/era"

def load_cards(era: int, player_number: int) -> list[Card]:
    with open(CARD_REGISTRY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    card_registry: dict[str, Card] = {}
    for card in data["cards"]:
        card = _load_card(card)
        card_registry[card.name] = card

    with open(_get_era_resitry_path(era), "r", encoding="utf-8") as f:
        data = json.load(f)
    
    cards: list[Card] = []
    for card in data["era"]:
        name = card["name"]
        number = card["number"][player_number - 3]
        for _ in range(number):
            cards.append(copy.deepcopy(card_registry[name]))
    return cards

def _get_era_resitry_path(era_number: int) -> str:
    return f"{ERA_REGISTRY_PATH}/{era_number}.json"

def _load_card(card_data) -> Card:
    name = card_data["name"]
    card_type=Type[card_data["type"]]
    effect=_load_effect(card_data["effect"])
    # Parse cost as (money, [Resource,...])
    cost_data = card_data.get("cost", {"money": 0, "resources": []})
    cost = (
        cost_data.get("money", 0),
        [Resource[r] for r in cost_data.get("resources", [])]
    )
    give_icon=[Icon[i] for i in card_data.get("give_icon", [])]
    require_icon=Icon[card_data["require_icon"]] if card_data.get("require_icon") else None

    return Card(name, card_type, effect, cost, give_icon, require_icon)

def _load_effect(effect_data) -> Effect:
    if not effect_data:
        return Effect(lambda _, __: None, lambda _, __: None)
    on_play_effects: list[Callable[[Game, Player], None]] = []
    # TODO implement all on play effects
    product = effect_data.get("product", False)
    if product:
        production = _load_production(product)
        def add_production(_game: Game, player: Player):
            player.city.productions.append(production)
        on_play_effects.append(add_production)

    on_game_end_effects: list[Callable[[Game, Player], None]] = []
    # TODO implement all on game end effects

    return Effect(chain(on_play_effects), chain(on_game_end_effects))

def _load_production(production_data) -> Production:
    productions: list[list[Resource]] = []
    for prod in production_data:
        products = []
        for resource_name in prod:
            products.append(Resource[resource_name])
        productions.append(products)
    return Production(productions)

