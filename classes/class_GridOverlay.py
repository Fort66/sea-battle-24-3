from ursina import Entity, Grid, color, Vec3

from icecream import ic


class GridOverlay(Entity):
    def __init__(self,
                width=5,
                height=5,
                color=color.black,
                position=Vec3(0, 0, 0),
                **kwargs
                ):

        super().__init__(
            model=Grid(
                width=width,
                height=height,
                thickness=3
                ),
            scale=width,
            color=color,
            rotation=Vec3(90, 0, 0),
            position=position,
            collider='box',
            **kwargs
        )

        self.grid_width = width
        self.grid_height = height
        self.grid_scale = width
        self.map_position_cells = {}
        self.get_map_position_cells()

    def get_map_position_cells(self):
        for col in range(self.grid_width):
            for row in range(self.grid_height):

                start_position = -self.grid_scale / 2
                offset = self.grid_scale / self.grid_height / 2

                cell_x = start_position + (col * (self.grid_scale / self.grid_width)) + offset - .2
                cell_z = start_position + (row * (self.grid_scale / self.grid_height)) + offset + .2

                self.map_position_cells[(col, row)] = Vec3(cell_x, 0, cell_z) + self.position

