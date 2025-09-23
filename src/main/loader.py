import json
import copy

from card import Card
from card_type import Type
from game_resource import Resource
from effect import Effect
from icon import Icon
# card info taken from : https://7-wonders.fandom.com/wiki/List_of_Cards#Overview
CARD_REGISTRY_PATH = "./src/main/assets/cards.json"
ERA_REGISTRY_PATH = "./src/main/assets/era"

def load_cards(era: int, player_number: int) -> list[Card]:
    with open(CARD_REGISTRY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    card_registry: dict[str, Card] = {}
    for c in data["cards"]:
        # Parse cost as (money, [Resource,...])
        cost_data = c.get("cost", {"money": 0, "resources": []})
        cost = (
            cost_data.get("money", 0),
            [Resource[r] for r in cost_data.get("resources", [])]
        )
        name = c["name"]

        card_registry[name] = Card(
                name=name,
                card_type=Type[c["type"]],
                effect=Effect(),
                cost=cost,
                give_icon=[Icon[i] for i in c.get("give_icon", [])],
                require_icon=Icon[c["require_icon"]] if c.get("require_icon") else None,
            )

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
