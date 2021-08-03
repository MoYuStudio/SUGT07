import panda3d
from panda3d.core import loadPrcFile
loadPrcFile('config/config.prc')

from panda3d.core import loadPrcFileData

from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):

    def __init__(self):
        super().__init__(self)

        box = self.loader.loadModel('models/box')
        box.setPos(0,10,0)
        box.reparentTo(self.render)

        panda = self.loader.loadModel('models/panda')
        panda.setPos(-3,10,0)
        panda.setScale(0.1,0.1,0.1)
        panda.reparentTo(self.render)

game = MyGame()

game.run()
