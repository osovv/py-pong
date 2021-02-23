from PyQt5.QtWidgets import QWidget

from Object import Object

class GameField(Object):
	def __init__(self, color, width, height, pos_x, pos_y, parent = None):
		super(GameField, self).__init__(color, width, height,  pos_x, pos_y, parent)