from ursina import Entity, color, Vec3, mouse, scene, camera, raycast
from ursina.prefabs.draggable import Draggable

from icecream import ic

class Ships(Entity):
    def __init__(self,
                whater=None,
                model=None,
                texture=None,
                scale=1,
                rotation=Vec3(0, 0, 0),
                position=Vec3(0, 0, 0),
                deck_amount=0
                ):


        super().__init__(
            model=model,
            scale=scale,
            rotation=rotation,
            position=position,
            color=color.white,
            collider='box'
        )

        self.whater = whater
        self.model = model
        self.texture = texture
        self.scale = scale
        self.rotation = rotation
        self.position = position
        self.deck_amount = deck_amount
        self.following_mouse = False
        self.is_selected = False

        self.is_grabbed = True

    def input(self, key):
        if self.is_grabbed:
            if key == 'left mouse down':
                if mouse.hovered_entity == self:
                    self.is_selected = True
                    self.following_mouse = True

            if key == 'left mouse up':
                self.is_selected = False
                self.following_mouse = False

            if key == 'right mouse down':
                if self.is_selected:
                    self.rotation += Vec3(0, 90, 0)

    def update(self):
        if self.following_mouse:
            self.position = Vec3(mouse.world_point[0], 0, mouse.world_point[2])

