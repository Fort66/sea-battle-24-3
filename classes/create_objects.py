from ursina import Vec3, color

from .class_SeaPlane import SeaPlane
from .class_GridOverlay import GridOverlay
from .class_CoordinatesText import CoordinatesText
from .class_NavButton import NavButton
from .class_ShipsMenu import ShipsMenu




my_water_area = SeaPlane()
my_grid_overlay = GridOverlay(10, 10, position=Vec3(0, .002, 0))
my_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, 0), position=Vec3(0, -.002, 0))

my_coordinates = CoordinatesText(my_lower_grid)



enemy_water_area = SeaPlane(position=Vec3(-18, 0, 0))
enemy_grid_overlay = GridOverlay(10, 10, position=Vec3(-18, .002, 0))
enemy_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, 0), position=Vec3(-18, -.002, 0))

enemy_coordinates = CoordinatesText(enemy_lower_grid)

nav_button = NavButton(position=Vec3(-1, .4, 0))


four_deck_menu = ShipsMenu(
    model='assets/models/newport/newport.glb',
    scale=.011,
    position=Vec3(8, .2, 5),
    rotation=Vec3(90, 90, 0),
    ship_counter=1,
    deck_amount=4,
)

three_deck_menu = ShipsMenu(
    model='assets/models/ton/tone.glb',
    scale=.009,
    position=Vec3(8, .2, 3),
    rotation=Vec3(90, 90, 0),
    ship_counter=2,
    deck_amount=3,
)

two_deck_menu = ShipsMenu(
    model='assets/models/lowa/uss_iowa_model.glb',
    scale=.006,
    position=Vec3(8, .2, 1),
    rotation=Vec3(90, 0, 0),
    ship_counter=3,
    deck_amount=2,
)

one_deck_menu = ShipsMenu(
    model='assets/models/meteor/meteoro_class_patrol_vessel.glb',
    scale=.007,
    position=Vec3(8, .2, -1),
    rotation=Vec3(90, 0, 0),
    ship_counter=4,
    deck_amount=1,
)
