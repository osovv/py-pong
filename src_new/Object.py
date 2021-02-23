from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import  QColor, QPalette

class Object(QWidget):
	def __init__(self, color, width, height, pos_x, pos_y, parent = None):
		super(Object, self).__init__(parent)
		self.setAutoFillBackground(True)
		self.color = color
		self.w = width
		self.h = height
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.newpos_x = pos_x
		self.newpos_y = pos_y
		self.neww = width
		self.newh = height
		self.flag = True
		self.scale_x = 1
		self.scale_y = 1
		self.resize(width, height)
		self.move(pos_x, pos_y)
	
	def resizeEvent(self, e):
		self.w = self.width()
		self.h = self.height()
		self.newpos_x *= self.scale_x
		self.newpos_y *= self.scale_y
		self.neww *= self.scale_x
		self.newh *= self.scale_y
		if abs(self.newpos_x - self.pos_x) >= 1:
			self.pos_x = self.newpos_x
		if abs(self.newpos_y - self.pos_y) >= 1:
			self.pos_y = self.newpos_y
		if abs(self.neww - self.w) >= 1:
			self.w = self.neww
			self.flag = False
			self.resize(self.w, self.h)	
			self.flag = True
		if abs(self.newh - self.h) >= 1:
			self.h = self.newh
			self.flag = False
			self.resize(self.w, self.h)	
			self.flag = True			
		self.move(self.pos_x, self.pos_y)
		
		
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
	def h(self):
		return self._h
	@h.setter
	def h(self, h):
		self._h = h

	@property
	def w(self):
		return self._w
	@w.setter
	def w(self, w):
		self._w = w

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

	@property
	def scale_x(self):
		return self._scale_x
	@scale_x.setter
	def scale_x(self, scale_x):
		self._scale_x = scale_x

	@property
	def scale_y(self):
		return self._scale_y
	@scale_y.setter
	def scale_y(self, scale_y):
		self._scale_y = scale_y
