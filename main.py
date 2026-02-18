from ursina import *

from icecream import ic

from classes.class_ShipsCreater import ShipsCreater

from classes.create_objects import my_water_area, enemy_water_area, nav_button, four_deck_menu

scene1_coordinates = my_water_area.position
scene2_coordinates = enemy_water_area.position

ships_creater = ShipsCreater()

if __name__ == "__main__":
    window.vsync = False
    app = Ursina()

    ambient_lights = AmbientLight(color=color.yellow)

    # EditorCamera()
    # camera.position = Vec3(0, 15, 0)
    # camera.rotation = Vec3(35, 0, 0)
    # camera.fov = 60

    camera.position = Vec3(0, 15, -22)
    camera.rotation = Vec3(35, 0, 0)

    def update():
        ships_creater.update()

        if nav_button.is_enemy_position:
            if camera.position > scene2_coordinates:
                camera.position -= Vec3(20, 0, 0) * time.dt
        else:
            if camera.position < scene1_coordinates:
                camera.position += Vec3(20, 0, 0) * time.dt




    app.run()

