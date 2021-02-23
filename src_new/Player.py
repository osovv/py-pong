from PyQt5.QtWidgets import QWidget

from Object import Object

from settings import *


class Player(Object):
	def __init__(self, color, width, height, pos_x, pos_y, parent = None):
		super(Player, self).__init__(color, width, height, pos_x, pos_y, parent)
		self.flag = True

	def resizeEvent(self, e):
		if self.flag:
			super(Player, self).resizeEvent(e)

	def move_up(self):
		pass

	def move_down(self):
		pass

	@property
	def step_size(self):
		return self._step_size
	@step_size.setter
	def step_size(self, step_size):
		self._step_size = step_size
