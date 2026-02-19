from ursina import Entity, color, Vec3, mouse, scene, camera, raycast
from ursina.prefabs.draggable import Draggable

from icecream import ic

from .class_ShipsCreater import ShipsCreater

ships_creater = ShipsCreater()

class ShipsMenu(Entity):
    def __init__(self,
                water=None,
                model=None,
                texture=None,
                scale=1,
                rotation=Vec3(0, 0, 0),
                position=Vec3(0, 0, 0),
                ship_counter=0,
                deck_amount=0
                ):


        super().__init__(
            model = model,
            texture=texture,
            scale = scale,
            rotation = rotation,
            position = position,
            collider='box'
        )

        self.whater = water
        self.model = model
        self.texture = texture
        self.scale = scale
        self.rotation = rotation
        self.position = position
        self.ship_counter = ship_counter
        self.deck_amount = deck_amount
        self.sub_ships_counter = True

    def input(self, key):
        if key == 'left mouse down':
            if mouse.hovered_entity == self and self.sub_ships_counter:
                # if self.sub_ships_counter:
                self.ship_counter -= 1
                    # self.sub_ships_counter = False

                ships_creater.count_deck = self.deck_amount
                ships_creater.create_ship_command = True
                ships_creater.model = self.model
                ships_creater.texture = self.texture

        # if key == 'left mouse up':
        #     self.sub_ships_counter = True

        if self.ship_counter <= 0:
            self.visible = False

