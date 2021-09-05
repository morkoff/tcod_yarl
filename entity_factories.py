from entity import Entity

player = Entity(char="@", fg_color=(255, 255, 255), bg_color=(20, 20, 20), name="Player", blocks_movement=True)

orc = Entity(char="o", fg_color=(24, 127, 56), name="Orc", blocks_movement=True)
troll = Entity(char="T", fg_color=(63, 72, 204), name="Troll", blocks_movement=True)