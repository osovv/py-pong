from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import  QColor, QPainter, QPen
from PyQt5.QtCore import Qt
from settings import *
from Object import Object


class GameField(Object):
	def __init__(self, color, width, height, pos_x, pos_y, parent = None):
		super(GameField, self).__init__(color, width, height,  pos_x, pos_y, parent)

	def resizeEvent(self, e):
		super(GameField, self).resizeEvent(e)
		self.bthick = int(self.w / BORDER_SCALE + self.h / BORDER_SCALE)

	def paintEvent(self, e):
		qp = QPainter(self)
		qp.setPen(QPen(QColor(self.bcolor), int(self.w / BORDER_SCALE + self.h / BORDER_SCALE), Qt.DashLine))
		qp.drawLine(int(self.w/2), 0, int(self.w/2), self.h)
		qp.setPen(QPen(QColor(self.bcolor), int(self.w / BORDER_SCALE + self.h / BORDER_SCALE), Qt.SolidLine))
		qp.fillRect(0, 0, self.w, self.bthick, QColor(self.bcolor))
		qp.fillRect(0, self.h-self.bthick, self.w, self.bthick, QColor(self.bcolor))

	@property
	def bthick(self):
		return self._bthick
	@bthick.setter
	def bthick(self, bthick):
		self._bthick = bthick
	@property
	def bcolor(self):
		return self._bcolor
	@bcolor.setter
	def bcolor(self, bcolor):
		self._bcolor = bcolor
