from engine.card import BasicMaterial
from load.generics import load_generics
from engine.production import Production
from engine.game_resource import Resource

def load_raw_material(card_data) -> BasicMaterial:
    name, cost, required_icon = load_generics(card_data)  
    production = _load_production(card_data["product"])
    return BasicMaterial(name, cost, required_icon, production)

def _load_production(production_data) -> Production:
    productions: list[list[Resource]] = []
    for prod in production_data:
        products = []
        for resource_name in prod:
            products.append(Resource[resource_name])
        productions.append(products)
    return Production(productions)


