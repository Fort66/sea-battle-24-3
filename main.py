from ursina import *

from icecream import ic

from classes.create_objects import my_wather_area, enemy_wather_area, nav_button, my_four_deck

scene1_coordinates = my_wather_area.position
scene2_coordinates = enemy_wather_area.position


if __name__ == "__main__":
    window.vsync = False
    app = Ursina()

    ambient_lights = AmbientLight(color=color.yellow)

    EditorCamera()
    camera.position = Vec3(0, 15, 0)
    camera.rotation = Vec3(35, 0, 0)
    camera.fov = 60

    def update():
        if nav_button.is_enemy_position:
            if camera.position > scene2_coordinates:
                camera.position -= Vec3(20, 0, 0) * time.dt
        else:
            if camera.position < scene1_coordinates:
                camera.position += Vec3(20, 0, 0) * time.dt




    app.run()

