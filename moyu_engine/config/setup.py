
import os
import sys
import random

import pyglet

boarder = 16
tile_level = 1
tile_size = 64*tile_level
move_x,move_y = 19*30,3*30
move_speed = 5

tile_choose_info = [0,0,0,0,0,0]

mouse_x,mouse_y = (boarder/2*(tile_size/2)-boarder/2*(tile_size/2)),(boarder/2*(tile_size/4)+boarder/2*(tile_size/4))

#icon1 = pyglet.image.load('16x16.png')
#icon2 = pyglet.image.load('32x32.png')
#window.set_icon(icon1, icon2)

#clock = pygame.time.Clock()

window = pyglet.window.Window()
window.set_caption('TinyLand 弹丸之地')
#window.set_size(1280, 720)

@window.event
def on_draw():
    window.clear()
    #label.draw()

pyglet.app.run()