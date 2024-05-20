from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

boxes = []

def add_box(position, box_color=color.green, box_texture='grass'):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=box_color,
            position=position,
            texture=box_texture
        )
    )

for x in range(20):
    for y in range(20):
        add_box((x, 0, y))

def input(key):
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal, box_color=color.white, box_texture='brick')  # Neue Farbe und Textur für den Block
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)

app.run()