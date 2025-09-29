from engine.card import Cost
from engine.game_resource import resource_type, ResourceType

def get_rp(cost: Cost) -> int:
    total = cost.money
    for resource in cost.resources:
        if resource_type(resource) == ResourceType.BASE:
            total += 1
        elif resource_type(resource) == ResourceType.RARE:
            total += 3
    return total

