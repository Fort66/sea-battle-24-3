from ursina import Entity, color, Vec3, mouse, scene, camera, raycast
from ursina.prefabs.draggable import Draggable

from icecream import ic

class Ships(Entity):
    def __init__(self,
                whater=None,
                model='',
                texture='',
                scale=1,
                rotation=Vec3(0, 0, 0),
                position=Vec3(0, 0, 0),
                ):


        super().__init__(
            model = model,
            scale = scale,
            rotation = rotation,
            position = position,
            collider='box'
        )

        self.whater = whater
        self.model = model
        self.texture = texture
        self.scale = scale
        self.rotation = rotation
        self.position = position

        self.is_grabbed = False
        

