from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import  QColor, QPalette

class Object(QWidget):
	def __init__(self, color, height, width, pos_x, pos_y, parent = None):
		super(Object, self).__init__(parent)
		self.setAutoFillBackground(True)
		self.color = color
		self.height = height
		self.width = width
		self.pos_x = pos_x
		self.pos_y = pos_y

	@property
	def color(self):
		return self._color
	@color.setter
	def color(self, color):
		palette = self.palette()
		palette.setColor(self.backgroundRole(), QColor(color))
		self.setPalette(palette)
		self._color = color

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, height):
		self._height = height

	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, width):
		self._width = width

	@property
	def pos_x(self):
		return self._pos_x
	@pos_x.setter
	def pos_x(self, pos_x):
		self._pos_x = pos_x

	@property
	def pos_y(self):
		return self._pos_y
	@pos_y.setter
	def pos_y(self, pos_y):
		self._pos_y = pos_y
