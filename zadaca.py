import pyglet
import life_logic
import life_data

from pyglet import shapes
from pyglet.window import mouse

g_x = life_data.g_x
g_y = life_data.g_y
sq = life_data.sq

window = pyglet.window.Window(g_x * (sq + 1) + 100, g_y * (sq + 1))
batch = pyglet.graphics.Batch()

life_color = [80, 80, 80], [80, 80, 80]

shape_rect = []
for y in range(80):
    for x in range(120):
        shape_rect.append(
            shapes.Rectangle(x=x * (sq + 1), y=y * (sq + 1), width=sq, height=sq, color=life_color[0], batch=batch))

r0 = [0, 0, g_x * (sq + 1) + 100, g_y * (sq + 1)]
r1 = [g_x * (sq + 1) + 100, g_y * (sq + 1)]
r2 = [g_y * (sq + 1) + 100, g_y * (sq + 1)]
region = [r0, r1, r2]


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT :
        pass


pyglet.app.run()
