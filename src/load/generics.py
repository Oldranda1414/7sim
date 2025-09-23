from engine.cost import Cost
from engine.game_resource import Resource

def load_generics(card_data) -> tuple[str, Cost, str | None]:
    name = card_data["name"]
    cost_data = card_data.get("cost", {"money": 0, "resources": []})
    cost_data = (
        cost_data.get("money", 0),
        [Resource[r] for r in cost_data.get("resources", [])]
    )
    cost = Cost(cost_data[0], cost_data[1])
    require_icon=card_data["require_icon"] if card_data.get("require_icon") else None
    return name, cost, require_icon
