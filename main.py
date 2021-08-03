from panda3d.core import loadPrcFile
loadPrcFile('config/config.prc')

from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):

    def __init__(self):
        super().__init__(self)

game = MyGame()

game.run()
