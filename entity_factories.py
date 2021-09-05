from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    fg_color=(255, 255, 255), 
    bg_color=(20, 20, 20), 
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

orc = Actor(
    char="o",
    fg_color=(24, 127, 56),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)

troll = Actor(
    char="T",
    fg_color=(63, 72, 204),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)
