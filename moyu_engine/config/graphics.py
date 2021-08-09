
import pyglet
from pyglet.gl import *
from pyglet.image.codecs.png import PNGImageDecoder

import constants as C

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

tl1 = pyglet.image.load('moyu_engine/assets/graphics/tileland/tl1.png', decoder=PNGImageDecoder())
#tl1_width,tl1_height = 64*2 , 64*2
#tl1.scale = min(tl1.height, tl1_height)/max(tl1.height, tl1_height), max(min(tl1_width, tl1.width)/max(tl1_width, tl1.width))

tl6 = pyglet.image.load('moyu_engine/assets/graphics/tileland/tl6.png', decoder=PNGImageDecoder())

tl11 = pyglet.image.load('moyu_engine/assets/graphics/tileland/tl11.png', decoder=PNGImageDecoder())

tl16 = pyglet.image.load('moyu_engine/assets/graphics/tileland/tl16.png', decoder=PNGImageDecoder())

tl21 = pyglet.image.load('moyu_engine/assets/graphics/tileland/tl21.png', decoder=PNGImageDecoder())