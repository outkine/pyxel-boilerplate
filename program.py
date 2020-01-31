from pyxel import *
from lib import *
init(64, 64, fps=3)
load('my_resource.pyxres')

while True:
    cls(0)
    sprite(0, 0, 1, 0)
    flip()
