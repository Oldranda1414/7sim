import itertools

from engine.card import CommercialBuilding
from engine.gain import Condition, Gain, Multiplier, PrizeType
from engine.card_type import card_colors, from_color
from load.generics import load_generics

def load_commercial_building(card_data) -> CommercialBuilding:
    name, cost, required_icon = load_generics(card_data)  
    gain = card_data.get("gain", None)
    gains: list[Gain] = []
    if gain:
        coins = gain.get("coins", None)
        if coins:
            gains.append(Gain(coins, PrizeType.COIN))
        for color in card_colors():
            color_value = gain.get(color, None)
            if color_value:
                for gain_type, gain_condition in itertools.product(["coins", "victory"], ["own", "neighbor"]):
                    gain_type_value = color_value.get(gain_type, None)
                    if gain_type_value:
                        gain_condition_value = gain_type_value.get(gain_condition, None)
                        if gain_condition_value:
                            if gain_type == "coins":
                                if gain_condition == "own":
                                    gains.append(Gain(gain_condition_value, PrizeType.COIN, Multiplier(Condition.OWN, from_color(color))))
                                else:
                                    gains.append(Gain(gain_condition_value, PrizeType.COIN, Multiplier(Condition.NEIGHBOR, from_color(color))))
                            else:
                                if gain_condition == "own":
                                    gains.append(Gain(gain_condition_value, PrizeType.VICTORY, Multiplier(Condition.OWN, from_color(color))))
                                else:
                                    gains.append(Gain(gain_condition_value, PrizeType.VICTORY, Multiplier(Condition.NEIGHBOR, from_color(color))))
    return CommercialBuilding(name, cost, required_icon, gains)
