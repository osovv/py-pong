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

	def move_up(self, field):
		if self.y() >= field.bthick + self.step_size:
			self.move(self.x(), self.y() - self.step_size)
			self.pos_y -= self.step_size
			self.rel_y = self.y() / field.h
		else:
			self.move(self.x(), field.bthick)
			self.pos_y = field.bthick
			self.rel_y = self.y() / field.h
		self.move(self.pos_x, self.pos_y)

	def move_down(self, field):
		if self.y() + self.h + self.step_size <= field.h - field.bthick:
			self.move(self.x(), self.y() + self.step_size)
			self.pos_y += self.step_size
			self.rel_y = self.y() / field.h
		else:
			self.move(self.x(), field.h - field.bthick - self.h)
			self.pos_y = field.h - field.bthick - self.h
			self.rel_y = self.y() / field.h
		self.move(self.pos_x, self.pos_y)

	@property
	def step_size(self):
		return self._step_size
	@step_size.setter
	def step_size(self, step_size):
		self._step_size = step_size
