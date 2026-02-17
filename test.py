from ursina import *

app = Ursina()

# Создаём невидимую плоскость для raycast (всегда на уровне y=0)
drag_plane = Entity(model='plane', scale=(100, 1, 100), collider='box', visible=False)

selected_object = None
drag_offset = Vec3(0, 0, 0)

def input(key):
    global selected_object, drag_offset
    
    if key == 'left mouse down':
        # Проверяем клик по объекту
        if mouse.hovered_entity and mouse.hovered_entity != drag_plane:
            selected_object = mouse.hovered_entity
            # Сохраняем смещение между центром объекта и точкой клика
            drag_offset = selected_object.position - mouse.world_point
            selected_entity_info.text = f'Выбрано: {selected_object.model.name}'
            selected_object.animate_scale((1.2, 1.2, 1.2), duration=0.1)
    
    elif key == 'left mouse up':
        if selected_object:
            selected_object.animate_scale((1, 1, 1), duration=0.1)
            selected_object = None
            selected_entity_info.text = 'Не выбрано'

def update():
    global selected_object
    
    if selected_object and mouse.left:
        # --- ИСПРАВЛЕНИЕ ---
        # Вычисляем вектор направления от камеры к позиции мыши в 3D мире
        # camera.screen_to_world(mouse.position) даёт точку перед камерой, соответствующую курсору
        mouse_direction = (camera.screen_to_world(mouse.position) - camera.position).normalized()
        # -------------------

        # Raycast к плоскости drag_plane
        hit_info = raycast(
            origin=camera.position,
            direction=mouse_direction, # Используем вычисленное направление
            ignore=[selected_object, camera]
        )
        
        if hit_info.hit:
            # Плавное перемещение к новой позиции
            target_position = hit_info.world_point + drag_offset
            selected_object.position = lerp(
                selected_object.position,
                target_position,
                time.dt * 10  # Скорость интерполяции
            )

# Создаём визуальную плоскость
ground = Entity(
    model='plane',
    color=color.dark_gray,
    scale=(10, 1, 10),
    texture='white_cube',
    texture_scale=(10, 10)
)

# Создаём несколько объектов
for i in range(3):
    Entity(
        model='sphere',
        color=color.hsv(i * 120, 0.8, 0.9),
        position=(i - 1, 0.5, 0),
        scale=0.5,
        collider='sphere'
    )

# UI для отображения информации
Text(text='Кликните на сферу и перетаскивайте', position=(-0.85, 0.45), scale=1)
selected_entity_info = Text(text='Не выбрано', position=(-0.85, 0.4), scale=1, color=color.yellow)

app.run()