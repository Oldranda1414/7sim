import json
from card import Card
from card_type import Type
from game_resource import Resource
from effect import Effect
from icon import Icon

def load_cards(path: str) -> list[Card]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cards = []
    for c in data["cards"]:
        # Parse cost as (money, [Resource,...])
        cost_data = c.get("cost", {"money": 0, "resources": []})
        cost = (
            cost_data.get("money", 0),
            [Resource[r] for r in cost_data.get("resources", [])]
        )

        cards.append(
            Card(
                name=c["name"],
                card_type=Type[c["type"]],
                effect=Effect(),
                cost=cost,
                give_icon=[Icon[i] for i in c.get("give_icon", [])],
                require_icon=Icon[c["require_icon"]] if c.get("require_icon") else None,
                era=c["era"],
                player_number=c["player_number"],
            )
        )
    return cards
