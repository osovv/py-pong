from PyQt5.QtWidgets import QWidget

from Object import Object

class Ball(Object):
	def __init__(self, color, height, width, pos_x, pos_y, parent = None):
		super(Ball, self).__init__(color, height, width, pos_x, pos_y, parent)