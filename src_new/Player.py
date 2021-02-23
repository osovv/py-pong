from PyQt5.QtWidgets import QWidget

from Object import Object

class Player(Object):
	def __init__(self, color, height, width, pos_x, pos_y, parent = None):
		super(Player, self).__init__(color, height, width, pos_x, pos_y, parent)

	def move_up(self):
		pass

	def move_down(self):
		pass
