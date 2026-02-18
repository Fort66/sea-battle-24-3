from ursina import Button, color



class NavButton(Button):
    def __init__(self,
                color=color.blue,
                position=(0, .4, 0),
                scale=.1,
                text='Click',
                **kwargs
                ):

        super().__init__(
            color=color,
            position=position,
            scale=scale,
            text=text,
            **kwargs)

        self.is_enemy_position = False
        self.on_click = self.change_value

    def change_value(self):
        self.is_enemy_position = not self.is_enemy_position