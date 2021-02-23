from PyQt5.QtWidgets import QWidget

from Object import Object

class Ball(Object):
	def __init__(self, color, width, height, pos_x, pos_y, parent = None):
		super(Ball, self).__init__(color, width, height, pos_x, pos_y, parent)
	
	def resizeEvent(self, e):
		# self.scale_x = (self.scale_x + self.scale_y) / 2
		# self.scale_y = self.scale_x
		if self.flag:
			super(Ball, self).resizeEvent(e)