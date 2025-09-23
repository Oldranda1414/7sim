from wonder import Wonder
from card import Card
from game_resource import Resource
from production import Production

class City:
    def __init__(self, name: str, wonder: Wonder, base_resource: Resource):
        self.name = name
        self.wonder = wonder
        self.productions: list[Production] = []
        self.productions.append(Production([[base_resource]]))
        self.cards: list[Card] = []
        self.war_points = 0
        self.money = 3
