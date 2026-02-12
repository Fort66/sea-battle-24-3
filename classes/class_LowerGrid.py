from ursina import Entity, Grid, color, Vec3

from icecream import ic

class LowerGrid(Entity):
    def __init__(self, width, height, **kwargs):
        super().__init__(
            model=Grid(
                width=width,
                height=height,
                thickness=3
                ),
            scale=width,
            color=color.rgba(0, 0, 0, 0.1),
            rotation=Vec3(90, 0, 0),
            position=Vec3(-.515, -.02, 5.515),
            collider='box'
        )

        self.grid_width = width
        self.grid_height = height

    def get_cells_coordinates(self):
        self.cell_size = self.scale_x / self.grid_width  # предполагаем квадратные ячейки  
        for x in range(self.grid_width):  
            for z in range(self.grid_height):  
                # локальные координаты центра ячейки (относительно grid)  
                local_center = Vec3(  
                    (x - self.grid_width/2 + 0.5) * self.cell_size,  
                    0,  
                    (z - self.grid_height/2 + 0.5) * self.cell_size  
                )  
                # мировые координаты  
                # world_center = self.world_position + self.world_transform_point(local_center)  
                
                world_center = self.world_position + local_center * self.world_scale
                ic(f"Cell ({x},{z}): local={local_center}, world={world_center}")