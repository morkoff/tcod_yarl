from components.ai import HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item
import color

player = Actor(
    char="@",
    fg_color=(255, 255, 255), 
    bg_color=(20, 20, 20), 
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

orc = Actor(
    char="o",
    fg_color=(24, 127, 56),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)

troll = Actor(
    char="T",
    fg_color=(63, 72, 204),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
)

health_potion = Item(
    char="!",
    fg_color=(127, 0, 255),
    bg_color=color.floor,
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
)
