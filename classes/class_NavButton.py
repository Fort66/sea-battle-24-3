from ursina import Button, color



class NavButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = color.blue
        self.scale = 0.1
        self.position = (0, .4, 0)
        self.scale = .1
        self.text = 'Click'

        self.is_enemy_position = False
        self.on_click = self.change_value

    def change_value(self):
        self.is_enemy_position = not self.is_enemy_position