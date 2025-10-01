from engine.card import Guild
from engine.gain import Gain, Multiplier, Condition, PrizeType
from engine.card_type import card_colors, from_color
from load.generics import load_generics

def load_guild(card_data) -> Guild:
    name, cost, required_icon = load_generics(card_data)  
    gain = card_data.get("gain", None)
    gains: list[Gain] = []
    if gain:
        for color in card_colors():
            color_value = gain.get(color, None)
            if color_value:
                for gain_condition in ["own", "neighbor"]:
                    gain_condition_value = color_value.get(gain_condition, None)
                    if gain_condition_value:
                        if gain_condition == "own":
                            gains.append(Gain(gain_condition_value, PrizeType.VICTORY, Multiplier(Condition.OWN, from_color(color))))
                        else:
                            gains.append(Gain(gain_condition_value, PrizeType.VICTORY, Multiplier(Condition.NEIGHBOR, from_color(color))))
    return Guild(name, cost, required_icon, gains)
