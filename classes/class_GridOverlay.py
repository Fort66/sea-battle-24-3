from ursina import Entity, Grid, color, Vec3

class GridOverlay(Entity):
    def __init__(self, width, height, **kwargs):
        super().__init__(
            model=Grid(
                width=width,
                height=height,
                thickness=3
                ),
            scale=width,
            color=color.black,
            rotation=Vec3(90, 0, 0),
            position=Vec3(0, .002, 5),
            collider='box',
        )

        self.grid_width = width
        self.grid_height = height