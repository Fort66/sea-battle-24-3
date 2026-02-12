from ursina import *
from ursina.prefabs.grid_editor import GridEditor

from icecream import ic

from string import ascii_letters

from classes.class_SeaPlane import SeaPlane
from classes.class_GridOverlay import GridOverlay
from classes.class_LowerGrid import LowerGrid
from classes.class_SceneText import SceneText


# sea_plane = SeaPlane()
grid_overlay = GridOverlay(10, 10)
lower_grid = LowerGrid(11, 11)

# ic(lower_grid.get_cells_coordinates())
# editor = GridEditor()

letters_list = [ascii_letters[i] for i in range(10)]


# letters = [
#     SceneText(
#         text=symbol,
#         position=(-.75, 0, 0),
#         rotation=(35, 30, 0),
#         scale=2,
#     ) for symbol in letters_list
# ]

letter = SceneText(
    text=letters_list[0],
    position=(0.045454546, 0.045454546, 0),
)

if __name__ == "__main__":
    window.vsync = False
    app = Ursina()

    ambient_lights = AmbientLight(color=color.yellow)

    # def get_cursor_position(self):
    #     y = int(round(self.cursor.y))
    #     x = int(round(self.cursor.x))
    #     return Vec2(x,y)

    def update():
        pass

    AmbientLight(color=color.white)




    EditorCamera()
    camera.rotation = Vec3(0, 0, 0)
    camera.position = Vec3(0, 15, -20)
    camera.rotation = Vec3(30, 0, 0)


    def on_click():
        if mouse.hovered_entity == lower_grid:
            local_x = mouse.point.x + .5
            local_y = mouse.point.y + .5
            cell_x = floor(local_x * lower_grid.grid_width)
            cell_y = floor(local_y * lower_grid.grid_height)
            local_center = Vec3((cell_x + 0.5) / lower_grid.grid_width, (cell_y + 0.5) / lower_grid.grid_height, 0)
            world_center_cell = lower_grid.world_position + local_center * lower_grid.world_scale

            ic(f'Local center: {local_center}')
            ic(f'Cell indices: {cell_x}, {cell_y}')
            ic(f'World center: {world_center_cell}')


    lower_grid.on_click = on_click






    app.run()

# cells = []
# for z in range(10):
#     for x in range(10):
#         cell = Button(
#             parent=scene,
#             position=(x, 0, z),
#             model='cube',
#             color=color.white,
#             highlight_color=color.azure,
#             origin_y=0.5
#         )
#         cell.coords = (x, z) # Сохраняем логические координаты
#         cell.on_click = lambda c=cell: print(f"Нажата клетка: {c.coords}")
#         cells.append(cell)



    # cells = []
    # for z in range(10):
    #     for x in range(10):
    #         cell = Button(
    #             parent=scene,
    #             position=(x, 0, z),
    #             rotation=(30, 30, 0),
    #             model='cube',
    #             color=color.blue,
    #             # highlight_color=color.rgba(0, 0, 0, 0),
    #             origin_y=0.5
    #         )
    #         cell.coords = (x, z) # Сохраняем логические координаты
    #         cell.on_click = lambda c=cell: print(f"Нажата клетка: {c.coords}")
    #         cells.append(cell)

