from engine.game_resource import Resource

class Cost:
    def __init__(self, money: int, resources: list[Resource]):
        self.money = money
        self.resources = resources

