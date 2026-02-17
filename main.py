from ursina import *

from icecream import ic

from classes.create_objects import my_wather_area, enemy_wather_area


if __name__ == "__main__":
    window.vsync = False
    app = Ursina()

    ambient_lights = AmbientLight(color=color.yellow)


    def update():
        pass


    EditorCamera()
    camera.position = Vec3(0, 15, 0)
    camera.rotation = Vec3(35, 0, 0)
    camera.fov = 60


    app.run()

