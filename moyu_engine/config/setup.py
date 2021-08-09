
import os
import sys
import random

import pyglet
from pyglet.gl import *
from pyglet.window import key

import components.tilemap_manager

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
    glEnable(GL_BLEND)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    components.tilemap_manager.tilemap_loarder()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

components.tilemap_manager.tilemap_builder()
pyglet.app.run()