'''
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,0): local=Vec3(-5, 0, -5), world=Vec3(-55.515, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,1): local=Vec3(-5, 0, -4), world=Vec3(-55.515, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,2): local=Vec3(-5, 0, -3), world=Vec3(-55.515, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,3): local=Vec3(-5, 0, -2), world=Vec3(-55.515, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,4): local=Vec3(-5, 0, -1), world=Vec3(-55.515, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,5): local=Vec3(-5, 0, 0), world=Vec3(-55.515, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,6): local=Vec3(-5, 0, 1), world=Vec3(-55.515, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,7): local=Vec3(-5, 0, 2), world=Vec3(-55.515, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,8): local=Vec3(-5, 0, 3), world=Vec3(-55.515, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,9): local=Vec3(-5, 0, 4), world=Vec3(-55.515, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (0,10): local=Vec3(-5, 0, 5), world=Vec3(-55.515, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,0): local=Vec3(-4, 0, -5), world=Vec3(-44.515, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,1): local=Vec3(-4, 0, -4), world=Vec3(-44.515, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,2): local=Vec3(-4, 0, -3), world=Vec3(-44.515, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,3): local=Vec3(-4, 0, -2), world=Vec3(-44.515, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,4): local=Vec3(-4, 0, -1), world=Vec3(-44.515, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,5): local=Vec3(-4, 0, 0), world=Vec3(-44.515, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,6): local=Vec3(-4, 0, 1), world=Vec3(-44.515, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,7): local=Vec3(-4, 0, 2), world=Vec3(-44.515, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,8): local=Vec3(-4, 0, 3), world=Vec3(-44.515, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,9): local=Vec3(-4, 0, 4), world=Vec3(-44.515, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (1,10): local=Vec3(-4, 0, 5), world=Vec3(-44.515, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,0): local=Vec3(-3, 0, -5), world=Vec3(-33.515, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,1): local=Vec3(-3, 0, -4), world=Vec3(-33.515, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,2): local=Vec3(-3, 0, -3), world=Vec3(-33.515, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,3): local=Vec3(-3, 0, -2), world=Vec3(-33.515, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,4): local=Vec3(-3, 0, -1), world=Vec3(-33.515, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,5): local=Vec3(-3, 0, 0), world=Vec3(-33.515, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,6): local=Vec3(-3, 0, 1), world=Vec3(-33.515, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,7): local=Vec3(-3, 0, 2), world=Vec3(-33.515, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,8): local=Vec3(-3, 0, 3), world=Vec3(-33.515, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,9): local=Vec3(-3, 0, 4), world=Vec3(-33.515, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (2,10): local=Vec3(-3, 0, 5), world=Vec3(-33.515, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,0): local=Vec3(-2, 0, -5), world=Vec3(-22.515, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,1): local=Vec3(-2, 0, -4), world=Vec3(-22.515, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,2): local=Vec3(-2, 0, -3), world=Vec3(-22.515, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,3): local=Vec3(-2, 0, -2), world=Vec3(-22.515, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,4): local=Vec3(-2, 0, -1), world=Vec3(-22.515, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,5): local=Vec3(-2, 0, 0), world=Vec3(-22.515, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,6): local=Vec3(-2, 0, 1), world=Vec3(-22.515, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,7): local=Vec3(-2, 0, 2), world=Vec3(-22.515, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,8): local=Vec3(-2, 0, 3), world=Vec3(-22.515, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,9): local=Vec3(-2, 0, 4), world=Vec3(-22.515, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (3,10): local=Vec3(-2, 0, 5), world=Vec3(-22.515, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,0): local=Vec3(-1, 0, -5), world=Vec3(-11.515, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,1): local=Vec3(-1, 0, -4), world=Vec3(-11.515, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,2): local=Vec3(-1, 0, -3), world=Vec3(-11.515, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,3): local=Vec3(-1, 0, -2), world=Vec3(-11.515, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,4): local=Vec3(-1, 0, -1), world=Vec3(-11.515, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,5): local=Vec3(-1, 0, 0), world=Vec3(-11.515, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,6): local=Vec3(-1, 0, 1), world=Vec3(-11.515, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,7): local=Vec3(-1, 0, 2), world=Vec3(-11.515, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,8): local=Vec3(-1, 0, 3), world=Vec3(-11.515, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,9): local=Vec3(-1, 0, 4), world=Vec3(-11.515, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (4,10): local=Vec3(-1, 0, 5), world=Vec3(-11.515, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,0): local=Vec3(0, 0, -5), world=Vec3(-0.515, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,1): local=Vec3(0, 0, -4), world=Vec3(-0.515, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,2): local=Vec3(0, 0, -3), world=Vec3(-0.515, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,3): local=Vec3(0, 0, -2), world=Vec3(-0.515, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,4): local=Vec3(0, 0, -1), world=Vec3(-0.515, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,5): local=Vec3(0, 0, 0), world=Vec3(-0.515, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,6): local=Vec3(0, 0, 1), world=Vec3(-0.515, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,7): local=Vec3(0, 0, 2), world=Vec3(-0.515, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,8): local=Vec3(0, 0, 3), world=Vec3(-0.515, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,9): local=Vec3(0, 0, 4), world=Vec3(-0.515, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (5,10): local=Vec3(0, 0, 5), world=Vec3(-0.515, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,0): local=Vec3(1, 0, -5), world=Vec3(10.485, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,1): local=Vec3(1, 0, -4), world=Vec3(10.485, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,2): local=Vec3(1, 0, -3), world=Vec3(10.485, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,3): local=Vec3(1, 0, -2), world=Vec3(10.485, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,4): local=Vec3(1, 0, -1), world=Vec3(10.485, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,5): local=Vec3(1, 0, 0), world=Vec3(10.485, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,6): local=Vec3(1, 0, 1), world=Vec3(10.485, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,7): local=Vec3(1, 0, 2), world=Vec3(10.485, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,8): local=Vec3(1, 0, 3), world=Vec3(10.485, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,9): local=Vec3(1, 0, 4), world=Vec3(10.485, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (6,10): local=Vec3(1, 0, 5), world=Vec3(10.485, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (7,0): local=Vec3(2, 0, -5), world=Vec3(21.485, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (7,1): local=Vec3(2, 0, -4), world=Vec3(21.485, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (7,2): local=Vec3(2, 0, -3), world=Vec3(21.485, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (7,3): local=Vec3(2, 0, -2), world=Vec3(21.485, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (7,4): local=Vec3(2, 0, -1), world=Vec3(21.485, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (7,5): local=Vec3(2, 0, 0), world=Vec3(21.485, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (7,6): local=Vec3(2, 0, 1), world=Vec3(21.485, -0.02, 16.515)'
ec3(43.485, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (9,5): local=Vec3(4, 0, 0), world=Vec3(43.485, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (9,6): local=Vec3(4, 0, 1), world=Vec3(43.485, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (9,7): local=Vec3(4, 0, 2), world=Vec3(43.485, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (9,8): local=Vec3(4, 0, 3), world=Vec3(43.485, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (9,9): local=Vec3(4, 0, 4), world=Vec3(43.485, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (9,10): local=Vec3(4, 0, 5), world=Vec3(43.485, -0.02, 60.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,0): local=Vec3(5, 0, -5), world=Vec3(54.485, -0.02, -49.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,1): local=Vec3(5, 0, -4), world=Vec3(54.485, -0.02, -38.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,2): local=Vec3(5, 0, -3), world=Vec3(54.485, -0.02, -27.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,3): local=Vec3(5, 0, -2), world=Vec3(54.485, -0.02, -16.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,4): local=Vec3(5, 0, -1), world=Vec3(54.485, -0.02, -5.485)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,5): local=Vec3(5, 0, 0), world=Vec3(54.485, -0.02, 5.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,6): local=Vec3(5, 0, 1), world=Vec3(54.485, -0.02, 16.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,7): local=Vec3(5, 0, 2), world=Vec3(54.485, -0.02, 27.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,8): local=Vec3(5, 0, 3), world=Vec3(54.485, -0.02, 38.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,9): local=Vec3(5, 0, 4), world=Vec3(54.485, -0.02, 49.515)'
ic| f"Cell ({x},{z}): local={local_center}, world={world_center}": 'Cell (10,10): local=Vec3(5, 0, 5), world=Vec3(54.485, -0.02, 60.515)'

'''